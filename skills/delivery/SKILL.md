---
name: delivery
description: "Controls for a signed-client engagement: baseline, acceptance, change and obligation records, and close-out. USE WHEN a client contract is signed and the delivery lead must establish the baseline, track acceptance or client dependencies, assess a change, record an approval, or close the engagement. Not solution-architect, which owns presignature architecture and the signed handoff; not project, which owns general project-planning methods; not communication, which turns agreed facts into audience-ready client messages; not dev, which owns code design and implementation. Keywords: delivery lead, engagement baseline, acceptance tracker, change request, CR log, client obligation, cost variance, actuals, UAT, acceptance evidence, close record, fixed price, scope change."
license: MIT
---

# Delivery

Delivery produces the signed-client baseline, acceptance, change and client-obligation records, and the close record for the lead accountable for an accepted and paid engagement. Use the recorded agreement event in Phase −1 as the operational signature gate. The one pre-signature role is set out under Pre-signature exception below.

> Inherits the core kernel. Use its shared gates through the canonical references; do not restate them. See [core](../core/SKILL.md).

## When it fires — and when a sibling owns it

- Use this skill after signature to establish and maintain the engagement records, assess changes against the signed set, execute acceptance, and close the engagement.
- The solution-architect handoff supplies the signed scope and acceptance set, estimate, roadmap, client obligations and risks. Delivery reconciles that handoff and records inconsistencies.
- General project-plan methods belong to project. Communication owns audience-ready client messages; delivery supplies the approved facts and tracker evidence behind them.
- Code design, implementation, codebase assessment and sprint execution belong to dev. [book:scrum-masters-path], Developers

> **Disambiguation:** choose by artifact and audience. Delivery owns records that control a signed client engagement; project owns general project planning, communication owns client messages, solution-architect owns presignature solution and contract work, and dev owns the software build.

### Pre-signature exception

Before signature, the effort estimate is drafted and collected through `project`'s WBS and confirmed by the leads who will be held to it, the delivery planner among them; the delivery planner owns the release split and cut order. Solution-architect does not hand over a prefilled version. Reason: an estimate written by someone who will not be held to it is a proposal for an estimate, not an estimate. Nothing is baselined, tracked or accepted before signature; the Phase −1 loop in `references/delivery-lifecycle.md` covers the mechanics.

## Principles / anchoring rules

1. The signed scope baseline is the reference for comparison. Tailor the governance around it to the engagement context. For a small engagement, use the compact cycle view in `references/progress-measurement.md` while retaining its required source records. [book:pmbok-guide-7e], 3.7. Tailor Based on Context; (derived: dogfood 2026-10-01)
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
- **Register gate (local)** — anything going to a client, partner or funder is written in their register from the start, not filtered into it afterwards. The redaction scan runs as the last build step; a clean scan means no residue was found, not that the prose was written for the reader. See the Final QA pass in [the RFI/RFP reference](../solution-architect/references/rfi-rfp-response.md).

## Anti-patterns (hard no-list)

- Starting comparison without a baseline reference, or silently moving the signed baseline to conceal variance.
- Treating effort spent, submitted work, working increments and client-signed acceptance as one progress number.
- Letting a verbal request or an unasked extra become an undocumented commitment.
- Marking a criterion accepted without a written acceptance record and supporting evidence.
- Replacing the signed criterion IDs with a parallel tracker namespace.
- Reporting a client dependency without its owner, due date and concrete effect.
- **Shipping the derivation with the result.** A client copy carrying internal reasoning (gross-before-discount, productivity factor, seniority mix) invites a negotiation about method that has no natural end. Build the client copy on a code path where those fields do not exist; removal steps get forgotten, absent fields cannot.
- **Delivering more than was asked.** An extra section passes wording and reconciliation checks and still enlarges what the client must approve. Check the artifact against the list of requested items. The usual reason is a guess about what the client "will want", made by the person most invested in the extra work.
- **A gate that has to be remembered.** A redaction or QA check run by hand fails silently, and the file still looks finished. Wire it as the last step of the build on the shipping path, and have it refuse to save on failure.

## Composition

- **Inherits:** core.
- **Consumes:** the signed solution-architect handoff and project methods where the engagement needs broader planning.
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
- [references/templates/warranty-defect-log.md](references/templates/warranty-defect-log.md) — criterion-linked defects during the contractual warranty period. (derived: dogfood 2026-10-01)
