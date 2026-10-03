---
name: solution-architect
description: "Client-facing solution architecture and presale response pack for a presale solution architect and client evaluation team. USE WHEN an RFI/RFP, discovery output, or brief must become a defensible solution, consulting agreement, or proposal options. Not business-intelligence (qualification and account intelligence), ai-discovery-workshop (use-case scoping), delivery (signed engagement control), or dev (implementation); this skill owns presignature solution design, terms, and response shaping. Keywords: solution architect, SA, RFI, RFP, proposal, tender, bid, response pack, solution architecture, reference architecture, technology options, trade-offs, NFR, traceability, consulting agreement, value pricing, negotiation, presale."
license: MIT
---

# Solution Architect

This skill produces a client-facing solution architecture and response pack for a presale solution architect and the client evaluation team. It turns client requirements, a discovery output, or a brief into a defensible solution, proposal options, and a handoff that is usable after signature.

> Inherits the shared `core` kernel. Use its canonical gates and references; do not copy their definitions here. See `../core/SKILL.md`.

## When it fires — and when a sibling owns it

Use this workflow for a presignature solution architecture, RFI/RFP/tender response, proposal, technology options analysis, NFR definition, requirements traceability, or a consulting agreement and negotiation that shapes the response pack.

- Look beyond product lists to compare decision options and trade-offs; use a vendor-neutral default unless explicit vendor positioning is part of the client decision [book:software-architect-elevator], Measuring an Architect’s Value.
- Keep this work client-facing: engineering owns implementation specifications and the delivery of running software [book:software-architect-elevator], What Architects Are Not.
- At signature, hand negotiated acceptance criteria and obligations to delivery for tracking; keep project status reporting outside the architecture role [book:software-architect-elevator], What Architects Are Not.

## Principles / anchoring rules

1. Understand the client decision before selecting a product or drawing a view.
2. Compare viable options against the client’s constraints, quality priorities, and intended outcome.
3. Trace requirements, keep assumptions correctable, and explain the option that binds the proposal.

