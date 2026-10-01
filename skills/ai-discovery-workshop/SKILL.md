---
name: ai-discovery-workshop
description: "Facilitate a client workshop that produces a client-validated AI use-case brief with journey, evidence, score caveats, and handoff for presale decision-makers. USE WHEN preparing or running AI discovery, BXT scoring, AI Discovery Cards, Golden Questions, journey mapping, or a PoV use-case decision. Keywords: AI discovery workshop, BXT, AI use case, Design Thinking, agentic workflow, journey map, Golden Questions, PoV. Disambiguation: business-intelligence prepares client research; product-management owns general product decisions; solution-architect owns the final architecture and proposal."
---

# AI Discovery Workshop

## Artifact and scope

The completed artifact is a client-validated AI use-case brief with a journey, evidence, score caveats, and handoff. Before client contact, the legitimate interim artifact is a clearly labeled `prework draft`: all scores remain provisional and the Golden Questions are marked not yet asked. A draft is not a client-validated decision. (derived: dogfood 2026-10-01)

The audience is the facilitator and the client's presale decision group, including business and technology decision-makers, business-unit stakeholders, end users, and subject-matter experts. Discovery teams benefit from including business stakeholders, subject-matter experts, customers, and end users. [book:user-story-mapping], A Discovery Team Needs Lots of Others to Succeed (5907 · U4 · L29 · 00:00–02:27)

Keep consulting within human experience and business process, generally giving process impact close attention. Avoid adjacent areas beyond your certainty. Use the four AI transformation pillars in references/discovery_cards.md to organize relevant opportunities within that scope; they do not expand it.

Map secondary personas as well as the primary persona when a complex workflow crosses roles. [book:user-story-mapping], Tell Your Users' Stories (5907 · U4 · L33 · 07:04–09:29)

Use business-intelligence for client research before Day 1 and bring its validated context into the room; this workshop turns that context into a client-validated use-case brief. After selection, hand architecture and proposal work to solution-architect. General product decisions belong to product-management. The workshop may capture an initial architecture conversation and prototype question, but it does not approve architecture or implement the prototype.

Inherit the shared kernel. Apply relevant integrity, grounding, and output-contract guidance by reference to ../core/SKILL.md and its current references; do not copy those gates into this skill. When a substantive unrouted task needs coordination, conductor owns the approach declaration; this workshop skill does not add one.

## Working principles

- Start with the client's problem and workflow, not a technology choice. A solution-led brief narrows the team before it understands the problem. [book:lean-ux], Problem Statement (5907 · U4 · L32 · 00:00–01:53)
- Make only claims you can defend. Mark uncertainty, missing evidence, and questions that need follow-up; being direct about possible AI failure builds trust. [book:art-of-ai-product-development], 12.3.2 Communicating about AI failure
- If technical feasibility is unknown, say so and leave the score provisional. Before pursuing higher-risk tasks, check that the team has the needed expertise and that potential payoff justifies the investment. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation (5907 · U4 · L34 · 01:50–03:20)
- Do not state a performance or savings statistic without a concrete baseline and a measurement plan. A suitable baseline is part of understanding the business task. [book:data-science-for-business], Evaluation, Baseline Performance, and Implications for Investments in Data
- Derive decision measures from the client's goals and express value in the client's terms; funding arrangements do not decide which use case is best. [book:meddicc], Metrics (5907 · U4 · L28 · 02:53–04:40)
- Keep commercial content out of the opening. The supplier enters after the client has agreed on the problem and is ready to discuss solutions. [book:challenger-sale], Step 6: Your Solution
- Tailor the opening to the business priorities of the people in the room, not only to their sector. [book:challenger-sale], Tailoring for Resonance

Opening frame: “You described [workflow or goal]. Today we will map how it works, test where AI may help, and leave with what we know, what remains uncertain, and what needs proof.” Use the client's words and fill in only details they have confirmed. Use this as the problem-first hook when asked how to approach an AI engagement. (5907 · U4 · L28 · 13:07–15:31) For products that use human-in-the-loop machine learning, the book recommends starting with the problem to solve and working backward. [book:human-in-the-loop-ml], Summary

## Four-phase working flow

Use Discover, Define, Develop, Deliver as a sequence: understand people and their work; frame and assess candidate problems; map the journey and explore AI assistance; then agree evidence, value, and next steps. Spend time empathizing, defining, and ideating before prototyping or testing. [book:art-of-ai-product-development], 2.3.1 The careful approach: Ready, aim, fire (5907 · U4 · L30 · 06:20–07:50)

Screen every candidate for AI suitability and record the evidence. Complete a BXT assessment for every candidate across Business, Experience, and Technology before routing; leave unknown scores provisional. After scoring, keep candidates with a plausible or uncertain AI role in the AI matrix. Route a clear `no` out of that matrix and, if the client wants further design, hand it to solution-architect as conventional scope. Treat the numeric matrix as intelligence gathering: keep details, evidence gaps, and open questions visible, and remain ready to revise scores. (derived: dogfood 2026-10-01) [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity

For enterprise AI engagements, use BXT to assess the candidate opportunities.

Target 3–5 agentic use cases per engagement and narrow them to one PoV-approved case by Day 8. This is a candidate use-case target, not a target count of agentic journey steps.

During journey mapping, prioritize a small number of journey steps, likely one, at the stage with the highest payoff. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation. Do not invent agentic steps where the workflow has none.

The Day 1 brief can carry two or three BXT-screened candidates into further discussion. Build the three-lane Agentic Journey Map between Day 1 and Day 8 and estimate where AI could augment or automate a step; mark the Agentic Workflow lane `none found` when no qualifying task exists, without inventing steps. The map and cards are the workshop method. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation

Estimate a feature's potential ROI to validate business value. [book:art-of-ai-product-development], 2.3.1 The careful approach: Ready, aim, fire

The standard Day 8 close produces the skill's output bundle: an approved PoV use case, ROI baseline, architecture draft, and a small rapid prototype, using ROI analysis, an architecture design session, and rapid prototyping. The PoV approval requires sufficient evidence, the relevant decision-makers, and agreed follow-up; when readiness is missing, mark the approval and dependent outputs pending, name the missing evidence and owner, and do not report them as complete. The architecture draft is a handoff input; solution-architect owns the formal architecture and proposal, and the implementation owner carries the prototype forward after handoff. (derived: dogfood 2026-10-01)

Use the references below as working materials. Prepare client-specific variants for the Five Golden Questions. Use supplied facilitator-script questions literally; for another language, agree the exact translated wording during prework and record it. Ask clarifying follow-ups and skip a prompt already answered, while adapting follow-ups and Golden Question variants to the room. Leave time for evidence and discussion. (derived: dogfood 2026-10-01)

## References

- references/workshop_agenda.md — contract, prework, session flow, timing, and materials.
- references/bxt_template.md — assessment fields, scoring, examples, and matrix caveats.
- references/discovery_cards.md — journey mapping, card use, transformation pillars, and automation levels.
- references/five_golden_questions.md — the BXT question bank and facilitation guidance.
- references/facilitator_scripts.md — literal prompts for BXT, journey mapping, approach choice, ROI, and handoff.
- references/methods_glossary.md — discovery, framing, synthesis, and convergence methods.
- references/commercial_framing.md — client-value framing and agreed next steps.
