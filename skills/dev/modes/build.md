# Build Mode

Build a code change from fixed criteria, existing contracts and accepted design choices. Choose the lightest process that still protects the behavior at risk; keep the implementation, checks and handoff tied to the same contract.

## Scope and size

Classify the work before implementation:

| Shape | Example | Starting process |
|---|---|---|
| Light | focused bug fix or small update | Define binary completion, build, test, verify |
| Medium | new behavior in an existing system | Agree interfaces and criteria, test first, build, verify, review when risk calls for it |
| Heavy | new application, service or API | Define contracts and criteria, prove a walking skeleton, build in phases, verify each phase and review |
| Mechanical | predictable repeated edits | Use the structured edit pattern in modes/sprint.md |
| Exploratory | scope or cause is unknown | Assess or research before changing code |
| Wire/prep | ingestion, conversion, data preparation, wiring or configuration | Coordinator-direct when the work is bounded and unambiguous |

For medium and heavy work, usually keep each reviewable change near 200 lines or fewer. Split coherent pieces when that makes verification and rollback easier; the number is a guide, not a reason to fragment a cohesive change. [book:software-engineering-at-google], Write Small Changes

Use the Pattern declaration in SKILL.md. Work directly for small, clear changes. Use a subagent chain when independent test authorship, implementation, verification or review meaningfully reduces risk; use parallel work only for streams that do not share files or depend on each other's output. Keep every worker's assigned paths explicit and isolate concurrent writers.

For a greenfield project, begin with a walking skeleton: prove the thinnest end-to-end path and toolchain before building out the full design. [book:growing-oo-software-by-tests], First, Test a Walking Skeleton

## Requirements and contracts

Define what “done” means with binary, specific and verifiable conditions. Keep the user's original criteria fixed; if evidence shows they cannot be met, surface the blocker instead of changing them. Before a test is authored, ensure the criterion for that behavior names a testable input and output that independent engineers would interpret consistently. [book:continuous-delivery], Real-Life Situations and Strategies; [book:swebok], Quantifiable Requirements

When a non-obvious choice affects behavior—such as authorization, schema, caching, concurrency or error handling—present two or three options with tradeoffs and a recommendation. Ask for the user's answer to the unresolved fork. If the user has already authorized the implementation and no material choice remains, continue without asking them to approve the build a second time. [book:swebok], Requirements Negotiation

For the behavior in scope, use the pushback loop and ask for a concrete result. If the user remains vague after two attempts, stop and request binary criteria. In iterative work, move one testable behavior at a time; later criteria may be refined as evidence arrives. If the user explicitly accepts shallow tests, proceed while recording which edge cases are unknown or untested and why that is the accepted gap. [book:real-world-software-development], Why Use TDD?; [book:real-world-software-development], Code Coverage

In a greenfield system, create refinable schemas and interface contracts. Verify provider-consumer compatibility with contract tests at service boundaries and record contract changes; a changelog by itself cannot show whether both sides still agree. For an existing codebase, treat the code and its current behavior as the contract; read it rather than re-specifying it. Focus bug fixes on the indicated defect and normally add or update a regression test. [book:software-engineering-at-google], Bug Fixes and Rollbacks Fix or triage a red test promptly—within minutes where practical—so failures remain attributable. [book:building-evolutionary-architectures], Case Study: Validating API Consistency in an Automated Build; [book:continuous-delivery], Implementing Acceptance Tests

Before changing a function definition, inspect callers, importers and shape-dependent test doubles, then read the call sites. Update changed callers and test doubles together; if an out-of-scope stale caller remains, assign the migration to the system owner rather than leaving it unowned. For broad changes, use the semantic code index to enumerate references; for narrow changes, a focused search is sufficient. When a migration touches many internal callers, keep migration ownership with the system team and update the callers in place, rather than scattering migration tasks among users. [book:swebok], Technical Issues; [book:software-engineering-at-google], Codebase Insight; [book:software-engineering-at-google], Policies that Don’t Scale

## Test-first build

Use test-driven development for new behavior and changes to existing behavior. Write a failing test first, then the smallest production change that makes it pass, then refactor while keeping tests green. Each new behavior needs a test for the behavior the team intends to keep. For structural invariants, inspect source structure or its syntax tree; use a simple text search only for a narrow change where it can distinguish the invariant. [book:clean-code], The Three Laws of TDD; [book:growing-oo-software-by-tests], Separate Tests That Measure Progress from Those That Catch Regressions

