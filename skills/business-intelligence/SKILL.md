---
name: business-intelligence
description: "Produces evidence-grounded client/account intelligence dossiers and meeting preparation for consultants in consequential presale work. USE WHEN client, stakeholder, competitor, qualification, or business-case research is needed before signature. CERIC owns argument audits; this skill owns client-source verification and product-fact checks. `solution-architect` owns the resulting solution architecture and proposal response. Keywords: presale intelligence, client research, account plan, stakeholder map, competitor research, qualification, MEDDICC, executive profile, business case, meeting preparation, win/loss."
license: MIT
---

# Business Intelligence

This skill helps a consultant prepare for a consequential presale conversation by producing an evidence-grounded client or account intelligence dossier and a usable meeting brief. It supports qualification, research, account context, stakeholder understanding, competitor comparisons, business-case inputs, and conversation preparation before signature.

> Inherits the `core` kernel — see `../core/SKILL.md`. Use its shared gates and references; do not restate them here.

## When it fires — and when a sibling owns it

- **This skill:** client, stakeholder, competitor, qualification, or business-case research is needed before signature; existing account intelligence needs an update; or a presale conversation needs evidence-based preparation.
- **CERIC:** owns the argument audit of claims, evidence, and reasoning. This skill gathers and verifies client sources and product facts, then supplies evidence and ranked findings for that review.
- **`solution-architect`:** owns the client-facing architecture, options, and proposal response that may follow this intelligence work.
- **Communication work:** uses the dossier and brief to make audience-ready updates; this skill does not draft the solution response.

## Principles / anchoring rules

1. Tie research to the decision and conversation it must support. Give each research question a source plan and a reason to matter.
2. Separate observed facts, source statements, analysis, and unknowns. Unqualified evidence stays unknown; it does not become proof of absence.
3. Treat qualification scores as confidence prompts for more discovery, not as unsupported automatic thresholds.
4. Carry counterevidence, uncertainty, and source limits into the synthesis. A separate caveat section cannot repair a one-sided main story.
5. Prepare for likely concerns with grounded responses. Stakeholder questions are not an adversarial profile.
6. Keep information about named people relevant to the presale decision and handle it with care.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Qualify | Decide how much pursuit effort the evidence warrants and what remains unknown | Qualification view and open questions |
| Scope | Set the client decision, audience, timeframe, questions, and evidence needs | Research brief |
| Research | Build current, source-linked findings about the account, stakeholders, market, and alternatives | Evidence log and topic findings |
| Synthesize | Explain what the evidence means, its limits, the decision implications, and the counterevidence | Intelligence dossier and concise executive story |
| Prepare | Convert the dossier into meeting objectives, questions, likely concerns, and next steps | Pre-meeting brief |
| Learn | Capture decision and relationship changes; promote recurring lessons through the evolution loop | Debrief and refreshed account record |

Use only the phases needed for the request. For depth, see the references below.

## Gates (declared, inherited from core)

- **Grounding gate** — apply to client findings, source claims, and product facts. See `../core/references/grounding-gate.md`.
- **Output Contract** — apply to the dossier, evidence log, and meeting brief. See `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- **Pushback and teach** — use the shared response pattern when the user’s proposed claim or plan is unsupported. See `../core/references/pushback-and-teach.md`.
- **Approach declaration** — state the approach for work involving multiple actors or stages; use the core single-actor tailoring where appropriate. See `../core/SKILL.md` §7.

## Anti-patterns (hard no-list)

- Treating an unverified pain point as evidence that no problem exists.
- Using a fixed score total to override missing evidence or contradictory qualification signals.
- Treating job title, public profile, or one contact’s view as proof of decision authority or consensus.
- Presenting a competitor or product claim without source support, limits, and relevant counterevidence.
- Collecting personal detail that does not help the presale decision.
- Reusing stale account or executive assumptions without checking for changed roles, priorities, or relationships.

## Composition

- **Inherits:** `core`.
- **Consumes:** graded argument findings from CERIC and current client or product evidence.
- **Hands off:** a grounded dossier and meeting brief for communication work and any resulting solution architecture or proposal response.
- **Learning source:** meeting retrospectives, qualification outcomes, and win/loss debriefs update the account record and later skill hypotheses.

## References

- `references/deal-qualification.md` — qualification evidence, scores, buying process, and pursuit decisions.
- `references/deep-research-patterns.md` — scoping, source selection, evidence quality, and research iteration.
- `references/account-strategy.md` — account position, relationship health, priorities, and growth.
- `references/stakeholder-mapping.md` — buying group, influence, champions, and decision path.
- `references/executive-profiling.md` — role context, political dynamics, and profile refresh.
- `references/battle-cards.md` — competitor evidence and comparisons against buyer criteria.
- `references/defensive-positioning.md` — claims, proof, capability fit, and negative space.
- `references/value-engineering.md` — outcome measures, value hypotheses, and financial assumptions.
- `references/discovery-methodology.md` — meeting objectives, discovery questions, listening, and follow-through.
- `references/win-loss.md` — debriefs, internal learning, and presale handoff.
- `references/frameworks_vocabulary.md` — frameworks used in the references and how to choose them.
- `references/subagent-directives.md` — harness-neutral instructions for delegating research tracks.
- `EVOLUTION.md` — the skill’s durable learning record.
