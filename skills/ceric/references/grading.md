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
| Quote provenance | `scripts/check_quotes.py`; render-page review or authoritative-text comparison for symbol-sensitive matches | A flagged quote remains unverified, or a symbol-sensitive pass has not been checked against its original source. |
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
| Quote matches cited locator | `check_quotes.py` requires an exact normalized match at the named page, line range, or section | Inspect symbol-sensitive matches on the rendered page or compare them character by character with the authoritative text. |
| Every element row has a quote or an explicit MISSING/THIN reason | `check_narrative.py` checks shape | Decide whether the quote or status is correct. |
| Narrative form | Check one paragraph, CCERI order, 150–450 words, no copied eight-word run, and each verbatim sentence-builder stem | Decide whether smoothing preserved CCERI order and meaning. |
| Hedge and strengthener | Lints identify likely changes | Compare each Claim and Reasoning sentence with its source quote. |
| Outside facts | Lints identify numbers and capitalized terms | Check each item against the source or its † note. |
| Element mark | — | Choose ✓/○/✗ and justify it from the source. |
| Missing register | — | Check both false absences and omissions presented as found. |

Run `scripts/ceric_check.py <run_dir> --paper <paper.pdf-or-txt>` and retain its
mechanical table. Add `--freeform` for notes that do not use the templates.

## Grade procedure

1. Run the mechanical check. Resolve every eye-check against the rendered page or authoritative text, according to the source.
2. Grade only the named activity or element group. Read the run against the source,
   element by element. For each mark, record a one-line reason and the run line and source
   locator that support it. Apply `elements.md` boundaries literally.
3. Complete all five failure-mode rows with evidence.
4. Check the missing register in both directions: an absence listed that is actually
   present, and source content presented as present when it is absent.
5. For every mechanically flagged quotation, note whether the rendered page or text-source comparison settles it.
   Return the element marks, failure modes, mechanical checks, coverage, and ranked
   findings from most severe to least severe, with a fix for each. Include two to four
   practices worth copying. If a review report is needed, add a brief event chain, what
   helped, what needs improvement, and actions; keep the CERIC scores, failure modes,
   coverage, and ranked findings intact. [book:site-reliability-engineering], Closing Remarks

When there is no key, grade against the source itself and state that no key was used.

## Cold grading and reasoning quality

A cold grader receives the run, the source, and the instrument, but not the writer's
reasoning or another grader's output. Read every run file; use rendered pages for visual
content when they exist, or the authoritative text for unpaginated sources. Prefer two
graders on different model lanes over asking one grader to repeat the same pass; route
their disagreements for human review. [book:swebok], 2.3. Reviews and Audits; [book:facilitating-software-architecture], Seek advice from those with conflicting views

Do not reward volume, style, or effort, and do not penalize a reader for retaining a
hedge that the key dropped. Record unresolved doubts as findings with their line instead
of settling them in the reader's favor.

For a Reasoning or Implications paragraph, ask whether it is reliable (true and
justified), relevant to the claim and context, cohesive across its parts, and cogent to
the reader. [book:learning-systems-thinking], Strengthen the Reasons

Keep the review blameless: examine the contributing conditions, method, and process, not
the reader's character or intent. [book:site-reliability-engineering], Google's Postmortem Philosophy

## Claim audit

An Audit produces `claim-audit.md` from `templates/claim-audit.md` and ranked
`findings.md` from `templates/findings.md`. These are the audit contract and size the
review; do not substitute a CCERI narrative unless the caller asks for one. The audit's
source corpus is the target artifact and the named documents supplied for checking it.
Check what those documents say and whether the target cites and qualifies them correctly.
Independent client, product, and vendor fact research remains with
`business-intelligence`. If a named source is unavailable, record it in the corpus table
and leave affected claims open instead of inferring support. (derived: dogfood 2026-10-01)

| Audit depth | Scope | Size box |
|---|---|---|
| **abstract** | Target title and executive summary or abstract | ≤ 20 claim rows and ≤ 800 words |
| **hunt** | Named target sections or the main body | ≤ 60 claim rows and ≤ 2,500 words |
| **full** | Every material claim in the target | ≤ 120 claim rows and ≤ 6,000 words |

State the audit depth before starting. At the limit, record how many claims were not
examined and why; do not imply full coverage. These claim and word limits are derived
from the read size boxes. (derived: dogfood 2026-10-01)

### Audit sequence

1. Declare the target, named source corpus, audit depth, and review approach; mark sources
   unavailable before treating any claim as supported.
