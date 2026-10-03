# Method for a Product Decision Brief

## Choose brief depth by decision

Use one product decision brief for both discovery and release decisions. For a new product or a decision with major market, user, or lifecycle uncertainty, use the full method. For an incremental release on an established product, keep the brief focused on the decision, current user problem and evidence, proposed delta, outcomes and measures, release criteria, dependencies, and next review. Reuse or link prior evidence for context that has not changed, and mark an inapplicable field with a short reason instead of inventing content. Link the engineering or project tracker for task-level owners, commits, worktrees, asset distribution, migration steps, or operating schedules. (derived: dogfood 2026-10-01)

Human-participant research fields apply when the decision needs research with people. An automated benchmark or system evaluation can instead name its evaluated population or configuration, task scenario, run count, measures, and decision threshold; do not fabricate interview participants or prompts. Keep all applicable discovery, learning, and release guidance available for cases that need it. (derived: dogfood 2026-10-01)

## Treat the product as a continuing decision

A product continues after launch and can change as its users, market, and organization change. Use the brief as a dated snapshot of the current decision, evidence, and next review point; do not treat it as a one-time project plan.

Connect the choice to the product vision and strategy, and state why the decision matters now. Clarify the customer or user benefit alongside the business outcome. Frame the work around the change people should experience, rather than beginning with a feature request. Business understanding starts with the problem and the decision to be supported. [book:data-science-for-business], Chapter 2. Business Problems and Data Science Solutions

Describe an intended outcome as a change in user or business behavior, then treat a proposed feature as a hypothesis about how to produce that change. Outcomes give the team a way to judge progress after implementation. [book:lean-ux], Chapter 3. Driving Vision with Outcomes

## Frame the problem and gather evidence

Name the customer, buyer, and user groups where they differ. Describe who experiences the problem, the situation in which it occurs, the goal they are trying to reach, current workarounds, and what the organization needs to change. State the decision the evidence must inform.

Gather evidence from direct conversations and observation, and add relevant quantitative, market, or competitor evidence. Keep the source, date, audience, and scope with each finding. Synthesize across people and segments; label inference and uncertainty instead of blending them into facts.

For interviews, make an exploration plan that separates what is known from what still needs to be learned. Reuse and adapt suitable prompts from a question bank, and write new interview questions for each learning gap. Decide whether the team needs to understand how a task or process is carried out; if it does, use the journey-focused template.

For quantitative benchmarks, record the metric definition, baseline, observed value and delta, population or sample size, and significance or p-value when calculated. Distinguish values reported by a source from values measured or calculated in this work; use the matching `_reported` and `_measured` fields, and mark statistical fields not applicable when the method does not produce them. (derived: dogfood 2026-10-01)

Connect what matters to users with business viability and technical or operational feasibility. Turn a grounded insight into a positive, open question that invites multiple solutions without naming one in advance. A clear point of view helps the team explore the right problem before choosing an implementation.

## Choose outcomes and preserve uncertainty

Compare opportunities against the product strategy and the people they serve. Consider user value, business impact, feasibility, effort, risk, and uncertainty. Use a prioritization lens such as impact and effort or an opportunity tree when it helps the conversation; name the assumptions behind each estimate.

Challenge a favored idea by asking why it matters now, why this approach fits, and what evidence would change the recommendation.

Recommend one opportunity and explain why it is the best next decision. A score can support comparison, but it should not erase rationale, unknowns, or evidence gaps. Prioritization should retain the questions that could change the choice. [book:art-of-ai-product-development], 2 Discovering and prioritizing AI opportunities

Define an objective that names the desired change and a small set of measurable results that show progress. Link the results to product strategy and record a baseline, target, period, and any guardrail. Keep the roadmap at the level of outcome-focused initiatives, with a horizon and confidence appropriate to what is known.

