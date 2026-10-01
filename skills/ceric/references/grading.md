# Grade a CERIC read or audit a claim

## CERIC score and scale

Grade each element against the source of record (and a key, if one exists):

| Mark | Workshop credit | Meaning |
|---|---:|---|
| ✓ | 1 | The content matches the source and stays within the element boundary. |
| ○ | ½ | The core is right, but a load-bearing part is missing or filed under another element. |
| ✗ | 0 | The element is absent, wrong, or fabricated. |

These are ordinal judgments, not a measured interval scale. Report each element mark;
do not average scores across readers or runs. The five-credit total and 4.0 threshold
are a workshop convention, not evidence that all five elements passed. To ship, require
at least ○ for every element, a workshop total of at least 4.0, and the failure-mode
conditions below. [book:swebok], 4.9. Multiple Attribute Evaluation; [book:swebok], 3.2. Direct and Derived Measures

## Five failure modes

Each row needs an evidence line: a quote, run line, page, or check output.

| Failure | Detected by | Fail when |
|---|---|---|
| Quote provenance | `scripts/check_quotes.py`; render-page review for symbol-sensitive matches | A flagged quote remains unverified, or a symbol-sensitive pass has not been checked on the rendered page. |
| Element classification | `elements.md`, narrative lints, grader | More than one misfiling remains. |
| Missing element filled in | Missing register and source comparison | Any element content absent from the source is presented as present. |
| Hedge erased or strengthened | `scripts/check_narrative.py` and sentence-level comparison | A quote's hedge disappears from its paraphrase, or an unsupported strengthener is added; Claim and Reasoning must preserve hedges. |
| Outside information added | Narrative lints and source comparison | A number, name, or mechanism absent from the source is untagged. |

**Pass condition:** every element is at least ○; the workshop total is at least 4.0;
quote provenance, missing-content, and outside-information failures are zero; hedge
failure is zero for Claim and Reasoning; classification failures are at most one; and
mechanical checks are green with visual checks resolved. The total cannot cancel a failed
element.

## Mechanical checks and grader judgment

| Check | Mechanical part | Grader part |
|---|---|---|
| Quote matches cited page | `check_quotes.py` requires exact normalized text on the cited page | Inspect symbol-sensitive matches on the rendered page. |
| Every element row has a quote or an explicit MISSING/THIN reason | `check_narrative.py` checks shape | Decide whether the quote or status is correct. |
| Narrative form | Check one paragraph, CCERI order, 150–450 words, no copied eight-word run, and each verbatim sentence-builder stem | Decide whether smoothing preserved CCERI order and meaning. |
| Hedge and strengthener | Lints identify likely changes | Compare each Claim and Reasoning sentence with its source quote. |
| Outside facts | Lints identify numbers and capitalized terms | Check each item against the source or its † note. |
| Element mark | — | Choose ✓/○/✗ and justify it from the source. |
| Missing register | — | Check both false absences and omissions presented as found. |

Run `scripts/ceric_check.py <run_dir> --paper <paper.pdf-or-txt>` and retain its
mechanical table. Add `--freeform` for notes that do not use the templates.

## Grade procedure

1. Run the mechanical check. Resolve every eye-check against the rendered page.
2. Grade only the named activity or element group. Read the run against the source,
   element by element. For each mark, record a one-line reason and the run line and paper
   page that support it. Apply `elements.md` boundaries literally.
3. Complete all five failure-mode rows with evidence.
4. Check the missing register in both directions: an absence listed that is actually
   present, and source content presented as present when it is absent.
5. For every mechanically flagged quotation, note whether the rendered page settles it.
   Return the element marks, failure modes, mechanical checks, coverage, and ranked
   findings from most severe to least severe, with a fix for each. Include two to four
   practices worth copying. If a review report is needed, add a brief event chain, what
   helped, what needs improvement, and actions; keep the CERIC scores, failure modes,
   coverage, and ranked findings intact. [book:site-reliability-engineering], Closing Remarks

