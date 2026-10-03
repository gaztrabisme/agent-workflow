# ML Heuristics

Use these decisions before implementation: reduce the task, define what the labels mean, choose an objective, make sure the evaluation can answer the question, and fit the model to the actual operating constraints.

## Problem formulation and task choice

- Read the specification literally. Do not add model complexity the requested outcome does not need. [book:real-world-software-development], KISS Principle
- Decompose a difficult task into solved subproblems and chain existing solutions where that is sufficient. A detector plus a small attribute classifier may be simpler than a single fine-grained detector. [book:designing-ml-systems-huyen], When to Use Machine Learning
- Choose the simplest useful problem type before selecting a model. A different frame can turn a difficult task into one with fewer classes or a smaller prediction space. [book:designing-ml-systems-huyen], Multiple ways to frame a problem
- Fit-Check the six constraints in `SKILL.md` before committing to the chosen formulation.

## Labels, uncertainty, and error costs

First ask whether labels can coexist on the same example.

| Relationship | Formulation | Typical output |
|---|---|---|
| One state excludes the others | Binary or multiclass classification | Softmax probabilities and a cross-entropy objective |
| Attributes can independently be true together | Multilabel classification | Independent sigmoid scores and binary cross-entropy |

Use sigmoid binary cross-entropy for genuinely multilabel targets; its independent scores allow more than one label to be active. [book:kagglebook_secondedition], Training loop

Do not encode mutually exclusive states as independent binary labels. For example, “no helmet,” “helmet backward,” and “helmet without strap” are alternative states of one helmet label; independent sigmoids can predict incompatible states together. [book:designing-ml-systems-huyen], Multiclass versus multilabel classification

Do not create a learnable “unknown” class for an absence that has no visual pattern, such as a head outside the frame. Mask that task's loss for the sample. Handle inference uncertainty separately with a confidence threshold and a defined path for below-threshold cases, such as abstention, human review, or requesting more information. [book:designing-ml-systems-huyen], Confidence measurement

Multitask models can share a representation while using separate heads for different tasks. If tasks have different numbers of classes, keep those output sizes separate and use a suitable per-task loss. [book:human-in-the-loop-ml], 9.4 Embeddings and contextual representations

Weight task losses according to the real-world cost of their errors. A false negative with safety impact may warrant a different cost from a mistaken accessory label. [book:designing-ml-systems-huyen], Cost-sensitive learning

When a class has fewer than about 5% of the examples in the most common class, use normalized inverse-frequency class weights. Class counts alone do not establish the right objective: inspect label quality, the cost of each error, and performance by class; aggressive weights can amplify noisy rare labels or distort the operating objective. [book:designing-ml-systems-huyen], Class-balanced loss

## Data quantity, splits, and model selection

Before investing in additional data, define a reasonable evaluation baseline and estimate whether more data could plausibly repay its collection cost. [book:data-science-for-business], Evaluation, Baseline Performance, and Implications for Investments in Data

Plot learning curves: generalization performance against training-set size helps distinguish a data-limited model from a model that needs a different formulation or more capacity. [book:data-science-for-business], Learning Curves

Use cross-validation when data is limited and a single holdout would waste too much information for model selection. Keep a final test set outside the tuning process. [book:data-science-for-business], From Holdout Evaluation to Cross-Validation

Never evaluate on resampled data. Rebalance only the training split; evaluation must retain the deployment distribution or the reported result will reflect the artificial resampling distribution. [book:designing-ml-systems-huyen], Data-level methods: Resampling

Split before scaling or fitting any learned preprocessing. Fit those transformations on the training split and apply the fitted values to validation and test data to prevent leakage. [book:designing-ml-systems-huyen], Scaling before splitting

## Metrics and evaluation validity

Choose a primary selection metric, but report the component axes of a composite beside it. A single aggregate can stay flat while precision, recall, latency, or faithfulness move in opposite directions. [book:building-machine-learning-pipelines], 7. Model Analysis and Validation

Use cheap, broad signals to rank candidates and an expensive, higher-quality evaluation where it adds confidence. Only the decisive full-scale gate authorizes a ship. [book:ai-engineering-huyen], Select evaluation methods