Map the end-to-end user story before expanding feature detail. Put activities and steps in the order people experience them, then add important tasks, alternatives, and failure paths beneath the relevant step. Use the map to create shared understanding, reveal gaps, and discuss trade-offs together. [book:user-story-mapping], Chapter 1. The Big Picture

Slice the map into releases by asking what outcome a specific user needs to achieve in each release. The smallest useful release must deliver that outcome; a minimum viable release is not merely the least functionality the team can ship. Order later slices around the outcomes they are expected to create. [book:user-story-mapping], Chapter 2. Plan to Build Less

## Map AI- and agent-mediated journeys

When an AI system or autonomous agent is the direct product user, map its goal and decision loop alongside any human journey. Include the initiating context or prompt, available tools and schema constraints, token or context budget, tool selection and calls, returned results and secondary reads, retries, handoffs, and recovery from partial or failed actions. State what success the agent can observe, where it must stop or ask for human input, and how it recovers without losing important state. Include human setup, oversight, and outcomes where people are part of the system. (derived: dogfood 2026-10-01)

## Shape a bounded specification and learning step

Describe the chosen user, scenario, core journey, and behavior the solution must support. Include in-scope and out-of-scope work, acceptance signals, material constraints, dependencies, risks, and unanswered questions. Keep implementation detail proportional to the decision and the next work being planned.

State the highest-risk assumption and what evidence would change the decision. Write a testable hypothesis that links a user or segment, a proposed change, an expected observable result, and the reason for expecting it. Choose a test and predeclare the metric or decision threshold that will count as support, failure, or inconclusive evidence.

Choose the least costly prototype or experiment that can answer the next important question. Match its fidelity to the question and audience; test the risky part of the journey before investing in a complete solution. Learning can come from a sketch, service trial, concierge step, or software slice. [book:lean-ux], Chapter 5. Minimum Viable Products and Prototypes

When validation uses human participants, plan around a defined participant or audience, realistic scenario, tasks, and neutral prompts. Record observable behavior and participant feedback separately. Decide beforehand what would support or weaken the hypothesis, and what the team will do with each result. For an automated evaluation, use the benchmark population and configuration, task scenario, measures, sample size, and a predeclared threshold instead. (derived: dogfood 2026-10-01)

## Define measures and plan release

For each outcome, explain how it will be observed. Connect the objective to a user or business signal, then to a defined metric with its unit, data source, population, period, and baseline. Choose a comparison that makes sense for the actual product decision; a metric without a relevant baseline can create false confidence. [book:data-science-for-business], Chapter 7. Decision Analytic Thinking I: What Is a Good Model?

Use a small group of complementary measures when one number would hide important effects. Depending on the product, consider reach, frequency of use, depth of use, efficiency, and user satisfaction alongside the business result. Name guardrails that would reveal harm or unacceptable cost.

Describe the roadmap as a sequence of outcome initiatives and release horizons, not a task inventory. Record dependencies across teams, decision points, confidence, and what evidence could reorder the work. For launch, include readiness conditions for stakeholders, support, communication, dependencies, and measurement; name the owner and timing of the first post-release review.

## Learn and change direction

After a test or release, compare observed results with the baseline, target, and guardrails. Record what worked, what needs improvement, what was surprising, new questions, and possible next solutions. Update the evidence and assumptions before changing the priority or specification.

Keep a lightweight decision log with each brief. Append a new row when a review changes or reaffirms the decision; preserve prior rows so the rationale remains visible. Create a versioned copy only when organizational change control or audit needs require it, and link the versions. Use the schema in the brief template. (derived: dogfood 2026-10-01)

Keep an opportunity backlog for problems and outcomes still worth exploring, and a solution backlog for options supported by evidence. Revisit both after validation so that the next slice reflects what the team has learned.

At lifecycle reviews, decide whether to evolve the product, transition users to another option, or sunset it. Consider customer and user impact, stakeholder and organizational effects, support needs, and the evidence for continuing investment. Communicate the decision and its transition plan to the people affected.
