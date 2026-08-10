---
name: ai-discovery-workshop
description: "Run an AI Discovery & Envisioning workshop with an enterprise client — Discover/Define/Develop/Deliver, BXT-scored use cases, agentic journey mapping, one use case approved for PoV. USE WHEN preparing or facilitating an AI discovery or envisioning workshop, scoring use cases on BXT, working the AI Discovery Cards, prepping the five golden questions, or scoping an AI engagement with a client. Not `business-intelligence` — that researches the client before Day 1; this runs the room. Not `solution-architect` — that turns the output into an architecture and a proposal. Keywords: AI discovery workshop, AI envisioning, BXT, discovery cards, agentic use case, design thinking, Rose Thorn Bud, journey map, five golden questions, PoV, workshop facilitation, use case prioritization."
---

# AI Discovery & Envisioning

The operating manual for running an AI Discovery & Envisioning workshop as a presale consultant: a structured two-session engagement that takes an enterprise client from vague AI ambition to one use case scored, agreed and ready for a funded proof of value.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## Anchoring principles (read first, every time)

These override anything downstream. If a downstream artifact conflicts with them, the principle wins.

1. **Scope consulting to two domains: human experience and business process.** These are the only two areas this framework targets AI & Data at. When consulting clients, focus the conversation here. Of the two, **process is generally the higher-leverage.** Do not consult on adjacent domains you're less certain about.

2. **Don't overconfident-consult.** If you can't defend a claim under pushback, don't make it. This is not about being timid — it's about not getting caught in a follow-up question you can't answer. Build escape hatches. Flag uncertainty. Know the negative space.

3. **The Five Golden Questions must be prepped before every workshop.** They are the **BXT screening questions** — the ~5 probing questions under each pillar's "Is it viable? / Is it desirable? / Is it feasible?" header. Know them cold. Full verbatim set in `references/facilitator_scripts.md`; concept overview in `references/five_golden_questions.md`.

4. **Use the systematic design-thinking approach.** The procedure is a structured Discover → Define → Develop → Deliver flow with specific methods at each stage. Don't improvise — run the flow.

## The 4-phase flow (at a glance)

| Phase | Duration | Output | Key methods |
|-------|----------|--------|-------------|
| **Discover** | Day 1 prework + opening | Personas, pain points | Five Whys, Move off the Solution, Rose/Thorn/Bud, Statement Starters |
| **Define** | Day 1 core | 2–3 candidate use cases scored on BXT | BXT framework + **Five Golden Questions** (per pillar), Affinity Clustering, Prioritization Matrix |
| **Develop** | Day 1 → Day 8 | Agentic Journey Map, GenAI approach selected | Journey Mapping, AI Discovery Cards (79), Agentic Cards (12) |
| **Deliver** | Day 8 close | Approved use case for PoV, ROI baseline, architecture draft | ROI Analysis, Architecture Design Session, Rapid Prototyping (AI coding assistant) |

Workshop targets **3–5 agentic AI use cases** per engagement, narrowed to **1 approved for PoV** by end of Day 8.

## How to use this skill

**For quick lookups**, go to `references/` — these are tight digests of the most-accessed content:

- `references/workshop_agenda.md` — Day 1 / Day 8 structure, prework, prep checklist
- `references/bxt_template.md` — BXT scoring model, rubric, Factory AI example
- `references/facilitator_scripts.md` — verbatim questions to ask the client by phase
- `references/discovery_cards.md` — 79 AI Discovery Cards + 12 Agentic Cards by category
- `references/commercial_framing.md` — how to position the workshop commercially, and the ROI conversation
- `references/methods_glossary.md` — 1-liner on every named method (Rose/Thorn/Bud, Sailboat, etc.)
- `references/five_golden_questions.md` — concept overview (the BXT screening questions)

**For prework intel**, use the `business-intelligence` skill before Day 1. That skill produces the executive profiles (with political-layer analysis), competitive context, Capability Map, and Claims Verification that the workshop then structures into BXT-scored use cases. The two skills compose: BI is *what* you know about the client; this skill is *how* you run the room.

**For the step after the workshop**, use the `solution-architect` skill. The BXT-scored use cases, agentic journey map, and ROI baseline this workshop produces become the inputs to its Architect phase, where they're turned into a solution architecture and an RFI/RFP/proposal response. `solution-architect` pulls this skill's stack and `commercial_framing.md` rather than re-deriving them — so the pipeline is: BI → this skill → solution-architect → dev (the build).

**Kernel:** this skill inherits the `core` spine — integrity constraints, gate-by-artifact, the Grounding Gate (ground BXT scores and claims in the evidence; "don't overconfident-consult" is the honesty corollary), and the evolution loop. Reference `../core/references/…`, don't re-derive. No real workshop has yet been run through this skill and written up, so treat its method as `PENDING` until validated in practice (see `../evolution/references/loop.md`).

## Anti-patterns (hard no-list)

- **Tech-first framing.** "We should use a managed LLM service for..." before the problem is nailed down. The method opens with the ~80% AI project failure rate — tech-first is the root cause.
- **Scoping outside experience or process.** If the use case isn't clearly (a) enriching a human experience or (b) reshaping a business process, stop and rescope.
- **Claiming maturity we don't have.** The framework bakes in "is it feasible?" scoring — if we don't know, score honestly.
- **Unverified stats.** "100x acceleration", "50% productivity gain" without a concrete baseline — don't.
- **Skipping the BXT scoring.** Every candidate use case must get scored across Business / Experience / Technology. No "gut feel" prioritization.
- **Single-persona shortcut.** Complex workflows usually have secondary personas (submitter / reviewer / approver / finance). Map them all or the HITL design is broken.

## Opening hook for a client conversation

When asked how you'd approach an AI engagement, you can answer along these lines:

> "Industry data shows roughly 80% of AI projects fail because teams solve the wrong problem. We run a structured 2-session workshop — Discover, Define, Develop, Deliver — that scores every candidate use case across Business, Experience, and Technology before we commit. By the end of Day 8 you have one use case ready for a funded PoV. We stay scoped to AI for your human experience and business process. We don't consult outside that."

Adjust the language to the client's sector — compliance-first for a regulated industry, throughput-first for heavy industry — but keep the structure honest.
