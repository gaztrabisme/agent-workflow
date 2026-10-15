---
name: xlsx
description: "Read, generate, verify and correct .xlsx workbooks from Python — the mechanics that make a spreadsheet trustworthy when a machine wrote it. USE WHEN a .xlsx/.xlsm is an input or an output: dumping a workbook to see what is in it, generating an estimate/WBS/costing/inventory workbook, recalculating formulas headlessly, gating a workbook before it is sent, correcting text in a finished file, or diagnosing why a figure reads as zero or blank. Not `pptx` (decks), not `drawio` (diagrams), not `dev` (software), not `solution-architect` (what belongs IN an estimate). Keywords: excel, xlsx, xlsm, spreadsheet, workbook, openpyxl, LibreOffice, soffice, recalculate, cached value, data_only, formula, sharedStrings, WBS, estimate workbook, costing sheet, send copy, redaction gate, apportionment, largest remainder."
license: MIT
---

# xlsx — machine-written spreadsheets

An `.xlsx` a program wrote is a **zip of XML that lies to a cell walk**. A cell can hold a formula, a cached
value, both, or neither, and those are three different loads. Text lives in about twenty places and an
`iter_rows` sees one of them. openpyxl and LibreOffice write the same workbook two different ways.

This skill is the **mechanics**: how the bytes get written, read back, recalculated and gated. It does not
decide what belongs in the workbook — see *Scope boundary*.

Every rule here was written after a defect on a real engagement. The price is in the clause.

## When this fires — and when a sibling owns it

- **This skill:** a `.xlsx`/`.xlsm` is input or output. Dump, generate, recalculate, gate, patch, diagnose.
- **`pptx` instead:** the artifact is a deck. (`show.py` here reads `.pptx` too — that is a convenience, not
  ownership.)
- **`drawio` instead:** the artifact is a diagram.
- **`dev` instead:** you are building software that happens to emit a spreadsheet as one of many outputs.
- **`solution-architect` instead:** the question is *what goes in* an estimate, a WBS, an acceptance sheet.
  Sheet inventory, column set, the prose budget and the lane test live in
  `../solution-architect/references/templates/delivery-wbs-workbook.md`. Come back here for the bytes.

## Principles

1. **Read it back.** A generator that reports success has told you a `save()` returned. Re-open the written
   file and assert the figures. Four separate defect classes on one engagement — a wrong banner, printed
   obligations, a stale sheet, blank cached values behind live formulas — were each caught only this way, and
   by nothing else.
2. **The model is the source of truth; the workbook is output.** Never derive a plan by patching a returned
   spreadsheet. A generator that patches its own input guarantees the two drift.
3. **A roll-up cell is a formula over the detail sheet, never a literal.** A literal total is a claim that
   goes stale; a formula is a check that runs every time the file opens.
4. **Print the addition chain on the face of the sheet.** If a reader selects a column and the status bar
   disagrees with your printed total, the sheet is broken however small the gap.
5. **A count nobody can re-run is worth less than no count.** Verification lives in a saved, argument-taking
   script that prints its own check count — not in a shell heredoc.
6. **Recalculation is the last step.** Everything that opens the workbook with openpyxl happens before it.
7. **Assert the layout you are about to index into.** Column bounds and header patterns, before you sum.

## Flow

| Step | Do | Gate |
|---|---|---|
| **0. Look** | `python scripts/show.py FILE [sheet …]` — never a throwaway dump script | — |
| **1. Model** | Put the numbers in one importable module: rows as data, every row stating a driver and a rate or declared fixed | Module asserts its own row accounting and ratio closure at import |
| **2. Generate** | Generator imports the model, writes sheets. Roll-ups are formulas. Reconciliation line printed on the sheet | Sheet order asserted; layout asserted before any column index |
| **3. Recalculate** | `soffice --headless --convert-to xlsx --outdir <SCRATCH> <file>` then copy back — **never `--outdir` at the input's own directory** | `show.py FILE` reports `MISSING: 0` |
| **4. Verify (numbers)** | Saved script, `data_only=True`, asserts every published figure. Prints its own check count | Exit non-zero on any miss |
| **5. Gate (content)** | Scan the **raw XML of every zip part**, `html.unescape` first. Runs on a **path**, and it is the **last** step | Fails the build, does not warn |
| **6. Correct prose** | `patch_prose`-shaped edit of `xl/sharedStrings.xml` only, or a full rebuild | Divergence check: the generator must hold the new text too |

## Hard no-list

- ❌ **Recalculating with `--outdir` pointed at the input's own directory.** LibreOffice prints
  `Overwriting: <path>`, fails `SfxBaseModel::impl_store … Code:12`, exits 1 and leaves the file
  byte-identical. *Measured: md5 unchanged.* Piping it (`| tail`) throws away the exit code and it becomes
  silent. Convert into a scratch dir, copy back.
- ❌ **Opening a recalculated workbook with openpyxl and saving it.** openpyxl cannot evaluate a formula and
  **discards the cached values** on load+save. The file still opens and every figure a human reads is blank.
  *Cost: one full rebuild pass, and the constraint that there is no such thing as a small edit.*
- ❌ **Summing a column without saying which load you used.** A formula cell is its formula string under a
  normal load and `None` under `data_only=True`. *Cost: a workbook mislabelled as the wrong priced option for
  hours, because the guard that would have caught it was broken by this.*
