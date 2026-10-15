---
name: infrastructure
description: "Cloud infrastructure and deployment for the infrastructure lead's job: environments, infrastructure as code, CI/CD and release, provisioning, and the cloud cost estimate (per environment and service; monthly, whole-phase, multi-year; consumption drivers). USE WHEN deciding which environments a plan needs, designing infrastructure code or a deployment pipeline, planning a release or rollback, building a cloud cost estimate or three-year run projection, rescoping a pricing workbook, or reproducing and checking a colleague's pricing workbook. Not `solution-architect` (client-facing solution and how cost is shown), `dev` (application code and tests), `xlsx` (workbook mechanics), or `project` (effort, schedule, price). Keywords: infrastructure, cloud, Azure, AWS, environment, dev/test/prod, staging, IaC, Terraform, Bicep, provisioning, subscription, CI/CD, pipeline, deployment, release, rollback, canary, cloud cost, pricing workbook, TCO, run rate, reservation, pay-as-you-go, consumption, SKU."
---

# Infrastructure

Produces the infrastructure lead's artifacts for a software project: the environment plan, the infrastructure-as-code and pipeline design, the release and rollback plan, and the infrastructure cost estimate with its drivers. It also produces a review of someone else's cloud pricing workbook: a reproduced total and a defect list. The audience is the project lead who prices and plans the work, the engineer who builds it, and, through `solution-architect`, the client or funder who reads the cost.

> Inherits the `core` kernel — see `../core/SKILL.md`. Follow shared gates through their canonical references; do not copy their definitions.

## When it fires — and when a sibling owns it

- **This skill:** how many environments, what each runs and for how long; infrastructure code and deployment pipeline; release and rollback; the cloud cost per environment, per service and over the run; checking or rescoping a pricing workbook.
- **`solution-architect` instead:** the client-facing architecture, options and response pack. Its "Cloud cost by environment" section in `../solution-architect/references/estimation-and-costing.md` sets the row fields a client-facing cost sheet carries; this skill produces the figures and their drivers.
- **`dev` instead:** application code, its tests and container builds (`../dev/modes/build.md`). This skill owns the environments and pipeline the code is deployed through.
- **`xlsx` instead:** reading formulas and cached values, recalculating headlessly, gating a workbook before it is sent (`../xlsx/SKILL.md`). This skill decides what the cost workbook must contain and what is wrong with it.
- **`project` instead:** effort, schedule, price, margin and tolerances (`../project/references/estimating.md`). Provisioning and pipeline tasks from this skill go into its WBS as rows.

> **Disambiguation:** decide on artifact and audience. A cost figure with its driver and period is this skill's; how that figure is priced to the client is `project`'s; how it is shown in a proposal is `solution-architect`'s; the cells it lives in are `xlsx`'s.

## Principles

1. **Every environment is counted or excluded with a reason.** An environment sheet, stack or subscription that is neither in a total nor marked out of it is how a total goes wrong without anyone choosing it. (derived: EVOLUTION case 1)
2. **Environments are instances of one definition.** One reusable infrastructure definition with per-environment parameters, not copies edited by hand. [book:infrastructure-as-code], Antipattern: Copy-Paste Environments
3. **Every figure carries its period.** Per hour, per month, whole phase, per year, multi-year. Figures with different periods are converted before they are added. (derived: EVOLUTION case 1)
4. **Every consumption line names its driver and the driver's source.** Measured, stated by the client, or an assumption with an owner. The largest driver gets the most checking. [book:site-reliability-engineering], Provisioning
5. **The billing basis follows the usage period.** A commitment discount is used only where usage covers the commitment term; a short phase is priced pay-as-you-go. [book:cloud-native-devops-kubernetes], Using Reserved Instances
6. **A colleague's workbook is reviewed, not edited.** Work on a copy, reproduce its totals, and hand back findings with cells; the owner decides. (derived: EVOLUTION case 2)

## The flow (at a glance)

| Step | Goal | Primary artifact | Reference |
|---|---|---|---|
| Environments | Decide count, purpose, sizing and lifetime of each environment; tie each to plan rows | Environment plan | [environments-and-iac.md](references/environments-and-iac.md) |
| Infrastructure code | One reusable definition, per-environment parameters, secrets out of code | Stack layout and parameter list | [environments-and-iac.md](references/environments-and-iac.md) |
| Pipeline and release | Build once, deploy the same way everywhere, rollback planned | Pipeline and release plan | [ci-cd-and-release.md](references/ci-cd-and-release.md) |
| Cost estimate | Per environment and service, each line with driver, period and source; run projection from production volume | Cost workbook and basis note | [cost-estimate.md](references/cost-estimate.md) |
| Review a workbook | Reproduce totals, find unit, coverage, rate and driver defects | Reproduced total and defect list | [reviewing-a-pricing-workbook.md](references/reviewing-a-pricing-workbook.md) |

Scale to the request: a question about one cost line needs only the relevant check from the cost or review module.

## Gates (declared, inherited from core)

- **Grounding gate** — substrate: the plan's provisioning rows, the architecture's component list, the provider's current price list for the deployment region, and measured volumes. See `../core/references/grounding-gate.md`.
- **Output Contract** — done means: every total recalculated and read back, every environment counted or excluded with a reason, every driver sourced or marked as an assumption with an owner. See `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- **Pushback and teach** — when a requested figure would mix periods, drop an environment silently, or pick a driver because of the total it produces, say so and give the corrected figure. See `../core/references/pushback-and-teach.md`.

## Anti-patterns

- Adding a monthly run-rate to a whole-phase total, or sending a figure whose period is not stated.
- Leaving an environment sheet out of a total without a reason written next to the total.
- Choosing an environment count, a capacity size or a volume because of what it does to the total or to a funding ratio.
- A reservation discount on a phase shorter than the reservation term.
- A rate typed into many cells; a change to the rate card that does not reach every sheet.
- Editing a colleague's pricing workbook instead of returning findings.
- Hand-built environments, or production changes made outside the pipeline.

## Composition

- **Inherits:** `core`.
- **Consumes:** the WBS and schedule from `project`; the architecture and component list from `solution-architect`; workbook mechanics from `xlsx`.
- **Hands off to:** `project` (provisioning and pipeline rows, infrastructure cost for the business case); `solution-architect` (cost lines and assumptions for the response); `dev` (deployment conventions the code must follow).

## References

- [references/environments-and-iac.md](references/environments-and-iac.md) — environment plan, infrastructure code, parameters, secrets, provisioning rows.
- [references/ci-cd-and-release.md](references/ci-cd-and-release.md) — deployment pipeline, release, rollback, production change control.
- [references/cost-estimate.md](references/cost-estimate.md) — building the cost estimate, periods, pricing basis, drivers, run projection, rescoping a workbook.
- [references/reviewing-a-pricing-workbook.md](references/reviewing-a-pricing-workbook.md) — reproducing and checking someone else's pricing workbook.
- [EVOLUTION.md](EVOLUTION.md) — birth record, cases and test.
