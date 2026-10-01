---
name: ceric
description: >-
  A page-cited CERIC read, argument audit, or graded review packet that tests whether
  claims are supported by evidence and reasoning, preserves uncertainty, and records
  what the document leaves out. USE WHEN a paper, report, standard, synthesis, proposal,
  or other artifact needs its claims, support, reasoning, or hedges reviewed, or a CERIC
  read needs grading. Keywords: CERIC, CCERI, claim evidence reasoning, critical reading,
  paper review, argument audit, hedge, quote verification, journal club. Disambiguation:
  CERIC's artifact is per-document argument review; a client intelligence dossier triggers
  business-intelligence, whose claim review may use CERIC findings.
license: MIT
---

# CERIC

CERIC turns a source document into page-cited notes, a still-missing register, and a
CCERI narrative; it can also audit claims in an existing artifact or grade a CERIC read.
Its audience is a reader, reviewer, or editor testing whether an argument is supported.

## Modes and handoffs

- **Read:** use this mode for a paper, preprint, thesis, report, or standard that needs
  reading, summarizing, critique, or notes. Make one six-field CERIC hunt—Claim,
  Evidence, Reasoning, Context, Implications, and missing material—and one set of notes
  per input document; a multi-document synthesis belongs to the caller and can be audited
  claim by claim afterward. [book:learning-systems-thinking], Chapter 7. Collective Systemic Reasoning
- **Audit:** list the artifact's claims and check their evidence, reasoning, hedge, and
  needed study-validity support. Do not treat a conclusion as supported just because the
  source reports it. Leave a claim open when its support does not pass the check.
  [book:critical-thinking-about-research], 9 Inferences, Conclusions, and the Research Report
- **Grade:** score your own read, another reader's, or a participant's, with or without a
  key, using the source document as the record. Name the activity or element group being
  graded. [book:swebok], 2.3. Reviews and Audits
- **Conductor** schedules the work. CERIC supplies the per-document argument map; the
  caller synthesizes across documents and can ask CERIC to audit the result.
  [book:learning-systems-thinking], Chapter 7. Collective Systemic Reasoning
- A surviving grade or audit table can inform solution clarification and client-claim
  review.

## Read and audit principles

1. Work from the source document's page-marked text and rendered pages, never from memory.
   A summary may be a fallback when you are stuck; cite it wherever its wording reaches
   the write-up, and do not let it replace the source read. [book:research-methods-psychology], Finding and Reading the Research
2. Capture exact words, one quote per cell, with page and section before paraphrasing.
   Verify the normalized quote against the explicitly cited page. If symbols or equations
   make extraction uncertain, inspect the rendered page. [book:research-methods-psychology], Ethical Principles and Practices
3. Mark outside definitions with †. Do not add untagged facts, names, numbers, or
   mechanisms from outside the document. [book:research-methods-psychology], Presenting Results: APA-Style Reports and Conference Posters
4. Missing is a finding. Record what is absent, why it matters, and a question it raises;
   never fill the gap from memory, another paper, or assumed author intent.
5. Preserve each hedge and its strength through the paraphrase and narrative. Record any
   shift in strength across title, abstract, and conclusion. [book:critical-thinking-about-research], 2 Research Questions and Hypotheses
6. Keep assignment defects in a separate `issues.md` beside the notes. They do not change
   the read of the supplied paper.

## Shared gates inherited from core

Use the core grounding, output-contract, and pushback gates by reference; do not restate
their general rules here. See `../core/SKILL.md`,
`../core/references/grounding-gate.md`,
`../core/references/output-contract.md`, and
`../core/references/pushback-and-teach.md`. For a single reader at abstract depth, a
pair-read approach declaration can be skipped; when the read will inform a decision or
leave the room, declare the independent review approach.

CERIC's own completion condition is concrete: the requested notes, missing register,
and narrative exist; every mechanical check is green; and any quote needing visual review
has been checked on its rendered page. [book:swebok], Software Process Definition

## Workflow and references

| Work | Read next |
|---|---|
| Define CERIC elements, boundaries, hedges, and genre-aware section mapping | `references/elements.md` |
| Choose a mode and depth; extract, hunt, record, and write | `references/hunt.md` |
| Audit claims or grade a read, including validities, score interpretation, and corrections | `references/grading.md` |
| Fill notes, narrative, and grader-brief templates | `references/templates/` |
| Extract pages and run quote, narrative, and full-read checks | `scripts/` |

## Composition

- **Inherits:** `core` shared integrity and grounding rules, gate-by-artifact, pushback,
  cold review, and evolution loop.
- **Receives work from:** `conductor` for scheduling; `business-intelligence` may use
  CERIC claim-audit findings in its dossier review.
- **Hands findings to:** solution-architect clarification work and business-intelligence
  claim review.
- **EVOLUTION harvest:** surviving graded reads, scorecards, audit tables, and ranked
  findings.
