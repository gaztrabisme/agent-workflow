# The CERIC read, step by step

In Read mode, one source produces traceable notes, a still-missing register, and a
one-paragraph narrative. Declare the depth before starting. A bounded, time-boxed probe
gathers information; it does not pretend to settle more than it examined.
[book:facilitating-software-architecture], Introducing Spikes

Hunt in CERIC order—Claim, Evidence, Reasoning, Implications, Context—and write the
finished narrative in time order: Context, Claim, Evidence, Reasoning, Implications.

## Choose the mode and depth

| Depth | What you produce | Size box |
|---|---|---|
| **abstract** | Mark title and abstract; notes table; status for each element; missing list | ≤ 20 rows and ≤ 800 words |
| **hunt** | Above, plus 1–3 questions per element answered from named sections, missing register, and narrative | ≤ 60 rows and ≤ 2,500 words |
| **full** | Hunt every element through the register; include glossary and new questions | ≤ 120 rows and ≤ 6,000 words |

State the chosen depth and stop at its size box. More pages or words are not a substitute
for a defined inquiry. [book:facilitating-software-architecture], Introducing Spikes

## Ground the document

For a paginated source, extract page-marked text with `scripts/extract_pages.py` and read
from it and the rendered pages, not from memory. Inspect figures, tables, and error bars
on the rendered page; text extraction can scramble them. For a
paper-level task, do not stop after an abstract when the requested read is of the full
paper; abstract depth is valid only when that is the requested scope. Always inspect
figures and tables on the rendered page. For a source supplied only as plain text or
markdown, cite its source alias plus `L12-L15` or `§ Heading`; the exact-quote checker
compares against that line range or heading section. (derived: dogfood 2026-10-01)

If a symbol-sensitive quote has a rendered original, inspect that page. If the authoritative
source has no rendered form, compare each symbol in the quote character by character with
the source text and record `text-source comparison` in Status or the run record. If the
plain text was extracted from a paginated original, use the original page and render for
this review instead. (derived: dogfood 2026-10-01)
[book:research-methods-psychology], Ethical Principles and Practices; [book:how-to-read-a-paper], Ten questions to ask about a paper describing a questionnaire study

A summary does not replace the source read. If stuck, a GenAI summary is a fallback; cite
it wherever its wording enters the write-up, and return to the source for the evidence
and classification. [book:research-methods-psychology], Finding and Reading the Research

Assistance may help translate or define terms, or find relevant material, but you make the
element classifications.

## Mark the abstract and set statuses

Read the title and abstract once for meaning. Mark phrases C, E, R, I, or Co according to
`elements.md`; a phrase can carry two marks only when each has its own reason. The title
often states a Claim and the abstract may compress all five elements. [book:research-methods-psychology], Presenting Results: APA-Style Reports and Conference Posters

For each element, record **present**, **thin** (name what is missing), or **MISSING**.
At abstract depth, stop after these statuses and the missing list.

## Plan and hunt

Write one to three answerable questions per element yourself. Require source quotes for
each hunt answer; a summary alone is not a hunt answer. Name the likely section using the
genre-aware map in `elements.md`; use
headings, tables of contents, appendices, and cross-references where the source does not
follow IMRaD. Read the planned section for its question; if no useful map exists, search
the whole document. An unmapped section is not evidence of absence. [book:research-methods-psychology], Finding and Reading the Research

For every answer, record the exact quote, Source alias, page or text locator, section,
question answered, and status (**answered**, **partly**, or **missing**). Keep one verbatim
quote in each Quote cell. Use page labels such as `p3` and `pp3-4` for paginated sources,
or `L12-L15` / `§ Heading` for plain text. Figures and tables count as evidence and
reasoning: quote a caption or row label, identify the figure/table and page in Section,
and put your visual observation in Status. [book:research-methods-psychology], Finding and Reading the Research; [book:research-methods-psychology], Ethical Principles and Practices

Immediately after capturing quotes, run `scripts/check_quotes.py`; correct or remove any
quote that is not an exact match at its cited page, line range, or section before
continuing. For an audit using several documents, add `Source` and `Where` columns and
configure each source by alias, for example `--source synthesis=./synthesis.md --source
web=./agent-ready-web.txt`. (derived: dogfood 2026-10-01)

### Design-specific checks

The five CERIC elements apply across designs. Add questions from a reporting checklist
that fits the source's design, and keep a bank of those questions keyed by study type.
For a randomized trial, use the applicable CONSORT checklist and check allocation,
intervention and control details, outcomes, sample-size rationale, blinding, analysis,
participant flow, deviations, recruitment dates, and harms where the checklist requires
them. [book:how-to-read-a-paper], What information to expect in a paper describing a randomised controlled trial: the CONSORT statement

