# Design Mode

Produce a development-ready engineering design from an idea, request, or accepted upstream decision. Clarify the user problem, decide the technical shape, identify consequential unknowns, and hand off one coherent specification that can guide a build.

## Clarify and decide

Start with the problem, users, motivation, constraints and scope. Ask naturally rather than interrogating; summarize the shared understanding, state assumptions, and list unknowns that need research. [book:swebok], Process Actors; [book:swebok], System Requirements Specification

When a request uses broad business language such as “add authentication” or “make it fast,” surface the actual decisions as two or three options per fork. State the tradeoff, recommend one, and ask for direction before accepting scope. If two answers remain vague, stop and request binary, testable criteria. Requirements negotiation should reach agreement instead of leaving an engineer to choose unilaterally. [book:swebok], Requirements Negotiation; [book:swebok], Tradeoff Analysis; [book:swebok], Quantifiable Requirements

A decision that affects implementation must be stated so two engineers can interpret the test the same way. Research may still be needed to close a gap; do not block research just because the answer is not yet known. In iterative work, refine one behavior at a time and make its criterion testable before its test is written; do not require every later behavior to be settled before learning can begin. Before handing a design to Build, turn the agreed requirements into verifiable inputs and outcomes, and record any accepted uncertainty. [book:swebok], Quantifiable Requirements; [book:real-world-software-development], Why Use TDD?

For ML, CV, or NLP work, hand off the decision framing before choosing the engineering design. Dev takes the framed decision back for implementation; it does not restate or perform the sibling's decision method. See ../applied-ml-problem-solver/SKILL.md.

## Research and ground

Calibrate research to the situation: use a light check for clear, familiar requirements; focus on clarification for unclear requirements in a familiar domain; investigate unfamiliar or ambiguous areas deeply enough to make the decision. Research is a response to a surfaced unknown, not a mandatory phase before every task.

For a covered domain, search the whole project Knowledge Base before deciding and write one result line in Key Decisions. Use a second query or generated passage only when the first search missed because it used different vocabulary. For uncovered areas, inspect the code and official documentation. The project's version-controlled guidance should point to canonical sources rather than duplicating their content. [book:software-engineering-at-google], Guidance; [book:software-engineering-at-google], Considerations When Importing

Do not leave Design Phase 1 until the decision owner approves a design document and every key decision records its trade-offs and covered alternatives. [book:software-engineering-at-google], Design Docs

When research finds a direction-changing alternative, a major constraint, or scope larger than expected, stop and present it to the user before proceeding. Keep the useful finding and the source in the project decision record.

For qualifying designs, apply the Invariant Gate from SKILL.md before build: multi-tenant data, authorization, external or irreversible effects, and crash/restart recovery. Add one Key Decisions line per applicable class, with a test that proves the guarantee is reachable. This five-class gate is dev field practice.

## Development-ready specification

Keep the system's design coherent: write one spec in one voice instead of concatenating producer documents. Multiple sound ideas can still make a confusing design when nobody reconciles their boundaries. [book:learning-systems-thinking], Chapter 2. Crafting Conceptual Integrity

Scale the document set to the change. A small tool may need only a concise design and project quick start; a service may need a design, data and API contracts; a multi-component system needs a canonical design document covering architecture, technology, data and interfaces. Prefer one coordinated design document over several disconnected architecture, tech-stack, data-model and API files. [book:software-engineering-at-google], Design Docs

Give each project document one purpose. Use the project's standard agent-instructions filename for operational guidance, and link to separate overview, quick-start, architecture, decisions and constraints documents when those topics need durable detail. A quick start should assume nothing and show a reader how to make the first real thing work. [book:software-engineering-at-google], Documentation Types; [book:software-engineering-at-google], Tutorials

The design should name its goals and how the team will later tell whether the delivered system achieved them. Write concrete acceptance conditions, implementation strategy, key decisions, alternatives and tradeoffs for each key decision, constraints, and any remaining unknowns. Keep contracts refinable during greenfield work; when a service boundary matters, add provider-consumer contract tests rather than relying only on a schema changelog. [book:software-engineering-at-google], Design Docs; [book:building-evolutionary-architectures], Case Study: Validating API Consistency in an Automated Build

For cross-cutting security, privacy, storage or reliability sections, request review by an engineer with the relevant expertise before implementation. [book:software-engineering-at-google], Design Docs
For a reliability-sensitive service, state the SLO as a target on a defined SLI, including the measurement and the conditions under which it is valid. [book:site-reliability-engineering], Service Level Objectives

## Review and hand off

Review every design before code is written. The level can be proportionate to the task, but do not silently bypass the design check. For consequential handoffs, have another engineer review the requirements document for the right product, clarity, consistency and completeness; provide the material needed to understand the requirements rather than claiming the source mandates a context-free review. [book:software-engineering-at-google], Design Docs; [book:swebok], 6. Requirements Validation

For higher-risk or complex designs, use a separate reviewer who did not make the design decisions. Ask them to find gaps in the requirements, contradictions, architectural risks and missing unknowns. Close every review comment before handoff: fix critical findings, get an owner decision on warnings, and record the disposition of advisory comments. If three or more critical findings appear, revise the design rather than patching them one by one.

A design handoff is ready when its goals and measures are written down, requirements are testable, accepted unknowns are visible, all review comments have a disposition, and a stranger can build from the specification. Present the artifacts and ask the decision owner to accept the design after debate and expert critique. Then transition to Build using those artifacts. [book:software-engineering-at-google], Design Docs; [book:software-engineering-at-google], Code Review Flow