Skip test-first work for deletion-only changes, predictable mechanical renames, configuration changes, or logic-free visual changes when another suitable check exists. Configuration changes need a smoke test. For frontend UI with no logic, check the build and the rendered appearance; when the UI is an application boundary, add a user-facing test through that frontend. State the reason for any TDD skip. [book:continuous-delivery], Managing Software Configuration; [book:software-engineering-at-google], Browser and Device Testing

Use a test brief that covers every success criterion, relevant error path and both sides of each variant axis. Name the axis in the test description so the next reader can tell which behavior the suite covers. For important boundaries, use the smallest useful input and assert the specific observable. Keep tests small and focused so a failure is easy to diagnose. [book:real-world-software-development], Testing Error Cases; [book:growing-oo-software-by-tests], Small, Focused, Well-Named Tests

Name each test after its contract clause and behavior; when no formal contract exists, name the success criterion and behavior. Use a consistent setup, exercise, and verification structure. For Python suites, parameterize repeated inputs that exercise the same behavior along one axis. [book:growing-oo-software-by-tests], Test Names Describe Features; [book:growing-oo-software-by-tests], Canonical Test Structure; [book:python-for-devops], Parametrization

Tests should be fast, independent, repeatable, self-validating and timely. Classify tests by size: small tests stay in one process, medium tests on one machine, and large tests may use broader infrastructure; prefer the smallest class that proves the contract. Keep a little descriptive repetition in tests when it makes their setup and intent clear. A test should exist for every behavior the team does not want to break. [book:clean-code], F.I.R.S.T.; [book:software-engineering-at-google], Test Size; [book:software-engineering-at-google], Tests and Code Sharing: DAMP, Not DRY; [book:software-engineering-at-google], The Beyoncé Rule

Prefer real implementations or contract-faithful fakes. Use a mock only when its tradeoffs are justified, and do not stub the very behavior under test. A stub cannot prove that the real contract still holds; use the project's supported marker for interfaces that must not be mocked. [book:software-engineering-at-google], Prefer Realism Over Isolation; [book:software-engineering-at-google], The Dangers of Overusing Stubbing

Before implementation, verify that the test suite parses, the new tests fail for the expected reason without the implementation, and the criteria have coverage. Check the smallest input that exposes each failure. Do not let a test that fails to compile or fails for an unrelated reason count as a valid red test. [book:learning-test-driven-development], Red-Green-Refactor: The Building Blocks of TDD

## Implementation

Read adjacent code, relevant callers and real inputs before editing. Keep one concern in a file and separate commands from queries where that makes side effects clear. Leave touched code a little cleaner when the improvement is local and does not broaden the change. [book:clean-code], The Single Responsibility Principle; [book:clean-code], Command Query Separation; [book:clean-code], The Boy Scout Rule

Use real code or the project's well-tested dependency for behavior with meaningful edge cases. Choose a subprocess API that passes executable and arguments separately instead of concatenating a shell command. [book:software-engineering-at-google], Considerations When Importing; [book:python-for-devops], Avoid shell=True

For container builds, scan the produced image as part of the CI pipeline, run the service as a non-root user, keep credentials out of image layers, and fetch secrets from an approved runtime store. Build the image contents as immutable deployment artifacts so a scan describes what runs. Apply these checks only when the change builds or modifies a container. [book:container-security], Scanning in the CI/CD Pipeline; [book:container-security], Containers Run as Root by Default; [book:practical-cloud-security], Cloud Asset Management and Protection; [book:container-security], Immutable Containers

When code launches work through an existing CI or presubmit system, automate the checks it can reliably cover; run manually only what the automated gate does not cover. For mechanically checkable architecture constraints, add a fitness function to the build so the invariant is checked continuously instead of drifting unnoticed. [book:software-engineering-at-google], Automate Where Possible; [book:building-evolutionary-architectures], What Is a Fitness Function?

For deployments whose resilience claim matters, define the steady state and run a controlled failure experiment to see whether it still holds. This is a targeted proof for systems with meaningful failure modes, not a routine requirement for every code change. [book:hands-on-site-reliability-engineering], Chaos engineering process
When launching a new service, use the organization’s reliability launch checklist and automate its verification or the collection of supporting data where practical. [book:hands-on-site-reliability-engineering], 3. Introduction to SRE

