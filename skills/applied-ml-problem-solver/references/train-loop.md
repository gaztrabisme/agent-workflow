# The Experiment Loop

For running many trials unattended, use the `autoresearch` skill ([../../autoresearch/SKILL.md](../../autoresearch/SKILL.md)); this page covers the ML judgement around it.

Use this loop for training, fine-tuning, model comparisons, and other ML experiments where success is measured by outcomes rather than a binary code test. Read `ml-heuristics.md` for problem formulation and model choices, and use the shared teaching gate in `../../core/references/pushback-and-teach.md` when explaining ML mechanisms.

## Ground, define convergence, and size the study

Before the first run, search the available knowledge base for the planned technique, architecture, and metric; record the useful finding or that the search found nothing relevant. Declare the approach before substantive work.

Before collecting data or training, state the hypothesis, primary and secondary metric thresholds, and stop condition. If convergence cannot be defined, return to problem framing. [book:research-methods-psychology], Psychology Is a Way of Thinking

Size the sample from the smallest worthwhile difference and the outcome's variability. Plan enough observations to detect that difference at roughly 80–90% power; do not start with an arbitrary sample size and retrofit a rationale. [book:how-to-read-a-paper], Were preliminary statistical questions addressed?

## Prepare data and evaluation

Before spending compute, inspect the data source, processing history, statistics, and known uses. Check whether class imbalance reflects the actual population or a collection artifact and whether it matches the objective. [book:ai-engineering-huyen], Inspect Data; [book:designing-ml-systems-huyen], Challenges of Class Imbalance

Manually inspect 20–50 examples and compare the labels with your own assessment before trusting a label set. [book:ai-engineering-huyen], Inspect Data

Keep training, validation, and test splits separate. Split before scaling or fitting learned preprocessing, then apply transformations fitted on training data to the other splits. [book:designing-ml-systems-huyen], Scaling before splitting

Before trusting an evaluation score, verify that the set measures the lever being changed. Check for a near-ceiling baseline, positives derived from their answer text, and distractors too easy to distinguish. [book:ai-engineering-huyen], Evaluate your evaluation pipeline; Challenges of Comparative Evaluation

## Run the experiment loop

Define primary and secondary thresholds, a stop condition, an iteration proxy, and the decisive ship gate before the run. Write the threshold against the recorded baseline and confirm that the evaluation can resolve the smallest worthwhile delta.

`Change one variable → train → evaluate → record → decide`

Change one variable per run when runs execute one at a time. [book:effective-conversational-ai], 1.3.2 The continuous improvement cycle. When runs execute in parallel, a small factorial grid can expose interactions one-at-a-time changes miss (SkyPilot, "Scaling Karpathy's Autoresearch", 18 Mar 2026: 16-GPU run, grids of 10–13 runs).

Use a cheap proxy to rank candidates, but ship only if the pre-registered decisive gate passes. After the convergence criteria are met or returns diminish, stop unless the business requires further gains. [book:ai-engineering-huyen], Select evaluation methods; [book:human-in-the-loop-ml], 3.5.3 When do I stop if I'm not time- or budget-constrained?

After selecting a candidate on validation data, run the final evaluation on the held-out test set; never use test results to tune hyperparameters. [book:designing-ml-systems-huyen], Soft AutoML: Hyperparameter tuning

After final evaluation, profile inference latency, throughput, and memory; export the converged model in the target serving format and record the final evaluation results. [book:ai-engineering-huyen], Inference Performance Metrics; [book:machine-learning-production-systems], Exporting Keras Models for TF Serving; Experiment Tracking

## Record, stop, and learn

Maintain an append-only project-root `experiment-log.md` with the goal, current best, and a short entry per run: changed variable, configuration, result, verdict, and next action. Track experiment progress and version the data, code, environment, and model artifacts with the result so the run can be reproduced. [book:machine-learning-production-systems], Experiment Tracking; [book:designing-ml-systems-huyen], Experiment Tracking and Versioning

For each training run, record its configuration, metric against the pre-registered baseline, and verdict. Write every ship/no-ship reason and post-mortem, direction-changing conclusion, and negative outcome to `wiki/decisions.md` as well as the run log. [book:site-reliability-engineering], Negative Results Are Magic

Do not mark an experiment complete until its log entry and any required direction-changing decision exist. Keep entries terse because they will be reread. [book:software-engineering-at-google], Types of Audiences

When a candidate misses its gate, honor the threshold; do not move it after seeing the result. [book:research-methods-psychology], Research Transparency and Credibility. Revert to the baseline and confirm its score returns. Retain rejected artifacts for a later revisit, and record the failure cause so a dead end is not retried without new evidence. [book:machine-learning-production-systems], Experiment Tracking

Write a post-mortem explaining why and how a candidate lost. For a rejected direction, add a `wiki/Rejected Approaches` entry. Use a blameless structure: summary, timeline, primary cause, impact, actions with owners, and lessons learned. A negative result is useful when it changes what the next run will do. [book:software-engineering-at-google], Blameless Postmortem Culture

Keep reusable experiment infrastructure and state when it can be rerun under a changed corpus or objective.
