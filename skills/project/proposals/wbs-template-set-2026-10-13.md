# Proposal: what two projects' WBS work adds to this skill (2026-10-13, revised)

Status: **decided 2026-10-13, all four as recommended** (owner). Applied as Evolution 4 (`EVOLUTION.md`): rule A and the colour legend in `references/wbs-workbook.md`, the checklist in `references/issue-checklist.md` (fifteen lines: the legend was added as line 13), rule B held, scripts in `templates/wbs/`. PRINCE2 cite for rule A: 11.1, The change theme.

## Sources

| | Presale WBS with pricing | Delivery WBS in a team template |
|---|---|---|
| Workspace | `Documents/pwc/scripts/` | `Documents/scgc-lsp/wbs/` |
| Who owns the plan | We wrote it | The tech lead wrote it; we adjust rows |
| Who owns the layout | We did, then the PM's own workbook | The PM's standard layout, filled exactly |
| Where the price is computed | Our Python, from the PM's rate card and weekly seat minimums | The PM's Master sheet formulas |

Plus the LSP session's reply of 13 Oct 2026, 18:08.

## The split

Most of what both projects needed is already in this skill as PM practice. What is left divides three ways:

| Layer | What it holds | Test |
|---|---|---|
| 1. Method | Rules a PM follows in any tool | A PM with Excel and no AI can follow it; it names its standard; two projects needed it |
| 2. Checklist | One page a PM runs by hand before issuing a workbook | Every line points to a rule already in layer 1 |
| 3. Accelerator | Template scripts for when an agent builds the workbook | Optional; the method never requires it |

Already in the skill, so not proposed again: reproduce the owner's total with their method (`wbs-workbook.md`, "Summarize only from detail"); a reviewer who did not draft it, fresh each round, three rounds at most ("Hand over a workbook…"); our business case only on an internal sheet (`business-case-and-tolerances.md`); outside inputs as dependencies (`estimating.md`, "Plan from products"); staffing minimums and duration options with slack (Evolution 3).

## Layer 1: method

### Rule A, version control of issued files (ready)

Proposed text, appended to "Hand over a workbook the planner can edit" in `references/wbs-workbook.md`:

> Identify every issued version by number and date, in the file name and on its first sheet. Before replacing an issued file, compare it with the copy you issued: a difference you did not make is someone's edit. Carry it into the new version or ask its author; never overwrite it.

Cases, two projects:
- LSP: shared files were downloaded before and after each edit and diffed, so only the intended cells changed (LSP session reply, item 4).
- PwC, 13 Oct: a rebuild overwrote a deck the owner had hand-edited after the build; the builder now refuses to overwrite a changed output (`wiki/log.md`, 13 Oct).

Standard: PRINCE2 configuration management (identifying and controlling versions of products). **Chapter and section not cited yet:** the knowledge base was unreachable this session. Cite before adopting.

### Rule B, proposed changes in another owner's estimate (owner's call)

Proposed text, appended to "Drafting into a team's WBS":

> When you change a figure in a row someone else owns, mark it as a proposal (a visible prefix or fill, and a one-line reason) until the owner accepts it. Give the workbook one colour legend; a colour means one thing.

Cases:
- LSP: changed figures carry "adjusted by AI engineer:" and a yellow fill; added rows get their own ID prefix; out-of-scope rows stay visible with a status.
- PwC, 12 Oct: our copy of the PM's cost table changed two of his formulas, raised as "his to confirm". Whether the file itself marked them is not checked.

Two things to settle: whether PwC 12 Oct counts as the second case (it shows the need, not the practice), and the colour conflict. The skill already says "yellow for fillable cells" ("Hand over a workbook…"); LSP used yellow for "our change, to confirm". Recommendation: keep yellow for fillable, and mark proposals with the prefix plus a different fill named in the legend.

The existing line "A row for another discipline shows who drafted it and which lead confirms it" covers drafts we wrote for other roles; rule B covers changes to rows they wrote.

## Layer 2: checklist before issuing a workbook

Proposed as a new file `references/issue-checklist.md`, linked from the "Hand over" row of the flow in `SKILL.md`. Each line is a check and a pointer; the reasons stay where they are.

