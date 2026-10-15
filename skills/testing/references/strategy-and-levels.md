# Test strategy and levels

How to decide what gets tested, at which level, and when testing is finished. The output is a one-page strategy that the project lead and the client's acceptance authority can both read.

## Risks

Designing a test strategy is identifying and ranking the project's risks and deciding what action reduces each. [book:continuous-delivery], Types of Tests (part 1). Risk-based testing uses product risks to prioritise and focus the strategy. [book:swebok], 5.1. Practical Considerations. Write each risk as something specific and checkable; the risks decide which testing is done, whether the plan is formal or a single page. [book:software-testing-with-genai], 5.1 Defining test planning in modern testing

For each risk record:

| Field | Content |
|---|---|
| Risk | What could go wrong, in the user's or client's terms |
| Where it would show | The component, interface or output where a failure is visible |
| Level | The lowest test level that can detect it (below) |
| Oracle | What decides pass or fail: a specification, a labelled answer, a computed check, a person |
| Evidence | The artifact that shows it was tested: a log, a scorecard, a recorded run |
| Not covered | What this test cannot see (see "Published limits" below) |

A larger system needs a strategy that names its risks and the larger tests that address them; unit tests alone do not cover them. [book:software-engineering-at-google], TL;DRs

## Test levels

Levels are distinguished by their target (a unit, a group of units, the whole system) and by their objective. The three stages unit, integration and system imply no process model, and none is more important than the others. [book:swebok], 2. Test Levels

| Level | Question it answers | Usual owner |
|---|---|---|
| Unit | Do our objects do the right thing? | Developer, per change (`dev` build mode) |
| Integration | Does our code work against code we cannot change? | Developer and tester |
| System / end-to-end | Does the whole path work, from input to output? | Tester |
| Acceptance | Does the whole system do what the client agreed? | Client and tester together |

The first three questions are from [book:growing-oo-software-by-tests], Levels of Testing. Per-change tests, their sizes and the preference for real implementations over mocks are in [dev build mode](../../dev/modes/build.md); do not restate them in the strategy, point to them.

For a system that calls an outside service (an extraction service, a model endpoint), integration tests check the contract with that service: field names, types, positions, empty results and errors. A component the client has declared out of scope is still a dependency whose output the strategy must check at the boundary, even if it is not tuned or benchmarked. (derived: EVOLUTION.md case 2)

## Other test activities

- **Regression** — selecting, minimising or prioritising a subset of existing tests to re-run after a change; it applies at every level. [book:swebok], 2. Test Levels. Detail in [cases-and-data](cases-and-data.md).
- **Non-functional** — capacity, security and other non-functional requirements are set early and enforced by tests, so a breach is caught while it is cheap. [book:continuous-delivery], Types of Tests (part 1)
- **Security** — test across the life cycle (definition, design, development, deployment), not only by penetration testing at the end, which on its own finds few defects and depends on the tester's skill. [book:owasp-wstg-v4.2], 0 - The Web Security Testing Framework (part 1)
- **Exploratory** — charters, each exploring one risk from one angle, find what scripted cases miss. [book:software-testing-with-genai], 8.1 Organizing exploratory testing with LLMs
- **Accuracy measurement** — for a model-based system, see [accuracy-measurement](accuracy-measurement.md).

## Environments

Test in an environment whose configuration matches production, so configuration problems surface early; it need not be a full-size copy. [book:continuous-delivery], Managing Your Environments (part 1). Environment design belongs to the `infrastructure` skill; the strategy names which environment each level runs in.

## Exit criteria

Decide in advance how much testing is enough for each stage. Coverage, fault density and reliability estimates support the decision but do not settle it; weigh the cost and risk of remaining failures against the cost of more testing. [book:swebok], 5.2. Test Activities. Spend on testing in proportion to how critical the application is. [book:swebok], 5.2. Test Activities

Write exit criteria as counts that can be checked: cases run, passed, failed, blocked; open defects by severity. [book:swebok], 5.2. Test Activities. An aggregate accuracy percentage is reported beside the exit criteria, not used as one, until the measurement behind it exists and has been run. (derived: EVOLUTION.md case 5)

## Published limits

State what the tests cannot detect, in the strategy and in any client-facing measurement page. Testing shows the presence of defects, never their absence. [book:swebok], 1. Software Testing Fundamentals. For a system whose checks are consistency rules, name the class of error that passes every rule (for example, a wrong value that leaves the document internally consistent). (derived: EVOLUTION.md case 3)

A completeness check belongs in the strategy whenever checks only test relations between values present: a missing value breaks no relation, so compare expected against populated fields. (derived: EVOLUTION.md case 2)

## One-page strategy template

```markdown
# Test strategy — <system>, <phase>
Scope tested: <what>. Out of scope: <what, and who owns it>.
## Risks and tests
| Risk | Level | Oracle | Evidence | Not covered |
## Levels and owners
| Level | Runs in | Owner | Automated? |
## Non-functional and security
| Requirement (throughput, latency, cost per item, access) | Threshold, or "reported, no threshold" | Test | Evidence |
## Measurement (model-based systems only)
Golden set, match rule, classes, rates reported, injected errors, tuning set vs scoring set.
## Defects
Severity scale (from the contract if it has one), triage cadence, who verifies a fix.
## Entry and exit criteria
Per stage, as checkable counts.
## Acceptance
Scripts, dry run, binding run, evidence pack items and the task that produces each.
## Limits
## Independence
Who writes cases, who runs them, who judges results.
```
