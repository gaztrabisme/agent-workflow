# Output Contract

A completion claim is about the result artifact. Name what was checked and show the evidence that answers the question the work was meant to resolve.

## Result integrity gate

- Keep the original success criteria fixed. If they cannot be met, stop and report rather than changing them to fit the result. If new evidence requires a baseline change, use the approved variance protocol below and report both baselines. [book:building-evolutionary-architectures], Fitness Function-Driven Architecture.
- Do not claim success without evidence; show the artifact or output itself. [book:continuous-delivery], Principles of Software Delivery.
- Do not silently skip a requirement or a planned gate. Obtain approval, or state what was skipped and why. [book:building-applications-ai-agents], Conclusion.
- Report failures honestly; never fabricate results. [book:site-reliability-engineering], Keep a History of Outages.
- If blocked after more than three attempts, stop and report the blocker rather than silently working around it. [book:site-reliability-engineering], All Problems Have Solutions.
- Verify the artifact the work was meant to produce, not the activity intended to produce it. [book:continuous-delivery], The Automated Acceptance Test Gate.
- Choose a check that can distinguish the outcome it is meant to test; a passing proxy that cannot resolve the question is not enough. [book:continuous-delivery], The Automated Acceptance Test Gate.
- Run a planned gate when an action is irreversible or could fail silently. [book:building-applications-ai-agents], Reflection Agents.
- For every success criterion, show evidence; if it is deferred or not applicable, state the reason. [book:swebok], Modeling, Simulation, and Prototyping.

## Completion evidence and durable outputs

- Write each mode's result to the project wiki or the skill's evolution log before calling it done. Confirm the named artifact exists. [book:software-engineering-at-google], Documentation Is Like Code.
- Keep the process that produced a deliverable somewhere durable. When a session creates a generator, treat it as part of the deliverable: move it into the project, index it, and record its expected inputs and the verification that proved its output correct. [book:continuous-delivery], Principles of Software Delivery.
- Keep build or generation scripts in version control, preferably alongside the source they produce. [book:continuous-delivery], Principles and Practices of Build and Deployment Scripting.
- Use repository-relative paths by default. If an absolute path is unavoidable, isolate it as configuration rather than making it the normal path. [book:continuous-delivery], Tips and Tricks.

## Success measures and contracts

- For important success criteria, encode a checkable fitness function when practical so later changes can be tested against the same target. [book:building-evolutionary-architectures], Fitness Function-Driven Architecture.
- Before adopting a measure, check whether it rewards volume over value, changes behavior merely by being measured, or invites people to optimize the wrong thing. [book:pmbok-guide-7e], Measurement Pitfalls.

## Approved variance

An approved variance records a newly discovered mismatch between the plan and the work; it does not silently change the original success criteria.

- Record the original baseline, the newly discovered evidence, the proposed change, affected artifacts and gates, and the expected impact before applying the variance.
- Obtain written approval from the accountable decision owner and an independent reviewer before changing scope, source coverage, artifact expectations, or a gate's applicability. Update the plan, audit brief, and review record together; do not coach an auditor privately or alter a check to force a pass.
- If success criteria themselves need revision, preserve the original set and create a separately versioned baseline with the reason and approvals before evaluation. Report the result against both baselines; never use the new baseline to relabel an observed failure as a pass.
- If approval is unavailable, keep the original baseline and report the unresolved mismatch. (derived: dogfood 2026-10-01)

## Independent review

- Before a primary artifact ships, pre-register expected weaknesses in the shared gate review record. When the artifact warrants the full review floor, use three distinct passes: technical accuracy by a subject-matter expert, audience clarity by someone with no prior context checking against the source of record, and writing consistency. [book:software-engineering-at-google], Documentation Reviews.
- Judge the review by whether it found the pre-registered weaknesses; record that check in the review record.
- Scale cold review to the stakes. It may be skipped for reversible internal work, but not for client-facing work. [book:software-engineering-at-google], Documentation Reviews.
- Automate mechanical checks so human reviewers can focus on judgment. Aim their attention at content the checks cannot inspect, including rendered or image-based material. [book:software-engineering-at-google], Automate Where Possible.
- For a judgment likely to be tested, brief two cold reviewers on different models with the same facts; do not share either reviewer's conclusions with the other. [book:learning-systems-thinking], One perspective is always insufficient.
- Act on defects where independent reviews converge, and record the agreed defects and actions in the review record. (derived: dogfood 2026-10-01)
- Investigate areas where independent reviews diverge, and record the disagreement and resolution. (derived: dogfood 2026-10-01)
- Brief adversarial reviewers cold with the architecture, constraints, and open questions. Withhold your conclusions and the other reviewers' conclusions. [book:swebok], Requirements Reviews.
- Record a review in the [shared gate review template](templates/gate-review.md): identify the artifact and version, state the review scope and pre-registered weaknesses, and record gate outcomes, findings, evidence, and approved exceptions. (derived: dogfood 2026-10-01)
- The two-reviewer gate requires two independent reviewer sessions using different models, the same fact packet, and isolated conclusions. Arrange a multi-model runner or separate reviewers before the gate begins. If the active lane cannot provide this, mark the gate DEFERRED in the review record, name what is missing, and hold any completion or shipping claim that depends on the judgment until the review runs. A self-review or persona shift does not satisfy the gate. (derived: dogfood 2026-10-01)

## Tailoring the gate set

Set the rigor, checks, balances, and artifact set from project criticality and context. Use just enough process to achieve the outcome, explain the tailoring to affected stakeholders, and gather their feedback as the work progresses. [book:pmbok-guide-7e], Why Tailor?; [book:pmbok-guide-7e], Tailor Based on Context.
