# Running acceptance

Acceptance is where a fixed-price engagement is actually won or lost. The build can be excellent and the
engagement still fail here — held open by a client who won't test, disputed over what "working" meant, or
quietly expanded because rejecting a deliverable is cheaper for the client than raising a change request.

The presale side — writing criteria, negotiating the contract terms — belongs to
`../../solution-architect/references/acceptance-and-contract.md`. This page is about **executing** them.

## Before any test runs: is it actually testable?

Per criterion, confirm all five. A criterion missing any of them will generate a dispute:

| | Check |
|---|---|
| **Preconditions** | What must exist for the test to even run — data, environment, accounts, integrations, a trained user |
| **Preparer** | Which *party* provides each precondition. Most acceptance disputes trace to a precondition nobody owned |
| **Method** | How it will be demonstrated — test script, sample run, live demo, document review |
| **Pass condition** | What specifically constitutes a pass, in terms both sides read identically |
| **Signatory** | Who on the client side is authorised to sign this off |

A criterion whose pass condition is "the system performs adequately" is not a criterion; it is a future
argument. Raise it as a defect in the annex *before* you build against it.

## Defect severity — define the consequence, not just the label

Nearly every contract classifies defects. Most classify them uselessly, because they define what each class
*means* but not what each class *does*. The consequence mapping is the load-bearing part:

| Severity | Meaning | **Consequence** |
|---|---|---|
| **Critical** | Core function unusable; data loss or corruption; security exposure | Blocks acceptance. Fix and re-test before sign-off |
| **High** | Major function impaired, no acceptable workaround | Blocks acceptance, or conditional acceptance with a fix deadline |
| **Medium** | Function impaired but a workaround exists | Does **not** block acceptance. Fixed within warranty by an agreed date |
| **Low** | Cosmetic, minor UI, wording | Does **not** block acceptance. Backlog / warranty |

Two rules that prevent most disputes:

- **Severity is assessed against the criterion, not against opinion.** "It's critical to us" is a priority
  statement, not a severity classification. Priority orders your queue; severity determines whether the
  deliverable is accepted.
- **Only Critical and High can block.** Without this, any deliverable can be held indefinitely on an
  accumulation of cosmetic findings — which is the single most common way fixed-price acceptance is used as
  a free change-request channel.

Where a defect is genuinely a **new requirement** rather than a failure to meet an agreed criterion, it is
not a defect at all. It is a change request. Say so at the moment it is raised, politely and immediately —
the classification gets much harder to argue a week later.

## The response window, and what silence means

The mechanics that must be settled in the contract before Phase 3 begins:

- **Testing window** — the client's period to test after you submit. **15–20 business days is market
  standard**; shorter for small deliverables.
- **Response deadline** — a written acceptance notice *or* an itemised deficiency report, typically within
  **~5 business days** of the testing window closing. "Itemised" matters: a rejection without specifics
  cannot be acted on and should not be accepted as a rejection.
- **Deemed acceptance** — if no written response arrives within the window, the deliverable is **deemed
  accepted**. This is standard, and it is the *only* structural answer to the silent client.
- **Re-test cycle** — after a fix, a defined (usually shorter) window applies, and re-testing is scoped to
  the reported defects. Without this, each re-submission reopens the whole deliverable to fresh findings and
  acceptance never converges.

**If deemed acceptance isn't in your contract, that is a commercial escalation, not a delivery problem.**
Without it, a client who simply stops replying can hold the final payment indefinitely while your team is
demobilised and your costs are already sunk. Flag it upward the moment you discover it, and record the
exposure in writing.

## Conditional acceptance — useful, and dangerous

Accepting with a schedule of agreed open items lets the engagement move forward. It's a good instrument,
badly used. Make it safe:

- The open items are **listed, severity-classified, and dated** — never "a few small things."
- Acceptance and any linked **payment are released now**, not held pending the open items. If payment is
  withheld, this isn't conditional acceptance; it's rejection with softer wording, and it should be recorded
  as rejection.
- The list is **closed** — no items added later to the same conditional acceptance.

## The silent client — the escalation ladder

Chronologically, before the deadline bites:

1. **Cycle 1** — written follow-up to the focal point, restating the deadline and the deemed-acceptance date.
2. **Cycle 2** — flag in the status report as an *overdue client obligation* with the number of days and the
   named owner. This puts it in the permanent record.
3. **Cycle 3** — escalate to the agreed escalation contact, in writing, stating the schedule and cost
   consequence.
4. **At the deadline** — invoke deemed acceptance in writing, or invoke the standby/idle rate if the
   contract provides one.

Do all of this in a neutral, factual register. The purpose is not to win an argument; it is to make sure the
consequence of the delay lands where the delay was caused, and that this is documented before anyone
disputes it.

## Evidence

Every accepted criterion carries: the **test record** (what was run, when, by whom, with what result), the
**signatory**, and the **date**. A criterion marked passed with no evidence is not accepted — it is
remembered as accepted, which is a different and much weaker thing when the final invoice is queried.
