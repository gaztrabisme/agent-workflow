---
name: applied-ml-problem-solver
description: "Produces an ML problem-framing and experiment decision record for practitioners choosing and evaluating an approach. USE WHEN an ML data, model, evaluation, retrieval, training, or inference decision is unresolved. `ai-discovery-workshop` frames the client use case; this skill tests its ML framing. `dev` implements code; `solution-architect` owns the wider client solution. Keywords: ML, CV, NLP, model selection, labels, metrics, evaluation, retrieval, training, inference, latency, baseline, experiment."
license: MIT
---

# Applied ML Problem Solver

This skill helps an ML practitioner decide whether a data or ML approach can solve the stated problem and how to tell whether it worked. Its primary artifact is an ML problem-framing and experiment decision record: the reduced problem, chosen mechanism, constraints, baseline, evaluation plan, and evidence-based verdict. It also guides retrieval and inference-serving decisions; implementation work moves to the engineering handoff.

> Inherits the `core` kernel — see `../core/SKILL.md`. Use its integrity contract and gates; keep their shared mechanics there.

## When it fires — and when a sibling owns it

- **This skill:** choose and evaluate an ML, CV, NLP, retrieval, training, or inference approach from its data, signal, evaluation, and runtime constraints.
- **`ai-discovery-workshop` first:** validate the client use case and intended outcome; then reduce the accepted use case to a testable ML problem here.
- **`dev` next:** build or change the code after the problem and evaluation decision are framed.
- **`solution-architect`:** own the wider client platform, integrations, non-functional requirements, and client-facing trade-offs.
- **`omlx`:** operate a local MLX endpoint.

Use this skill for ML decision questions and hand code construction to `dev`. When both the decision and implementation are needed, frame the problem and pre-register its gate here first; use the deliverable of the turn to route the next work, and split a turn that would produce both a decision and code.

## Principles / anchoring rules

- Reframe before selecting a model: changing the problem frame can make it substantially easier or harder. A detection request may reduce to classification after a solved detector crops the region. [book:designing-ml-systems-huyen], Multiple ways to frame a problem
- A simulated, synthetic, or replay result is a distinct evidence class. Describe what it represents and scrutinize which claims transfer to real use; do not present it as a result from the target population. [book:critical-thinking-about-research], Research Variables and Strategies
- A negative trial of a complex intervention does not prove every version will fail. Inspect delivery and implementation—for example, whether exercises were too difficult or home practice did not happen—and use the findings to refine the intervention. [book:how-to-read-a-paper], Papers that report trials of complex interventions
- Change one variable per experiment so the outcome is easier to attribute and debug. [book:effective-conversational-ai], 1.3.2 The continuous improvement cycle
- For a small, direct utility on the ML path, prefer standard-library primitives over a wrapper or framework; leave code construction to `dev`.
- A proxy is useful only after its relationship to the outcome that matters is checked; evaluate surrogates against that outcome before relying on them. [book:how-to-read-a-paper], Surrogate endpoints
- Give every reported metric or constant an operational definition: name the procedure and instrument that produced it. [book:research-methods-psychology], Variables
- Fit a non-RL baseline before choosing reinforcement learning for a retrieval or decision problem.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Frame | Reduce the request to a testable problem and state the intended outcome | Problem statement, structured question, rejected framings |
| Ground and fit-check | Read the relevant evidence and compare the mechanism with the problem's constraints | Grounding note and six-row Fit-Check |
| Instrument | Define the evaluation and its decision before running the system | Filled evaluation harness |
| Baseline | Name a comparable published system, benchmark, and trivial baseline | Baseline and headroom note |
| Experiment | Change one variable at a time against a pre-registered gate | Append-only experiment log |
| Decide and serve | Record ship/no-ship evidence and test the inference system under its real constraints | Decision record and production checklist |

## Frame before naming a method

Write the structured question before work begins: who or what is the population, what mechanism or intervention is considered, what is the comparison, and which outcome matters. For ML work, name the input and output unit and the person or system that consumes the result. Appraise a proposed study or experiment by asking what is being changed, compared with what, and how the outcome is measured. [book:how-to-read-a-paper], Before you start: formulate the problem; Was the design of the study sensible?

