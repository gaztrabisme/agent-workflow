# Delivery Baseline — <engagement>

> **Plan of record.** Frozen at kickoff; changes only via an approved change request (`change-request-log.md`).
> Never overwrite — version it. Variance is measured against this document, so if it moves silently, nothing
> downstream means anything.

| | |
|---|---|
| Baseline version | v1 |
| Frozen on | YYYY-MM-DD |
| **T0 (clock start)** | *the named event — signature / deposit received / access granted / kickoff held* |
| T0 actual date | YYYY-MM-DD |
| Derived from | *proposal vX, cost model vX, acceptance annex vX — name the exact versions* |
| Governing-language artifact | *which document wins if two language versions disagree* |
| ID spine | *acceptance-criteria IDs from annex vX — the single numbering for this engagement* |

## Parties

| Role | Name | Authority |
|---|---|---|
| Client focal point | | Single authorised channel for instruction |
| Acceptance signatory | | Signs criteria off (if different) |
| Escalation contact | | Above the focal point |
| Delivery lead | | |

## Scope baseline

Scope **is** the acceptance-criteria set. Do not restate it in prose — reference it, so there is one source.

| | |
|---|---|
| Criteria in baseline | N (IDs …) |
| Explicitly out of scope | *the things worth naming because they were discussed and excluded* |
| Assumptions carried forward | *link to the presale assumptions register* |

## Schedule baseline

| Phase / milestone | Deliverable | Criteria IDs | Planned submission | Planned acceptance |
|---|---|---|---|---|
| | | | | |

## Cost baseline

| Element | Baselined | Notes |
|---|---|---|
| Effort (person-days) | | By phase, **and by discipline** — discipline is what turns a total into a staffing plan, and what makes actuals comparable back to the estimate at close |
| Labour cost | | |
| Hardware / CapEx | | |
| Third-party / licences | | |
| Contingency | | State whether it is held by delivery or by commercial |
| **Total** | | |

*Record the effort distribution this was built on — it is what the next estimate gets corrected against.*

### Capacity fit

A cost baseline that has never been divided by the calendar is a total, not a plan.

| | |
|---|---|
| Available | *N people × M working days = **A** person-days* |
| Required | *the effort baseline above* |
| **Gap** | *required − available* |
| Contingency | *days, and whether delivery or commercial holds them* |

A gap of zero is not a pass — it is a plan with no contingency, and it should be frozen only if someone has
said that out loud. A positive gap cannot be frozen as-is: re-scope, re-staff, or extend, and record which.

## Reconciliation at mobilisation

Run before freezing. Every discrepancy is a finding to report, not to silently fix.

**Each line is a comparison you run, not a box you tick — write the two values beside it.** A tick with no
numbers next to it is a claim *about* a check rather than the check. This table freezes the plan of record,
so a false clean report here has money attached.

| # | Check | Value A | Value B | ✓ / finding |
|---|---|---|---|---|
| 1 | Every criterion in the annex appears in the cost model | *annex: N* | *cost model: N* | |
| 2 | Every function priced in the cost model appears in the annex | | | |
| 3 | Criterion count matches across annex, cost model, and any workplan | | | |
| 4 | Effort baseline fits declared capacity, or the gap is stated and signed | *required* | *available* | |
| 5 | **ID spine is unique across every register** — criteria, decisions, risks, assumptions, obligations. Two registers sharing a prefix is the second-numbering-system failure arriving early *(SA `artifact-integrity.md` C8)* | | | |
| 6 | Language versions agree on scope (governing version declared) | | | |
| 7 | No dangling references to removed items | | | |
| 8 | T0 event is contractually defined | | | |
| 9 | Deemed-acceptance term exists *(if not — escalate, see `acceptance-execution.md`)* | | | |

**Discrepancies found:**

| # | Discrepancy | Values compared | Money at stake | Raised with | Date | Resolution |
|---|---|---|---|---|---|---|
| | | | | | | |

## Baseline history

| Version | Date | Cause (CR ref) | Scope Δ | Schedule Δ | Cost Δ |
|---|---|---|---|---|---|
| v1 | | Initial baseline | — | — | — |
