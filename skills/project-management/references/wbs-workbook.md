# WBS workbook

## Define the decision before choosing rows

Before building or filling the plan, ask what decision it must serve and remove rows that do not help with that decision. If a task does not need discussion, it does not need to be mapped. [book:user-story-mapping], Don’t Sweat the Small Stuff. Then run the lane test on every row: name the recipient and the decision they must make, and check that the row helps that person make it. A row can be correct and still belong to a different plan or reader.

## Choose the effort collection form

Use this WBS instrument when a delivery planner owns the release split and staffing. Treat effort as an input for the planner: enumerate work, but do not fill estimates as the architect or plan author.

Ask the planner which form they want before building the workbook. Choose by the unknown:

| Form | Use when | Collection rule |
|---|---|---|
| Pre-filled estimates | Never from the architect or plan author | Do not choose this form. |
| Empty effort column | The delivery window is fixed and effort is unknown | Ship no numeric values; the responsible lead supplies a number per row. |
| Schedule position | Duration is unknown while effort is roughly understood | Collect when each task sits; its duration becomes visible from the placement. |

Planning and estimation start from the WBS tasks and their schedule relationships. [book:swebok], 7. Software Engineering Management Tools. For a fixed window with unknown effort, keep the column empty and attribute each number to the responsible lead; those collection conventions extend the source method. (5907 · U2 · L13 · 02:17–05:14)

The workbook normally ships without numeric estimates. When using an effort column, leave it empty, highlight it, and mark it fill-only for the planner. Omit that column when schedule position is the information being collected.

When the planner needs to determine duration, ask for a week grid instead of an effort column. Supply `N + 2` week columns where `N` is the duration already committed in public; mark the columns beyond `N` and place task bars in dependency order. The extra columns make the overrun visible. On one engagement, the planner asked for work grouped by week instead of person-days; placing the work in the grid showed it landing in week five against a four-week commitment.

## Show milestones and durations honestly

Present milestones in a milestone schedule with planned dates. In a week grid, place milestones on the time axis in their own row, never as horizontal bands across a feature-ordered task list. A band can read as though everything above it is complete even while later weeks still contain work. One review caught an `End W1` band while its tasks continued into weeks two through four. [book:pmbok-guide-7e], 4.6.5. Baselines. (5907 · U2 · L13 · 05:14–07:15)

Remove any column whose value is constant across every row; it adds no information. A phase column that named the same phase throughout and a priority column with no defined scale were both dropped after the recipient asked what they contributed.

## Structure and staff the WBS

Decompose deliverables into work packages that create them; do not require each row to belong to a single discipline. [book:head-first-pmp], Decompose deliverables into work packages. Repeat the parent group and feature labels on every row so the work stays filterable.

Choose a WBS hierarchy that suits the project. Common structures organize by deliverable or by phase; do not force every plan into feature group, feature, and task as its only three levels. [book:head-first-pmp], Break it down by project or phase. Give each row a stable hierarchical WBS ID that also names it in the workbook's other sheets.

Use the buyer's own vocabulary for release buckets and let the planner set the release boundary. Give each task a P0, P1, or P2 priority so the planner can cut work without rereading it.

Plan resources against each WBS task. Assign a discipline to each row when the planner needs the work divided among leads; this extends the source's use of task-level resources for scheduling. [book:swebok], 7. Software Engineering Management Tools. Use S, M, or L for complexity, with a separate calibration anchor for each discipline.

Represent dependencies as typed WBS IDs, not prose. For generated workbooks, give each task a stable slug, declare dependencies by slug, resolve them to WBS IDs when writing the workbook, and fail the build if any dependency cannot be resolved.

Limit each uncertainty driver to 12 words and state what must be true for the estimate to hold within ±20%. Keep Notes to one clause; put decisions in the project's decision record and link to them from Notes. Make every column understandable to the named recipient without a glossary. An internal reference such as `T0-1` or an undefined priority scale failed that test: if the reader needs the author in the room to decode a field, rename or define it.

## Summarize only from detail

Calculate every summary cell from the work detail with formulas. Roll up counts by group, release, and priority, effort, percent of total, and Origin. Do not type numeric totals into the summary sheet; a typed value can drift away from its source rows.

## Check capacity after collection

Build the capacity view after estimates have been collected. Show the available capacity, effort envelope and exclusions, required versus available effort, the gap, and the trade-offs that could close it. Derive those values from the collected work estimates. Present fit as the planner's post-collection check, not as a constraint imposed before the team has supplied its inputs.

## Register dependencies

For each dependency, record its ID, what is needed, the named provider, a schedule-relative deadline, the WBS IDs it blocks, and what happens if it arrives late. Check the ID prefix against every other engagement register before choosing it.

## Hand over a workbook the planner can edit

Use yellow for fillable cells and grey for reference cells. Include one calibration anchor per discipline and ship the workbook empty with a short assignment note. Keep that note to one paragraph naming who fills each discipline and by when.

When the recipient takes over hand editing, mark the generated workbook final and hand-maintained, reverse any regenerate instruction in the index, and retain the generator as a record only. A prior handover told the planner not to work on the WBS again while the index still said to regenerate it; the next run would have overwritten the planner's edits.