Record the reduced problem and at least one rejected framing with a reason. Then state the hypothesis or expected outcome publicly before collecting data; this makes a later result distinguishable from a prediction invented after the fact. [book:research-methods-psychology], Research Transparency and Credibility

## Ground and probe assumptions

Before choosing a technique, search the relevant knowledge base and record one cite-or-null line; if the domain is not covered, say so. Then survey the literature systematically across appropriate databases and follow citations to earlier and later work. Record search terms and what the search supports; one quick query is not evidence that no benchmark or prior method exists. [book:how-to-read-a-paper], What are you looking for?

For an expensive or irreversible choice, declare the approach and run the cheapest probe that tests the highest-risk assumption. A preliminary study can also verify that the setup and intended manipulation actually work before the main run; use a separate pilot group when the task requires it. [book:critical-thinking-about-research], Manipulation and Measurement Validity; Interrogating Causal Claims with the Four Validities

## Fit-check the proposed mechanism

Run Fit-Check before naming an algorithm, framework, architecture, metric, evaluation set, or scoring protocol. Write one answer for each of these six dimensions; compare them with the mechanism's stated requirements and redesign on any mismatch. Fill the easy rows too, because they are often what exposes a hidden constraint.

| Dimension | Ask |
|---|---|
| Signal volume | How many labeled or scored examples exist for each decision the method makes? |
| Signal latency | How long after the action does the outcome arrive? |
| Signal breadth | Can every sample the method needs actually be scored? |
| Budget | What memory, time, and money are available? |
| Failure mode | Would a mismatch fail loudly or silently? |
| Instrument stability | Does the system expose and honor the control or parameter the measurement assumes? |

A delayed outcome and too few scores can make a group-based learner silently train on zero advantages rather than crash. A retrieval eval also fails the fit-check if it lacks known relevant items for its recall claim or the system ignores the requested result count. Fix the method or the measurement substrate before spending. Extend the Fit-Check when a real mismatch fits none of its rows, and retire dimensions that stop recurring.

## Can the gate resolve the change?

A null result can reflect an insensitive measure: a thermometer marked only in whole degrees will miss a tenth-degree change. Check that the instrument can resolve the smallest difference the decision requires; an unresolved gap is inconclusive, not a confirmed win or null. [book:research-methods-psychology], Interrogating Null Effects

For a paired, continuous per-item comparison at 80% power and two-sided α = .05, a planning approximation is:

`MDE ≈ 2.8 × σ_diff / √n`

This paired form and its 2.8 constant are skill-specific; the source supports power-based sample sizing generally. [book:statistics-by-simulation], 3.4. Testing Hypotheses and Assessing their Support

When n is under about 30, use an exact noncentral-t calculation; the normal approximation is optimistic. For multiple gated metrics, divide α by the number of tests and recompute the critical value—do not multiply the constant by the number of tests. [book:statistics-by-simulation], 5.5. Multiple Testing and the Inflation of False Positives

For orientation, paired-unit MDE is approximately .56σ at n=25, .40σ at n=50, .28σ at n=100, .18σ at n=240, and .089σ at n=1,000. These are planning references, not a substitute for measuring noise. Measure σ_diff on the first run; if it is not available, label sizing provisional. Before sizing from a published study, inspect the worthwhile effect, outcome mean and standard deviation, and reproduce the calculation where needed. [book:how-to-read-a-paper], Were preliminary statistical questions addressed?

Do not apply the continuous paired formula unchanged to other metrics:

| Statistic | Appropriate check |
|---|---|
| Paired binary outcomes | Use a paired binary test such as McNemar; the disagreement rate controls precision. |
| AP/mAP or other whole-set ranking metrics | Bootstrap over images or queries and inspect the interval. |
| A metric with no per-unit decomposition | Use a bootstrap if resampling is possible; otherwise say the delta cannot be sized with that method. |