For questionnaire studies, ask whether the question fits the method; whether the measure
is valid, reliable, understandable, piloted, and suitable for the target group; how the
sample was chosen; how the questionnaire was administered; whether response and
nonresponse could bias results; whether analysis fits the data; whether results are
complete; and whether conclusions stay within the findings. [book:how-to-read-a-paper], Ten questions to ask about a paper describing a questionnaire study

For diagnostic, qualitative, and other designs, select a relevant published checklist or
appraisal guide and record the checks that apply; do not invent design-specific criteria.
Use design-check findings to sharpen the missing register, not to claim that a paper failed
only because a general CERIC section map did not expose an item. [book:how-to-read-a-paper], What information to expect in a paper describing a randomised controlled trial: the CONSORT statement; [book:how-to-read-a-paper], Ten questions to ask about a paper describing a questionnaire study

## Missing register, new questions, and glossary

For each absence, record the element, what is absent, why it matters, and the research
question it could inspire. Content deferred to a companion paper you do not have is
missing here; name where the source says it lives. Do not fill the gap from another paper,
memory, or inference.

Record questions raised by the hunt that the abstract did not raise. In full depth, define
every unfamiliar term and symbol with the page where it is defined, or mark your own
definition with †. Keep one stable glossary shared across related reads so a term does not
change meaning between documents. [book:learning-systems-thinking], Building Conceptual Bridges

Use plain language: define or replace jargon so a reader can follow the argument.
[book:learning-systems-thinking], Understandable

## Write the CCERI narrative

Before drafting, write a descriptive outline with one sentence per section capturing who,
what, when, where, why, and how. Build the narrative from that outline so each sentence
can be traced back to a part of the source. [book:hbr-guide-business-writing], Learn to summarize— accurately

Use the five sentence-builder stems in `templates/narrative.md` verbatim, then complete
them in your own words: central Claim, supporting Evidence, justifying Reasoning, future
work, and study motivation.
Carry every hedge into the sentence. Then reorder the material into time order—Context,
Claim, Evidence, Reasoning, Implications (CCERI)—and merge it into one paragraph without
headings, 150–450 words. Define or replace jargon, mark any outside definition with †,
record outside-document definitions in the template's † note, and do not add untagged
facts.

Run `scripts/check_narrative.py`: meet the word band, avoid any copied eight-word run,
begin a sentence with every sentence-builder stem, preserve hedges, and ensure outside
numbers and names are tagged. The lint supports review; read the sentences for meaning as
well.

## Mechanical handoff

Run `scripts/check_quotes.py` before continuing and correct every quote that fails its
cited locator. For one source, use `--paper <paper.pdf-or-txt>`; for an audit with several
sources, use `--source alias=path` once per source and keep those aliases in each table row.
Run `scripts/ceric_check.py <run_dir> --paper <paper.pdf-or-txt>` over a complete Read;
use `--freeform` when the notes do not use the templates. Keep the output table, resolve
eye-check rows against the original rendered page or authoritative text, and hand over
only when mechanical checks are green. Broken checks should be fixed promptly; if the fix
is not available, revert the change that broke the check. [book:continuous-delivery], Essential Practices

## Pair reads and review advice

When a read informs a decision or will be tested outside the reading group, declare a pair
read in the notes header as `pair` and name both readers. A second reader independently
marks the title, abstract, and element statuses
without seeing the first reader's work. A third pass resolves each disagreement against
`elements.md` and records the rule used. Skip the pair read for private notes. [book:swebok], 2.3. Reviews and Audits; [book:facilitating-software-architecture], The Architecture Advice Process: One Rule, Two Advice-Offering Groups, and One Contract

One decision owner seeks advice from people affected by the decision and people with
relevant expertise. Listen to understand each view, record advice that changes the read,
and share the outcome; consultation does not require consensus. For grading or an
important audit, a cold second grader is preferable to having the same grader repeat the
pass; two graders on different model lanes can reveal disagreement that needs human
attention; prefer this over asking one grader to repeat the same pass. [book:facilitating-software-architecture], Seek advice from those with conflicting views

If a second lane is unavailable, put `DEFERRED` and the reason in that same field, follow
the shared core grounding gate's DEFERRED path, and limit the claim to the solo review.
(derived: dogfood 2026-10-01)

## Out-of-lane findings

Errors in the assignment itself—such as the wrong abstract, broken link, or shifted
translation—go in `issues.md` beside the notes. They do not change the read of the supplied
document; read it on its own text.
