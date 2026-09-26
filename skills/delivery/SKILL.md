---
name: delivery
description: "Project management for a signed client engagement — baseline the plan, measure progress against it, control change, drive acceptance, get paid. USE WHEN a contract is signed and the work must now be delivered and accepted: setting a delivery baseline, tracking acceptance criteria to sign-off, chasing client obligations, pricing a change request, writing a client status report, running UAT and defect triage, or diagnosing why an engagement is slipping. Not `solution-architect` — that sells the work and stops at signature; this runs it. Not `dev` — that builds the software; this manages the engagement around the build. Keywords: project manager, PM, delivery manager, project management, baseline, re-baseline, variance, actuals, progress, percent complete, acceptance criteria, UAT, sign-off, defect severity, deemed acceptance, change request, CR, scope creep, client obligations, status report, RAG, milestone, invoice, escalation, slippage, fixed price."
license: MIT
---

# Delivery

Take a **signed engagement** and drive it to **accepted and paid**, without absorbing the client's slippage as your own.

This is the phase nobody writes down. Presale produces a forecast; the build produces software; **delivery is what keeps the forecast and the software attached to each other** — and what makes the difference between "the work is done" and "the work is accepted, the obligation is discharged, and the invoice is payable."

```
business-intelligence → solution-architect ──signed──┐
   (know the client)      (sell the work)            │
                                                     ├──→ [ DELIVERY ]  ── runs continuously
                                                     └──→   dev (build) ── cycles inside it
```

Note the shape: delivery is **not** the next box after `dev`. It runs *concurrently* with the build for the whole engagement. `dev` cycles inside it.

## When this fires — and when a sibling owns it

- **This skill:** anything after the contract is signed that is about the *engagement* rather than the *code* — baseline, progress, acceptance, change, obligations, reporting, escalation, invoicing triggers.
- **`solution-architect` instead:** the deal isn't signed yet — architecting, positioning, writing the proposal, negotiating acceptance criteria and contract terms. SA *produces* the artifacts this skill baselines; it does not track them. **But see the pre-signature exception below: the effort number SA prices is not SA's to author.**
- **`dev` instead:** the unit of work is code — designing a spec, building a feature, assessing a codebase, coordinating a sprint's waves. Delivery says *which* deliverables are due and whether they're accepted; `dev` builds them.

> **Disambiguation rule:** both SA and delivery touch "acceptance criteria," "estimate," and "risk." Decide on **tense**. Criteria being *negotiated* → SA. Criteria being *tracked to sign-off* → delivery. An estimate being *derived* → SA. An estimate being *measured against* → delivery.

### The pre-signature exception

The tense rule has one bounded exception, and it sits exactly where engagements get mispriced. **The delivery planner is a consumer of SA's artifacts *before* signature, not only after it** — because the effort number SA prices is the number this skill will later be measured against, and whoever will be held to an estimate owns authoring it.

> *Observed.* On a live presale, the architect produced a WBS with the effort column filled, capacity pre-derived, releases collapsed to one and the cut order pre-decided. The delivery PM rejected it and rebuilt it — *"too mechanical," "the AI suggestion doesn't look sensible," "I can work this out myself"* — as 234 task rows with the **effort column empty**, tagged by discipline so the sheet could be split and filled by the leads who would do the work.

**An estimate authored by someone who will not be held to it is a proposal for an estimate, not an estimate.** Engaged pre-signature, this skill *supplies* the effort, the release split and the cut order rather than receiving them (`references/delivery-lifecycle.md` → Phase −1). Everything else in the tense rule stands: nothing is baselined, tracked or accepted until there is a contract.

## Anchoring principles

1. **The baseline is the promise; everything else is measurement.** At kickoff, freeze scope, schedule, and cost as the plan of record and record what it was derived from. Without a frozen baseline there is no such thing as variance, only opinion — and an engagement without variance data cannot be argued about, only felt.
2. **Measure with the client's own signature, not your own judgement.** Percent-complete is a self-report and self-reports drift optimistic. On an acceptance-gated deal the honest metric already exists: criteria the *client* has signed off. See `references/progress-measurement.md`.
3. **Client slippage must be visible, dated, and consequential.** The default failure of fixed-price delivery is silently absorbing client delay — you wait for data, wait for access, wait for sign-off, and the schedule loss lands on you. An obligation not tracked with a date and a named owner is a cost you will pay without ever having agreed to.
4. **No unpriced scope. Ever.** Every "small addition" is either inside the baseline or it is a change request with an impact and a price. The word "quick" is a pricing event. See `references/change-control.md`.
5. **Green is a claim that needs evidence.** Status that is green until it is suddenly red was never green — it was unmeasured. RAG must be derived from the trackers, not from mood.
6. **Acceptance is a process with deadlines on *both* sides.** You owe a testable deliverable; the client owes a response within a defined window. Silence must resolve to something, or an engagement can be held open indefinitely by a client who simply never replies.
7. **The engagement is one graph, not a pile of documents.** Everything keys to the acceptance-criteria ID spine declared in presale. A criterion is simultaneously a scope item, a progress unit, a test, and a payment trigger — the same row, four views. Never invent a second numbering system.