When there is no key, grade against the source itself and state that no key was used.
Do not reward volume, style, or effort, and do not penalize a reader for retaining a
hedge that the key dropped. Record unresolved doubts as findings with their line instead
of settling them in the reader's favor.

## Cold grading and reasoning quality

A cold grader receives the run, the source, and the instrument, but not the writer's
reasoning or another grader's output. Read every run file; use rendered pages for visual
content. Prefer two graders on different model lanes over asking one grader to repeat the
same pass; route their disagreements for human review. [book:swebok], 2.3. Reviews and Audits; [book:facilitating-software-architecture], Seek advice from those with conflicting views

For a Reasoning or Implications paragraph, ask whether it is reliable (true and
justified), relevant to the claim and context, cohesive across its parts, and cogent to
the reader. [book:learning-systems-thinking], Strengthen the Reasons

Keep the review blameless: examine the contributing conditions, method, and process, not
the reader's character or intent. [book:site-reliability-engineering], Google's Postmortem Philosophy

## Claim audit

Give every claim in the audited artifact its own row. Include the claim, its type, the
source and provenance for its **Evidence**, the step of **Reasoning** from evidence to
claim, the claim's **Hedge**, the applicable validity dimensions, and one verdict:
**supported**, **evidence only** (evidence named but no reasoning), **assertion** (no
evidence), or **overstated** (the hedge was dropped or strengthened). Classify the claim
and identify the validity needed before assigning the verdict. [book:research-methods-psychology], Finding and Reading the Research; [book:research-methods-psychology], Chapter 3: Three Claims, Four Validities: Interrogation Tools for Consumers of Research; [book:learning-systems-thinking], Chapter 7. Collective Systemic Reasoning; [book:learning-systems-thinking], Strengthen the Reasons

Use a defined audit process with named reviewer roles. If the method owner does not
review the result, assign a different model lane to check every claim against its source
and apply the four verdicts consistently. [book:swebok], 5. Software Configuration Auditing

| Claim type | Checks that usually apply |
|---|---|
| Frequency | Construct: does the measure fit the variable? External: does the sample support the stated population? Statistical: what is the estimate, its precision, and the replication evidence? |
| Association | Construct: are both variables measured suitably? External: can the relationship generalize? Statistical: how large and precise is it, and has it replicated? Do not read causality into association language. |
| Causal | Construct: do measures and manipulations fit? Statistical: how large and precise is the effect, and has it replicated? External: where might it generalize? Internal: is there covariance, temporal precedence, and a design that addresses alternative explanations? |

The four dimensions are **construct** (measurement or manipulation), **external**
(generalization to other populations, settings, or times), **statistical** (strength,
precision, and replication), and **internal** (whether alternatives account for a causal
effect). Name only dimensions relevant to the claim; do not label a study simply valid or
invalid. [book:research-methods-psychology], Chapter 3: Three Claims, Four Validities: Interrogation Tools for Consumers of Research

When a claim is presented as confirmatory, check whether its hypothesis and analysis plan
were prespecified. Mark a hypothesis adopted after results were seen as post hoc; do not
present it as confirmation. [book:critical-thinking-about-research], 9 Inferences, Conclusions, and the Research Report

## Corrections after delivery

When an error is found after handover, assign a responsible correction owner, acknowledge
the error clearly, state the corrected information, attach the correction to the read,
and send it through the channels used to distribute the original. Close the loop with the
person who reported it and with people who received the read. Keep a standing corrections
policy so readers know how to report errors and how corrections will be handled.
[book:new-ethics-of-journalism], 10 Corrections and Ethics: Greater Accuracy through Honesty

Corrections should be clear and sincere, identify what was wrong and what is now correct,
and reach the original audience. [book:new-ethics-of-journalism], 10 Corrections and Ethics: Greater Accuracy through Honesty
