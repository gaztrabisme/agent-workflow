# Test cases, test data, regression and defects

## Case design

Start from the list. Write down every behaviour you know must be tested before writing any of them, add new items to the list as they come up, and decide consciously whether each belongs now, later or not at all. [book:tdd-by-example], (part 19)

Derive cases with named techniques rather than by habit:

- **Equivalence partitioning** — split the input domain into classes expected to behave alike and test one or more from each. [book:swebok], 3.3. Code-Based Techniques
- **Boundary values** — choose cases on or near the edges of the input domain, where faults concentrate (for documents: the shortest and longest accepted, one page over a stated limit). [book:swebok], 3.3. Code-Based Techniques; [book:clean-code], Conclusion
- **Error guessing and fault models** — design cases aimed at the most plausible faults, using the fault history of earlier projects and the engineer's experience. [book:swebok], 3.5. Usage-Based Techniques
- **Scenarios** — cases built from specified user scenarios. [book:swebok], 5.1. Practical Considerations

Each case records: ID, the requirement or risk it traces to, preconditions, input, steps, expected result, oracle, and level. Requirements are traced forward to the test case that verifies them, and the trace is kept current or it becomes unreliable for impact analysis. [book:swebok], 8. Software Requirements Tools

Write an expected result that independent readers would interpret the same way; the testability rule for criteria is in [dev build mode](../../dev/modes/build.md). "Works correctly" is not an expected result; "the reviewer sees the flagged value, the rule that fired and the source page" is.

## Oracles

An oracle is whatever decides pass or fail: a specification, a model, an assertion, or a person; automating one can be hard and costly. [book:swebok], 1. Software Testing Fundamentals. Name the oracle for every case. When the oracle is a person's label (a golden set), the label process is part of the test design: see [accuracy-measurement](accuracy-measurement.md).

When a case's expected value is computed by code, that code must not be the code under test. (derived: EVOLUTION.md case 10)

## Code coverage

Coverage tells you what you have definitely not tested; it says nothing about the quality of the tests that ran. Prefer branch coverage over line coverage. [book:real-world-software-development], Code Coverage. Use it to find gaps, never as an exit criterion on its own. [book:swebok], 5.2. Test Activities

## Test data

- **Known starting state.** Each test establishes the data it needs, or checks the environment for a known starting position, before it runs. [book:continuous-delivery], Managing Test Data (part 2)
- **Isolated tests.** One test's outcome must not depend on another having run; then one broken test means one problem and tests can run in any order. [book:tdd-by-example], (part 19)
- **No copied production data.** Do not mirror real databases into test environments; seed them with non-sensitive test data, which also makes them easy to reset. [book:building-secure-reliable-systems], Dynamic Program Analysis. Where the client's real documents must be used (a labelled set, a working session), keep them in the environment the contract names and record who may see them.
- **Representative data.** Build the test set to cover the input classes the system will meet in use (for documents: native and scanned, short and long, each layout family), and record the class of each item. A set drawn from one class tests that class only. (derived: EVOLUTION.md case 4)
- **Generated data.** An LLM can generate test data quickly when given explicit rules for it; check the output against those rules before use. [book:software-testing-with-genai], 3.3 Knowing when to use LLMs in testing
- **Size drivers.** When the size of a test set is computed from another figure (fields per document, documents per class), name that figure and its status. If it is unconfirmed, the test set inherits its uncertainty. (derived: EVOLUTION.md case 11)

## Regression

The automated suite runs on every change, which makes it the regression suite. [book:continuous-delivery], Types of Tests (part 1). When the full suite is too costly to run each time, select, minimise or prioritise a subset, and say which. [book:swebok], 2. Test Levels

Run a full regression pass before any build is shown to the client, so the demonstration build is not the first time recently changed paths have run together. (derived: EVOLUTION.md case 9)

For a model-based system, the regression suite includes the scored accuracy run: re-run it on a fixed set after every configuration or prompt change and compare per class with the previous run.

## Flaky tests

A test is nondeterministic when its result can change with no change to the system; flakiness makes people distrust and ignore failures. [book:software-engineering-at-google], Real Implementations (part 1). Flaky tests catch only consistent bugs, and cannot tell a bug from a badly written test. [book:testing-javascript-applications], 11.3.3 Retrying tests. Retrying is a stopgap with a recorded owner and date, not a fix.

For a model-based component, separate expected variation from flakiness: fix the inputs and settings, run twice, and record whether outputs are identical. If identical outputs for identical inputs are promised, that is a test case of its own.

## Defects

Record each unexpected result in a problem register; it is the basis for debugging and fixing, and an anomaly not yet classed as a fault is still recorded in case it proves serious. [book:swebok], 6. Software Testing Tools

| Field | Content |
|---|---|
| ID, date, raised by | |
| Case or session that found it | Link to the case ID or exploratory charter |
| Steps, expected, observed | Reproduction against the unchanged build |
| Severity | Impact, on the contract's scale where it has one ([delivery acceptance](../../delivery/references/acceptance-execution.md)) |
| Priority | Order of fixing; once understood, severity stays fixed while priority may change [book:building-secure-reliable-systems], Define Operating Parameters for Engaging the IR Team |
| Fixed by, verified by | Two different people or agents |
| Regression test | The test that now guards it |
| Cause class | Requirement, design, code, data, configuration, environment |

- Fix a defect with an automated test that detects its return; a defect entered in a backlog without one is a known delivery problem. [book:continuous-delivery], Common Delivery Problems—Their Symptoms and Causes. Reproduction before the fix is in [dev build mode](../../dev/modes/build.md).
- Analyse defects by when they were introduced and why, to see which parts of testing and the process need improving. [book:swebok], 6. Software Testing Tools
- A rejection that asks for behaviour the agreed criteria do not require is a change request, not a defect; route it to `delivery`.
