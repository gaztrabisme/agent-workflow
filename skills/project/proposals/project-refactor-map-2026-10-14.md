# Refactor map: old `SKILL.md` files to the `project` modules (2026-10-14)

Every bullet, paragraph and table of the two old entry files, as of commit `5c8e304`, and where it now lives. Paths are relative to `project/`.

## Old `project-management` SKILL.md (`git show 5c8e304:project/SKILL.md`)

| Old section and item | New file | New heading |
|---|---|---|
| Frontmatter `name`, `description` | `SKILL.md` | frontmatter (name `project`; description covers planning and running agents) |
| Frontmatter `license` | `SKILL.md` | frontmatter (kept: Proprietary) |
| Intro paragraph (plan before execution; WBS default deliverable; lighter plan when a WBS would not help) | `SKILL.md`; `references/lifecycle.md` | intro; Build the plan ("Adapt the detail to the project; do not build every view for every job") |
| "Inherits the `core` kernel" note | `SKILL.md` | intro note |
| When it fires: "This skill" bullet | `SKILL.md` | frontmatter description (USE WHEN) |
| When it fires: "Presale WBS and effort estimate" bullet | `references/roles.md` | Ownership of plan figures |
| When it fires: "`delivery` instead" bullet | `SKILL.md`; `references/lifecycle.md` | Sibling skills; Stages (paragraph under the table) |
| When it fires: "`conductor` instead" bullet | removed; cross-skill staging is now this skill | `references/run/flow.md` Scope |
| Disambiguation note (artifact and audience; plan vs signed record) | `references/routing.md` | Disambiguation, item 3 |
| Foundation paragraph (principles are the root; tailoring) | `SKILL.md` | Foundation |
| Foundation table (seven principles) | `SKILL.md` | Foundation (links updated to roles and lifecycle) |
| "On a supplier's bid, the client's business case and ours are separate" | `references/lifecycle.md` | Build the plan |
| The flow table (Frame, Decompose, Sequence, Commit, Hand over) | `references/lifecycle.md` | Planning flow |
| Build the plan, paragraph 1 | `references/lifecycle.md` | Build the plan |
| Build the plan, paragraph 2 (client project inputs; delivery owns baseline) | `references/lifecycle.md` | Build the plan |
| Gates: Grounding gate | `references/lifecycle.md` | Gates applied to planning |
| Gates: Output Contract | `references/lifecycle.md` | Gates applied to planning |
| Gates: Pushback and teach | `references/lifecycle.md` | Gates applied to planning |
| Anti-patterns, all ten bullets | `references/anti-patterns.md` | Planning |
| Composition: inherits core | `SKILL.md` | intro note; Gates (inherited from core) |
| Composition: hands off to delivery, solution-architect, conductor | `SKILL.md`; `references/routing.md` | Sibling skills; Skills by stage |
| References list (five references and templates) | `SKILL.md` | Modules |

## Old `conductor` SKILL.md (`git show 5c8e304:project/references/run/conductor-skill-source.md`)

| Old section and item | New file | New heading |
|---|---|---|
| Frontmatter description (keywords: orchestrate, Plan Block, fan-out, UAT ...) | `SKILL.md` | frontmatter description |
| Frontmatter license MIT | not carried; the merged skill keeps the project-management license | — |
| Intro paragraph (coordinated plan and record; domain work belongs elsewhere) | `references/run/flow.md` | opening paragraph |
| "Inherits the `core` kernel" note | `SKILL.md` | intro note |
| When it fires: Conductor / owning skill / disambiguation bullets | `references/run/flow.md` | Scope |
| Principle 1 Coordinate; do not take the unit | `references/run/flow.md` | Principles |
| Principle 2 Facilitate decisions | `references/run/flow.md` | Principles |
| Principle 3 Scale the ceremony | `references/run/flow.md` | Principles |
| Principle 4 Evidence trail visible | `references/run/flow.md` | Principles |
| Principle 5 Name the meeting point | `references/run/flow.md` | Principles |
| Flow at a glance table | `references/run/flow.md` | Flow at a glance |
| Gates: intro sentence and gates 1 to 8 | `references/run/flow.md` | Gates as applied |
| Approach declaration paragraph | `references/run/flow.md` | Approach declaration |
| 1. Classify | `references/run/flow.md` | 1. Classify |
| 2. Ground, paragraph 1 (read project before planning) | `references/run/flow.md` | 2. Ground |
| 2. Ground, paragraph 2 (CERIC hunt, `grounded.md`, Office comments) | `references/run/flow.md` | 2. Ground |
| 2. Ground, paragraph 3 (carry forward open forks) | `references/run/flow.md` | 2. Ground |
| 2a. Interview | `references/run/flow.md` | Intent interview |
| 3. Compose, paragraphs 1 to 3 | `references/run/flow.md` | 3. Compose |
| 4. Declare, opening paragraph | `references/run/flow.md` | 4. Declare: the Plan Block |
| Plan Block template | `references/run/flow.md` | 4. Declare: the Plan Block |
| Fork register table | `references/run/flow.md` | 4. Declare: the Plan Block |
| "If the INTENT restatement is wrong, stop" | `references/run/flow.md` | 4. Declare: the Plan Block |
| Only scheduled stop; go rules; mid-run stop cases | `references/run/flow.md` | 4. Declare: the Plan Block |
| 5. Goal, paragraphs 1 and 2 | `references/run/flow.md` | 5. Goal: the stop condition on disk |
| 6. Run, paragraph 1 (dispatch, ledger, milestone reports) | `references/run/flow.md` | 6. Run |
| 6. Run, "Mid-run stops carry their own context" | `references/run/flow.md` | Mid-run stops |
| 6. Run, run schedule paragraph | `references/run/flow.md` | 6. Run |
| 6. Run, acceptance and reroute paragraph | `references/run/flow.md` | 6. Run |
| 7. Converge | `references/run/flow.md` | 7. Converge |
| 8. Close | `references/run/flow.md` | 8. Close: the UAT audit |
| Anti-patterns, all ten bullets | `references/anti-patterns.md` | Running agents |
| Composition: inherits, coordinates, owns, defers to | `references/run/flow.md` | Ownership |
| References list (twelve files) | `SKILL.md` | Modules (`routing-table.md` replaced by `references/routing.md`) |

## Old `references/run/routing-table.md` (deleted)

| Old section | New file | New heading |
|---|---|---|
| Intro line | `references/routing.md` | opening paragraph |
| The table | `references/routing.md` | Routes by request |
| Carrier and capability skills (two rules, override, tables, frontend/visual-design paragraphs, boundary, ambiguity rule) | `references/routing.md` | Carrier and capability skills |
| Disambiguation items 1 and 2 and closing rule | `references/routing.md` | Disambiguation |
| Compose-order | `references/routing.md` | Compose order |
| What conductor never routes | `references/routing.md` | Work this skill never routes |
| ML / model work | `references/routing.md` | ML and model work |
| When a route absorbs an existing collection | `references/routing.md` | When a route absorbs an existing collection |
