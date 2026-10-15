# Measuring the accuracy of an AI or extraction system

How to turn "how accurate is it?" into test cases, rates and limits that both sides can recompute to the same value. The model choice and experiment design belong to `applied-ml-problem-solver`; its [eval harness](../../applied-ml-problem-solver/references/templates/eval-harness.md) holds the sample-size formulas and baseline rules. This module covers what the tester owns: the reference set, the scoring rule, the reported figures and their limits.

## Three tiers of figure

Sort every figure the measurement produces into one tier before anything is promised. (derived: EVOLUTION.md case 1)

| Tier | What belongs | Why |
|---|---|---|
| Commit | Counts, coverage, determinism, and any rate whose denominator the team constructs (injected errors, below) | The team controls them by construction |
| Report | Every rate measured on labelled real data, with its sample size | The team does not control the data's error mix or size |
| Method | The measurement contract: field list, match rule, label protocol, classes, frozen sets | Without it neither side can recompute a figure |

While the system does not yet exist, every rate is a prior. A target can be locked only after a first measured run; before that it is reported, not committed. (derived: EVOLUTION.md case 1)

## Reference set (golden set)

- **Two labellers, independently, then adjudication.** Disagreements are settled by a named person with authority, not averaged. Publish the disagreement rate. (derived: EVOLUTION.md case 4)
- **Drop rate.** If unsettled items are dropped from scoring, publish how many, beside every result, so the answer key cannot be thinned into a better score. (derived: EVOLUTION.md case 4)
- **Freeze before scoring.** Freeze the set, the field list, the classes and the configuration before the run that counts. Any later change re-bases the measurement and is recorded; no old run is re-scored against new rules. (derived: EVOLUTION.md case 1)
- **Labels before scoring.** Schedule scoring after labelling closes. A plan that scores before the answer key exists has a sequencing defect. (derived: EVOLUTION.md case 8)
- **Stratify first.** Declare the classes (for documents: text layer or scanned, layout family, framework) and choose the set so each class has its own items. (derived: EVOLUTION.md case 4)

## Match rule and test case unit

Write the comparison rule before scoring: what normalisation is applied (scale, sign, presentation), and edge cases such as an empty cell versus a zero. An unwritten rule turns every disagreement into a judgement during acceptance. (derived: EVOLUTION.md case 4)

Make each labelled item one test case, and report a rate as cases passed out of cases run, both numbers shown, so the client's own quality team can re-run it. (derived: EVOLUTION.md case 4)

## Per-class rates

Report each class on its own. An overall figure can rank a model that is worse on a minority class above one that is even across classes. [book:designing-ml-systems-huyen], Slice-based evaluation (part 1). A single metric averaged over the whole evaluation set hides important detail. [book:building-machine-learning-pipelines], 7. Model Analysis and Validation (part 1)

- Pool two classes only where they have been declared comparable in advance.
- For injected errors, report per error class, never one detection rate across classes. (derived: EVOLUTION.md case 1)
- Give each class its share of real volume beside its rate, so the reader can weigh it.

## Counting unit

Count each rate in the unit where one event is one observation. For false alarms from consistency rules, count per fired rule (rule, document, column), not per field: one broken total implicates many correct fields by design, and a per-field count inflates the rate. (derived: EVOLUTION.md case 1)

For rule execution, keep a coverage matrix of rule × document × column in which every applicable cell is either executed or skipped with a logged reason; an empty cell with no reason is a defect. (derived: EVOLUTION.md case 1)

## Sample size

Standard estimators assume independent observations; when observations are not independent, they are invalid. [book:statistics-by-simulation], 6.5. Time Series Should Not be Detrended by Default (part 1). Values extracted from one document share its layout, scan quality and labeller, so they are not independent: the certainty of a rate follows the number of documents, not the number of values. Publish both counts with every rate. (derived: EVOLUTION.md case 4)

A class with too few documents gets a band or a count, not a level. State the minimum per class in the method before scoring.

## Paired figures

Some figures can be met by doing less. "Few items sent to a human" is met by an engine that flags nothing; "high precision on items cleared automatically" is met by clearing almost nothing. Quote each with its partner (errors still caught; share cleared), on the same page, always. (derived: EVOLUTION.md case 6)

## Injected errors

Real labelled data contains few errors of each kind, so a detection rate measured on it has a small and uncontrolled denominator. Insert errors of known class into items already verified correct; the number inserted is the denominator, so the detection rate can be committed. (derived: EVOLUTION.md case 1)

This is fault seeding: the share of seeded faults found estimates the testing's effectiveness. Its limits apply: seeded faults may not be distributed like real ones, extrapolations rest on small samples, and a seeded fault can be left behind. [book:swebok], 5. Test Process. So:

- Base each injected class on errors seen in real data or named in the error model, and say which.
- Publish the suite to the client before the run and let them add or veto items.
- Inject into copies; never into the reference set.
- Report per class, and report the real-data detection figure separately.

If injection is cut from scope, no detection rate can be committed, and every page that implies one must say so. (derived: EVOLUTION.md case 6)

## Tuning and scoring sets

A model tuned against a test set is checked at the end against a holdout set that was not used until then; a holdout score much lower than the test score means overfitting. [book:ai-powered-search], 14.2.4 Formatting the golden set for training, testing, and validation. The same holds for configuration, prompts, thresholds and field descriptions: if they are adjusted after looking at errors on a set, a later score on that same set overstates accuracy on new documents. Split the reference set into a tuning part and a scoring part before tuning starts, or state on the result that it was scored on the set it was tuned on. (derived: EVOLUTION.md case 12)

## Robustness

Test on inputs that differ slightly from clean development data (noise, a cropped page, a lower-quality scan) and compare. [book:designing-ml-systems-huyen], Perturbation tests

## Published limits

Name the error classes the measurement cannot see, on the same page as the rates. For a rule-based checker, a wrong value that leaves every rule satisfied passes unflagged; the scored accuracy figure is the only place it shows. (derived: EVOLUTION.md case 3). Also list inputs not represented in the frozen set (new layouts, frameworks, input types) and report them separately when they occur.

## Measurement design checklist

- [ ] Each figure placed in commit, report or method tier.
- [ ] Classes declared; set stratified; minimum documents per class stated.
- [ ] Label protocol: two labellers, adjudicator named, disagreement and drop rates published.
- [ ] Match rule written; one labelled item is one case.
- [ ] Tuning and scoring sets separated, or the overlap stated.
- [ ] Injected-error suite, or a statement that no detection rate is committed.
- [ ] Every rate with case count and document count, per class.
- [ ] Paired figures quoted together.
- [ ] Limits published beside the rates.
- [ ] Unit stated for each rate; rule coverage matrix has no unexplained empty cell.
- [ ] Scoring scheduled after labelling closes.
