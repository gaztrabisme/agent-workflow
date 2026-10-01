# Evolution Log — delivery

The ledger for this skill's own improvement. Protocol: `../evolution/references/loop.md`.
Harvest source for this skill: **completed engagements** — estimate vs actual, which criteria were contested,
which client obligations slipped, where the trackers failed to catch a problem in time.

---

## Evolution 4 — stage B rebuild (2026-10-01)

### Sources read

Read the approved proposal, delivery rules ledger and book crosswalk; cited chapters in `scrum-masters-path`,
`swebok`, `pmbok-guide-7e`, `user-story-mapping`, `project-management-with-ai`, `learning-agile`,
`head-first-pmp`, `software-architect-elevator`, `project-planning-scheduling-control`, `holacracy`,
`fundamentals-enterprise-architecture`, `refactoring`, and `getting-to-yes`; the practitioner review and
former skill; and the rebuilt core and skill-builder authoring guidance. The course sources named by the
proposal did not supply routed rules that needed a course citation.

### Coverage and decisions

- **Rules:** 123 routed exactly once — 43 agrees, 46 refines, 34 field-rule, 0 disputed (89 book-supported,
  34 field rules).
- **Additional practices:** 16 crosswalk candidates adopted; the remaining candidates were outside this
  skill's signed-client artifact and audience boundary. No extra book practice was added outside the
  candidate list.
- **Structure:** replaced the prior rule-led material with a signed-engagement flow: bounded estimate inputs,
  signed mobilisation, active records, recurring measurement and change control, criterion acceptance, and
  closure. Kept the lifecycle reference and surviving reference names, and added focused trackers for client
  obligations and close-out. General project-planning methods and client-message drafting now route to their
  approved sibling skills.
- **Hard placement:** effort estimation that occurs before signature remains a bounded input in the
  lifecycle reference because it supplies the signed baseline; it does not open precontract delivery
  tracking.
- Dogfood (2026-10-01, shared past-presale task): 7 findings (2 high, 3 med, 2 low); 6 fixed, 1 rejected. F5 was rejected because project planning and client-message artifacts are assigned to the sibling skills for the next wave. Verdict remains PENDING.

### Validation plan

The coverage map records the 123 rules and 16 adopted candidates. Run the programme verifier for coverage,
citations and skill shape. The rebuild is authoring-time evidence only; no real delivery use is claimed.

**Verdict: PENDING** — retain this verdict until two real uses provide evidence about the new structure and
records.

---

## Evolution 0 — 2026-07-27 — Birth

### Why this skill exists

The constellation covered *selling* the work (`solution-architect`) and *building* it (`dev`), with nothing
owning the period in between signature and final acceptance. The gap was confirmed rather than assumed:

