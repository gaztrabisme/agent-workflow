# The delivery lifecycle

Five phases from signature to close-out, plus **Phase −1**, which runs before there is a contract at all.
Scale each to the engagement — but **Phase 0 and Phase 1 are not optional at any size.** They are cheap when
done first and impossible to retrofit once the engagement is already slipping.

---

## Phase −1 — Pre-signature input *(runs inside SA's planning phase; there is no contract yet)*

**Goal:** the effort number that gets priced is authored by the people who will be held to it.

Not a delivery phase in the contractual sense — nothing is baselined and nothing is tracked. But a skill that first sees the plan at mobilisation inherits a number it had no hand in, and Phase 0's reconciliation can then only discover the problem *after* it has been quoted.

**Do, when SA hands over a WBS for pricing:**
- **Fill the effort column — do not accept it pre-filled.** An architect who arrives with it filled has answered a question this role owns. Split the sheet by discipline and have the leads price their own rows.
- **Own the release split**, in the buyer's recorded vocabulary. What is in the first release is a delivery judgement about risk, not an architecture judgement about coherence.
- **Own the cut order** — what comes out under pressure, and what the client loses per line.
- **Return a capacity verdict, not just a total.** People × days available vs required. If it does not fit, the answer is *"it does not fit, by N days"* — a finding handed back for re-scoping, not a number to be closed by adjusting an input (`../../solution-architect/references/estimation-and-costing.md` §capacity-fit gate).

**Say which form the effort takes before the sheet is built.** There are three, not two, and only you can pick:

| Form | Use when | You supply |
|---|---|---|
| **Effort column, empty** | the window is fixed and effort is the unknown | a number per row, from the lead who will do it |
| **Schedule position** | **duration is the unknown** and effort is roughly understood | *when* each task sits; duration falls out of it |
| Pre-filled | never | — |

**Where duration is yours to determine, ask for the week grid instead of the column.** *Observed:* a PM asked for *"not man-day estimates but grouped by week"* — and the grid collected exactly what the empty column was designed to collect, in the unit he actually owned. It also produced the capacity verdict for free: with bars placed from dependency order, the work landed one week past the duration already stated publicly, and **the gap was visible rather than argued**. That is a stronger artifact than a total, because a schedule that does not fit shows it.

Two things to insist on in that form: **milestones belong on the time axis**, never as horizontal bands across a task list ordered by feature — a band reads as *"everything above is done"* and it is not; and **the number of columns should exceed the committed duration**, with the excess marked, so overrun is expressible rather than requiring a renegotiation to state. Full column spec: `../../solution-architect/references/templates/delivery-wbs-workbook.md`.

**Artifact:** the filled WBS — or the placed grid — returned to SA for pricing.

**When you take the artifact over, retire its generator.** If the WBS was generated and you begin hand-editing it, *"regenerate, don't hand-edit"* inverts into a destructive instruction: the next run silently overwrites your work. Say so in the index, mark the generated version final, and keep the script only as the record of what it produced.

**Common failure:** treating the architect's estimate as settled because it arrived with confidence and a formula behind it. The second failure is the mirror image — refusing to engage until signature, and then being handed the result. **The third is answering the wrong question well:** pricing an artifact aimed at a different reader. Ask what decision the sheet must serve before filling anything in it.

---

## Phase 0 — Mobilise

**Goal:** convert a signed proposal into a plan of record.

The proposal was a *sales artifact*: written to win, with optimism in it. The baseline is a *delivery
artifact*: what you will actually be measured against. They are rarely identical, and the gap between them
is the first thing worth knowing.

**Do:**
- **Inherit the ID spine.** Take the acceptance-criteria IDs from the signed annex verbatim. Do not renumber,
  do not "improve" them, do not create a parallel delivery WBS. Every tracker in this skill keys to these IDs.
- **Reconcile what was sold against what was priced.** Compare the acceptance annex's function list to the
  cost model's line items. A function in one and not the other is a defect with money attached, and it is
  *far* cheaper to find now than at acceptance. (`../../solution-architect/references/artifact-integrity.md` is the
  full check — run it once more against the signed set.)
- **Freeze scope, schedule, cost** into `delivery-baseline.md`, recording for each what it was derived from.
- **Define T0 explicitly.** "Week 1" is meaningless until you name the event that starts the clock — signature,
  deposit received, access granted, kickoff held. Whichever it is, it should already be a contract term; if it
  isn't, that's your first escalation.
- **Name the counterpart.** A single authorised client focal point who can decide, and the acceptance
  signatory if different. Multiple channels of instruction is how unpriced scope enters.
