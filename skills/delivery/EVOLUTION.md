# EVOLUTION — delivery

The ledger for this skill's own improvement. Protocol: `../core/references/evolution-loop.md`.
Harvest source for this skill: **completed engagements** — estimate vs actual, which criteria were contested,
which client obligations slipped, where the trackers failed to catch a problem in time.

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
- **Dogfood gate: NOT RUN.** The evolution loop requires a fresh-context critic using the skill on a real
  task. Recorded explicitly as skipped rather than quietly omitted, per `core` §3. This is a second reason
  the verdict is `PENDING`.

### First validation opportunity

The next fixed-price delivery. Harvest specifically: estimate vs actual per phase, which criteria were
contested and why, which client obligations slipped and by how much, and which of these five templates were
actually maintained past week 3.
