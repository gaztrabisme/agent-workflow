# Estimating

How each effort figure in a plan or WBS is produced, shown and later checked. The workbook mechanics (columns, collection forms, roll-ups) are in [the workbook reference](wbs-workbook.md); the price, margin and tolerance side is in [the business case reference](business-case-and-tolerances.md).

## Read past lessons before the first figure

Before drafting any estimate, read the estimates-against-actuals file and any lessons recorded on past projects. If neither exists, say so in the plan note: every figure in the plan is then judgement, and the reviewer should know that. A project that is a first of its kind looks for outside experience instead (books, a colleague who has delivered one). [book:prince2-managing-successful-projects], 3.2. Learn from experience

A lesson counts only once it changes something. A lesson written down and not applied to the next plan is still only "identified". [book:prince2-managing-successful-projects], 3.2. Learn from experience

## Plan from products, then activities

List what must be delivered before listing tasks: each deliverable with its acceptance check, plus the inputs that come from outside the team (the client's footage, another company's hardware). Then derive the activities for each deliverable, including management, quality checks and the time spent waiting for approvals, which plans often leave out. An outside input is a dependency and a threat to the plan, not a task. [book:prince2-managing-successful-projects], 9.3. Guidance for effective planning

## Every row states its basis

**Every row states its basis**, one of: actuals from a named past project, analogy to a named past project, parts breakdown, or expert judgement. Rows on expert judgement alone are flagged for their lead. Recommend range estimates grounded in calibrated historical data, expert judgment, or analogy. [book:swebok], 2. Software Project Planning. (derived: LSP 2026-10-01 — 167 of 169 tasks were "three-point expert estimate, no reference actuals" and could not be defended row by row.)

The person who will build the deliverable estimates it or confirms a draft of it (see [the workbook reference](wbs-workbook.md)), and the estimate states its assumptions and exclusions. Assume about 80% of a person's time is productive, and expect estimators to be optimistic. [book:prince2-managing-successful-projects], 9.3. Guidance for effective planning

An estimate has two parts: the figure and how sure it is. Near-term work is estimated in detail with a narrow range; work beyond the planning horizon is estimated in outline with a wide range, and is re-estimated at the stage boundary before it starts. Say which rows are outline. [book:prince2-agile], 12.3: PRINCE2 Agile guidance for the plans theme; [book:prince2-managing-successful-projects], 9.1. The plans theme

**Get two independent estimates per feature where you can** (for example the tech lead's plan and your own breakdown). A gap over 30% is a scope question before it is a speed question: find the assumption that differs before averaging. (derived: LSP 2026-10-08 — three estimates of the same AI features differed by more than 30% on most rows, e.g. face enrolment 8 vs 40 days; each large gap traced to a scope assumption such as photo collection or a shoe detector.)

A row its lead cannot break into parts is not understood well enough to estimate. Decompose it, or plan a short investigation task first and estimate after it. Set the size above which a row must show its parts (the team's threshold, or 30 days if it has none) and list the rows above it. [book:project-planning-scheduling-control], CHAPTER 8 Implementation Planning; [book:head-first-pmp], Tools and techniques for Define Activities

## Activities derived as a percentage

Deriving requirements, testing or PM effort as a fixed percentage of coding is a parametric estimate. It holds only when the ratios come from the team's own past projects; state where each ratio comes from. [book:prince2-managing-successful-projects], 9.4. Techniques: prioritization, estimation and scheduling

An adjustment made to coding (AI assistance, a reuse saving) does not pass through to the derived activities by itself. Writing specs, reviewing generated code and testing it can grow when coding shrinks. Set those rows on their own basis after the coding adjustment. (derived: LSP 2026-10-12 — a per-task AI cut on coding also cut requirements, testing and acceptance support, because each was a fixed percentage of coding.)

## AI-assisted work

Split each task by what limits its duration:

| Task type | What the effort is | What AI changes |
|---|---|---|
| Built by an agent from a spec | Writing the spec, reviewing and integrating the result | The build time, by a factor from your own measured runs |
| Bounded by people | Client reviews, approvals, answers to questions, teammates' feedback | Nothing; it is calendar time |
| Bounded by the physical world | Measuring on real data, labelling, site surveys, hardware tuning, acceptance tests on site | Little; state any saving per task |

- **Show the adjustment as its own column** beside the base estimate, with a one-line reason per task type, the same way the buffer is shown separately. (derived: LSP 2026-10-12 — the team's re-estimate added a per-task "AI-adjusted" column with a reason by task type, which made each cut reviewable.)
- **Apply it once.** A per-task AI column and a flat AI factor on the total are two applications of the same assumption. (derived: LSP 2026-10-12 — a flat 0.8 factor stayed on top of the new per-task figures; the combined cut on coding was about 0.45, and it also reduced field work the task notes said AI does not speed up.)
- **Basis:** your own measured runs, from prompt to accepted result, on the same kind of task. Until those exist the factor is an assumption: state it, show a range, and recalibrate after the first sprints. [book:prince2-agile], 12.2: The agile view of the plans theme
- **Record AI use with actuals** (below), so the next estimate has a measured factor.

## Where contingency lives

Keep three amounts apart, each with its owner. [book:prince2-managing-successful-projects], 10.3. Guidance for effective risk management; [book:prince2-managing-successful-projects], 11.3. Guidance for effective change control

| Amount | What it is for | Who controls it |
|---|---|---|
| Tolerance | How far a plan may deviate before it is escalated; a limit, not money to spend | Set by the level above (client or internal board for the project, the project board for a stage) |
| Risk budget | Paying for planned responses to named risks, plus a provision for risks not yet identified | Drawn through the risk approach, not by the PM at will |
| Change budget | Paying for change requests the client approves | Agreed with the client; held by the change authority |

When the team's template has a single buffer, keep it, and state in the basis which of the three it stands for. Tolerance never funds a change request. [book:prince2-managing-successful-projects], 11.4. Technique: recommended issue and change control procedure

State a confidence level with every estimate, from the evidence behind it: high when the scope is traced to the client's words and no input is missing; medium when it rests on assumptions, missing inputs or another party's work; low when the scope is not traced or a test of the approach has failed. A low-confidence estimate is a range to recover from, not a price: say what must be resolved, and by whom, before it can be quoted. [book:pmbok-guide-7e], 2.4. Planning Performance Domain

Build the risk budget from named causes. Each line names the cause, its evidence, its effect on effort, time or cost, its owner, and what would remove it; the provision for risks not yet identified is its own line. Do not cover a missing input with a larger general buffer. [book:pmbok-guide-7e], 2.8.5.3 Management and Contingency Reserve; [book:prince2-managing-successful-projects], 10.3. Guidance for effective risk management; [book:prince2-managing-successful-projects], 10.4. Technique: recommended risk management procedure

## Keep estimates against actuals

When a project you estimated is delivered, record each feature's estimate beside its actual effort, with the basis it used and whether agents did the build, in a file the user names. Use those records as the analogy basis and the AI factor for the next estimate. Without them every estimate starts from judgement again. A past project the user has already delivered (on LSP: the user's PPE project) is the first anchor if its effort was recorded. [book:swebok], 2. Software Project Planning; [book:prince2-managing-successful-projects], 20.4. Activities. (derived: LSP 2026-10-10 — no estimate in the bid traced to actuals.)

At close, also record the lessons: what went well, what went badly, and what to change next time, each with its cause. [book:prince2-managing-successful-projects], 20.4. Activities
