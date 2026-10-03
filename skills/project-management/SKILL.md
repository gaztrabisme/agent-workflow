---
name: project-management
description: "A project plan with scope, sequence, capacity, dependencies, and sprint commitments for a project lead coordinating a team or internal project. USE WHEN work needs a plan or sprint before execution, whether or not it is under contract. Not `delivery`, which owns signed-client baselines and acceptance, change, and obligation controls; use `conductor` for cross-skill staging. Keywords: project plan, WBS, work breakdown, schedule, sprint planning, capacity, dependencies, Kanban, Gantt, release plan, weekly planning."
license: Proprietary (private; cites a paid course)
---

# Project-management

This skill helps a project lead turn work into a usable plan before execution: a work breakdown structure (WBS), schedule, capacity view, dependency register, and sprint commitments. When a WBS is needed, the default deliverable is a concise plan note plus an editable workbook the team can update. Use a lighter shared plan when a WBS would not help the decision.

> Inherits the `core` kernel. Use its canonical gates through [core/SKILL.md](../core/SKILL.md); keep shared gate definitions there.

## When it fires — and when a sibling owns it

- **This skill:** a project lead needs to frame, sequence, staff, or commit project work before it starts, for an internal or client project.
- **Presignature priced estimate:** use `delivery`'s pre-signature estimate step for client response estimates, release split, and capacity decisions; `solution-architect` owns the response pack. This skill can frame and sequence a separate team plan, but it does not own the priced estimate or response pack.
- **`delivery` instead:** a signed client engagement needs its baseline, acceptance, change, or obligation controls. This plan may feed that work, but does not replace its records.
- **`conductor` instead:** the request needs cross-skill staging or coordination; this skill builds the project plan itself.

> **Disambiguation:** choose by artifact and audience. This skill produces a working project plan for the project lead and team; `delivery` manages the signed engagement record for the delivery lead and client.

## Principles / anchoring rules

1. **Fit the planning view to the decision.** A project plan is a working instrument for its recipient, not a fixed workbook shape.
2. **Make work discussable before making commitments.** Keep task scope, order, and ownership visible so the team can plan together.
3. **Keep the plan inside its lane.** Record project work here; route signed-engagement controls to `delivery`.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Frame | Clarify the plan's purpose, audience, outcome, and scope | Project brief or plan outline |
| Decompose | Turn deliverables into right-sized work and a suitable hierarchy | WBS |
| Sequence | Show timing, dependencies, milestones, and available capacity | Schedule and dependency register |
| Commit | Select a feasible release or sprint slice with the team | Sprint or period commitment |
| Hand over | Keep the plan editable, readable, and current | Shared plan and handover note |

## Build the plan

Start with [the planning method](references/planning-method.md) to clarify the brief, choose a useful view, and shape release or sprint work. Use [the workbook guidance](references/wbs-workbook.md) when the plan needs a WBS, effort collection, capacity check, or dependency register. Adapt the detail to the project; do not build every view for every job.

For a client project, use the brief and any agreed scope document as planning inputs. Keep the external commitment and the internal task plan distinguishable. The signed-engagement baseline and acceptance/change/obligation records belong with `delivery`.

## Gates (declared, inherited from core)

- **Grounding gate** — use the brief, agreed scope, team input, and relevant plan history as the substrate; mark unknowns rather than guessing. See [core grounding gate](../core/references/grounding-gate.md).
- **Output Contract** — the plan, schedule, and any needed dependency or capacity view must exist and be usable by their recipient before work is committed. See [core output contract](../core/references/output-contract.md) and [core wiki protocol](../core/references/wiki-protocol.md).
- **Pushback and teach** — when a requested scope, date, or workload does not fit the plan, explain the constraint and offer a workable fork. See [core pushback and teach](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Fill estimates or decide the release cut for the person who owns those decisions.
- Use the same WBS hierarchy or visualization for every project.
- Hide overrun, dependencies, or capacity gaps behind a tidy summary.
- Keep regenerating a workbook after its recipient has taken over hand editing.
- Turn the general plan into a signed-engagement tracker.

## Composition

- **Inherits:** `core` shared gates.
- **Consumes / hands off to:** `delivery` for signed-client controls and pre-signature estimate, release-split, and capacity decisions; `solution-architect` for the presignature response pack; `conductor` for cross-skill staging. A presale solution plan can pass planning inputs into this workflow when a separate team plan is needed.

## References

- [references/planning-method.md](references/planning-method.md) — brief, plan views, release slicing, sprint preparation, and client-project planning.
- [references/wbs-workbook.md](references/wbs-workbook.md) — WBS structure, estimate collection, schedule forms, capacity, dependencies, and handover.
