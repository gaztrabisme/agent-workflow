# Client-Obligation Register — template

*What the **client** must physically deliver, by when, or the schedule slips. Distinct from the assumptions
register: an assumption you can proceed on; an unmet obligation stops you. Guidance:
`../acceptance-and-contract.md`.*

**Two rules that make it work:** deadlines are **schedule-relative** ("on signature", "week 1 phase 1"), not
absolute — so the register survives a start-date slip. And every row carries a **named client focal point**;
a deadline with no name is a wish.

*Group rows so the client sees what they owe now versus later. The **Contract terms** group is first because
those rows cost money to fix after signature.*

| # | Group | Item the client provides / both parties agree | Serves criterion | Linked question | Proposed deadline | Client focal point | Completed | Status |
|---|-------|-----------------------------------------------|------------------|-----------------|-------------------|--------------------|-----------|--------|
| 1 | Contract terms | `[nominate a single authorized focal point with decision authority]` | — | | On signature | | | Not delivered |
| 2 | Contract terms | `[agree the four defect-severity definitions in writing]` | — | | On signature | | | Not delivered |
| 3 | Contract terms | `[agree the client's acceptance-response deadline before a submission is deemed accepted]` | — | | On signature | | | Not delivered |
| 4 | Contract terms | `[fix T0 — the precise event that starts the delivery clock]` | — | | On signature | | | Not delivered |
| 5 | Contract terms | `[state volume caps numerically: documents, users, transactions, hours]` | `[TC-x.y.z]` | `[Qn]` | On signature | | | Not delivered |
| 6 | Contract terms | `[agree the change-request day rate]` | — | | On signature | | | Not delivered |
| 7 | Contract terms | `[agree the standby rate when client-caused delay holds the team idle]` | — | | On signature | | | Not delivered |
| 8 | Contract terms | `[name the acceptance council and whether one dissent blocks]` | — | | On signature | | | Not delivered |
| 9 | Infrastructure | `[power, network, cabinet space at every install location]` | `[TC-x.y.z]` | | Before each phase milestone | | | Not delivered |
| 10 | Phase 1 | `[the source data, in an agreed format, at an agreed volume]` | `[TC-x.y.z]` | `[Qn]` | Week 1 phase 1 | | | Not delivered |
| 11 | Phase 1 | `[test accounts across the permission groups needed to prove access control]` | `[TC-x.y.z]` | `[Qn]` | Before UAT | | | Not delivered |
| 12 | | | | | | | | |

**Status vocabulary:** `Not delivered → Partially delivered → Delivered → Waived (with reason)`.

*Every row should trace to a criterion whose test cannot run without it — that traceability is what makes
the register a schedule instrument rather than a wish list. Rows serving no criterion belong in the
contract-terms group or don't belong at all.*
