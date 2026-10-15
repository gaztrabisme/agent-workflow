---
name: testing
description: "The tester's job on a software delivery: test strategy and plan, test levels (unit, integration, end-to-end, acceptance), test cases and data, regression, defects, acceptance scripts run with the client, accuracy measurement for an AI or extraction system (golden set, injected errors with a known answer, per-class rates with sample sizes), test effort, and agents testing without marking their own work. USE WHEN a delivery needs a test strategy, cases or data, a regression or defect process, acceptance scripts and evidence, an accuracy measurement design, test rows for a WBS, or a check that agent-written tests are independent. Not `dev` (code and per-change tests), `delivery` (signed acceptance records), `applied-ml-problem-solver` (model choice and experiments), `data-engineering` (pipeline checks). Keywords: testing, test strategy, test plan, QA, QC, regression, test cases, test data, defect, severity, UAT, acceptance test, golden set, accuracy, error injection, fault seeding, sample size, test effort."
---

# Testing

Produces the test strategy and the test artifacts that follow from it (test cases, test data, regression and defect records, acceptance scripts and evidence, an accuracy measurement design, and the test rows of an estimate) for the person doing the tester's job on a delivery, often one person working with agents. The strategy is written for the project lead and the client's acceptance authority; the cases and scripts are written for whoever runs them.

> Inherits the `core` kernel — see `../core/SKILL.md`. Follow shared gates through their canonical references; do not copy their definitions.

## When it fires — and when a sibling owns it

- **This skill:** what to test, at which level, with which data, how defects are handled, how acceptance is run and evidenced, how accuracy is measured and reported, what testing costs, and who may mark a test as passed.
- **`dev` instead:** writing a change test-first and running its suite. `dev` owns the per-change tests ([build mode](../dev/modes/build.md)); this skill owns the strategy those tests sit inside and the levels above them.
- **`delivery` instead:** recording signed acceptance, waivers and change requests ([acceptance execution](../delivery/references/acceptance-execution.md)). This skill prepares the scripts and the evidence that record points to.
- **`applied-ml-problem-solver` instead:** choosing a model and running experiments, including sample-size formulas ([eval harness](../applied-ml-problem-solver/references/templates/eval-harness.md)). This skill turns the chosen system's accuracy into test cases, reported rates and acceptance evidence.
- **`data-engineering` instead:** quality checks inside the pipeline and tests of transforms, contracts and replay ([estimating and testing](../data-engineering/references/estimating-and-testing.md)).
- **`project` instead:** the WBS, schedule and price. This skill supplies the test rows and their basis.

> **Disambiguation:** decide on artifact and audience. Code with its tests is `dev`; a signed acceptance record is `delivery`; a model choice is `applied-ml-problem-solver`; a test strategy, case set, measurement design or test estimate is this skill.

## Principles

1. **The strategy starts from risks.** Each test level and activity exists because it reduces a named risk; a test nobody can tie to a risk is a candidate to drop. [book:continuous-delivery], Types of Tests (part 1); [book:software-testing-with-genai], 5.1 Defining test planning in modern testing
2. **Every test has an oracle and a stated pass condition before it runs.** Who or what decides pass or fail is written down with the case. [book:swebok], 1. Software Testing Fundamentals
3. **A passing suite shows the presence of tested behavior, not the absence of defects.** Publish what was not tested beside what passed. [book:swebok], 1. Software Testing Fundamentals
4. **Rates are reported per class with their sample size, never pooled across classes.** [book:designing-ml-systems-huyen], Slice-based evaluation (part 1)
5. **The producer does not mark its own work.** The agent or person who wrote the code does not write the oracle that judges it, and does not declare it passed. (derived: EVOLUTION.md case 10)
6. **Every piece of acceptance evidence has a task that produces it.** When a task is cut, every promise that depends on it is cut or re-homed in the same change. (derived: EVOLUTION.md case 7)

## The flow

| Step | Goal | Module |
|---|---|---|
| Strategy and levels | Name the risks, choose levels and activities, set entry and exit criteria | [strategy-and-levels](references/strategy-and-levels.md) |
| Cases, data and defects | Design cases and test data; run regression; triage and close defects | [cases-and-data](references/cases-and-data.md) |
| Accuracy measurement | Golden set, match rule, per-class rates, injected errors, published limits | [accuracy-measurement](references/accuracy-measurement.md) |
| Acceptance testing | Scripts agreed with the client, dry run and binding run, evidence pack | [acceptance-testing](references/acceptance-testing.md) |
| Agents and independence | Split authoring, running and judging between agents; check agent-written tests | [agents-and-independence](references/agents-and-independence.md) |
| Test effort | Size test work from its products and drivers; check the plan carries it | [estimating-test-effort](references/estimating-test-effort.md) |

Scale to the request. A question about one defect needs the defect section only; a new delivery starts with the strategy and its one-page template.

## Gates (declared, inherited from core)

- **Grounding gate** — substrate: the requirements or acceptance criteria, the architecture, the plan's test rows, and the system's real inputs. See `../core/references/grounding-gate.md`.
- **Output Contract** — primary artifacts: the strategy page, the case list with oracles, the defect register, the acceptance scripts and evidence index, and for a model-based system the measurement design. A result is reported from the run's own output, not from a summary. See `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- **Independent review** — for client-facing acceptance material, use core's independent review. See `../core/references/output-contract.md`.
- **Pushback and teach** — see `../core/references/pushback-and-teach.md`.

## Anti-patterns (hard no-list)

- One accuracy figure averaged across document types, input modes or error classes.
- A detection rate with no stated denominator, or a rate quoted without the number of documents behind it.
- Tuning a system on the same labelled set that later decides acceptance.
- A threshold paired criterion (for example, few items sent to review) quoted without its partner (errors still caught).
- Acceptance evidence promised in a plan or deck whose producing task was removed.
- An agent writing both the code and the tests that judge it, then reporting its own pass.
- Test effort carried as a percentage of development with no stated source for the ratio.

## Composition

- **Inherits:** `core`.
- **Consumes:** requirements and acceptance criteria (`solution-architect`, `product-management`), the model and its evaluation decision (`applied-ml-problem-solver`), the data design (`data-engineering`), the plan (`project`).
- **Hands off to:** `dev` for per-change tests and fixes; `delivery` for recording acceptance; `project` for the test rows of the WBS and for agent briefs ([goal file](../project/references/run/goal-file.md)).

## References

- [references/strategy-and-levels.md](references/strategy-and-levels.md) — risk-based strategy, test levels, non-functional and security testing, exit criteria, one-page template.
- [references/cases-and-data.md](references/cases-and-data.md) — case design, oracles, traceability, test data, regression, flaky tests, defects.
- [references/accuracy-measurement.md](references/accuracy-measurement.md) — golden sets, match rules, per-class rates, sample size, injected errors, tuning separation, published limits.
- [references/acceptance-testing.md](references/acceptance-testing.md) — acceptance criteria as test cases, scripts, entry conditions, dry and binding runs, evidence pack.
- [references/agents-and-independence.md](references/agents-and-independence.md) — who writes, runs and judges tests when agents do the work.
- [references/estimating-test-effort.md](references/estimating-test-effort.md) — test products, drivers, basis per row, plan checks.
- [EVOLUTION.md](EVOLUTION.md) — birth record, the cases behind derived rules, and the first test.