- Maintain forward traceability from requirements into design; for the response, map each requirement to a solution element and phase, and turn gaps into questions [book:swebok], Requirements Tracing. (5907 · U3 · L23 · 08:42–10:47)
- Connect clause answers to an explanatory solution narrative the evaluator can follow [book:storytelling-with-data], Who, what, and how.
- Compare two or three viable options on client-relevant axes, recommend one, and explain why the alternatives lost [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Tie each win theme to a customer pain, the metric that makes it matter, and a related decision criterion [book:meddicc], COMPETITION.
- Set lifecycle rigor from project criticality, stakeholder count, uncertainty, and deal risk [book:pmbok-guide-7e], 3.2. Why Tailor?.
- State the decision problem, goals, and constraints; add what success means and frame it before choosing a solution [book:fundamentals-enterprise-architecture], Overview. (5907 · U3 · L20 · 06:41–07:20)
- Use repeated why-questions to uncover root causes; challenge vague briefs before architecture and explain the reframing in the response [book:software-architect-elevator], Five Whys. (5907 · U3 · L20 · 02:47–03:41)
- Write the decision context before drawing an architecture diagram [book:facilitating-software-architecture], Step 2: Write the Context.
- Define NFRs from the client’s business needs and prioritize their trade-offs; do not assume every named quality applies universally [book:fundamentals-enterprise-architecture], Summarizing NFRs.
- Translate business outcomes into technical drivers, then state decision criteria, constraints, and sequence before drawing architecture [book:software-architect-elevator], Measuring an Architect’s Value.
- Let requirements and trade-offs drive architecture; position products after the decision options are clear [book:software-architect-elevator], Measuring an Architect’s Value.
- Surface tacit assumptions and hidden dependencies. Mark unconfirmed matters as correctable assumptions and flag uncertainty [book:software-architect-elevator], Architects Deal with Nonrequirements. (5907 · U3 · L22 · 09:47–11:00)
- Show alternatives and trade-offs; do not present a single-option architecture [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Compare solution options and trade-offs before positioning a vendor; treat the neutral-first sequence as a presale practice, not as a claim the source makes [book:software-architect-elevator], Measuring an Architect’s Value.
- Translate relevant security requirements into architecture decisions early; do not treat a generic NFR checklist as a complete universal gate [book:fundamentals-enterprise-architecture], Security NFRs.


## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Frame | Establish the outcome, decision, constraints, negative space, and intended reader. | Internal engagement frame |
| Clarify | Resolve requirements, assumptions, and client-only questions. | Clarification questions and assumptions register |
| Architect | Compare viable options and document the recommendation and its consequences. | Solution architecture and decision records |
| Shape the response | Tie the solution to the evaluator’s criteria and present proposal options. | Response pack, traceability matrix, commercial options |
| Agree terms | Negotiate scope, client inputs, measures, fees, and the written consulting agreement. | Consulting agreement and pre-signature annexes |
| Sign and hand off | Transfer accepted decisions, estimates, criteria, obligations, and risks to delivery. | Delivery handoff packet |

Scale the work to the deal. A narrow clarification can stay light; a multi-round bid may need a blueprint workbook. The sale does not authorize a general project plan: general project planning belongs to the project-planning workflow.

## Work-specific operating rules



- Quote the client's ask verbatim, list the artifacts that answer it, and mark extras as proposed with a named consumer and decision. (5907 · U3 · L22 · 08:04–09:47)
- For covered technical domains, search the Knowledge Base first and record the query and applied finding, or that nothing relevant was found.
- Before substantive solution-architecture work that fans out or forks, state the lane's approach and reason; compare independent options for wide decision spaces and research unknowns first. In a coordinated multi-skill run, conductor records the task-level approach declaration in its Plan Block; this rule governs the SA workstream.
- For research that changes the build, present audience-relevant findings rather than exploratory analysis; use a concise findings list where useful [book:storytelling-with-data], Who, what, and how.


## Presale artifacts

| Artifact | Audience and purpose |
|---|---|
| Engagement frame | Internal use; holds the problem, decision, constraints, negative space, and candidate projects. |
| Clarification questions and assumptions register | Client-facing questions and the correctable positions used while answers are pending. |
| Solution architecture and decision records | Client evaluation and engineering handoff; explain context, options, recommendation, and what the choice binds. |
| Response and requirements traceability | Client evaluator; show how every stated need is addressed or left open. |
| Consulting agreement, acceptance annex, and client-obligation register | Client and delivery; capture negotiated terms through signature. Delivery owns live signed-client trackers. |
| Delivery WBS instrument | Delivery planner; enumerate work for estimation and staffing, leaving effort blank. |
| Blueprint workbook | Multi-round bid carrier; propagate each answer across affected sheets and log cell-level changes. |

The client-facing exports and cross-artifact integrity checks are different reviews; use both when their scope applies.

## Gates (declared, inherited from core)

- Grounding: `../core/references/grounding-gate.md`.
- Result evidence and completion: `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- Cooperative pushback and teaching: `../core/references/pushback-and-teach.md`.

The presale-specific checks are in this skill’s linked references. Apply them to the artifact and deal shape in front of you.

## Anti-patterns (hard no-list)

- Starting with technology or a diagram before the client problem and decision are clear.
- Comparing one preferred option to nothing, treating a generic NFR list as universal, or claiming full coverage without traceability.
- Turning intake into account research or qualification; consume the evidence from its owner.
- Filling delivery effort estimates as the architect, or continuing to own signed-client tracking after handoff.
- Adding artifacts that do not answer the ask or serve a named reader’s decision.

## Composition

- **From business-intelligence:** use evidence-grounded account, stakeholder, competitor, and qualification inputs. Do not recreate the dossier or qualification method.
- **From ai-discovery-workshop:** use the accepted use case, journey, and outcome baseline; the workshop owns its scoped brief.
- **From applied-ml-problem-solver:** use its model, metric, and evaluation decisions when the solution includes ML.
- **From ceric:** use source-document claim gaps and ranked findings to shape clarifications.
- **With delivery:** the delivery planner authors presignature effort estimates; this skill supplies architecture and technical cost drivers. At signature, transfer the agreed packet. Delivery owns baselines, change control, acceptance tracking, and signed-client follow-up.
- **To dev:** hand over the accepted client architecture and decision context for implementation. General project planning remains outside this skill.

## References

- `references/sa-lifecycle.md` — presale phases, proportionate depth, and phase outputs.
- `references/engagement-intake.md` — frame, negative space, candidate projects, and client inputs.
- `references/deal-shapes.md` — choose the commercial shape before its instruments.
- `references/tech-selection.md` — options, reference architecture, decision records, and trade-offs.
- `references/nfr-checklist.md` — client-specific quality, security, integration, and operational requirements.
- `references/rfi-rfp-response.md` — clarification, response structure, traceability, win themes, and final export review.
- `references/acceptance-and-contract.md` — terms negotiated before signature, acceptance annex, and client obligations.
- `references/estimation-and-costing.md` — effort-estimate ownership, technical cost drivers, and commercial options.
- `references/artifact-integrity.md` — presale artifact consistency and cross-reference checks.
- `references/blueprint-workbook.md` — multi-round bid workbook and answer-folding loop.
- `references/composition.md` — input and signature handoffs.
- `references/templates/engagement-frame.md` — internal intake form.
- `references/templates/clarification-questions.md` — client question form.
- `references/templates/assumptions-register.md` — correctable assumptions form.
- `references/templates/client-obligations-register.md` — client inputs and schedule-relative deadlines.
- `references/templates/rfi-rfp-response-template.md` — response-pack outline.
- `references/templates/delivery-wbs-workbook.md` — delivery planner’s work-collection instrument.
