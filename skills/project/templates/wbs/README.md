# WBS workbook template (first cut)

Builds a WBS workbook (.xlsx) from YAML data and one settings file, and verifies it independently.
The plan owner's figures are the base; our changes sit on top as status changes, added tasks and proposed
changes, each with a source. Totals are live formulas; the team's own sheet formulas compute the price
(`pricing: team-sheet`), we only fill rows.

## Files
| File | What it is |
|---|---|
| `project.yaml.example` | Every per-project setting, one comment each. Copy it to `project.yaml` and fill it in. |
| `SCHEMA.md` | The data contract: fields of each YAML file and the hard rules. |
| `build.py` | YAML data + `project.yaml` -> workbook. Exit 2 on malformed or inconsistent input. |
| `verify.py` | Re-derives every expected value from the YAML and checks the workbook. Does not import `build.py`. |
| `wbs_common.py` | Settings and data loading, LibreOffice recalculation. Computes no figure. |
| `tests/run_negative.py`, `tests/fixtures/` | Broken inputs the builder must refuse; broken workbooks the verifier must name. |
| `examples/` | Settings that reproduce a real project's workbook. Project names and figures live only there. |

## Commands
```
python build.py --project project.yaml --data DATA_DIR --out OUT.xlsx --recalc
python verify.py OUT.xlsx --project project.yaml --data DATA_DIR
python tests/run_negative.py
```
- `--recalc` runs LibreOffice headless so formulas carry cached values; `verify.py` reads them, so always
  recalculate before verifying. LibreOffice is found on PATH, in its default install folder, or via `SOFFICE`.
- `--plan-total N` (both scripts) overrides `plan.total` for a one-off check.
- `verify.py` prints PASS or FAIL per check group and exits 0 only if every group passes. It also prints
  `WARNING version stamp` lines when the file name or first sheet lacks a version number and a date; these
  do not fail the run.

## Check groups in verify.py
structure, master inputs, cached values (no formula errors), task detail rows, effort rule, proposals,
sources (every changed or added figure has one), removals, live formulas (no typed totals), effort summary,
base total, reference check (the owner's plan total reproduced), WBS sums, criteria coverage, stories,
dependencies, references, text length, diacritics, person names and sources (no names, excluded owner or
internal-source tags on shown sheets), acceptance clause, proposal marking (prefix, fill and one legend).

## Colour marking
Yellow (`fills.fill_in`) means a cell to fill in or confirm. A proposed change to someone else's figure
carries `marking.proposal_prefix` in its note and a different fill (`fills.proposal`, light orange by default).
One colour legend, on the sheet named in `marking.legend_sheet`, says what each fill means.

## Limits
- First cut. Built and tested on one real project and the fixtures in `tests/`.
- No scheduler: no dates, durations, dependencies between tasks or critical path.
- No pricing model: `pricing: model` is reserved and the builder exits 2. Price comes from the sheet formulas
  (man-days / days per month x rate); there is no rate card per role. Planned for the pricing batch: a copy
  without prices (no rate, cost or currency), dropping every assumption tagged as price-bearing.
- Exactly two add-ons, named `qc` and `ba`; their ratios are settings, their names are not.
- The Effort Summary layout is fixed: base activity table, option blocks, other-owner lines, the plan check
  block and the bridge from the plan's effort, in that order. Labels are settings; the shape is not.
- Sheet keys are fixed (master, summary, wbs, task_detail, stories, assumptions, dependencies, references).
  Names, order and columns are settings; a sheet cannot be left out.
- The diacritics check looks only for accented Vietnamese letters.
- The internal-source check finds only what `text.internal_source_patterns` describes; it cannot tell a client
  document citation from an internal one by itself.
- Plan task ids must be dot-separated; the plan feature is the first `data.feature_key_parts` parts.
- `verify.py` reads figures from cached values, so a workbook saved without recalculation fails "cached values".