2. Make a six-field hunt of the target artifact itself—Claim, Evidence, Reasoning,
   Implications, Context, and missing material—before building the claim table.
3. Check the missing register both ways: note unsupported absence claims, and note material
   present in the named sources but presented as absent or omitted from the target.
4. Enumerate each material target claim within the declared size box; give it one stable ID
   and its target source alias and locator.
5. Type each claim and add one row per evidence quote, naming its source alias and exact
   page, line range, or section; check source attribution and evidence quality. Run
   `scripts/check_quotes.py --source alias=path ... --notes claim-audit.md` over the
   target-claim and evidence quote tables and keep the checker output with the audit record. `ceric_check.py`
   covers the Read notes and narrative only; it does not mechanically pass audit or grade
   tables, `issues.md`, or separate quote files. (derived: dogfood 2026-10-01)
6. Trace the stated reasoning from evidence to claim, preserve the target's hedge, and
   identify the validity dimensions needed for that claim.
7. Assign a verdict only after those checks; record attribution and hedge defects in their
   separate fields, then tally verdicts and defects.
8. Rank the resulting findings in `findings.md`, point each to claim IDs and evidence
   locators, and state the correction or question that would resolve it.

The procedure and named outputs are derived from the synthesis audit dogfood.
(derived: dogfood 2026-10-01)

Give every material claim its own row. Include the claim, its type, the source and
provenance for its **Evidence**, the step of **Reasoning** from evidence to claim, the
claim's **Hedge**, applicable validity dimensions, a verdict, attribution status, hedge
check, and any defect or reason it remains open. Classify the claim and identify needed
validity checks before assigning a verdict. [book:research-methods-psychology], Finding and Reading the Research; [book:research-methods-psychology], Chapter 3: Three Claims, Four Validities: Interrogation Tools for Consumers of Research; [book:learning-systems-thinking], Chapter 7. Collective Systemic Reasoning; [book:learning-systems-thinking], Strengthen the Reasons

The four verdict labels are **supported**, **evidence only** (evidence named but no
reasoning), **assertion** (no evidence), and **overstated** (the hedge was dropped or
strengthened). Keep these as the only adjudicated verdicts, as required by
`ceric-R141`. If the evidence cannot yet be adjudicated because a source is missing or a
check is incomplete, mark the claim **open** and state why; open is a workflow state, not
a fifth verdict. Track attribution separately as `correct`, `misattributed`, `unavailable`,
or `unclear`, and hedge separately as `preserved`, `weakened`, `strengthened`, or `not
assessable`. Count these defects separately from the four verdict totals so a wrong source
pointer or missing qualifier is visible even when the claim has some support.
(derived: dogfood 2026-10-01)

Use a defined audit process with named reviewer roles. If the method owner does not
review the result, assign a different model lane to check every claim against its source
and apply the four verdicts consistently. [book:swebok], 5. Software Configuration Auditing

| Claim type | Checks that usually apply |
|---|---|
| Frequency | Construct: does the measure fit the variable? External: does the sample support the stated population? Statistical: what is the estimate, its precision, and the replication evidence? |
| Association | Construct: are both variables measured suitably? External: can the relationship generalize? Statistical: how large and precise is it, and has it replicated? Do not read causality into association language. |
| Causal | Construct: do measures and manipulations fit? Statistical: how large and precise is the effect, and has it replicated? External: where might it generalize? Internal: is there covariance, temporal precedence, and a design that addresses alternative explanations? |
| Normative / recommendation | What factual premise, authority, conditions, and intended scope support the recommendation? Keep the empirical premise distinct from the prescriptive step. |

For a normative rule, classify its factual core separately when it makes an empirical
claim; use the frequency, association, or causal checks only when that core actually fits
one of them. Keep the recommendation's authority, scope, and conditions visible without
forcing them into a study-design category. (derived: dogfood 2026-10-01)

The four dimensions are **construct** (measurement or manipulation), **external**
(generalization to other populations, settings, or times), **statistical** (strength,
precision, and replication), and **internal** (whether alternatives account for a causal
effect). Name only dimensions relevant to the claim; do not label a study simply valid or
invalid. [book:research-methods-psychology], Chapter 3: Three Claims, Four Validities: Interrogation Tools for Consumers of Research

For a software, platform, or vendor benchmark claim, also record who ran it; sample size
or workload, task, and conditions; commercial interest; replication status; exact product
or model version and date; baseline; and uncertainty or known limitations. A field left
unknown remains unknown; this checklist assesses the named evidence and does not move
independent product-fact checking into CERIC. (derived: dogfood 2026-10-01)

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