1. The owner's total is reproduced with their own method and cost rules. → `wbs-workbook.md`, Summarize only from detail
2. A bridge from their total to ours lists what moved and why. → same
3. Every row states its basis; rows on judgement alone are flagged for their lead. → `estimating.md`, Every row states its basis
4. Each derived percentage names where its ratio comes from; an AI adjustment is its own column and applied once. → `estimating.md`, Activities derived as a percentage; AI-assisted work
5. Rows drafted for another discipline show who drafted them and which lead confirms. → `wbs-workbook.md`, Drafting into a team's WBS
6. Summary cells are formulas over the detail; no typed totals. → `wbs-workbook.md`, Summarize only from detail
7. Duration is shown as options with team size, end date and slack. → `planning-method.md`, Schedule with capacity and slack
8. Each concession is its own line with its amount; a price-driven cut is its own line on the bridge. → `business-case-and-tolerances.md`, Concessions; Cutting to reach a price
9. Each exclusion reads the same in every document the client sees, and a cut is traced through every text describing scope. → `business-case-and-tolerances.md`, Fixed price, fixed scope
10. Pricing assumptions (PM %, contingency, margin) are on the internal sheet only. → `business-case-and-tolerances.md`, Two business cases
11. Another company's work is one line naming its owner, not estimated. → `estimating.md`, Plan from products
12. Each dependency has a provider, a deadline relative to the schedule, the rows it blocks, and what happens if it is late. → `wbs-workbook.md`, Register dependencies
13. A reviewer who did not draft it has checked it. → `wbs-workbook.md`, Hand over a workbook…
14. The version is identified, and the last issued copy was compared before replacing it. → rule A

## Layer 3: accelerator (optional)

For a project where an agent builds the workbook. Referenced from `wbs-workbook.md` in one line; nothing in layers 1–2 depends on it.

```
project-management/templates/wbs/
  project.yaml        per-project settings (below)
  SCHEMA.md           data contract template, filled per project
  data/               tasks, changes, adjustments, assumptions, dependencies (YAML)
  build.py            YAML + project.yaml -> workbook(s); refuses malformed input; LibreOffice recalc
  verify.py           does not import build.py; re-derives every value; runs checklist items 1, 3, 6, 10, 14
  schedule.py         optional: weeks, critical path, minimum team, slack, options table
  price.py            optional: only when the price is ours to compute
  tests/negative/     broken inputs the builder must refuse and the verifier must name
```

`project.yaml` holds what differed between the two projects: the team's template and the sheet and column for each field; the effort rule (add-on ratios and rounding, or seat minimums per role per week); where the price is computed (`team-sheet` or `model` with rate card, onsite cost and currency rate); what the send copy drops and the words it must not contain; excluded roles (another company's work); how proposed changes are marked (rule B).

Taken from LSP: data out of the code, the written contract, the builder that refuses bad input, the independent verifier, the negative tests. Taken from PwC: pricing with seat minimums and a bridge, the scheduler, one model writing a send copy and an internal copy. Avoided from PwC: a new model file per pricing round (seven `estimate_model*.py`), and checks that live inside the model they check.

Kept project-side: the stale-figure hunter (`figure_ledger.py`, tied to one workspace's model) and the deck scan for blame, upsell and budget lines (`check_client_register.py`, which belongs to the `presentation` skill if it graduates).

Counts as reusable only when both workspaces rebuild their current workbook from it with the same totals. Until then neither switches.

## Decisions for the owner

1. **Rule A:** adopt now, once the PRINCE2 section is cited. Recommended.
2. **Rule B:** adopt now counting PwC 12 Oct as the second case, or hold for a project that practises it. Recommendation: hold the rule, but fix the colour conflict now, since it already exists between the skill and LSP.
3. **Checklist:** add `references/issue-checklist.md` as listed. Recommended.
4. **Accelerator:** start from LSP's builder and verifier; first cut is `project.yaml`, contract, builder, verifier, negative tests (about a day); scheduler and pricing second. Location `project-management/templates/wbs/`.

Each adopted item gets an `EVOLUTION.md` entry with its cases and a validation test, as Evolution 3 did.
