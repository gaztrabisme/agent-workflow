# Change control

On a fixed-price engagement, **uncontrolled change is the failure mode that eats the margin.** Not one big
scope reversal — dozens of small accommodations, each individually reasonable, none of them priced.

The instrument is boring and it works: everything new is *baseline*, *change request*, or *declined*. There
is no fourth category, and "we'll absorb this one" is not a category — it is a decision to reduce your own
margin, which may be right, but must be a decision rather than a drift.

## The workflow

```
raised → impact-assessed → priced → decided → re-baselined
```

1. **Raise.** Anyone can raise; log it the day it appears. Record who asked, when, and *in what words* —
   the original phrasing matters when scope is later disputed. A CR raised verbally and logged the same day
   is fine; a CR remembered three weeks later is not.
2. **Impact-assess.** Effort, schedule, cost, risk, and **which acceptance criteria are affected**. The last
   one is the part people skip, and it is the one that matters — a change that alters a criterion changes
   what you are contractually obliged to deliver.
3. **Price.** At the contractually agreed change-request day rate. Agreeing that rate during the deal
   (SA's job) is what makes this step a calculation instead of a negotiation.
4. **Decide.** Approved / rejected / deferred, by the named authorised counterpart, **in writing**.
   Approval by someone without authority is the most expensive kind of approval.
5. **Re-baseline.** On approval, the baseline moves: scope, schedule, cost, and the acceptance tracker gains
   or amends rows. **A CR that is approved but never re-baselined is worse than no CR process at all** — you
   now have a documented promise and an unchanged plan, and the variance report will blame the team for a
   slip the client bought.

State the impact in the client's terms, not yours: *"this adds 6 days and moves acceptance of criteria
F3.1–F3.4 from 12 May to 22 May"* — not *"this is a medium change."*

## Scope creep vectors that don't look like change

These are the ones that get absorbed, because none of them arrive labelled "change request":

- **The clarification that isn't.** "Just to confirm, it will also handle X?" — where X was never in scope.
  Answer the question honestly and separately from the scope implication: *"It doesn't today. Would you like
  a CR priced for it?"*
- **Defect-shaped requirements.** A new requirement raised as a defect during acceptance. Classify it at the
  moment it's raised (see `acceptance-execution.md`), not later.
- **Environment drift.** The client's landscape changes mid-engagement — a system upgraded, an API version
  moved, a security policy tightened. Your baseline assumed the old one. This is change, and it is usually
  nobody's fault, which makes it *easier* to raise, not harder.
- **The helpful extra.** Your own team adds something unasked because it's "quick." This is unpriced scope
  you inflicted on yourself; it also resets the client's expectation of what's included.
- **Volume drift.** Same functions, more of them — more report types, more document formats, more user roles.
  Where the baseline named a count, the count is scope.
- **Stakeholder substitution.** A new client-side stakeholder arrives with different expectations and no
  memory of the agreed criteria. Re-anchor to the signed annex immediately and in writing; do not re-litigate.
- **The pilot that became production.** Scope agreed for a proof of concept, quietly held to production
  standards for availability, security, and support.

## The pushback script

The moment matters more than the wording. Raise it when it's asked, not after you've done it:

> "Happy to do that — it's outside the signed scope, so let me raise a CR with the impact and cost, and you
> can decide. Should take a day to assess."

This works because it is not a refusal. It routes the request into a process rather than into an argument,
and it makes the cost visible *before* anyone is committed. The alternative — absorbing it and mentioning
the strain later — trains the client that scope is free and leaves you no record when the margin is gone.

If the answer is *"it's too small for a CR"*: log it anyway as a **zero-cost CR**, approved. The log entry
is the point — it is what lets you show the accumulated pattern at the fifth one, and it costs nothing to
agree to.

## Re-baselining discipline

- **Re-baseline on approved change, not on slippage.** A schedule missed for delivery reasons is *variance*
  and must stay visible as variance. Quietly re-baselining to erase it destroys the only signal that says the
  engagement is in trouble — and it is the delivery equivalent of modifying success criteria to match what
  you built.
- **Keep the original.** Version the baseline; never overwrite. `baseline-v1` → `v2` with the CR that caused
  it named in the change record. The comparison between v1 and final is the harvest for the next estimate.
- **One re-baseline per approved CR**, or batch them at a defined cadence — but never continuously. A
  baseline that moves every week is not a baseline.
