# Delivery WBS — the workbook as a collection instrument

> **Applies when** the recipient is a **delivery planner (PM / TL)** who owns the release split and the
> staffing plan (`../deal-shapes.md` §Axis 2). **Not** the client-facing priced attachment
> (`../estimation-and-costing.md`), the scope document, the acceptance annex
> (`../acceptance-and-contract.md`), or the blueprint workbook — that is the enterprise-bid carrier, aimed
> at a client evaluator.

## 0 — The governing principle

**The effort column is an input, not an output.** You enumerate the work; the people who will do it price
it. An architect who arrives with the column filled has answered a question the PM owns and silently
allocated work to a team nobody has named.

**The instrument ships empty.**

> *Observed.* The adopted artifact on a real engagement had **0 numeric cells across 234 task rows**, a
> legend reading *"Fill the YELLOW columns only"*, and a calibration anchor. The rejected one had the
> column pre-filled, capacity pre-derived, releases collapsed to one, and the cut order pre-decided. The
> second was an argument; the first was an instrument. Only one got used.

### Effort has three representations, not two

*Filled* and *empty* are not the whole space. Ask the planner which form they want before building the sheet.

| Form | When | What it collects |
|---|---|---|
| **Filled** | never, from an architect | — |
| **Empty column** | fixed window, effort is the unknown | a number per row, from the lead who will do it |
| **Schedule position** | **duration is the unknown**, effort is roughly understood | *when* each task sits, from which duration falls out |

> *Observed, a later window on the same engagement.* The PM asked for *"not MD est but grouped by week"* — a
> week grid, no man-day column at all. The template's filled/empty binary had no room for it. The grid did the
> same job the empty column was designed for: it collected the planner's judgement, and it collected it in the
> unit he actually owned.

**Where duration is set by engineering rather than given, the grid is the instrument that answers it.** Ship
`N + 2` week columns where `N` is the duration someone has already committed to publicly, mark which columns
are beyond it, and place bars from dependency order. Bars landing past column `N` **are** the engineering
view — derived and visible rather than asserted in an argument. On the trace that produced this, the work
landed in W5 against a deck that stated four weeks, and the one-week gap was the deliverable.

**Two rules that follow, both learned the hard way:**

- **Milestones live on the time axis, never as horizontal banner rows.** A band across a
  structurally-ordered list reads as *"everything above this is complete"* — which is false the moment rows
  are grouped by feature rather than by date. Put a single `Milestones` row **inside the grid**, marked in the
  column where each one occurs. *(Caught by the PM: "the End W1 title, but I see tasks going into W2 and 3,
  4" — and the reference schedule he had himself supplied already showed the correct pattern, a vertical band
  in one week column.)*
- **A column that is constant carries nothing — delete it.** When every row belonged to one phase, `Phase`
  became noise; when the cut order moved out of the sheet, `Priority` had no defined scale. Both were dropped
  on the recipient's question *"how to read Priority, and do we even need it?"*

## 1 — Sheet: WBS

One task = one deliverable one discipline can finish. Blank-repeat the group/feature levels so filtering
still works.

| Column | Holds | Why it exists |
|---|---|---|
| `WBS ID` | `G.F.T`, hierarchical, stable | the row's name in every other sheet |
| `Feature Group` / `Feature` / `Task` | three levels | the enumeration itself |
| `Source / Traceability` | client module ref · challenge ref · wireframe · or the token `Ours` | **every row anchored**; `Ours` rows are the ones a reviewer must defend |
| `Release` | phase bucket **in the buyer's own vocabulary** | the planner sets the boundary — you supply the enumeration |
| `Priority` | P0 / P1 / P2 | lets them cut without re-reading |
| `Discipline` | BE / FE / DE / AI / DevOps / QA / BA / SA / PM | **turns a total into a staffing plan**; lets the sheet be split and sent out to be filled |
| `Complexity` | S / M / L, **anchored per discipline** | one global anchor does not transfer from a BE row to an AI row |
| **`Est. Effort (md)`** | **empty · highlighted · fill-only** | the input you are collecting |
| `Depends on` | WBS IDs, **typed** | prose dependencies (*"feeds FG16"*) are untraversable |
| `Uncertainty driver` | ≤12 words: what must be true for this to hold to ±20% | without it, every row is equally confident and the sum is fiction |
| `Notes` | **one clause** | more than one clause means it is a decision — write it in `decisions.md`, put the ref here |

**Every column must be readable by the named recipient without a glossary.** Two failed this on a live
handover: `T0-1`, an internal package reference from the estimate document (*"what does T0-1 here mean?"*),
and `Priority`, an undefined scale (*"how to read Priority and do we even need it?"*). If a column needs you
in the room to explain it, it is not an instrument. Internal cross-references belong in `Notes` as a bare
token, not in a column heading.

**Declare dependencies by key, resolve to IDs at build time.** If the sheet is generated, have each task
carry a stable slug and reference other tasks by slug; resolve slugs to `WBS ID` when writing the file, and
fail the build on an unresolved one. Hand-maintained `Depends on` cells go stale silently the first time a row
is inserted; a dangling reference should not be shippable.

