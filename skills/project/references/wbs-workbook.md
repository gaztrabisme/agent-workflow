# WBS workbook

This reference is for you as project lead and workbook author. Unless a step names the delivery lead, `planner` means you; the delivery lead owns presignature priced-estimate, release-split, and capacity decisions. (derived: dogfood 2026-10-01)

## Define the decision before choosing rows

Before building or filling the plan, ask what decision it must serve and remove rows that do not help with that decision. If a task does not need discussion, it does not need to be mapped. [book:user-story-mapping], Don’t Sweat the Small Stuff. Then run the lane test on every row: name the recipient and the decision they must make, and check that the row helps that person make it. A row can be correct and still belong to a different plan or reader.

For a WBS-based project plan, the default deliverable is a concise plan note plus an editable workbook with these sheets: `WBS`, `Schedule`, `Dependencies`, `Capacity`, `Summary`, and `Key`. Mark an unused sheet `Not applicable` with a reason. Keep the `Capacity` sheet pending until estimates are collected; do not calculate or report fit before then. The note states the outcome, success measure, exclusions, assumptions, open decisions, and which work is proposed or committed. Use a lighter plan artifact when a WBS would not help the decision. (derived: dogfood 2026-10-01)

## Choose the effort collection form

Use this WBS instrument for the project lead's general plan and for a presale WBS. On a presale, this skill runs the structure and the effort collection; the leads who will be held to the estimate author their own rows, and `solution-architect` decides what the WBS must contain and owns the response pack. (owner decision 2026-10-11)

As project lead, enumerate the work and request effort from the responsible discipline leads. Treat effort as an input to the plan; do not substitute an estimate authored by you in the architect's role. Each responsible lead fills or confirms their own rows with authorship and assumptions visible. If you are also the responsible lead for a task, you may fill that row in that role after handover. (derived: dogfood 2026-10-01)

When you draft the WBS for the accountable PM (or as a PM in training), draft every role's effort rather than shipping it empty: each row shows who drafted it, its basis, and the lead who confirms it. Leave effort empty only where no basis exists, and name the lead who will fill it. A draft is a proposal for an estimate until its lead confirms it. (derived: LSP presale 2026-10-01..09 — the team's own PM drafts carried every role's figures; ours were marked as drafts for their leads only on day six.)

Each row states its basis, and large gaps between two estimates are resolved as scope questions first; both rules, ranges and the AI-assisted adjustment are in [the estimating reference](estimating.md).

Before building the workbook, confirm with the person responsible for estimates which form will reveal the unknown. Choose by the unknown:

| Form | Use when | Collection rule |
|---|---|---|
| Drafted estimates | You draft the plan for the accountable PM and a basis exists | Every row shows drafter, basis and confirming lead; never in the architect's role. On a presale this is the default form. |
| Empty effort column | The delivery window is fixed and effort is unknown | Ship no numeric values; the responsible lead supplies a number per row. |
| Schedule position | Duration is unknown while effort is roughly understood | Collect when each task sits; its duration becomes visible from the placement. |

Planning and estimation start from the WBS tasks and their schedule relationships. [book:swebok], 7. Software Engineering Management Tools. For a fixed window with unknown effort, keep the column empty and attribute each number to the responsible lead; those collection conventions extend the source method. (5907 · U2 · L13 · 02:17–05:14)

When effort is unknown, ship the workbook without numeric estimates. Highlight the effort column and mark it fill-only for the responsible lead. Omit that column when schedule position is the information being collected.

When the planner needs to determine duration, ask for a week grid instead of an effort column. Supply `N + 2` week columns where `N` is the duration already committed in public; mark the columns beyond `N` and place task bars in dependency order. The extra columns make the overrun visible. On one engagement, the planner asked for work grouped by week instead of person-days; placing the work in the grid showed it landing in week five against a four-week commitment.

## Show milestones and durations honestly

Present milestones in a milestone schedule with planned dates. In a week grid, place milestones on the time axis in their own row, never as horizontal bands across a feature-ordered task list. A band can read as though everything above it is complete even while later weeks still contain work. One review caught an `End W1` band while its tasks continued into weeks two through four. [book:pmbok-guide-7e], 4.6.5. Baselines. (5907 · U2 · L13 · 05:14–07:15)

