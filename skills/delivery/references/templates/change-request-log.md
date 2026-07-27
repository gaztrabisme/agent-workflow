# Change Request Log — <engagement>

> Everything new is **baseline**, **change request**, or **declined**. There is no fourth option.
> "We'll absorb this one" is a zero-cost CR — log it, approve it, and let the pattern become visible.

**Opened:** YYYY-MM-DD (at kickoff, empty — not after the first contested change)
**Change-request day rate:** *from the contract*

## Log

| CR | Raised | By | Request (their words) | Effort | Cost | Schedule Δ | Criteria affected | Decision | Decided by | Date | Re-baselined |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CR-001 | | | | | | | | Pending | | | v— |

**Decision values:** `Pending` · `Approved` · `Rejected` · `Deferred` · `Approved (zero-cost)`

**Re-baselined** — the baseline version this CR produced. An approved CR with no baseline version here is
the dangerous state: a documented promise against an unchanged plan, which will read as delivery slippage.

## Running totals

| | Count | Effort | Cost | Schedule Δ |
|---|---|---|---|---|
| Approved (priced) | | | | |
| Approved (zero-cost / absorbed) | | | — | |
| Pending | | | | |
| Rejected / deferred | | | | |

*Absorbed effort is margin you spent. It belongs in this table even though nobody invoiced it — it is the
number that answers "where did the profit go?" at close-out.*

## Impact assessment — per CR

Copy per change request. State impact in the client's terms, not internal ones.

**CR-___ · <short title>**

| | |
|---|---|
| Raised by / when | |
| Request, verbatim | *their exact words — this matters when scope is later disputed* |
| Is this actually a defect? | *If it's a failure to meet an agreed criterion, it's a defect, not a CR* |
| Effort | ___ person-days |
| Cost | at agreed CR rate |
| **Criteria affected** | *IDs — added, amended, or removed* |
| Schedule impact | *"moves acceptance of F3.1–F3.4 from 12 May to 22 May"* |
| Risk introduced | |
| If declined | *what the client should expect instead* |
| Recommendation | |

## Absorbed-change watch

Trigger a conversation when any is true:

- [ ] Zero-cost CRs exceed **5** in a single engagement
- [ ] Absorbed effort exceeds **contingency**
- [ ] The same requester has raised 3+ absorbed items
- [ ] Any absorbed item changed an acceptance criterion

The point is not to refuse small favours — it is to notice the fifth one before the margin is gone.
