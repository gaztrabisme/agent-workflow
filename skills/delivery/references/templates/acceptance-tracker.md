# Acceptance Tracker — <engagement>

> **The spine.** One row per acceptance criterion, IDs taken verbatim from the signed annex. This table is
> simultaneously the scope list, the progress metric, the test plan, and the invoice trigger. Do not create a
> second numbering system alongside it.

**Progress (computed, not estimated):** `signed / total` = __ / __ = __%
**In flight (reported separately, never summed into progress):** submitted-not-signed = __

| ID | Criterion | Preparer | Preconditions ready | Submitted | Testing ends | Status | Evidence | Signatory | Signed |
|---|---|---|---|---|---|---|---|---|---|
| F1.1 | | Us / Client | | | | Not started | | | |

**Status values** — use exactly these:

| Status | Meaning |
|---|---|
| `Not started` | |
| `Blocked` | Precondition outstanding — **must** have a row in the obligations tracker |
| `In progress` | |
| `Submitted` | Delivered; client testing window running |
| `Rejected` | Itemised deficiency received — see defect log |
| `Conditionally accepted` | Accepted with a closed, dated list of open items; payment released |
| `Accepted` | Signed, with evidence |
| `Deemed accepted` | Response window elapsed with no written response |

## Defect log (against submitted deliverables)

Severity determines whether acceptance is blocked; priority only orders the queue. A new *requirement*
raised as a defect is a change request — classify it at the moment it is raised.

| # | Criterion | Raised | Severity | Blocks? | Description | Status | Fixed | Re-tested |
|---|---|---|---|---|---|---|---|---|
| | | | Critical / High / Medium / Low | Yes (C,H) / No (M,L) | | | | |

## Client obligations

What the client owes. An obligation without a date and a named owner is a cost you will absorb silently.

| # | Obligation | Serves criterion | Owner (client) | Due | Received | Days late | Consequence flagged |
|---|---|---|---|---|---|---|---|
| | | | | | | | Cycle N report / escalated DD-MM |

> Carry these forward from the presale client-obligation register rather than re-deriving them, and convert
> schedule-relative deadlines ("week 1 phase 1") to real dates now that T0 is known.

## Acceptance mechanics (from the contract — fill at mobilisation)

| Term | Agreed value | In contract? |
|---|---|---|
| Testing window | ___ business days *(15–20 typical)* | |
| Response deadline after testing | ___ business days *(~5 typical)* | |
| Deemed acceptance on silence | Yes / **No → escalate** | |
| Re-test window after fix | ___ business days | |
| Re-test scope limited to reported defects | Yes / No | |
| Severity definitions + consequences agreed | Yes / No | |
| Standby / idle rate when client stalls | | |

**Any `No` above is a commercial escalation, not a delivery problem.** Raise it before Phase 3 starts —
these terms are almost impossible to agree once a deliverable is contested.