Remove any column whose value is constant across every row; it adds no information. A phase column that named the same phase throughout and a priority column with no defined scale were both dropped after the recipient asked what they contributed.

## Structure and staff the WBS

List the deliverables (with acceptance checks and the inputs that come from outside the team) before the tasks; see [the estimating reference](estimating.md#plan-from-products-then-activities). Decompose deliverables into work packages that create them; do not require each row to belong to a single discipline. [book:head-first-pmp], Decompose deliverables into work packages. Repeat the parent group and feature labels on every row so the work stays filterable.

Choose a WBS hierarchy that suits the project. Common structures organize by deliverable or by phase; do not force every plan into feature group, feature, and task as its only three levels. [book:head-first-pmp], Break it down by project or phase. Give each row a stable hierarchical WBS ID that also names it in the workbook's other sheets.

For a client plan, use the client's recorded vocabulary for release buckets and let the delivery lead set the boundary for the priced response. For internal work, use the team's agreed release names. Give each task a P0, P1, or P2 priority so you and the team can cut work without rereading it.

Plan resources against each WBS task. Assign a discipline when your staffing view needs the work divided among leads; for work that spans disciplines, keep the deliverable intact and show its contributing leads instead of forcing a single-discipline row. This extends the source's use of task-level resources for scheduling. [book:swebok], 7. Software Engineering Management Tools. (derived: dogfood 2026-10-01)

Staff by role position (a person allocated to a role for a week), not by fragments of task effort. The PM sets a minimum allocation per role per week (for example: a PM at least half-time; a role that needs two people at no less than one and a half full-time; the first and last week at half), and priced effort follows those allocations. Where the allocations exceed the task estimates, show the surplus as its own line and say which contingency amount it stands for (see [the estimating reference](estimating.md#where-contingency-lives)). Show the staffing plan week by week with a real ramp-up and taper (as the wbs-estimate skill does).

Before collecting estimates, check that every discipline required by the WBS has a named responsible lead. If an owner is not known, show the owner gap instead of implying that the work is staffed. (derived: dogfood 2026-10-01)

Use S, M, or L for complexity, with a separate calibration anchor for each discipline. The project lead records each task's category against an anchor supplied or confirmed by that discipline's lead; complexity is a category, not an effort estimate. (derived: dogfood 2026-10-01)

For a plan whose deliverable is a running software system, check whether the WBS needs work for third-party licence review, security and data protection, deployment and CI/CD, observability and alerts, backup and restore, fallback and retry behavior, upload or administration workflows, user and admin guidance or training, and support, SLA, or maintenance. Ask technical owners which apply and add rows for the applicable gaps. This is a prompt list, not a requirement to add every category to every system. (derived: dogfood 2026-10-01)

Include an explicit contingency row in the WBS for likely test, review, or rework cycles, such as a fix-and-iterate allowance; when none is warranted, record that decision and its reason. The project lead records the reason and owns its inclusion; the responsible lead supplies its effort input. If the amount is not known yet, leave effort blank and list the open sizing decision. (derived: dogfood 2026-10-01)

Represent dependencies as typed WBS IDs, not prose. For generated workbooks, give each task a stable slug, declare dependencies by slug, resolve them to WBS IDs when writing the workbook, and fail the build if any dependency cannot be resolved.

Limit each uncertainty driver to 12 words and state what must be true for the estimate to hold within ±20%. Keep Notes to one clause; put decisions in the project's decision record and link to them from Notes. Make every column understandable to the named recipient without a glossary. An internal reference such as `T0-1` or an undefined priority scale failed that test: if the reader needs the author in the room to decode a field, rename or define it.

## Drafting into a team's WBS

When the user drafts the WBS for the team's accountable PM (as a discipline lead, or a PM in training) and the team owns the file:

- The team's template wins over this skill's default sheet set. Map into it exactly, nothing more or less, and leave the owner's method in place. Project teams may be required to assume the parent organization's methodology, templates included. [book:pmbok-guide-7e], 3.7. Tailor Based on Context
- Fill your own discipline's rows with a parts breakdown behind each figure (for example "rack and wire 1 + commission 1 + spare validation 0.5"), so a later cut is arithmetic, not argument.
- A row for another discipline shows who drafted it and which lead confirms it; never leave our draft looking like their estimate.
- Raise WBS issues through the team's accountable PM, not in the file.
(derived: LSP presale 2026-10-08/09 — the team's PM made one layout standard and asked for a mapping "nothing more or less"; our drafts for other roles had to be caveated as AI-generated in team chat.)

A scope change updates the files the team already works from. A new file, or a different deck or template, is a question for the PM first.

With the PM, answer the question that was asked, not a guessed motive behind it. When an option is hard, state what it would take (its conditions and cost) rather than refusing it.

## Summarize only from detail

Before changing someone else's estimate, recompute their grand total with their own method and treat a match as the anchor; a mismatch is a question for them, not a correction. Ship every later version with a bridge from their total to yours and a short list of what moved and why, so nobody compares line by line. (derived: LSP 2026-10-08 — the tech lead's rule reproduced his 1,683.3575 days exactly; v1.2 carried a bridge from 1,381 to 1,330 days.)

Before pricing anything new on someone else's workbook, also reproduce their current total with their own cost rules (rates, overhead formulas). A formula of theirs that looks unusual (a role on an onsite rate, an allocation that seems high) is a question first; it is often deliberate.


Calculate every summary cell from the work detail with formulas. Roll up counts by group, release, and priority, effort, percent of total, and Origin. Do not type numeric totals into the summary sheet; a typed value can drift away from its source rows. Give each task one primary `Origin` value describing why it exists: `brief/scope`, `as-built gap`, `dependency`, `team input`, or `other` with a short reason. (derived: dogfood 2026-10-01)

## Check capacity after collection

Build the capacity view after estimates have been collected. Show the available capacity, effort envelope and exclusions, required versus available effort, the gap, and the trade-offs that could close it. Derive those values from the collected work estimates. As project lead, present fit as a post-collection check, not as a constraint imposed before the team has supplied its inputs. Until then, mark capacity pending; do not guess figures. (derived: dogfood 2026-10-01)

## Register dependencies

For each dependency, record its ID, what is needed, the named provider, a schedule-relative deadline, the WBS IDs it blocks, and what happens if it arrives late. Check the ID prefix against every other engagement register before choosing it. If you do not know where those registers live, ask the register owner; while waiting, choose a prefix unique within this workbook, mark the cross-register check pending in `Key`, and do not claim global uniqueness. (derived: dogfood 2026-10-01)

## Hand over a workbook the planner can edit

Use yellow for fillable cells and grey for reference cells. Give the workbook one colour legend; a colour means one thing, so any other marking (for example figures you changed in someone else's rows) takes a different fill. Include one calibration anchor per discipline and ship the effort cells empty when estimates are not yet collected. As project lead, write a one-paragraph assignment note naming the lead who supplies each discipline's estimates and calibration anchor, and the due date.

Before a primary workbook or proposal goes out, have it checked by a reviewer who has not seen its drafting, a fresh one each round, for at most three rounds (as the technical-proposal skill does); if the third round still has open findings, take them to the PM.

When your recipient takes over hand editing, mark the generated workbook final and hand-maintained, reverse any regenerate instruction in the index, and retain the generator as a record only. A prior handover told the planner not to work on the WBS again while the index still said to regenerate it; the next run would have overwritten the planner's edits.

Identify every issued version by number and date, in the file name and on its first sheet. Before replacing an issued file, compare it with the copy you issued: a difference you did not make is someone's edit. Carry it into the new version or ask its author; never overwrite it. A changed baselined product is a new version, and the original is kept unchanged; on a small project a file-naming scheme is enough. [book:prince2-managing-successful-projects], 11.1. The change theme

When an agent builds the workbook, the optional scripts in [templates/wbs](../templates/wbs/README.md) build and check it from data files; nothing in this reference depends on them.

Before issuing, run [the issue checklist](issue-checklist.md).

## Keep estimates against actuals

After delivery, record each feature's estimate beside its actual effort, as set out in [the estimating reference](estimating.md#keep-estimates-against-actuals).