Pre-register the ship threshold against the recorded baseline before running the decisive evaluation. The source supports registering the study design and analysis plan; the baseline-linked ship threshold is the ML-specific decision rule. [book:statistics-by-simulation], 3.5. Pre-registration

Keep a point estimate as the best single guess, but publish its confidence interval and describe the strength of the inference. A broad interval does not confirm the point estimate's apparent win. [book:how-to-read-a-paper], Probability and confidence

When a measure is at ceiling or floor, use a manipulation check and a more sensitive measure with detailed quantitative increments before interpreting a null or small difference. A perfect score can hide a real change. [book:research-methods-psychology], Interrogating Null Effects: What if the Independent Variable Does Not Make a Difference?

Test whether the delta is statistically or interval-resolved before calling a win; report unresolved differences as inconclusive. [book:how-to-read-a-paper], Probability and confidence

Check the minimum detectable effect before gating. If the expected change is smaller than the design can resolve, improve the sample, pairing, or measurement grid before running it. [book:statistics-by-simulation], 3.4. Testing Hypotheses and Assessing their Support

A surprising gain is a hypothesis, not proof of a mechanism. Check for bugs, coarse grids, and artifacts, and replicate the result independently before treating it as established. [book:research-methods-psychology], Research Transparency and Credibility

For a retrieval evaluation, check that it has headroom, that positives were not generated from their answer text, that distractors include real competitors, and that the scored unit matches what the consumer receives. Simple prompts or easy distractors can make weak systems look equivalent or excellent. [book:ai-engineering-huyen], Challenges of Comparative Evaluation

Measure lexical overlap between query and positive passage; when the overlap is high, rewrite the query into realistic user language and check that the measured overlap falls.

Seed retrieval distractors with real competitors, such as passages from the same source, section, or topic. Random off-topic negatives often make ranking trivial.

## Experiments and diagnostic controls

Build a cheap comparison or control before interpreting an experiment that can fail because of either the method or its measurement. A comparison condition is required, but it need not always be a full no-treatment group. [book:research-methods-psychology], Why Experiments Support Causal Claims

Use a non-learned oracle to separate insufficient input signal from a model's inability to use that signal. If an oracle can solve the task from the features but the trained model cannot, the failure is downstream of the input. A centroid or averaging decoder can serve as a diagnostic, not automatically as the fair comparator.

Calibrate a null control to the behavior of a correct system, not to an intuitive score. For example, removing all task signal should yield the global prior if that is what a signal-free system would predict. [book:designing-ml-systems-huyen], Baselines

For synthetic or finite-bank training, compare performance on seen realizations with fresh draws from the same generator before relying on train/validation loss. High performance on seen examples but substantially lower performance on fresh draws indicates memorization of the bank.

When finite-bank memorization is the issue, increase the number of generated realizations before adding regularization. If a trained model loses to a low-variance averaging oracle, do not declare the task impossible; report a fair single-snapshot comparator.

## Augmentation

Choose augmentation from real input variation and the label semantics. For camera-angle variation, horizontal flips can be appropriate; avoid vertical flips for upright people because they create an unrealistic distribution. [book:d2l-en], Flipping and Cropping

## Mechanisms and inference constraints

Choose the specific mechanism needed rather than defaulting to a full model architecture. A simpler method that meets the task can be cheaper and easier to maintain than a state-of-the-art model. [book:designing-ml-systems-huyen], Avoid the state-of-the-art trap

Establish the end-to-end inference latency budget before selecting a backbone. Filter out models that miss the latency requirement, then choose the best-accuracy option among those that fit. [book:ai-engineering-huyen], Cost and Latency

Research work often prioritizes throughput; production serving often prioritizes low latency. Select the objective from the workload rather than carrying one metric across both contexts. [book:designing-ml-systems-huyen], Computational priorities

## Added evaluation practices

These practices extend the experiment record with diagnostics for data, metrics, and external evidence.

- When an external AI study or benchmark supplies a baseline, appraise its intended use, intended users, design, comparator, data, and outcomes before treating its number as transferable. For AI decision-support studies, use the ten-question appraisal set based mainly on CONSORT-AI and DECIDE-AI. [book:how-to-read-a-paper], Ten questions to ask about a paper that reports AI studies in healthcare

