# Measuring progress honestly

The question this page answers: **"how far along are we, really?"** — in a form you can defend to a client,
to your own management, and to yourself six weeks later.

## The problem with the obvious answer

"We're about 70% done" is not a measurement. It is a *feeling with a number attached*, and it has three
properties that make it worse than useless:

- **It only goes up.** A measurement that cannot fall isn't measuring anything.
- **It is optimistic by construction.** The person estimating remaining work is the person who has to do it,
  and the unknown-unknowns are, definitionally, not in their estimate.
- **It hides the tail.** The last 10% routinely contains integration, environments, data migration, defect
  fixing, and client review — and none of those are visible from inside the 70%.

This is where **watermelon reporting** comes from: green outside, red inside. It is rarely dishonesty. It is
usually the arithmetic result of measuring effort spent against effort *estimated*, when the estimate was the
thing that was wrong.

## Pick the method deliberately

| Method | How it works | Gaming / failure mode | Use when |
|---|---|---|---|
| **Percent complete (subjective)** | Ask the doer | Optimism bias; 90% for weeks; never falls | Never, as the reported figure. Fine as a private smell test. |
| **Effort burn** | Spent ÷ budgeted | Measures *consumption*, not *achievement*. A project can be 100% burned and 0% delivered | As a *cost* control, never as a progress metric. Track it, don't report it as progress. |
| **0/100 rule** | A deliverable counts 0% until fully done, then 100% | Encourages splitting work small; a large chunk shows nothing for a long time | **Default for fixed-price work.** Pair with small deliverables. |
| **Weighted milestones** | Value assigned to sub-deliverables at defined checkpoints | Weights get argued; can be set to flatter progress | Long deliverables where 0/100 hides genuine movement |
| **Acceptance-criteria passed** | Criteria the *client* has signed / total | Requires the client to actually respond — needs the response deadline from `acceptance-execution.md` | **The reported metric on any acceptance-gated engagement** |
| **Full EVM (CPI/SPI)** | Earned value against planned value | Heavy machinery; the setup cost exceeds the value at small scale | Multi-year, multi-team capital programmes. Not a small consulting engagement. |

## The default: 0/100 on the acceptance-criteria spine

On a fixed-price, acceptance-gated engagement the honest metric already exists in the contract:

```
progress = criteria signed by the client / total criteria in the spine
```

It is the right metric for three converging reasons:

1. **It's binary.** A criterion is signed or it isn't. There is no 70%, so there is nothing to inflate.
2. **It's externally verified.** The client's signature is the evidence. Your own opinion doesn't enter.
3. **It's already the cash trigger.** On an acceptance-gated deal, the same row that measures progress
   also releases the invoice. Progress, acceptance, and revenue are one instrument rather than three
   that drift apart.

**Do not build a second measurement system alongside it.** The most common way this goes wrong is inventing
a delivery WBS with its own numbering, tracking that, and then having to reconcile two views of "done" that
disagree. One spine.

### Handling the honest objection

Clients and managers will say: *"but nothing shows as complete for the first six weeks."* That is true, and
it is a real weakness of 0/100 — not a reason to abandon it. Two mitigations:

- **Make the criteria small enough that something lands most weeks.** If a criterion takes six weeks to
  reach signature, it is probably several criteria.
- **Report a second, clearly-labelled leading indicator** alongside it — e.g. *criteria submitted for
  acceptance but not yet signed*. This shows work in flight without letting it count as achievement. Keep
  the two columns visibly separate, and never sum them into one headline number.

## Variance is the point

Progress alone says nothing without the baseline to compare it to. Each cycle, record:

- **Schedule variance** — criteria signed vs criteria planned-signed by this date.
- **Cost variance** — effort spent vs effort baselined for the work *actually accepted* (not for the calendar
  time elapsed).
- **The reason** — one line. Variance without a cause is a number nobody can act on.

**Attribute the cause honestly, including when it's the client.** "Behind by 2 criteria; both blocked on
production data access, requested 12 Mar, outstanding 19 days" is a fundamentally different management
situation from "behind by 2 criteria" — and only the first one is actionable, defensible, and fair to your
team.

## Deriving RAG without lying

RAG status should be *computed*, then sanity-checked — not chosen.

- **Green** — variance within tolerance, no unmitigated risk above threshold, no overdue client obligation on
  the critical path.
- **Amber** — variance outside tolerance **or** a critical-path obligation overdue, *with* a credible recovery
  plan that has a named owner and a date.
- **Red** — recovery requires a decision the delivery team cannot take alone: more budget, less scope, a later
  date, or an escalation to the client's management.

Two rules that prevent the watermelon:

- **Red is a request, not a confession.** A red status that arrives with a specific decision needed is doing
  its job. Teams hide red because they read it as failure; state explicitly that it is an escalation channel.
- **Amber must have an expiry.** An amber that has been amber for four cycles is red with better manners.
