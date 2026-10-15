# Estimating test effort

How to size the test rows of a plan and check that the plan carries the testing its promises depend on. The estimate method itself (basis per row, ranges, contingency, AI adjustments, actuals) is in `project`: [estimating](../../project/references/estimating.md). This module lists what to estimate for testing and what to check.

## Test products

List the test products before the tasks, each with its acceptance check, then derive tasks for each. The method is product-based planning in [project estimating](../../project/references/estimating.md). Test products usually include:

| Product | Drivers of its size |
|---|---|
| Test strategy and plan | Number of risks and levels; client review rounds |
| Case set per level | Number of requirements or acceptance criteria; variant axes per requirement |
| Test data and environments | Input classes to cover; data that must be prepared, cleaned or made non-sensitive |
| Reference set (model-based systems) | Documents × fields per document × labellers; adjudication; the client's labelling time |
| Scoring harness and runs | Classes; runs (dry, binding, regression after each tuning round) |
| Injected-error suite | Error classes × injections per class; client review of the suite |
| Integration and end-to-end runs | Interfaces and paths; external services in the path |
| Regression passes | Number of builds shown or released |
| Defect fixing and verification | Expected defects; fix and re-test per defect |
| Acceptance support | Scripts; dry run; remediation cycle; binding run; evidence pack assembly |
| Non-functional and security tests | Requirements stated; tools; environment |

Resources spent on testing should be in proportion to how critical the application is. [book:swebok], 5.2. Test Activities

## Row basis

- Each row states its basis, as `project` requires. Measures of past test effort and of how many faults each phase found are what managers use to control and improve testing; use your own where they exist. [book:swebok], 5.1. Practical Considerations
- **Percentage of development.** Testing derived as a fixed share of coding is a parametric estimate and holds only with a ratio from the team's own past projects; state its source. A cut to coding (for AI assistance) does not cut testing by itself. Both rules are in [project estimating](../../project/references/estimating.md).
- **Defect fixing.** If the defect budget is not from your own history, say so on the row and give a range. (derived: EVOLUTION.md case 13)
- **Time held by people outside the team.** Client labelling, adjudication, script sign-off and acceptance windows are calendar time that agents do not shorten. Estimate them as dated dependencies with an owner, not as task effort. (derived: EVOLUTION.md case 4)
- **Inherited drivers.** If a test-set size is computed from an unconfirmed figure (fields per document, documents in scope), every row sized from it moves with it; list those rows together. (derived: EVOLUTION.md case 11)

## Checks on the plan

Run these on any WBS or schedule that contains testing, and on every scope cut.

1. **Every evidence item has a producer.** For each item promised at acceptance (in the plan, the deck or the contract), name the task that produces it. A removed task leaves its promises orphaned. (derived: EVOLUTION.md case 7)
2. **Order follows the oracle.** Scoring starts after labelling closes; tuning finishes before the configuration freeze; the binding run comes after the dry run and its remediation. (derived: EVOLUTION.md case 8)
3. **Independence holds in the seats.** Defect fixing and fix verification sit on different seats; test authoring is not only on the implementer's seat. (derived: EVOLUTION.md case 10)
4. **Measurement tasks match the claims.** If injected errors are out of scope, no committed detection rate remains anywhere; if a repeatable regression harness is out, no promise of a scorecard at each checkpoint remains. (derived: EVOLUTION.md case 6)
5. **A regression pass precedes each client showing.** (derived: EVOLUTION.md case 9)
6. **Tuning and scoring sets are separate**, or the plan says the binding score is on the tuning set. (derived: EVOLUTION.md case 12)

## Progress reports

Report counts: cases specified, executed, passed, failed, blocked; open defects by severity. [book:swebok], 5.2. Test Activities. Combine phase reports with root-cause analysis to see whether faults are found as early as possible. [book:swebok], 5.2. Test Activities

## Actuals

Record each test row's estimate against its actual effort and the number of defects found per phase, so the next estimate has a basis. The actuals file and lessons are kept as in [project estimating](../../project/references/estimating.md).
