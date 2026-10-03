# Assess and Analyze Modes

Assess code health and investigate results with the smallest change that addresses a demonstrated problem. Separate source-grounded findings from recommendations and keep uncertainty visible.

## Assess code

### Scope and inspect

Start with the area the user identified. Ask what hurts and narrow the assessment to code causing defects, blocked work, onboarding friction, maintenance burden or slow development. For a small codebase, read the relevant code directly; for a large one, start with the affected directories.

Run scripts/analyze.py in summary mode first; use the full report only when a finding warrants it. Static analysis is a guide. Dynamic imports, plugins, generated entry points and external consumers can be invisible, so inspect relevant paths and call sites before recommending a high-impact change. [book:software-engineering-at-google], Code Correctness

### Review dimensions

- **Size and responsibility:** A file over 500 lines is a prompt to review cohesion and readability, except generated or data files. Keep one clear responsibility per file; do not treat a line count as a hard failure threshold. [book:clean-code], Vertical Formatting; [book:clean-code], Chapter 10: Classes
- **Configuration:** Look for scattered hardcoded URLs, thresholds and credentials. Keep build, deploy, test and release assets in version control, with configuration in a clear high-level location. [book:continuous-delivery], What Are the Benefits?
- **Dependencies:** Inspect the dependency graph for cycles and hotspots; identify the coupling that makes changes risky. [book:clean-architecture], The Acyclic Dependencies Principle
- **Reachability:** Confirm whether apparently unused code has a real caller before removal. For confirmed dead code, remove it; for a static-analysis hit with unknown dynamic entry points, investigate first rather than deleting blindly. [book:clean-code], Chapter 17: Smells and Heuristics
- **Test coverage:** Use branch coverage to locate behaviors and branches the suite has not exercised. Coverage is a map of likely gaps, not proof of correctness or a target percentage by itself. [book:real-world-software-development], Code Coverage

When proposing an API or system removal, trace actual callers and unexpected uses, then revisit the removal decision if that evidence changes. Deprecation is appropriate when the system is demonstrably obsolete and a comparable replacement exists; define the removal conditions and process before retiring it. [book:software-engineering-at-google], Deprecation Tooling; [book:software-engineering-at-google], Why Deprecate?

### Complete Assess

Complete Assess only when the page exists and the index and log point to it.

### Present and act

Order findings by severity, evidence, dependencies and the user's goal. Use impact-versus-effort to choose where testing should start, not as a universal ranking formula for every assessment finding. Give each finding a location, evidence, likely consequence and a concrete next step. [book:site-reliability-engineering], Creating a Test and Build Environment

Write the durable assessment page in the project's wiki, link it from the index and append a log entry. Save scratch analysis separately. Shared wiki mechanics are in ../core/references/wiki-protocol.md.

## Analyze results

Use Analyze when the question is why a metric, model output or system result looks a certain way. Separate defects in results from defects in code. Do not use this mode to make ML/CV/NLP evaluation or model-selection decisions; hand those to ../applied-ml-problem-solver/SKILL.md.

Follow this sequence:

1. **Failure taxonomy:** classify the result failures and their distribution.
2. **Causal model:** map candidate causes to effects.
3. **Disconfirmation:** hold two or three plausible causal frames. For each, ask what evidence should appear if it is true and what would contradict it. Search for the disconfirming log, query or metric. Classify anomalies as explained, concerning or frame-breaking; name the condition that would reopen the analysis.
4. **Prioritize tests:** when choosing tests to run first, prefer high expected impact for low effort. Do not rank all recommendations by a ratio.
5. **Experiment:** define a specific change and before/after measurement criteria. Confirm the instrument and units can resolve the target difference.
6. **Impact view:** estimate the expected improvement for each intervention and order by cumulative gain where the evidence supports it.

The first plausible cause is not enough: a past analysis anchored on its leading explanation until a contrary pattern in the results forced another frame. Look for evidence that could prove the preferred explanation wrong.

Save the working analysis and any before/after results under the project's scratch logs. Promote the conclusions into a durable wiki analysis page, link it from the index, add a log entry, and record any conclusion that changes direction in the decision record. Complete Analyze only after those records exist. See ../core/references/wiki-protocol.md.

## Harden findings

If the user chooses to act, make one change at a time and verify it before moving to the next. The user controls whether to continue.

When assessment findings need code changes, group them by severity and make phased success criteria. Use the Build mode test-first process for each phase; run the full regression suite after each severity tier. The failing-test phase is the source-backed TDD practice; grouping and tiered regression are dev's hardening workflow. [book:learning-test-driven-development], Red-Green-Refactor: The Building Blocks of TDD