- Neither sibling had any concept of **baseline**, **actuals**, **variance**, **status reporting**,
  **change-request logging**, or **milestone→invoice**. The word "baseline" appeared in both and meant
  something else in each — a *business* baseline in SA (today's cost), an *ML training* baseline in dev.
- The failure that motivated it was concrete: a live engagement produced defects that were almost entirely
  **document-control failures under multiple authors over time** — the same population counted four
  different ways across four artifacts, a cost model still pricing a deleted function, two language versions
  disagreeing on scope. SA's `artifact-integrity.md` was the response, but it is a *linter*: it detects drift.
  It does not say who owns the master, what the change process is, or when the baseline re-freezes.

### Prior art survey (2026-07-27)

Checked before authoring, to avoid rebuilding something that exists:

- **Anthropic's official skills** (17 in `anthropics/skills`) — no project-management skill. Closest are
  `doc-coauthoring` and `internal-comms`; neither is PM.
- **The largest community PM skill library** (800+ skills, MIT) — states outright that it does *not* cover
  acceptance criteria for client deliverables, milestone-based invoicing, change request management, client
  status reporting, or fixed-price engagement baselines. It targets internal product work.
- **A consulting-proposal skill constellation** with a `domain-delivery/project-management` module — the
  closest analogue found, and instructive: it produces *proposal-ready* governance content. It stops at
  signature too.

Verdict: **the post-signature consulting-delivery space is genuinely empty.** Worth noting honestly that
empty ≠ valuable — most agent-skill authors build for internal software teams, where this machinery doesn't
apply. This skill is justified by the engagement shape it serves, not by the vacancy.

### Design decisions

1. **A third skill, not a split.** Nothing moved out of `solution-architect` or `dev`. Both are correctly
   scoped; the hole was between them. Disambiguation is by **tense** — criteria being *negotiated* → SA,
   criteria being *tracked to sign-off* → delivery.
2. **Concurrent, not sequential.** Delivery is not the next box after `dev`; it runs for the whole engagement
   with `dev` cycling inside it. The pipeline diagram reflects this.
3. **One spine, four views.** Inherits SA's acceptance-criteria IDs. A criterion is simultaneously a scope
   item, a progress unit, a test, and a payment trigger. The single strongest design decision here, and the
   thing that makes the skill small: progress measurement, acceptance, and invoicing collapse into one
   instrument instead of three that drift apart.
4. **0/100 over percent-complete.** Practitioner consensus rejects full EVM at small scale in favour of the
   0/100 rule and weighted milestones. Applied to a client-signed criterion this is binary and externally
   verified — there is nothing to inflate. Its real weakness (nothing shows complete early) is stated in the
   text along with two mitigations rather than hidden.
5. **Contract mechanics quantified.** 15–20 business day testing windows, ~5 business day response deadlines,
   deemed acceptance on silence, severity classes that define their *consequence* and not just their meaning.
   SA's `acceptance-and-contract.md` gestured at these without numbers.

### Hypotheses applied

| # | Hypothesis | Files |
|---|---|---|
| H1 | The post-signature gap needs its own trigger and audience, not a reference inside SA | `SKILL.md` |
| H2 | Acceptance-criteria-passed is the least-gameable progress metric on an acceptance-gated deal | `references/progress-measurement.md` |
| H3 | Severity classes fail without a consequence mapping; only Critical/High may block acceptance | `references/acceptance-execution.md` |
| H4 | Deemed acceptance is the only structural answer to the silent client | `references/acceptance-execution.md` |
| H5 | Absorbed change must be logged as zero-cost CRs or the pattern stays invisible until the margin is gone | `references/change-control.md` |
| H6 | Re-baselining on *slippage* (rather than only on approved change) destroys the signal that the engagement is in trouble | `references/change-control.md` |
| H7 | Client-side delay must be dated, named, and in the permanent record or it is silently absorbed | `templates/status-report.md`, `templates/acceptance-tracker.md` |

### Verdict

**`PENDING` — every hypothesis above.** This skill is **distilled, not fire-tested**: authored from prior-art
research, practitioner sources, and one engagement's *presale* trace. No hypothesis here has yet survived a
real delivery. Per `core`, distilled confidence is borrowed confidence.

Specifically **unvalidated and worth watching**:
- Whether 0/100 on the criteria spine is workable when criteria are coarse — the mitigation ("make criteria
  smaller") is asserted, not tested, and may collide with a signed annex that can't be resubdivided.
- Whether the zero-cost CR log is actually maintained under pressure, or quietly abandoned in week 3 —
  which is exactly when it would start earning its place.
- Whether the five templates are the right five, or whether two of them collapse together in practice.

### Gates

- **Spec validation:** `skills-ref validate` — passing.
- **Dogfood gate: NOT RUN.** The evolution validation plan requires a fresh-context critic using the skill on a real
  task. Record skipped runs explicitly rather than quietly omitting them. This is a second reason the verdict is `PENDING`.

### First validation opportunity

The next fixed-price delivery. Harvest specifically: estimate vs actual per phase, which criteria were
contested and why, which client obligations slipped and by how much, and which of these five templates were
actually maintained past week 3.

---

## Evolution 1 — 2026-07-29 — The pre-signature seam

### Harvest scope

Harvested from a **presale** engagement (a Big-4 professional-services client in South-East Asia; see
`solution-architect`'s Evolution 4). This skill's stated harvest source is *completed engagements*, and none
has occurred — so the initial reading was that there was nothing to harvest.

**That reading was wrong, and the error is worth recording.** Evolution 0 declared this skill *distilled, not
fire-tested* — authored from prior-art research and one engagement's presale trace, with no practitioner
contact. What the trace supplies is not execution data but the thing a theory-built skill most lacks: a
**real delivery planner's behaviour**, in the form of an artifact he authored, an artifact he rejected, and
his stated reasons for both. That falls squarely inside the boundary this skill drew for itself — and it lands
on the one seam drawn purely by inference.

### Patterns found

1. **The tense rule is false at its own boundary — H/L.** `SKILL.md` sends anything pre-signature to SA:
   *"SA produces the artifacts this skill baselines."* Observed: the delivery PM was engaged **weeks before
   signature**, rejected SA's WBS outright, rebuilt it, and asserted ownership of exactly the decisions this
   skill later gets measured on — the effort figure (*"I can work this out myself"*), the release split, and
   the cut order (*"drop this cut order"*). Neither skill owned that interaction: SA believed it did and was
   rejected; delivery disclaimed it. **The estimate SA prices is the estimate delivery is held to.**
2. **The instrument/argument distinction, from the delivery side — H/M.** The adopted artifact carried **0
   numeric cells across 234 task rows**, yellow fill markers, a calibration anchor, and a discipline tag per
   row so the sheet could be split and priced by the leads who would do the work. The rejected one had the
   column pre-filled. The fix landed in SA as a template; the *principle* — whoever will be held to a number
   authors it — is delivery's, and was absent here.
3. **No capacity line in the baseline — M/L.** The cost baseline carried effort, labour, CapEx, licences,
   contingency, total — and no denominator. Both practitioner artifacts in the trace lacked one too: one
   tagged 165 tasks to a single release against a 15-working-day window with no capacity figure anywhere. A
   baseline frozen without a capacity check freezes an infeasible plan and only discovers it in Phase 2.
4. **The mobilisation reconciliation inherits SA's execution defect — H/L.** Seven prose checkboxes, the same
   shape as SA's `artifact-integrity.md` — which on this trace was *present, correct, and never executed*,
   shipping a false clean report over three live totals for one population. Delivery's version sits at a
   higher-stakes moment: it freezes the plan of record.
5. **Principle 7 fires too late — M/L.** *"Never invent a second numbering system"* is correct, and the
   collision it warns about was created **in presale**, by SA, accommodating the PM's vocabulary. Delivery is
   where it gets discovered, so the namespace check belongs in the mobilisation list — not only as a principle.

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **The pre-signature exception** — the delivery planner is a consumer of SA's artifacts before signature; an estimate authored by someone who will not be held to it is not an estimate | `SKILL.md` | 1, 2 |
| 2 | **Phase −1 — pre-signature input**: fill the effort column (never accept it pre-filled), own the release split and cut order, return a capacity verdict rather than a total | `references/delivery-lifecycle.md` | 1, 2 |
| 3 | **Capacity-fit block** in the baseline: available vs required vs gap; a zero gap is a declared choice, a positive gap cannot be frozen | `templates/delivery-baseline.md` | 3 |
| 4 | **Reconciliation as a value table, not checkboxes** — write both compared values; a tick with no numbers is a claim about a check | `templates/delivery-baseline.md` | 4 |
| 5 | **Namespace-uniqueness check** added to mobilisation; effort recorded **by discipline** | `templates/delivery-baseline.md` | 5, 2 |

### What was deliberately not changed

**Most of the skill.** Nothing was observed about running the cadence, acceptance execution, UAT, defect
severity, deemed acceptance, change control, status reporting or RAG derivation — so `progress-measurement.md`,
`acceptance-execution.md`, `change-control.md` and three of the five templates are **untouched**. Evolution 0's
three named unknowns (0/100 on coarse criteria, whether the zero-cost CR log survives week 3, whether five
templates is the right five) remain exactly as open as they were. This trace could not test any of them.

### Validation (fill on the next engagement)

- [ ] The skill is engaged **before** signature, and the effort column it returns is the one that gets priced.
- [ ] A capacity gap is reported as *"does not fit, by N days"* rather than closed by moving an input.
- [ ] The mobilisation reconciliation ships with **values in both columns**, not ticks.
- [ ] An ID-namespace collision is caught at mobilisation rather than after a tracker is built on it.
- **Verdict: `PENDING`.** One trace, and a *presale* one. Hypothesis 1 is the load-bearing change and also the
  riskiest: it widens this skill's trigger into territory SA currently claims, and the failure mode to watch
  for is two skills both trying to own the estimate. If that happens, the boundary is drawn wrong again — but
  in the other direction.

### Note on the initial mis-scoping

The first pass at this evolution concluded *"no delivery trace ⇒ nothing to harvest"* and shipped the skill
unchanged. The distinction it missed: **no execution trace is not no trace.** For a skill that has never met a
practitioner, a practitioner's rejection of its sibling's artifact is first contact. Worth stating as a loop
rule: *when a skill is distilled rather than harvested, the bar for what counts as evidence is lower, because
the alternative is not "wait for better data" — it is "keep shipping inference."*

---

## Evolution 2 — 2026-07-30 — The planner accepted the sheet, then asked for a different unit

### Harvest scope

**The same presale engagement as Evolution 1, one day later** — still pre-signature, so still Phase −1 only.
Evolution 1 authored Phase −1 on a single signal: a PM rejected an artifact and rebuilt it. This window shows
the **other half of that seam** — what the same PM does when handed an instrument built to his shape.

Traces: three WBS rebuilds driven by his written feedback; a Teams thread carrying two scope decisions and a
handover instruction; and a schedule grid that produced a duration verdict rather than receiving one.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **Phase −1's "fill the effort column" assumes the window is fixed.** When *duration* is the unknown and effort is roughly understood, the planner does not want a column at all | H/L | *"not MD est but grouped by week"*, then *"windows is depending on the amount of work required… I'm engineer, I get to push back realistically"* |
| 2 | **A week grid produces the capacity verdict for free, and produces it in a form that is harder to argue with.** With bars placed from dependency order, the work landed one week past a duration already stated publicly — visible, derived, not asserted | H/L | Grid lands in W5; the client-facing deck states four weeks in three places. Nobody had to make the argument; the sheet made it |
| 3 | **The planner will accept a machine-made artifact and then take it over.** Ownership transfer is the success condition, and it **inverts the regeneration instruction** | H/L | *"khi anh xong cái file slide, thì em work trên cái slide luôn đi, đừng work trên file WBS nữa."* The index still said *"regenerate, don't hand-edit"* — one run would have destroyed his edits |
| 4 | **A milestone drawn as a horizontal band across a task list is a false claim**, and the planner is who catches it | H/L | *"chỗ title End W1 nhưng task a thấy qua mấy W2 và 3,4."* Rows grouped by feature ran three weeks past a banner asserting completion |
| 5 | **The third Phase −1 failure mode: answering the wrong question well.** Ev.1 named two (accepting a pre-filled estimate; refusing to engage until signature). A third is pricing an artifact aimed at a different reader | H/L | The sheet arrived carrying obligations, risks, a cut order and commercial assumptions — all correct, none the planner's to price |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **Three effort forms, with a selector** — empty column / **schedule position** / never pre-filled; *"say which form before the sheet is built"* | `references/delivery-lifecycle.md` Phase −1 | 1 |
| 2 | **Ask for the grid when duration is yours to determine**, with the `N+2` column rule so overrun is expressible without a renegotiation | same | 1, 2 |
| 3 | **Milestones on the time axis, never horizontal bands** | same, pointing at SA's template for the column spec | 4 |
| 4 | **Handover retires the generator** — mark the generated version final, reverse the index instruction, keep the script as a record | same | 3 |
| 5 | **Third common failure named:** answering the wrong question well; ask what decision the sheet must serve before filling anything in | same | 5 |

### Validation (fill on the next engagement that reaches Phase −1)

- [ ] Effort form **agreed with the planner before the sheet is built**, and the returned artifact uses it.
- [ ] Where duration is engineering-set, the grid is what reports the overrun — not a paragraph.
- [ ] On handover, the generator is retired and the index instruction reversed **before** anyone re-runs it.
- [ ] A milestone never implies completion it cannot deliver.
- [ ] Phase −1 asks what decision the artifact serves, and declines rows outside it.
- **Verdict: `PENDING`.** Same engagement as Evolution 1, still pre-signature, and every hypothesis is a
  refinement of machinery authored one day earlier. Pattern 3 is the highest-value observation in this file:
  **Ev.1 assumed the seam's failure mode was rejection; the real end state is transfer**, and the skill had no
  guidance for the moment a practitioner takes the artifact and keeps it. Phases 0–4 remain entirely
  unvalidated — this skill still has no post-signature trace of any kind.

## Evolution 3 — 2026-08-04 — A remedy clause written before signature

### Harvest scope
Not a completed engagement — this skill's normal substrate. A **pre-signature** trace, which this skill
explicitly claims under the pre-signature exception: the effort number and the acceptance shape are what
delivery will later be held to, so they are delivery's to author. The engagement is a PoC bid where an
internal review demanded criteria that "cannot be argued against", and the first four thresholds went to two
adversarial reviews and were replaced.

### Patterns found

**P1 — Acceptance criteria without a remedy clause are ways not to get paid. `Impact: H, Effort: L`.**
Four numbers were drafted as *"the basis on which the work is accepted or disputed"* with **no statement of
what happens if one is missed**. No root-cause step, no re-run right, no distinction between our
underperformance and a client obligation that never arrived. A criterion missed for want of client-supplied
ground truth would have read identically to one we simply failed.

**P2 — "Not measurable" and "failed" are different verdicts and must be separately reachable.
`Impact: H, Effort: L`.** The measurement depended on labels the client had not committed hours to produce.
Without a distinct bucket, an unmet client obligation converts silently into a supplier failure — the exact
absorption this skill exists to prevent, arriving through the acceptance annex rather than the schedule.

**P3 — On a PoC, wiring a missed target to payment rebuilds the shape you just escaped. `Impact: M, Effort: L`.**
The prior criteria set had already been recorded as mis-aimed for being fixed-price acceptance gates on an
exploratory stage. Attaching money to a miss would have reintroduced that frame under a new number. The
consequence chosen instead: the miss conditions **the supplier's own** go/no-go recommendation for
production, which is real without being a payment gate.

### Hypotheses applied

| # | Pattern | Edit |
|---|---|---|
| H1 | P1, P2, P3 | **Correction belongs in `solution-architect`** rather than here — the artifact is authored pre-signature and lives in `references/acceptance-and-contract.md`. The three-bucket remedy is: supplier underperformance, with one re-run right · client obligation unmet, reported *"not measurable"* · scope change, re-baselined. This follows the loop's own note that a contested criterion is written ambiguously **upstream** |

> ⚠ **H1 is specified, not applied.** This entry originally read *"is recorded there"*. Verified 6 Aug:
> `solution-architect/references/acceptance-and-contract.md` contains no remedy clause, and that skill's
> Evolution 7 landed the criteria **tiering** sections only. The remedy above has never been written into the
> file that authors the artifact. Corrected here rather than by writing the clause, because the record of what
> was applied has to match what is in the file — this is the same defect class as `artifact-integrity.md`'s
> **C3a: a link is not a warrant**, arriving in an evolution log instead of a traceability map.

### Validation results
**`PENDING`**, and weakly evidenced — the clause has not been tested by an actual miss, which is the only
thing that validates a remedy clause, **and cannot be until H1 is actually applied**. The specific question for a later harvest: **when a target was missed,
did the three-bucket split hold, or did the argument relocate to which bucket applied?** If bucket assignment
becomes the new dispute, the clause needs an adjudication route of its own, and the fix is `REVISED` rather
than a stronger clause.
