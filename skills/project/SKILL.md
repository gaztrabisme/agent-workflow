---
name: project
description: "Runs a project end to end, presale to delivery to close, for one person working with AI agents: the plan (WBS, effort estimate, schedule, business case, tolerances, sprint) and the running of multi-step work through agents (Plan Block, briefs, fan-out, success criteria and UAT, convergence). USE WHEN work needs a plan, WBS, effort estimate or sprint before execution, whether or not it is under contract, or a multi-step request needs coordinated stages across skills. Not `solution-architect`, which owns the presignature solution and response pack; not `delivery`, which owns signed-client baseline, acceptance, change and obligation controls; not `dev`, which owns code. Keywords: project plan, WBS, work breakdown, effort estimate, AI-assisted estimate, business case, margin, tolerance, PRINCE2, schedule, sprint planning, capacity, dependencies, Gantt, release plan, orchestrate, coordinate stages, multi-step task, Plan Block, lane plan, fan-out, persona review, convergence, run ledger, success criteria, UAT."
license: Proprietary (private; cites a paid course)
---

# Project

This skill runs a project from presale to close with one person and AI agents: it plans the work (WBS, estimate, schedule, business case, tolerances, sprints) and runs multi-step work through agents that each work to a brief. Who holds each project role is set per project in [roles](references/roles.md); by default the one person and their agents hold every production role. It replaces the former `project-management` and `conductor` skills (merged 14 Oct 2026).

> Inherits the `core` kernel. Use its canonical gates through [core/SKILL.md](../core/SKILL.md); keep shared gate definitions there.

## Sibling skills

- **`solution-architect`:** the presignature solution and response pack, and what a presale WBS must contain.
- **`delivery`:** signed-client baseline, acceptance, change and obligation controls.
- **`dev`:** code design, build, review and root-cause analysis.
- Full routes and disambiguation: [routing](references/routing.md).

## Foundation

PRINCE2's seven principles are the root of this skill; themes, processes and templates may be tailored, but a plan that drops a principle is not managed. [book:prince2-managing-successful-projects], Chapter 3. Principles; 4.1. Tailoring PRINCE2

| Principle | What it means here | Where its rules live |
|---|---|---|
| Continued business justification | The work stays worth doing, for the client and for us (our margin), at every decision point | [Business case](references/business-case-and-tolerances.md) |
| Learn from experience | Read past estimates, actuals and lessons before the first figure; record them at close | [Estimating](references/estimating.md) |
| Defined roles and responsibilities | Who decides, whose word outranks whose, who drafts and who confirms each figure | [Roles](references/roles.md), [WBS workbook](references/wbs-workbook.md) |
| Manage by stages | Presale, then signed delivery, then each stage; plan in detail only to the next boundary and re-estimate there | [Lifecycle](references/lifecycle.md), [Estimating](references/estimating.md) |
| Manage by exception | Tolerances on time, cost, scope, quality, benefits and risk; escalate a forecast breach, adjust freely inside | [Business case](references/business-case-and-tolerances.md), [Running agents](references/run/flow.md) |
| Focus on products | Plan from deliverables and their acceptance checks, then activities; exclusions stated | [Estimating](references/estimating.md), [WBS workbook](references/wbs-workbook.md) |
| Tailor to suit the project | The team's template and the size of the job set the form; the principles stay | [WBS workbook](references/wbs-workbook.md) |

## Stages

| Stage | Modules | Linked skills |
|---|---|---|
| Qualify and discover | [roles](references/roles.md), [running agents](references/run/flow.md) | `business-intelligence`, `ceric`, `ai-discovery-workshop`, `product-management`, `ux` |
| Shape, plan and price | [lifecycle](references/lifecycle.md), [planning method](references/planning-method.md), [WBS workbook](references/wbs-workbook.md), [estimating](references/estimating.md), [business case](references/business-case-and-tolerances.md), [issue checklist](references/issue-checklist.md) | `solution-architect`, `xlsx` |
| Make the artifacts | [review and audience](references/review-and-audience.md) | `presentation`, `drawio`, `information-design`, `communication` |
| Build | [running agents](references/run/flow.md), [goal file](references/run/goal-file.md) | `dev`, `frontend`; `infrastructure`, `data-engineering`, `testing` |
| Stage boundary | [estimating](references/estimating.md), [business case](references/business-case-and-tolerances.md) | `delivery` |
| Close | [running agents](references/run/flow.md), [estimating](references/estimating.md) | `delivery`, `evolution` |

