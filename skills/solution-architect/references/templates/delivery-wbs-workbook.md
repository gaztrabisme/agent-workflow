# Delivery WBS — work-collection instrument

Use this form when a delivery planner owns effort estimates, release split, and staffing. It is a task inventory for estimation, not a priced client attachment, project plan, scope narrative, or signed-client tracker.

## Collection instrument rules

The planner authors the effort estimate. Ship the work inventory with effort cells empty, highlighted, and fill-only. Ask the planner which form they need: an empty effort column when effort is unknown, or a schedule-position grid when duration is the unknown. Do not arrive with an architect-authored estimate or a pre-decided release split.

### WBS sheet

| Column | Content |
|---|---|
| WBS ID | Stable hierarchical identifier shared with other sheets |
| Feature group / Feature / Task | Three levels; one task is one deliverable a discipline can finish |
| Source / traceability | Client module, challenge, or wireframe reference; mark internal work explicitly |
| Release | Buyer’s vocabulary; the planner sets the boundary |
| Priority | P0 / P1 / P2, with a shared meaning |
| Discipline | Discipline that will estimate and staff the task |
| Complexity | S / M / L with an anchor for each discipline |
| Estimated effort | **Blank; planner fills** |
| Depends on | Typed WBS identifiers |
| Uncertainty driver | At most 12 words describing what must be true for the estimate to hold |
| Notes | One clause; put decisions in the decision record and link them |

### Optional schedule-position grid

If duration is unknown, ask for the committed schedule boundary, provide two weeks beyond it, and place task bars in dependency order. Put milestones on the time axis rather than across task rows. Remove columns whose value is constant for every row.

### Summary and traceability

Calculate summary values from detail; do not type totals. Show counts and collected effort by group, release, and priority. Trace every client challenge forward to a WBS row and review each internally originated row as differentiation or scope creep.

### Handover

Use fill and reference formatting consistently. Add a short assignment note naming who fills each discipline and by when. When the recipient starts hand-editing, mark the delivered workbook as hand-maintained and retain any generator as a record rather than regenerating over the planner’s edits.

## Rules for the delivery planner

- Give the delivery planner an enumerated work inventory and leave the effort column empty for its estimates.
- Trace each requirement from its origin to its satisfying deliverable in a traceability matrix, rather than relying only on source labels on WBS rows [book:pmbok-guide-7e], 4.6.6. Visual Data and Information.
- Trace client challenges to their coverage status and WBS references [book:head-first-pmp], Chapter 5. Scope management: Doing the right stuff.
- Trace every client challenge forward to a row and do not leave silent gaps.
- Review every internally originated WBS row as either differentiation or scope creep.
- Label GAP rows as the differentiation and win-theme list.
- Before shipping, ensure sheets describing work outnumber sheets defending the estimate; otherwise remove defensive sheets.
- Limit long prose cells to no more than one per 100 non-empty cells and assert the budget in generated workbooks.
- Anchor every row in Source and justify or remove each Ours row.
- Check that every column is readable to the recipient without a glossary.
- Recompute summary formulas from detail and do not type totals.
- Check ID namespaces for uniqueness while preserving deliberately separate registers for different audiences.
- Use the buyer's vocabulary for release names, including after a phase collapse.
- Keep formulas in generated workbooks and open-resave them when cached values are required.
- Keep the priced client attachment in estimation-and-costing.md rather than using the planner WBS for pricing.
- Keep scope narrative and assumptions in the scope document rather than adding them to the planner WBS.
- Keep what the client is bound to in acceptance-and-contract.md rather than the planner WBS.
- Use the blueprint workbook as the multi-round bid carrier rather than the planner WBS.
- Record the reason for each choice in wiki/decisions.md rather than the planner WBS.
- Keep the planner WBS from accreting scope, obligations, risk, cut-order, and commercial-defense work.