Use an effect-size check to decide whether the expected change is detectable; if it is below the MDE, increase the sample, refine the grid, or improve pairing before the gate. An underpowered study cannot answer the question. Replicate a surprising finding independently before treating it as established. [book:statistics-by-simulation], 3.4. Testing Hypotheses and Assessing their Support; [book:research-methods-psychology], Research Transparency and Credibility

When comparing two conditions, include a comparison condition rather than assuming a full no-treatment group is always required. Calibrate a null control to what a correct system should do, not to an intuitive score. [book:research-methods-psychology], Why Experiments Support Causal Claims; [book:designing-ml-systems-huyen], Baselines

## Name the baseline and headroom

Before building a scheduler, ranker, scorer, retriever, or other component for a decision already made by published systems, identify what it must beat. Name the published system and whether a runnable implementation exists, its public score and evaluation protocol, and the span from a trivial baseline to the best result. Evaluation scores mean little without their baseline. [book:designing-ml-systems-huyen], Baselines

If a public benchmark number is not available, record `UNVERIFIED-PENDING-LOOKUP` with the search location, date, exact terms, and task level searched. Run and publish the trivial baseline before the real method so the project's headroom is measured. A negative search claim means “not found with these terms,” never “does not exist.” Iterate search terms until they match the field's own vocabulary before concluding that no result was found. [book:research-methods-psychology], Finding and Reading the Research

## Evidence and experiment decisions

- For every run, pre-register the threshold against a recorded baseline; log the configuration, result, and verdict. [book:effective-conversational-ai], 1.3.2 The continuous improvement cycle
- Before accepting a result, check its statistical or interval resolution. If a surprising gain appears, check for bugs, coarse grids, and artifacts, then replicate it independently. [book:how-to-read-a-paper], Probability and confidence; [book:research-methods-psychology], Research Transparency and Credibility
- When load behavior matters, an isolated component benchmark is only diagnostic: load behavior emerges from the full system, so measure with production-like traffic and topology. [book:software-engineering-at-google], Performance, Load, and Stress testing

## Gates (declared, inherited from core)

- **Grounding gate** — ground model, evaluation, retrieval, and serving choices in the relevant evidence; see [`../core/references/grounding-gate.md`](../core/references/grounding-gate.md).
- **Output Contract** — the problem framing, filled evaluation harness, per-run log, and decision record are the ML artifacts; see [`../core/references/wiki-protocol.md`](../core/references/wiki-protocol.md).
- **Pushback and teach** — explain the mechanism behind an ML loss, metric, optimizer, or architecture; see [`../core/references/pushback-and-teach.md`](../core/references/pushback-and-teach.md).
- When introducing ML math, explain what the loss, activation, optimizer, or architecture computes and why; use the shared teaching gate rather than duplicating its mechanics.
- **Approach declaration** — name the approach before substantive work and state why a probe is suitable for costly choices; see [`../core/SKILL.md`](../core/SKILL.md) §7.

## Anti-patterns (hard no-list)

- Naming a method before reducing the problem and checking its signal, budget, and measurement.
- Treating an unresolvable metric gap or unvalidated proxy as a ship decision.
- Reporting replay or synthetic performance as if it were measured on the target population.
- Changing several variables and assigning the result to one of them.
- Treating an isolated component benchmark as production latency.
- Moving a threshold after seeing the result.

## Composition

- **Inherits:** `core` for shared integrity and operating gates.
- **Consumes:** the client-validated AI use case when one exists.
- **Hands code construction to:** `dev` after the decision and evaluation plan are framed.
- **Reuses:** `dev` engineering conventions and `core` discipline by reference instead of copying their general rules here.
- **Feeds:** an ML-fit decision into the wider solution architecture when that work is in scope.

## References

- `references/ml-heuristics.md` — task framing, labels, training data, metric design, controls, and model choices.
- `references/train-loop.md` — convergence, data checks, experiment steps, and run records.
- `references/rag-heuristics.md` — retrieval architecture, chunking, ranking, and retrieval evaluation.
- `references/templates/eval-harness.md` — decision-specific evaluation plan to fill before running a system.
- `references/production-thinking.md` — serving constraints, system interactions, scaling, and operational failures.