Each stage's outputs and exit check: [lifecycle](references/lifecycle.md).

## Modules

Project and planning:

- [references/roles.md](references/roles.md) — roles table with who holds each per project; the two rules that do not depend on headcount; who drafts and confirms plan figures.
- [references/lifecycle.md](references/lifecycle.md) — stages from presale to close, the planning flow, building the plan, gates applied to planning.
- [references/routing.md](references/routing.md) — skills by stage, routes by request, carrier skills, disambiguation, compose order.
- [references/planning-method.md](references/planning-method.md) — brief, plan views, release slicing, sprint preparation, and client-project planning.
- [references/wbs-workbook.md](references/wbs-workbook.md) — WBS structure, estimate collection, schedule forms, capacity, dependencies, and handover.
- [references/estimating.md](references/estimating.md) — lessons first, product-based planning, row basis and ranges, derived activities, AI-assisted work, contingency and actuals.
- [references/business-case-and-tolerances.md](references/business-case-and-tolerances.md) — the client's and our business case, per-feature margin view, tolerances, fixed price, cutting to a price, and change-request recovery.
- [references/issue-checklist.md](references/issue-checklist.md) — twenty-two checks to run by hand before a workbook or plan is issued, each pointing to its rule.
- [references/checklist-uat.md](references/checklist-uat.md) — stress test for each issue-checklist line.
- [references/review-and-audience.md](references/review-and-audience.md) — declaring each artifact's reader, and checking every artifact rendered.
- [references/anti-patterns.md](references/anti-patterns.md) — the hard no-list for planning and for running agents.
- [scripts/check_quoted_figures.py](scripts/check_quoted_figures.py) — lists figures quoted in an email, note or slide that the cited file does not contain (checklist line 21).
- [templates/wbs/](templates/wbs/README.md) — optional scripts that build and check a WBS workbook from data files when an agent builds it.

Running agents:

- [references/run/flow.md](references/run/flow.md) — the method: PRINCE2 terms, Classify to Close, Plan Block, approach declaration, mid-run stops, gates as applied.
- [references/run/lane-plan.md](references/run/lane-plan.md) — lane check, providers, brief contract, selection, fallback, run ledger row.
- [references/run/goal-file.md](references/run/goal-file.md) — goal-file template, UAT criteria, amendments, and close audit.
- [references/run/intent-interview.md](references/run/intent-interview.md) — scenario questions about the outcome before planning.
- [references/run/convergence.md](references/run/convergence.md) — contradiction and interaction passes, decision records, landing.
- [references/run/ceric-gates.md](references/run/ceric-gates.md) — CERIC at Ground, Converge, and Close.
- [references/run/task-force-protocol.md](references/run/task-force-protocol.md) — sourced fact-finding, adversarial verification, and synthesis.
- [references/run/design-cell.md](references/run/design-cell.md) — cross-discipline producers, interface contracts, one coherent spec.
- [references/run/persona-fanout.md](references/run/persona-fanout.md) — stakeholder reactions and the objection register.
- [references/run/run-schedule.md](references/run/run-schedule.md) — waves, per-item loops, batch acceptance, resume state.
- [references/run/workflow-patterns.md](references/run/workflow-patterns.md) — engine choice, pipelines, barriers, resume safety, topologies.
- [references/run/harness-map.md](references/run/harness-map.md) — harness-specific instruction files and orchestration facts.

## Gates (inherited from core)

- Grounding — [core grounding gate](../core/references/grounding-gate.md); applied in [lifecycle](references/lifecycle.md#gates-applied-to-planning) and [running agents](references/run/flow.md#gates-as-applied).
- Output contract and records — [core output contract](../core/references/output-contract.md), [core wiki protocol](../core/references/wiki-protocol.md).
- Pushback and teach — [core pushback and teach](../core/references/pushback-and-teach.md).
- Approach declaration — [running agents](references/run/flow.md#approach-declaration).

## Anti-patterns

[references/anti-patterns.md](references/anti-patterns.md).

## History

- [EVOLUTION.md](EVOLUTION.md) — this skill (formerly `project-management`).
- [history/conductor-EVOLUTION.md](history/conductor-EVOLUTION.md) — the former `conductor` skill.