When building a command-line tool, treat its command names and flags as a user interface: make them easy to understand and document how to use them. [book:python-for-devops], Creating Command-Line Tools

## Verification and review

Before completion, use the integrated presubmit as the independent run for checks it covers; manually rerun only checks it omits, including tests affected by an interface change. Run the full relevant test suite through a covered gate or the test wrapper. [book:software-engineering-at-google], Automate Where Possible Triage each failure: fix it, quarantine it with a reason and follow-up task, or delete an obsolete test with an explanation. A pre-existing red test still needs a disposition; do not leave it as “not mine.” If the user excludes test hygiene, record the observed failures in the session summary and proceed with that limit disclosed. [book:clean-code], Simple Design Rule 1: Runs All the Tests; [book:continuous-delivery], The Acceptance Test Stage; [book:software-engineering-at-google], Write, Run, React

Run all planned gates before marking work complete. If a measurable gate is used, confirm its instrument can distinguish the target difference. For a release, repeat tests and security and quality scans until the package meets the release plan's standard; record the outputs that establish the gate. Checks or scaffolding that fail on missing, malformed, stale or empty inputs should produce a clear, documented failure. [book:site-reliability-engineering], The Launch Checklist; [book:site-reliability-engineering], Fail Sanely; [book:hands-on-site-reliability-engineering], Test for quality and security

Get each code change reviewed before submission. Add a separate cold adversarial review when a defect could be hard to reverse, fail silently, or appear green for the wrong reason. The cold reviewer should be independent of both code and test authors. Give that reviewer implementation paths only, so the review tests what the code says rather than repeating the author's rationale. For triggered reviews, ask about logic, edge cases, error propagation, wrong-reason success, architecture and code smells; have them execute a cheap reproduction when useful. [book:software-engineering-at-google], Code Review; [book:looks-good-to-me], The modern code review workflow; [book:software-engineering-at-google], Code Correctness

Report findings with file and line, what was found, VERIFIED or HYPOTHESIZED evidence status, severity and a suggested fix. Turn a reproduced failure into a regression test; re-check a hypothesized issue before changing code. [book:site-reliability-engineering], Creating a Test and Build Environment

Treat CRITICAL code-review findings as blockers. Present WARNING findings for an owner decision and note ADVISORY findings. Escalate three or more CRITICAL findings, except when all are verified, share one cause and have a mechanical fix that can be safely applied and disclosed; never use the exception for integrity failures. QUALITY findings are advisory and can be fixed, deferred or accepted by the user. Close every review comment with a fix or an explicit disposition before committing. [book:looks-good-to-me], Blocking issues; [book:looks-good-to-me], Nonblocking issues; [book:software-engineering-at-google], Code Review Flow

When test health or a planned gate is skipped, state the reason. For light work, report each criterion's evidence and the pass/fail targets that were run, not only the totals. Record decisions as they are made in the change description or nearby code comment; at completion, follow core's durable-record protocol for the outcome and any reusable failure pattern. [book:software-engineering-at-google], Riding the TAP Train; [book:software-engineering-at-google], Write Good Change Descriptions

## Handoff

Describe the change type, what changed and why in the review description. Keep build, deployment, testing and release assets under version control. For service work, carry the reliability target into the handoff as an SLI and SLO, with the measurement and valid conditions made explicit. [book:software-engineering-at-google], Write Good Change Descriptions; [book:continuous-delivery], What Are the Benefits?; [book:site-reliability-engineering], Service Level Objectives

## Script wrappers

Use the shipped wrappers for repeatable checks:

| Script | Use |
|---|---|
| scripts/run-tests.sh [path] | Discover or select the test runner and save a concise result |
| scripts/run-quality.sh [path] | Run available lint, security and type checks |
| scripts/run-command.sh -- <command> | Capture verbose command output in a log |
| scripts/analyze.py --mode summary [path] | Summarize a codebase before deeper assessment |

Read the log after a failed wrapped command rather than repeating an expensive run to recover its details. Do not treat a wrapper reporting success as proof of the artifact's behavior; inspect the result itself.
