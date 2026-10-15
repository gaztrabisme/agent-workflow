# Generator discipline

Ten rules. Each closed a real defect; the price is in the clause.

## 1. One normative model module

Rows as data in an importable module — `(id, group, role, effort, class, driver, note)` — with the generator
importing it. **Never derive the model by patching a returned spreadsheet.** One generator composed its plan
by applying twenty-one override tables (`OVERRIDE`, `DROP`, `RENAME`, `REROLE`, `REGROUP`, `REPOINT`,
`NEW_ROWS`…) to a reviewer's returned workbook. That shape is right while the plan is a series of negotiated
amendments to someone else's file and wrong the moment the estimate becomes parametric: it inverts the
dependency and guarantees the two drift.

**Import the downstream, do not copy it.** Three copies of one constant table already existed in that repo and
one of them was in a 3,688-line dead file.

## 2. The model asserts itself at import

Row accounting closes (base − cut + new); every ratio row's stated percentage reproduces its number. Cheap,
runs on every build.

**If you later cache the model, say in a comment why the lost repetition is not lost coverage** — these
assertions are functions of files on disk that do not change mid-run. A future reader will otherwise assume
5,500 executions were load-bearing. (They were not: caching took a probe from 6.74 ms to 1.93 ms and 76% of it
was model rebuild.)

## 3. Roll-ups are formulas over the detail sheet

Never literals. A generator that wrote literals produced a fork reporting **356.5 against a task grid summing
to 375.5** — a 19-unit drift a human reader would take at face value — while still printing
*"seat-cap breaches: 0"*, because the breach was created **after** the cap check ran.

**Corollary: overflow raises.** Work that does not fit must not be piled into the last available slot. That
produced a 54.5 MD week on a 30 MD team inside a workbook claiming zero breaches.

## 4. The reconciliation line is printed on the sheet

`task effort + PM = cost total`, with the rate and the count beside it. One plan carried **three live totals**
— 406.5 on the task sheet, 441.5 on the cost sheet, 352.5 in the deck built from a pinned older version — and
nothing on the face of any sheet said so. A cost line with no task row and no capacity consumption reads to a
reviewer as a new cost arriving as a spreadsheet row; say what it is where it appears.

## 5. Assert the layout before indexing into it

Bound a week grid at `max_column - <trailing columns>` and **check every header in range matches the expected
pattern**. Summing to `max_column` was right by coincidence on one version and inflated the total by
**+331.5 MD** on two earlier ones. Measured, not reasoned.

## 6. Assert sheet order, at import

One workbook reached fifteen sheets with five injected in **front** of the task list, so the person who owned
the estimate opened our argument about it first and his own task list sixth. Assert `KEEP[0] == "Tasks"` at
import and assert the spine before saving. Sheet order had no gate at all and the regression had already
happened once.

## 7. Two gates, not one

| | numeric verifier | content gate |
|---|---|---|
| asks | do the workbooks still say what we say they say | does internal-register text leave the building |
| reads | `data_only=True` cached values | **raw XML of every zip part**, `html.unescape`d |
| runs on | the finished files | a **path**, and it is the **last** step |
| fails | non-zero exit, per-check | fails the build |

**The verifier prints its own check count.** *"30 numeric checks pass"* was written into two records and
nobody could reproduce it — the checks were real, ran in a throwaway shell script, and were never saved. A
cold fact-check reconstructed ~27 for one claim and ~19 for the other. **A count nobody can re-run is worth
less than no count.**

**The content gate must run on the shipped bytes.** Version 1 checked the in-memory workbook before `save()`,
and the build then recalculated with LibreOffice — proven from `docProps/app.xml` — so anything touched between
the check and delivery went out unchecked.

**And state what the gate cannot do.** A cold review of one hand-built gate got **40 of 43 constructed
bypasses past it**, and found nine residual sentences no pattern could ever catch: a demonstrative pointing at
a document the reader does not have, an unexplained "our groups", a precise number whose evidence is a
conversation, our own option labelled "broken" on a comparison table. A green run is not a clean file.

**Scope ID patterns to prose.** An obligation register is a column of IDs written *for* the client; an ID
standing alone as a cell value passes, an ID inside a sentence does not.

## 8. Two registers, one set of numbers

`sheet_x(wb, data, audience="internal"|"external")`. Same solved figures, provenance dropped externally. It is
not a softer version and **no figure differs**. Then rebuild the external copy and run the redaction gate over
the whole workbook.

⛔ **Assert every audienced field.** One split audienced `verdict` and wrote `label` unchanged, so the external
copy shipped a label naming exactly the internal history the exclusion list forbade. *A register split that
covers one field of two is a labelling exercise, not a control.*

What deliberately does not cross into the external register: the history of our own corrected errors, and
**our read on how to handle the counterparty, in a file addressed to the counterparty**. The second is not a
matter of tone.

## 9. Read the artifact back

Four defects on one engagement lived where no check looked — a wrong banner, printed obligations, a stale
narrative sheet, and blank cached values behind live formulas. **The only thing that caught any of them was
re-opening the written file.** Make it the habit, not the exception.

## 10. Serialise the solve and byte-diff it

If the generator runs a search or a sweep, dump every result to JSON and diff it across a refactor. ~5,200
probe results in one file is the strongest regression test available for a numeric model with no test suite,
and it costs nothing. **If it differs, stop and find out why before proceeding.**

## Behaviour-neutral changes to a numeric model

Capture a baseline table of every published figure **before** touching anything, then reproduce it exactly
after each step. Change one thing, diff the sweep, then the next. Where a change reveals a pre-existing
discrepancy, **preserve current behaviour and record it in a comment** — resolving it is a separate decision
that moves numbers.

## What did not pay

Memoising a probe: 5,185 calls, **17.5% hit rate**, and **0%** in the caller whose greedy descent visits a
different key each time. Caching the *model* did all the work. And within that, `[dict(r) for r in rows]` beat
`copy.deepcopy(rows)` **43×** — licensed by an assertion that raises by name if anyone adds a mutable column,
so the equivalence is checked rather than audited.