- **Carry the risk register forward** from presale rather than starting a new one.

**Artifact:** `delivery-baseline.md`, plus a written list of every discrepancy found between the sold and
priced views.

**Common failure:** treating the proposal's phase plan as the baseline without re-reading it. Proposals
routinely contain a schedule written before the scope was final.

---

## Phase 1 — Establish control

**Goal:** the trackers exist and are populated *before* the first deliverable is due.

**Do:**
- Stand up the **acceptance tracker** — one row per criterion from the spine, every row status `Not started`.
  Empty is fine; absent is not.
- Stand up the **obligations tracker** from SA's client-obligation register, converting each schedule-relative
  deadline ("week 1 phase 1") to a real date now that T0 is known.
- Open the **change-request log** empty, and tell the client it exists. A CR log introduced *after* the first
  contested change reads as a defensive manoeuvre; introduced at kickoff it reads as professionalism.
- Agree the **reporting cadence and format** with the client, and the escalation path above your counterpart.
- Confirm the **acceptance mechanics** are contractually settled: testing window length, response deadline,
  defect severity definitions and their consequences, what happens on silence. If any is missing, raise it now
  — see `acceptance-execution.md`. These are far harder to agree once a deliverable is contested.

**Artifact:** three populated trackers + an agreed cadence.

**Common failure:** deferring this until "things settle down." Things do not settle down; the trackers are
what settles them.

---

## Phase 2 — Run the cadence

**Goal:** a repeating loop that keeps the baseline and reality attached.

Each cycle (weekly is right for most engagements; fortnightly for long slow ones):

1. **Update actuals** — effort spent, deliverables submitted, criteria signed. Facts only.
2. **Recompute progress** from the acceptance tracker, not from anyone's sense of it (`progress-measurement.md`).
3. **Chase obligations** — every overdue client dependency gets a dated, written follow-up. Written, because
   the record is the point. An overdue obligation that has never been raised in writing cannot later be
   claimed as the cause of a slip.
4. **Triage change** — anything new is baseline, CR, or explicitly declined. Never a fourth thing.
5. **Reassess risk** — what got closer, what materialised, what is newly visible.
6. **Report** — publish the status report. Derive RAG from the trackers.

**Artifact:** a status report per cycle, on disk, never verbal-only.

**Common failure:** the cadence lapses exactly when the engagement gets difficult — which is when the record
matters most. If you skip a cycle, say so in the next report rather than backfilling silently.

---

## Phase 3 — Accept

**Goal:** each criterion reaches signed acceptance with evidence attached.

This is the phase where money is decided, and it runs *throughout* delivery rather than as a final event —
criteria should be accepted in batches as they complete, not accumulated into one terminal negotiation.
A single end-loaded acceptance event is the worst possible structure: it concentrates all commercial risk at
the moment your leverage is lowest, because the work is already done.

Full mechanics — preconditions, severity classes, response windows, deemed acceptance, conditional
acceptance, the silent client — in `acceptance-execution.md`.

**Artifact:** signed acceptance records, each linked to its criterion ID and its evidence.

---

## Phase 4 — Close

**Goal:** discharge the obligation cleanly and convert the engagement into knowledge.

**Do:**
- **Final acceptance** and the formal start of warranty/support — these are different dates and the contract
  should distinguish them.
- **Release the final invoice** against the acceptance record, not against "the work being finished."
- **Hand over** documentation, credentials, runbooks, and the open-defect list. An honest open-defect list at
  handover is worth more than a clean one that isn't true.
- **Close the obligations tracker** with a written record of which client dependencies slipped and by how
  much. This is the evidence base for any commercial conversation, and for pricing the next engagement with
  this client realistically.
- **Harvest.** Run the retrospective into the evolution loop (`../../core/references/evolution-loop.md`):
  - **Estimate vs actual, per phase** → back to `../../solution-architect/references/estimation-and-costing.md`.
    This is the single most valuable output of the whole engagement for future bids.
  - **Which acceptance criteria were contested, and why** → back to SA's `acceptance-and-contract.md`. A
    criterion that caused a dispute was written ambiguously; the fix belongs upstream.
  - **Which client obligations slipped** → the pattern repeats across clients of the same shape.
  - **What this skill lacked** → its own `EVOLUTION.md`.

**Artifact:** close-out record + harvest entries in the relevant skills.

**Common failure:** the engagement ends, the team disperses, and nothing is harvested — so the next estimate
repeats this one's errors at a different client.