## 2 — Sheet: Summary — every cell a formula

`COUNTIF`/`COUNTIFS` by group × release × priority; `SUMIF` for effort; `% of total`; an `Origin` roll-up
(theirs / materially extended / ours) so the summary doubles as the differentiation story.

**No typed numbers on a summary sheet.** A typed total is a claim that goes stale; a formula is a check
that cannot disagree with its own source (`../artifact-integrity.md` §The check must execute).

## 3 — Sheet: Capacity & fit

The sheet the benchmark lacked, and the reason to keep it: capacity derivation (people × days), the effort
envelope with exclusions named, `required vs available`, `gap`, and the cut order with *what the client
loses* per line — all driven off Sheet 1 by `SUMIF` so it **moves when the estimate is filled in**.

Framed as the check the planner runs *after* collection, not a constraint the architect imposed *before* it.
Without it, a sheet can only discover it is undeliverable after it has been quoted.

## 4 — Sheet: Traceability, run both directions

Client challenge/requirement → *their own* coverage → `Covered / Partial / GAP` → WBS refs.

- **Forward:** every challenge has a row. No silent gaps.
- **Reverse:** every `Ours` row is examined. Unanchored rows are either differentiation or scope creep.
- **The `GAP` rows are the win-theme list.** Legend it that way (`../rfi-rfp-response.md` §Polarity).

## 5 — Sheet: Dependencies

`ID · what we need · from whom (**named person**) · by when (schedule-relative) · blocks (WBS IDs) · if it is late`

Keep this — a free-text `Notes` column cannot hold *"without it the estimate does not close; the
requirement becomes 102 MD against 58."* **Check the ID prefix against every other register in the
engagement before choosing it** (`../artifact-integrity.md` C8).

## 6 — Fill convention and handback

Yellow = fill, grey = reference. One calibration anchor per discipline. Ship empty with a one-paragraph
covering note naming who fills which discipline and by when. **That note is the only prose in the
transaction.**

## 6b — Handover retires the generator

The moment the recipient starts **hand-editing** the workbook, *"regenerate, don't hand-edit"* inverts from a
safeguard into a destructive instruction: the next run silently overwrites their work.

**On handover: mark the generated version final, record that the file is now hand-maintained, and reverse the
instruction in the index.** Keep the script on disk as the record of what was generated and why — it is no
longer a tool. *(On the trace: the PM took the artifact with "don't work on the WBS file any more"; the index
still said regenerate. That instruction would have destroyed his edits.)*

## 7 — Pre-ship checks

- **Count the sheets. Sheets describing the work must outnumber sheets defending the number.** If they do not,
  cut until they do. This replaces a prose warning that failed: §8 below already said accretion is *"exactly
  how an eight-sheet workbook gets built and rejected"* — and an author who had read that sentence then
  shipped obligations-with-consequences, a risk register, a cut order, commercial assumptions and a status
  banner into an engineering task inventory. **Prose warnings fail silently; countable checks do not.**
- **The lane test, per row:** name the recipient and the decision they must make, then ask whether *this row*
  helps *that* person make *that* decision. A row that is correct but aimed at a different reader is out of
  lane, which is a distinct failure from being too long. *(Recipient's verdict: "why are you including lots of
  commercial assumptions? We're building this WBS from engineering POV — we just went out of our lanes.")*
- **≤1 prose cell (≥12 words) per 100 non-empty cells** (`../../../core/references/pushback-and-teach.md`
  §Two channels) — and **if the workbook is generated, assert it.** A budget nobody measures is an
  aspiration. One `assert` that fails the build on a Notes cell of ≥12 words converts it into a gate, and it
  is three lines of code. This is the same lesson as `../artifact-integrity.md` §The check must execute.
- Every row anchored in `Source`; every `Ours` row justified or cut
- Every column readable by the named recipient without a glossary
- Summary recomputes from detail; no typed totals
- ID namespace unique across the engagement — **but see `../artifact-integrity.md` C8 on registers that
  serve different audiences and must not be merged**
- Release vocabulary matches the buyer's recorded word — if they said MVP, the column says MVP. **Including
  when a phase collapses:** if the team drops a stage, name the survivor in the buyer's vocabulary
  (*"MVP (next phase)"*, not *"next phase"*) so the workbook and the client deck do not diverge the same day
- If cached values are needed for non-Excel readers, keep the formulas and open-and-resave; never replace
  formulas with literals

## 8 — What this is not

| Not this | Lives in |
|---|---|
| The priced attachment | `../estimation-and-costing.md` |
| The scope narrative + assumptions | the scope document |
| What the client is bound to | `../acceptance-and-contract.md` |
| The multi-round bid carrier | `../blueprint-workbook.md` |
| Why each choice was made | `wiki/decisions.md` |

Letting this instrument accrete those five jobs is exactly how an eight-sheet workbook — three sheets about
the work, five about defending the number — gets built and rejected.
