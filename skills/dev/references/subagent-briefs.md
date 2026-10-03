# Subagent Briefs

The coordinator gives a worker only the brief for its role plus task-specific context. Every brief names the target, permitted paths, expected result and acceptance evidence. A role may decline a task; the coordinator reroutes it and records the result instead of taking over a rejected unit.

## Shared isolation rules

A worker with write access touches only its assigned worktree and never changes shared version-control state: no staging, commits, branch operations, resets, stashes or checkouts. Give concurrent writers separate worktrees. The coordinator reviews their diffs and owns staging and commits by explicit path.

## Test author

**When:** after criteria and contracts are defined, before implementation.

Ask a separate worker to write contract tests from the current criteria, not from the implementation. For iterative work, write one behavior test at a time as its criterion becomes testable. Tests should parse, fail for the expected reason without the implementation, cover the defined criteria and relevant edge cases, and avoid changing implementation files. Run them through scripts/run-tests.sh. The red-green-refactor cycle writes a failing test, runs the suite to verify it, implements the minimum, then refactors while keeping tests green. [book:learning-test-driven-development], Red-Green-Refactor: The Building Blocks of TDD

For each test:
- Cover both sides of a behavior axis and name the axis in the test description. [book:real-world-software-development], Testing Error Cases
- Keep tests small and focused so failure diagnostics are clear. Use the smallest useful triggering input, assert the specific observable, and exercise stated boundaries when they are part of the contract. [book:growing-oo-software-by-tests], Small, Focused, Well-Named Tests
- Use a stable test shape: setup, exercise, verification. [book:growing-oo-software-by-tests], Canonical Test Structure
- Name it for the contract clause and behavior, or for the success criterion when no contract exists. [book:learning-test-driven-development], Improving Our Tests
- For Python tests, parameterize repeated values that test the same behavior.
- Keep tests fast, independent, repeatable, self-validating and timely. [book:clean-code], F.I.R.S.T. Classify them small, medium or large, and prefer the smallest class that proves the behavior. [book:software-engineering-at-google], Test Size

Before implementation starts, independently check that tests parse, fail for the expected reason, and cover the currently defined criteria. Running the suite confirms the intended red; do not count a compile error or unrelated failure as that evidence. [book:learning-test-driven-development], Red-Green-Refactor: The Building Blocks of TDD

**Why this split matters:** A crash-recovery build once tested only the registry member that could not exhibit the failure. The suite passed, yet the important external effect had never been exercised. Naming the variant axis and testing both sides makes that blind spot visible.

## Implementation worker

**When:** after tests have been verified and, for medium or heavy work, independently validated against the agreed criteria.

Provide the contracts, tests, phase deliverables, prior handoff and relevant project patterns. Require the worker to pass the tests, preserve criteria, follow existing patterns, avoid mocking the behavior under test, and stop if the tests cannot be satisfied. On a failed command, read its log rather than rerunning it only to recover output. Run tests with scripts/run-tests.sh and verbose commands with scripts/run-command.sh. The implementation follows a failing test and suite run; keep the suite green while refactoring. [book:real-world-software-development], The TDD Cycle; [book:learning-test-driven-development], Keeping Code DRY

Require a closing Key Decisions section with three to five load-bearing choices. For each, state the chosen approach, a plausible naive alternative and why that alternative would be worse. Compare relevant risks, costs and benefits; the 3–5-item report shape is dev procedure. [book:swebok], Tradeoff Analysis

After the worker returns, independently check the integrated presubmit evidence and rerun only checks it does not cover. Report the most load-bearing implementation decision and why it matters; make sure an interface change has corresponding test evidence from the gate or a targeted rerun. [book:software-engineering-at-google], Automate Where Possible

## Verification worker

Ask the verifier to:
1. Run tests and quality checks; include the quality JSON summary.
2. Compare the implementation with the contract and report undocumented deviations.
3. Confirm mocks do not replace the behavior being tested.
4. Inspect algorithmic cost, resource lifetimes, concurrency and error propagation.
5. Review generated or agent-written code for dead paths, unsupported APIs, unnecessary wrappers and comments that restate the obvious.
6. Show evidence for every criterion.
7. Parse machine-readable YAML, JSON or TOML artifacts with their actual parser.

Use CI evidence for checks it covers; rerun only missing checks and changed interfaces. For a release, repeat tests and quality/security scans until they meet the release plan's standard. [book:hands-on-site-reliability-engineering], Test for quality and security; [book:software-engineering-at-google], Automate Where Possible. Report PASS, FAIL or PARTIAL with the evidence and command outputs. Mock-only proof of a production contract fails verification because a stub cannot prove the real contract. [book:software-engineering-at-google], The Dangers of Overusing Stubbing. Changed success criteria, unproved success, lint errors and high or critical security findings also fail verification. A justified fake or mock around a dependency is acceptable when it does not replace the contract under test.

## Cold code review

**When:** after verification, when an error could be hard to reverse, fail silently or appear green for the wrong reason. A review of every code change still happens before submission; this additional adversarial pass can be skipped only for work that is cheap to undo and loud when wrong. State the reason for a skip.

Use a reviewer independent of the code author and test author. Give the cold reviewer implementation paths only, with no criteria, design rationale or prior conclusion. Ask for a cold reading of the actual logic, null and failure paths, race conditions, hidden assumptions, architecture and smells. Review whether the code is properly tested, designed, correct and efficient. [book:software-engineering-at-google], Code Correctness Ask whether any passing result could be true for the wrong reason. When a finding has a cheap executable reproduction, run it.

Each finding records file and line, result, VERIFIED or HYPOTHESIZED status, severity and a one-sentence fix. Re-check HYPOTHESIZED findings before acting. Use a VERIFIED reproduction as a regression test. [book:site-reliability-engineering], Creating a Test and Build Environment Fix CRITICAL findings, present WARNINGs for an owner decision and note ADVISORY findings. Escalate three or more CRITICALs unless every finding is verified, has one cause and admits a mechanical fix that can be disclosed; the exception never applies to integrity findings.

## Mechanical edit pattern

For predictable multi-file edits, use modes/sprint.md.

## Reusable additions for engineering work

Keep repeatable test gates hermetic: self-contained inputs and isolated dependencies make their results more stable and attributable. [book:software-engineering-at-google], Hermetic Testing

Treat each review comment as a TODO. Disagreement need not be accepted, but discuss the alternatives and record a clear response before closing the comment. [book:software-engineering-at-google], Be Polite and Professional
