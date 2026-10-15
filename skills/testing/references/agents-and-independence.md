# Agents and independence

How one person working with agents writes and runs tests without any agent marking its own work. The general rules for independent review are in core ([output contract, independent review](../../core/references/output-contract.md)); agent briefs and success criteria are in `project` ([goal file](../../project/references/run/goal-file.md)). This module applies them to testing.

## Purpose

A test team can be internal, external (for an unbiased view), or both; cost, schedule and how critical the application is guide the choice. [book:swebok], 5.1. Practical Considerations. With agents, the cost of a second independent party is low, so the default is separation. An agent that writes the code, the tests and the report of the run has checked its own understanding against itself. (derived: EVOLUTION.md case 10)

Ownership and judgement are different things. The whole team owns the tests and fixes them when they fail. [book:continuous-delivery], The Automated Acceptance Test Gate (part 2). Deciding that a result passes is done by someone who did not produce it.

## Separate roles

| Role | Gets | Does not get |
|---|---|---|
| Case author | The requirement or criterion, the risk list, the interface | The implementation |
| Implementer | The requirement and the failing tests | Write access to the expected results |
| Runner | The build, the suite, the data | Permission to edit tests or data during the run |
| Judge | The raw run output and the pass conditions | The implementer's explanation of why it should pass |

The coordinator (the person, or an agent with no part in the build) runs the suite and reads its raw output; an agent's summary of its own run is not evidence. [dev build mode](../../dev/modes/build.md) holds the rule that reported success must be checked against the artifact.

A defect is verified fixed by someone other than the person who fixed it. In a plan, do not place defect fixing and fix verification on the same seat. (derived: EVOLUTION.md case 10)

## LLM-generated tests

- **The human directs, the model widens.** Tell the model which features and risks are in focus and use it to suggest risks not yet considered; the person keeps control of the direction of testing. [book:software-testing-with-genai], 5.2 Focused prompts with the use of models
- **Generated cases are proposals.** A model will produce test cases when asked, but that does not make them relevant to the risks that matter; relying on them increases the risk of wasteful or misleading testing. [book:software-testing-with-genai], 5.1 Defining test planning in modern testing; [book:software-testing-with-genai], 3.3 Knowing when to use LLMs in testing
- **Brief from the specification.** Give the case-writing agent the requirement, the risk, the interface and examples of the real input, not the implementation, so its tests encode what was asked rather than what was built. (derived: EVOLUTION.md case 10)

## Checks on agent-written tests

A green suite written by an agent proves little until the suite has been seen to fail for the right reason.

1. **Red first.** Each new test fails without the implementation, for the expected reason (rule in [dev build mode](../../dev/modes/build.md)).
2. **Seeded faults.** Introduce small deliberate changes to the code (mutants); a test that distinguishes the change "kills" it, and the share killed measures how effective the suite is. [book:swebok], 3.5. Usage-Based Techniques; [book:swebok], 5. Test Process. Run seeded faults on a copy and remove them afterwards; inserted faults can be left behind. [book:swebok], 5. Test Process
3. **Cold review of the cases.** A reviewer agent with no prior context gets the requirement and the case list and reports requirements with no case, cases with no requirement, and expected results that restate the implementation. (derived: EVOLUTION.md case 10)
4. **Oracle independence.** An expected value computed by code shares that code's errors if the code is the system under test. Compute expected values by a separate route (a label, a hand calculation, a second implementation). (derived: EVOLUTION.md case 10)

## Agent-run accuracy measurement

- The agent that tunes prompts or configuration does not choose, edit or see the scoring part of the reference set. [accuracy-measurement](accuracy-measurement.md) holds the split.
- Freeze the scoring script and record its version and the configuration hash with every run; a number comes from a scored run, never from hand calculation. (derived: EVOLUTION.md case 1)
- Where identical outputs for identical inputs are promised, the runner repeats a run and compares outputs byte for byte.

## Brief template

```markdown
Role: <case author | runner | judge | reviewer>
Product: <what this agent hands back, and its format>
Inputs: <requirement IDs, risk list, interface, sample data>; NOT given: <implementation | prior verdicts>
Pass conditions: <copied from the strategy, unchanged>
Do not: edit tests or data you did not author; report a result you did not read from raw output.
Report: cases written or run, passed, failed, blocked, each with ID and the evidence path.
```
