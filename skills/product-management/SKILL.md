---
name: product-management
description: "Produces a product decision brief connecting user problem, evidence, prioritization, measures, specification, and roadmap. USE WHEN a product manager must decide what to build, measure, change, launch, or retire. Disambiguation: client-validated AI use-case briefs belong to the specialized AI discovery workflow; this skill owns general product decisions. Keywords: product management, product discovery, product strategy, product brief, roadmap, prioritization, MVP, product metrics, feature definition, product lifecycle."
license: Proprietary (private; cites a paid course)
---

# Product Management: Product Decision Brief

Create a decision brief that connects a real user problem to evidence, an explicit choice, measurable outcomes, a bounded specification, and an outcome-led roadmap. The brief helps a product manager decide what to build, measure, change, launch, or retire.

## Scope

Use this skill for general product decisions across discovery, delivery, launch, and the product lifecycle. A brief can be revised as new evidence arrives; a roadmap records current choices and confidence, not a promise that every item will ship.

For a client-specific, validated AI use case, route to the specialized AI discovery workflow. This skill can carry the resulting opportunity into broader product planning, but it does not replace that client-validation artifact.

## Handoffs

When a brief needs a formal audit of how its claims follow from evidence, send those claims through the argument-review process and keep the decision brief as the product artifact. When an approved choice needs architecture or implementation, give the brief to the engineering build workflow; the product manager remains accountable for product outcomes, priorities, and roadmap choices.

## Workflow

1. **Name the decision.** State what decision is needed, who owns it, why now, and what product or lifecycle context constrains it.
2. **Frame the problem.** Identify the people affected, their context and goals, the unmet need, and the business or organizational outcome. Separate observed evidence from assumptions.
3. **Compare opportunities.** Connect user value, strategic fit, business viability, feasibility, effort, risk, and uncertainty. Recommend a choice and preserve the rationale and open questions.
4. **Set outcomes and measures.** Define an objective, measurable results, a baseline, a target, a time window, and guardrails. Make clear what user or business change would count as success.
5. **Shape the specification.** Map the important user journey, describe the smallest useful solution or learning step, set boundaries and constraints, and identify dependencies and risks.
6. **Plan the roadmap and learning.** Sequence outcome-based initiatives, release conditions, experiments, and review points. Include confidence and dependencies; avoid presenting a feature list as a committed delivery schedule.
7. **Revisit after evidence arrives.** Compare results with the stated measures, update the brief, and decide whether to improve, extend, transition, or sunset the product or capability.

Use [the decision method](references/decision-method.md) for the detailed practice and [the product decision brief template](references/templates/product-decision-brief.md) for the primary artifact.

## Shared gates

Before delivery, apply the shared kernel’s canonical grounding, output-contract, wiki, and pushback gates. Refer to `core/SKILL.md` and `core/references/grounding-gate.md`, `output-contract.md`, `wiki-protocol.md`, and `pushback-and-teach.md`; do not duplicate those gates in this skill.

## Output standard

The brief should make the decision and its consequences easy to inspect. Keep source, date, scope, confidence, and uncertainty visible for evidence and measures. Leave unknowns open instead of filling gaps with invented facts. If inputs are incomplete, produce a useful draft with explicit questions and assumptions for the decision owner.
