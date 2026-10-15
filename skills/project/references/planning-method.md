# Planning method

## Frame the plan from a brief

Start with the outcome the work should create, then name the deliverables and the success measure. On client work, distinguish the client's objective from the work they want done; a brief gives the team context and exposes questions that need answers before detailed planning. (5907 · U3 · L20 · 01:20–02:47)

Check what a success measure means and over what period before using it to order work. (5907 · U3 · L20 · 02:47–03:41)

Clarify the actual deadline and what the budget must cover before turning a brief into a schedule. (5907 · U3 · L20 · 05:12–06:41)

Identify who has final approval so that review and sign-off can be planned as real work. (5907 · U3 · L20 · 07:20–08:37)

Before the first WBS build, also settle whose template it uses and where the scope ends (which sites, phases or releases are in). Each answer that arrives after a build costs a rebuild. (derived: LSP 2026-10-01..08 — the review board as audience, the team template and a one-gate scope each arrived after a build; the WBS went through five versions in eight days.)

Write down who decides what and whose word outranks whose before planning, and the route for raising issues. On one client project the order was: the client's latest document, then the client's Q&A answers, then the tech lead, then everyone else; issues went through the accountable PM. (derived: LSP 2026-10-08 — the order was applied case by case and never written down.)

Record explicit exclusions with a reason and rough size, or mark the size unknown; ask the approver to confirm the list. (derived: dogfood 2026-10-01)

When the work changes an existing system, ask its technical owner for an as-built inventory of the repository, test status, data stores, third-party components and licences, and known demo-only shortcuts. Compare that state with the intended outcome and add a WBS row for each confirmed gap with `Origin = as-built gap`. The project lead records the planning gaps; the technical owner verifies the system facts. (derived: dogfood 2026-10-01)

Keep the core project information in a shared master plan or workbook: objective, deliverables, tasks, dates, owners, priorities, and only the indicators the team needs to watch. Choose a format the group can use and update. (5907 · U2 · L07 · 03:23–06:29)

Write down tasks and make their priority visible to the team. This makes the order of work easier to coordinate; urgent does not automatically mean important. (5907 · U2 · L08 · 00:54–01:38)

## Choose a useful view

Choose among a calendar, Kanban board, and Gantt chart based on what the team needs to see. Each offers a quick view of tasks and processes, but they answer different planning questions. (5907 · U2 · L10 · 01:55–02:48)

Use Kanban when work has distinct stages or short, well-defined sprints that need frequent status review. Columns may represent stages, priorities, or task owners. (5907 · U2 · L12 · 00:00–01:54)

Use Gantt for complex, dated work where the team needs to see task start and end dates, durations, order, dependencies, and milestones. It is a poor fit before tasks have planned start or delivery dates. (5907 · U2 · L13 · 00:09–02:17)

## Decompose, sequence, and prioritize

Use the WBS guidance in [the workbook reference](wbs-workbook.md) to turn deliverables into a project-suitable work structure.

For a release plan, first identify the outcome that matters outside the system. Slice out the smallest release that can create that outcome, then prioritize later work by the benefits it is meant to produce. A feature list without target outcomes gives the team no sound basis for ordering work. ([book:user-story-mapping], Slice Out a Minimum Viable Product Release; [book:user-story-mapping], Don’t Prioritize Features—Prioritize Outcomes)

One useful release sequence is an opening slice that works end to end, a middle slice that fills in important optional steps and rules, and an end slice that improves the product using real use and feedback. ([book:user-story-mapping], Opening-, Mid-, and Endgame Strategy)

When a work item is too large for a useful sprint commitment, discuss what is good enough first, what would make it better, and what would make it best. This separates a sufficient slice from later refinements without discarding the larger idea. ([book:user-story-mapping], Split and Thin)

Prepare sprint planning ahead: choose likely work a cycle or two early, refine large items with the team before the planning session, then state the cycle goal and give the delivery team time to plan its own work. ([book:user-story-mapping], Split and Thin)

To bridge WBS rows into a sprint candidate set, carry their WBS IDs into the backlog. Consider P0 decision rows and long-lead dependency requests first, then check that the candidates form a thin outcome slice and fit the team's capacity. (derived: dogfood 2026-10-01)

If the planner or team is not available yet, issue a `Draft for planner`: use a WBS with an empty effort column (or a schedule-position grid when that is the needed form), show a proposed sprint goal and candidate list as uncommitted, mark capacity unknown, and list open decisions. Turn the draft into a commitment only after the responsible leads supply estimates, capacity is checked, the team reviews the candidate set, and the accountable owner explicitly approves it. (derived: dogfood 2026-10-01)

## Schedule with capacity and slack

Set the planning period and milestones, list the steps to reach each milestone, estimate task duration with the people doing the work, and mark which dependencies are sequential and which work can overlap. (5907 · U2 · L11 · 15:41–17:15)

Group compatible work into useful calendar blocks and leave open capacity for replanning, rest, and unexpected work. Reserve recurring time for planning the next day or week. (5907 · U2 · L11 · 07:20–12:24)

Keep the shared schedule current as task dates or dependencies change. Treat it as a roadmap the team uses to coordinate; discuss material date changes with the team and refresh the plan rather than leaving old dates in circulation. (5907 · U2 · L13 · 05:14–07:15)

Shorter durations need more people, down to the length of the critical path. Report duration options as a table of team size, end date and slack, not as a single minimum. The fastest plan usually has no slack and can put the critical path in the client's hands (their reviews, data, approvals); recommend the option that keeps slack for the people delivering it, and show the cost of the faster ones.

For client work, put review and approval windows on the schedule. Learn who must respond and when; plan other work that can proceed while feedback is being gathered so a slow review does not stop the whole team. (5907 · U3 · L18 · 01:20–02:54)

## For client-backed work

Use the brief and agreed scope document as inputs to the internal work plan. A statement of work records the agreed deliverables, cost, and timing. (5907 · U3 · L22 · 00:00–01:11)

While the client's answers are pending, keep the open questions as part of the plan: each question names the WBS rows or assumptions its answer changes, and an answer is applied to the plan the day it arrives, with the change listed. (derived: LSP 2026-10-08 — one day of client answers removed liveness and uniform checks and changed the time target, and was applied in a rebuild.)

The client-facing plan can show a high-level phase timeline while the detailed task plan is prepared after project initiation. Keep the view understandable and show approval milestones; dates may move as the detailed plan develops. (5907 · U3 · L23 · 02:47–04:04)

Signed-engagement baselines and acceptance, change, and obligation records remain with `delivery`.
