---
name: delivery
description: "Controls for a signed-client engagement: baseline, acceptance, change and obligation records, and close-out. USE WHEN a client contract is signed and the delivery lead must establish the baseline, track acceptance or client dependencies, assess a change, record an approval, or close the engagement. Not solution-architect, which owns presignature architecture and the signed handoff; not project-management, which owns general project-planning methods; not communication, which turns agreed facts into audience-ready client messages; not dev, which owns code design and implementation. Keywords: delivery lead, engagement baseline, acceptance tracker, change request, CR log, client obligation, cost variance, actuals, UAT, acceptance evidence, close record, fixed price, scope change."
license: MIT
---

# Delivery

Delivery produces the signed-client baseline, acceptance, change and client-obligation records, and the close record for the lead accountable for an accepted and paid engagement. It starts when the client contract is signed. A delivery lead may contribute the effort estimate, release split and cut order before signature because those values feed the signed baseline; that bounded input does not create a precontract delivery baseline.

> Inherits the core kernel. Use its shared gates through the canonical references; do not restate them. See [core](../core/SKILL.md).

## When it fires — and when a sibling owns it

- Use this skill after signature to establish and maintain the engagement records, assess changes against the signed set, execute acceptance, and close the engagement.
- The solution-architect handoff supplies the signed scope and acceptance set, estimate, roadmap, client obligations and risks. Delivery reconciles that handoff and records inconsistencies.
- General project-plan methods belong to project-management. Communication owns audience-ready client messages; delivery supplies the approved facts and tracker evidence behind them.
- Code design, implementation, codebase assessment and sprint execution belong to dev. [book:scrum-masters-path], Developers

> **Disambiguation:** choose by artifact and audience. Delivery owns records that control a signed client engagement; project-management owns general project planning, communication owns client messages, solution-architect owns presignature solution and contract work, and dev owns the software build.

## Principles / anchoring rules

1. The signed scope baseline is the reference for comparison. Tailor the governance around it to the engagement context. [book:pmbok-guide-7e], 3.7. Tailor Based on Context
2. Carry one acceptance-criteria ID spine through scope, acceptance, change and close records. Keep the baseline, current forecast, and change history distinguishable.
3. Treat working progress, signed acceptance, and effort spent as different facts. The detailed measures and report fields are in the linked references.

## The flow (at a glance)

| Phase | Goal | Primary record |
|---|---|---|
| Before signature, when engaged | Supply delivery-owned effort, release and cut-order inputs for the estimate | Effort estimate returned to solution-architect |
| Mobilise | Reconcile the signed set and establish controlled baseline versions | Delivery baseline |
| Open the trackers | Populate acceptance, client-obligation and change records | Acceptance tracker, obligation tracker, change log |
| Run the cycle | Update actuals, acceptance, capacity, risks, changes and status facts | Cycle record and current trackers |
| Accept | Test and record criteria in batches as they complete | Acceptance evidence linked to criterion IDs |
| Close | Record acceptance, invoice release, handover and estimate feedback | Close record |

Delivery runs alongside the build for the engagement; engineering work proceeds in its own cycles inside the signed delivery envelope. [book:head-first-pmp], Sometimes you need to change your plans

## Gates (declared, inherited from core)

- **Grounding gate** — use the signed client set and current trackers as the record substrate. See [grounding gate](../core/references/grounding-gate.md).
- **Output Contract** — produce the baseline, current trackers, acceptance evidence and close record appropriate to the engagement. See [output contract](../core/references/output-contract.md) and [wiki protocol](../core/references/wiki-protocol.md).
- **Pushback and teach** — explain the contract, scope or evidence behind a recommendation. See [pushback and teach](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Starting comparison without a baseline reference, or silently moving the signed baseline to conceal variance.
- Treating effort spent, submitted work, working increments and client-signed acceptance as one progress number.
- Letting a verbal request or an unasked extra become an undocumented commitment.
- Marking a criterion accepted without a written acceptance record and supporting evidence.
- Replacing the signed criterion IDs with a parallel tracker namespace.
- Reporting a client dependency without its owner, due date and concrete effect.

## Composition

- **Inherits:** core.
- **Consumes:** the signed solution-architect handoff and project-management methods where the engagement needs broader planning.
- **Supplies:** tracker-grounded facts and approved record changes for communication to turn into client-ready messages; estimate-versus-actual findings return to solution-architect.
- **Works alongside:** dev, which builds and tests the software within the engagement baseline.

## References

- [references/delivery-lifecycle.md](references/delivery-lifecycle.md) — bounded presignature input, signed mobilisation, the record cycle, acceptance and close.
- [references/progress-measurement.md](references/progress-measurement.md) — separate measures for working progress, acceptance, cost, capacity and status.
- [references/acceptance-execution.md](references/acceptance-execution.md) — test preparation, acceptance evidence, waivers and rejection records.
- [references/change-control.md](references/change-control.md) — change intake, impact, authority, approval and baseline history.
- [references/templates/delivery-baseline.md](references/templates/delivery-baseline.md) — fields and reconciliation for the signed baseline.
- [references/templates/acceptance-tracker.md](references/templates/acceptance-tracker.md) — criterion IDs, traceability and acceptance evidence.
- [references/templates/client-obligation-tracker.md](references/templates/client-obligation-tracker.md) — dated, owned client dependencies and their impact.
- [references/templates/change-request-log.md](references/templates/change-request-log.md) — decisions, impact assessment and cumulative change records.
- [references/templates/status-report.md](references/templates/status-report.md) — tracker-derived cycle facts for a report or a communication handoff.
- [references/templates/close-record.md](references/templates/close-record.md) — final acceptance, invoice, handover and close data.
