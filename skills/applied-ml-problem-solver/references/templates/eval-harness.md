# Eval Harness — template

Fill this in before adapting, training, or optimizing the system being evaluated. State why any section is deliberately omitted. Define a clear evaluation guideline before scoring outputs; an ambiguous rubric creates ambiguous scores. [book:ai-engineering-huyen], Finetuning and RAG; Step 2. Create an Evaluation Guideline

## Decision served

- What choice will a result change?
- Is this an absolute score or a paired comparison? [book:ai-engineering-huyen], Ranking Models with Comparative Evaluation
- Who consumes the output, and what unit do they receive?

## Frame and grounding

- **Reduced problem:** …
- **Rejected framing:** … — why it fails.
- **Structured question:** population or input, mechanism, comparison, outcome. Record a rejected reframe and its reason. [book:designing-ml-systems-huyen], Multiple ways to frame a problem
- **Grounding search:** databases and sources searched, exact terms, date, useful findings, and unresolved questions.

When searching research literature, iterate field vocabulary and controlled subject terms. Use OR to broaden and AND to narrow, and follow relevant citations to earlier and later studies. [book:research-methods-psychology], Finding and Reading the Research

## Fit-Check

Fill all six rows from `SKILL.md` before choosing the evaluation. Any mismatch is a redesign.

| Constraint | Answer | Verdict |
|---|---|---|
| Signal volume | | |
| Signal latency | | |
| Signal breadth | | |
| Budget | | |
| Failure mode | | |
| Instrument stability | | |

## Baselines

| Field | Value |
|---|---|
| Published system or benchmark | |
| Runnable implementation | |
| Reported score | |
| Protocol and population behind the score | |
| Trivial baseline | |
| Headroom: trivial to best | |

Consider several relevant baseline types: random, simple heuristic, human performance, current product, and the best published system. Choose those that fit the decision. Evaluation scores have little meaning without a baseline. [book:designing-ml-systems-huyen], Baselines

If a public number is unavailable, record `UNVERIFIED-PENDING-LOOKUP`, the search location, date, exact terms, and the level searched. Run the trivial baseline before the new method.

## Evaluation set

| Field | Value |
|---|---|
| Size and unit | |
| Construction and labels | |
| Contamination control and measured check | |
| Strata and expected-to-fail cases | |
| Refresh policy | |
| Pre-gate review | |

Detect benchmark contamination and decontaminate where possible. Name the domain-specific leakage and how the split prevents it. [book:ai-engineering-huyen], Data contamination with public benchmarks

Use an out-of-scope or unanswerable stratum when the system should decline or fail safely. Report results by relevant archetype and stratum, not only as one aggregate. [book:ai-engineering-huyen], Annotate evaluation data

For an AI study or benchmark used as a baseline, record why its population, intended use, comparison, and outcome measure transfer to the present decision. See the ten-question AI study appraisal in `ml-heuristics.md`.

## Match unit and scoring guideline

Define a match as the unit actually returned to the consumer. State adjacency, partial-credit, and duplicate rules.

Before scoring any outputs, write a rubric with clear examples of good, bad, and borderline cases. Record how disagreements are handled.

For an experiment that depends on a human-facing manipulation or prompt, define a separate manipulation check to confirm people received or perceived the intended change before interpreting a null result. [book:research-methods-psychology], Interrogating Null Effects: What if the Independent Variable Does Not Make a Difference?

Before trusting small score changes, test evaluation reliability: repeat the evaluation to measure test-retest stability and use multiple raters where human judgment is involved. [book:research-methods-psychology], Reliability of Measurement: Are the Scores Consistent?

## Metrics and usefulness

| Role | Metric | Purpose |
|---|---|---|
| Decisive | | Gate for ship / no-ship |
| Proxy | | Cheap ranking signal |
| Diagnostic | | Explain how and where results changed |
| Business outcome | | When does the measured change make the system useful? |

Measure proxy-to-decisive correlation and recheck it after the system changes shape. [book:ai-engineering-huyen], Select evaluation methods

Map evaluation metrics to business outcomes and set the usefulness threshold before launch; a real offline score gain is not automatically an operational win. [book:ai-engineering-huyen], Tie evaluation metrics to business metrics

For open-ended generation, evaluate realistic prompts with human pairwise preferences when automated metrics cannot capture usefulness, tone, or clarity. [book:designing-ai-interfaces], Evals

For threshold decisions, report sensitivity and specificity across candidate thresholds or use likelihood ratios; a single accuracy value hides how a test changes the odds at the chosen cutoff. [book:how-to-read-a-paper], Likelihood ratios

## Sample size and resolution

| Field | Value |
|---|---|
| Sample size and unit | |
| Smallest worthwhile difference | |
| Statistical test or bootstrap method | |
| Confidence interval / uncertainty | |
| Multiplicity, if several tests are gated | |

Use bootstraps over evaluation examples or an appropriate significance test on score differences to assess whether the set can support the decision. Do not apply the paired continuous `σ_diff`/MDE formula mechanically to ranking metrics or metrics without a per-example decomposition. If the evaluation cannot resolve the smallest worthwhile difference, improve it before running the gate. [book:ai-engineering-huyen], Annotate evaluation data

## Substrate probes and run protocol

Record defects found by probing the system that invalidate a naive evaluation—for example, an ignored result-count parameter, mismatched preprocessing, or response truncation.

- One variable per run.
- Pre-register the gate and smallest worthwhile change.
- Log configuration, data and rubric versions, result, and verdict. [book:ai-engineering-huyen], Iterate
- Write negative results and direction-changing conclusions in the experiment record.
- Report any post-result review beside, never instead of, the pre-registered result.

