# Evolution Log — xlsx

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`.
Harvest source: sessions where a `.xlsx` is an input or an output.

---

## Evolution 1 — 2026-08-18 — birth, from one engagement's measured defects

### Harvest scope
`C:\Users\HuyTL10\Documents\pwc` — 22 days, 37 Python files / 17,449 lines of xlsx+pptx toolchain, no tests,
no git. Read: 13 generators and gates, `wiki/decisions.md` D-045/110/114/131/132/149/150/151/152,
`wiki/log.md`, `~/.claude/plans/purring-wobbling-lobster.md`, and 362 classified tool errors.
**Classify: authored** — every rule traces to a defect that fired in real work, not to documentation.
Four lessons were reproduced first-hand on the real deliverables before being written down.

### Patterns found
Ranked (Impact ÷ Effort):
1. **openpyxl discards cached formula values on load+save** — Impact H, Effort L. Cost one rebuild pass and
   the standing constraint that no edit is small.
2. **Text lives in ~20 places; a cell walk sees one** — Impact H, Effort L. A hand-built redaction gate let
   40 of 43 constructed bypasses through.
3. **A formula cell is a string under one load and `None` under the other** — Impact H, Effort L. A workbook
   was labelled the wrong priced option for hours.
4. **No inspection utility existed** — Impact H, Effort L. 20 distinct throwaway filenames for one job;
   agent-1 measured ~24 min of generation per session.
5. **openpyxl writes numeric character references, LibreOffice literal UTF-8** — Impact M, Effort L. A whole
   redaction class matched nothing on the exact file state the builder saves.
6. **LibreOffice cannot recalculate in place** — Impact M, Effort L. Prints `Overwriting`, exits 1, changes
   nothing; silent the moment you pipe it.
7. **cp1252 on stdout** — Impact M, Effort L. 37 of 362 tool errors, re-typed per call because no saved
   script owned it.
8. **Independent rounding breaks a printed column** — Impact M, Effort L. A one-dollar gap cost a reversed
   recommendation and two cold audits.
9. **Literal roll-up cells** — Impact H, Effort M. A 19-unit drift reported as zero breaches.
10. **Register splits that cover one field of two** — Impact H, Effort L. The external copy shipped the exact
    internal history the exclusion list named.

### Hypotheses applied
1. `SKILL.md` — flow table, hard no-list, someone-else's-workbook rule; closes 1, 2, 3, 5, 6, 7, 8, 10.
2. `references/mechanics.md` — the two loads, the twenty places, the two writers, the recalculation route,
   sharedStrings patching, apportionment, stdout encoding; closes 1, 2, 3, 5, 6, 7, 8.
3. `references/generator-discipline.md` — model-is-truth, self-asserting model, formula roll-ups, printed
   reconciliation, layout and sheet-order asserts, verifier/gate split, two registers, read-back,
   JSON-diff regression; closes 9, 10.
4. `scripts/show.py` — closes 4, and makes 1/3/5 visible rather than remembered.

Not modified (validated as already-sound): what belongs *in* a WBS workbook — owned by
`../solution-architect/references/templates/delivery-wbs-workbook.md`, which already carries the sheet
inventory, the prose-cell budget and the lane test.

### Validation results (settled by a later run's step 0)
- [ ] `show.py` is invoked in a real session in place of a throwaway dump script.
- [ ] The recalculation route is followed on a first attempt, with no in-place `--outdir` failure.
- [ ] A generated workbook is read back and its figures asserted before it is reported done.
- [ ] The `--grep` raw-XML path finds a string a cell walk missed.
- **Verdict: PENDING** — single engagement, single author, and the skill has never been loaded in a live
  session. Two independent real uses are needed before any rule here moves to KEEP.

### Open, deliberately
- **No tests ship with the skill.** The source toolchain had none; the JSON-diff regression in
  `generator-discipline.md` §10 is what stands in for one, and it is a technique, not a suite.
- **`patch_prose`'s precondition is stated but not enforced.** §4.2 §6 says to check `sharedStrings.xml`
  exists; no code in this skill does it.
- **xlsx writing beyond openpyxl** — xlsxwriter, pandas `to_excel`, COM automation — is unaddressed. Every
  measured lesson came from openpyxl + LibreOffice, and claiming more would be borrowed confidence.

## Evolution 2 — LSP presale after-action review (2026-10-10)

### Traces
LSP presale sessions 2026-10-01..09 (`C:\Users\HuyTL10\Documents\scgc-lsp`); skill files read in 6 sessions; `show.py` invoked in sessions on 1, 6 and 8 Oct. Report: `scgc-lsp/wiki/raw/2026-10-10-after-action-report.md`.

### Settled verdicts (Evolution 1 checklist)
- [x] `show.py` used in place of a throwaway dump script → **KEEP** (1 Oct WBS v0.1, 6 Oct v0.3, 8 Oct v1.1/v1.2: separate tasks).
- [x] Generated workbook read back and figures asserted before reported done → **KEEP** (independent verifier on every build; 43/43 negatives on v1.2).
- [ ] Recalculation route on first attempt → **REVISED**: failed once because the workbook was open in LibreOffice (8 Oct). Selector added (H8), itself PENDING.
- [ ] `--grep` raw-XML path → **PENDING**, not used.

### Changes
| ID | Edit | Evidence |
|---|---|---|
| H6 | `SKILL.md` "Someone else's workbook": when the owner asks for an edit, new cells take the column's number format; the check compares displayed text and lists changes outside the touched range | 2026-10-09: our rows reused the owner's accounting style; "$" appeared in quantities; the owner asked for a revert |
| H8 | `references/mechanics.md` §3: look for a lock file before rebuilding or recalculating | 2026-10-08 retro: recalculation blocked by a workbook open in LibreOffice |

### Verdict: PENDING
Both from one trace each. Validation: next edit in someone else's workbook ships with a displayed-text check and no format complaint; next rebuild of an open workbook writes to a new name instead of failing. Owner: Huy; revisit at the next project's close.