## The delivery lifecycle (at a glance)

| Phase | Goal | Primary artifact |
|-------|------|------------------|
| **0. Mobilise** | Convert the signed proposal into a plan of record. Inherit the ID spine; confirm what was actually sold. | Delivery baseline |
| **1. Establish control** | Stand up the trackers before work starts, not after the first slip. | Acceptance tracker + obligations tracker + CR log |
| **2. Run the cadence** | Weekly: update actuals, chase obligations, triage change, report status. | Status report (per cycle) |
| **3. Accept** | Drive each criterion to signed acceptance; run UAT, triage defects by severity, enforce response windows. | Signed acceptance records |
| **4. Close** | Final acceptance, warranty start, invoice release, retrospective into the evolution loop. | Close-out record + harvest |

Full method per phase: `references/delivery-lifecycle.md`. Scale to the engagement — a six-week build does not need a steering committee, but it does need a baseline and an acceptance tracker.

## Gates (declared, not skipped)

Inherited from the `core` kernel. On entry, read the referenced files.

- **Pushback gate.** "Can you just add…", "we'll sort the details later", "let's not raise a CR for something this small" — these are the moments this skill exists for. Challenge before absorbing, and explain the mechanism so the client learns it too. See `../core/references/pushback-and-teach.md`.
- **Grounding gate.** Ground status claims in the trackers, not in recall. Before reporting progress, state the source: `Grounded: acceptance tracker rows 12–18 → 4 of 7 signed`. A status number you cannot point at is a guess. See `../core/references/grounding-gate.md`.
- **Output Contract.** A cycle is not done until the status report and the updated trackers exist on disk and the wiki reflects them. See `../core/references/wiki-protocol.md`.
- **Integrity constraints.** Especially: *never modify success criteria to match what was built.* On an acceptance-gated engagement, quietly softening a criterion to make it pass is not a schedule fix — it is a misrepresentation with money attached.

## Anti-patterns (hard no-list)

- **No frozen baseline** — "the plan" is whatever the last conversation implied. Nothing can be measured or defended.
- **Percent-complete theatre** — 90% for six weeks. If a number can't go down, it isn't a measurement.
- **Watermelon reporting** — green outside, red inside. Usually produced by reporting on effort spent rather than acceptance achieved.
- **Absorbing client delay silently** — the schedule slips, nobody logged whose dependency caused it, and you carry it.
- **Verbal change** — scope agreed in a meeting, never priced, never re-baselined, remembered differently by each side.
- **Acceptance without evidence** — a criterion marked passed with no artifact, no test record, and no named signatory.
- **Two numbering systems** — presale's criteria IDs plus a fresh delivery WBS that maps to nothing. This is how the same fact acquires four different values.
- **Deferring the trackers until things get busy** — control set up under pressure is control set up too late.

## Composition with sibling skills

- **From `solution-architect`:** the estimate, phased roadmap, acceptance annex, client-obligation register, risk register, and the declared **ID spine** → these become the Phase 0 baseline. Delivery *inherits* these artifacts rather than re-deriving them; where delivery finds them inconsistent, that is a finding to report, not to silently fix.
- **Pre-signature, back to `solution-architect`:** the filled effort column, the release split, the cut order, and a capacity verdict. SA enumerates and prices; this skill supplies the numbers. SA's `templates/delivery-wbs-workbook.md` is the instrument that carries them.
- **To/with `dev`:** deliverables and their due dates flow in; built artifacts and their evidence flow back. `dev` runs its own design/build/sprint cycles inside the envelope this skill maintains.
- **Back to `solution-architect`:** every engagement's actuals are the correction signal for the next estimate. A delivery that ran 1.6× the estimate is the most valuable input SA's `estimation-and-costing.md` will ever get. Close the loop deliberately — see `references/delivery-lifecycle.md` → Phase 4.
- **Through the localization review:** on a Vietnamese-speaking engagement, every status report, acceptance note and change request that reaches the client receives an explicit register and language-parity review. This skill owns what the report says and when; the domain owner owns the language quality.

## References

- `references/delivery-lifecycle.md` — the five phases in full, with the per-phase checklist and close-out.
- `references/progress-measurement.md` — how to measure progress honestly on fixed-price work; why 0/100 beats percent-complete; the gaming failure mode of each method.
- `references/acceptance-execution.md` — running UAT, defect severity classes and their consequences, response windows, deemed acceptance, conditional acceptance, the silent client.
- `references/change-control.md` — raise → impact-assess → price → approve → re-baseline; the scope-creep vectors that never look like change requests.
- `references/templates/delivery-baseline.md` — the plan of record.
- `references/templates/acceptance-tracker.md` — the spine: criterion → status → evidence → signatory.
- `references/templates/change-request-log.md` — every CR with its impact and disposition.
- `references/templates/status-report.md` — the weekly/fortnightly client-facing report.