- ❌ **Searching a workbook with a cell walk.** Text lives in ~20 places: sharedStrings, cached formula
  results, sheet names, docProps core/app/custom, headers/footers, defined names, comments, data validation
  prompts, conditional formats, hyperlinks and tooltips, drawings, charts, tables, number formats.
  *Cost: a redaction gate that let 40 of 43 constructed bypasses through.*
- ❌ **A non-ASCII regex over raw XML without `html.unescape`.** openpyxl writes numeric character references
  (`&#7842;`), LibreOffice writes literal UTF-8. *Cost: a whole redaction class matching nothing on exactly
  the file state the builder saves.* And a hand-rolled list of the five named entities does not close it.
- ❌ **Adding or removing an `<si>` while patching `sharedStrings.xml`.** Indices shift and every later
  worksheet reference points at the wrong string. Refuse rich-text `<si>` too — replacing the text drops the
  formatting runs.
- ❌ **Independently rounding a column of money.** Printed cells must sum to the printed total. Use
  largest-remainder and assert closure. *Cost: a one-dollar gap found by hand, and the reader could not tell
  a rounding artifact from an error, so he distrusted the sheet.*
- ❌ **Piling work that does not fit into the last available slot.** A silent overflow dump produced a
  54.5 MD week on a 30 MD team while the workbook still reported *"breaches: 0"*, because the breach was
  created after the check ran. Raise.
- ❌ **A register split that covers one field of two.** If a sheet is generated in two audiences, assert every
  audienced field, not the one you remembered.
- ❌ **Writing a throwaway inspection script.** Use `scripts/show.py`. One engagement wrote 20 distinct
  filenames for the same job.
- ❌ **Printing non-ASCII without forcing UTF-8 on stdout.** On Windows the default is cp1252 and it raises.
  *37 of 362 tool errors in one corpus.* Put `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` at
  module scope in every saved script.

## Gates (declared, inherited from `core`)

- **Gate by the artifact.** *(`../core/references/output-contract.md`, "Verify the artifact".)* A workbook is verified by re-opening the written
  file and asserting its figures — never by the generator's exit code. State which file you re-read.
- **A planned gate skipped silently is an integrity miss.** *(`../core/references/output-contract.md`.)* The content gate runs on the shipped
  bytes, after the last write. A gate that ran before `save()` did not run.
- **Output Contract.** *(`../core/references/output-contract.md` and `wiki-protocol.md`.)* The workbook is not done until the run is recorded — what was rebuilt, in
  what order, what the verifier printed. See `../core/references/wiki-protocol.md`.
- **Cold review before a primary artifact ships.** *(`../core/references/output-contract.md`, cold review.)* Aim it where the automation structurally
  cannot look: tone, a demonstrative pointing at a document the reader does not have, our own argument about
  the reader sitting in the file addressed to him. A cold review of one hand-built gate got **40 of 43**
  constructed bypasses past it; a second found our own commercial argument inside the copy built for the
  counterparty. Neither is findable by pattern.
- **A sheet earns its place.** A sheet earns its place by being read. One workbook reached fifteen sheets with
  five of them in front of the task list, so the person who owned the estimate opened our argument about it
  first.

## Someone else's workbook

**A workbook with a named owner is not yours to re-derive.** Read it, cite it, and hand findings back as a
review note in a separate file — do not edit it and do not rebuild its numbers in a file of your own. Two
instances on one engagement: a reviewer's returned WBS was reviewed and **handed back with findings, not
edited**; and a pricing workbook owned by a colleague was declared out of lane
(*"we do not maintain, re-derive or defend it"*) and recorded only so its figures would not later be mistaken
for a client or vendor source. **And do not delete another person's sheet on your own authority** — whether a
rate card *travels* is a distribution decision taken with its owner, not a tidying one.

**When the owner asks for an edit in their file,** new cells take the number format of the column they
land in, checked cell by cell — not the style of a neighbouring cell. The check compares the text each
touched cell *displays*, not only its value, and lists every cell outside the touched range that changed.
(derived: LSP 2026-10-09 — our rows reused the owner's accounting style, quantities showed "$", and the
owner's workbook had to be reverted.)

Corollary: when someone else's number becomes the denominator of a decision that is yours, the move is to
**trace it and state what it computes**, not to substitute your own.

## Composition

- **`solution-architect`** — owns what goes in an estimate/WBS/blueprint workbook and the ≤1-prose-cell-per-100
  budget. This skill owns writing it and asserting the budget in code.
- **`delivery`** — consumes the baselined workbook; a re-baseline is a regenerate-from-model, never a hand edit.
- **`pptx`** — a deck reading figures out of a workbook loads with `data_only=True` and therefore **requires
  the workbook to have been recalculated**. Pin the deck generator to a named workbook path and move the pin
  in one commit with the audit that checks it.
- **`dev`** — if the generator becomes software with users, it needs tests, and this skill does not supply them.

## References

- `references/mechanics.md` — the file format: the two loads, the twenty places text lives, the two writers,
  the recalculation route, sharedStrings patching, apportionment.
- `references/generator-discipline.md` — the model-is-truth shape, the assertion set, the verifier/gate split,
  two-register generation, and the regression test you get free from a JSON dump.
- `scripts/show.py` — dump any xlsx/pptx/drawio/csv/json, plus the zip-level probes (`--members`, `--part`,
  `--grep`, `--meta`). Read this before writing any inspection code.
- `../core/SKILL.md` — the spine this inherits.
- `../solution-architect/references/templates/delivery-wbs-workbook.md` — what belongs in a WBS workbook.
