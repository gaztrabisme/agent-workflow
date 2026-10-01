# Distilling a book, course, or talk series into a skill

Reader: the author turning a complete source into a role-skill whose main content is the ordered method it teaches and the checks at each stage. Run this playbook inside `authoring-checklist.md`; this file adds the source, claim, execution, and verification work.

Worked example: `../../color-theory/` distilled one course in 2026. Its evolution record explains which decisions were reused and what the dogfood exposed.

Terms:
- **Reading copy:** checked text of the source, with its figures and pages or lessons intact.
- **Anchor:** a citation string locating a claim in that copy (for example, course · unit · lesson · time range). Each source section must have a resolvable anchor.
- **Method digest:** one reference file for one working stage; every source claim points back to an anchor.
- **Science library:** an existing factual or measurement collection on the same subject that does not supply the method being distilled.

## 0. Before starting

- The reading copy has passed its own checks: every lesson was owner-approved or passed an independent audit by an auditor from a different model lane against a stated pass condition; remove marketing material. An unreviewed copy makes every citation suspect. [book:swebok], Chapter 6: Software Configuration Management
- Read the full source before writing. The method is a synthesis across sections, and the source may teach in an order different from the work order. [book:facilitating-software-architecture], Chapter 1. Centralized Architecture Practices in a Decentralized World

## 1. Decide how an existing skill in the area fits

Find a skill that already fires on the subject and classify it before deciding how to incorporate the source. Confirm the classification with the owner; it determines the package shape. [book:facilitating-software-architecture], Your Radar’s Place in an Advice Process

| Existing skill | Then |
|---|---|
| A **collection** of facts and digests, with no ordered method | Make the source's method primary and include the collection as its factual library. Track a vendored collection as one versioned dependency; keep the vendored files unchanged and update them through version control. [book:continuous-delivery], Chapter 14: Advanced Version Control |
| A **system** with its own method | Do not merge competing methods. Add the source as a reference or create a separate skill with a clear trigger boundary. [book:software-engineering-at-google], Documentation Types |

## 2. Repo layout

```text
SKILL.md
EVOLUTION.md
NOTICE.md                  # private source material and vendored licenses
references/
  method/                  # one digest per stage, plus review-checklist.md and measurement.md
  course/                  # checked reading copy, tasks, figures, page map
  templates/               # reusable artifact forms
  crosswalk.md             # course-method claims compared with factual sources
  <science-library>/       # vendored factual collection, unchanged
scripts/
  check_refs.py            # copied into this skill so it works on its own
  checks.py                # measures tests without the course application's tool
```

Keep the method separate from its source. A reader should be able to follow every claim to an anchor, then from the anchor to the text, figure, and page. Give each stage digest its own trace row so future changes can be checked without relying on inline links alone. [book:swebok], Chapter 1: Software Requirements

### Claim traceability matrix

Use one row for each important method claim. Inline citations remain useful, but the matrix makes missing or stale links visible.

| Claim ID | Source anchor | Digest file and heading | Validation check | Status |
|---|---|---|---|---|
| `<id>` | `<lesson/page/frame anchor>` | `<file>§<heading>` | `<review test or script>` | `<open/checked>` |

## 3. Write the method digests

- Write one digest per stage in working order, starting from `templates/method-digest.md`. (field rule)
- Anchor each source claim. If an idea is yours, label it **derived** and name the evidence combined; never present a derived summary as the teacher's words. [book:swebok], 7.3. Requirements Attributes
- Preserve the teacher's examples because they carry meaning. Mark details read from a figure as `(frame)`. (field rule)
- End each digest with the practice task the teacher set and link to its unit or lesson file. (field rule)
- Before trusting a digest, run three distinct document reviews: technical accuracy by a subject-matter expert, audience clarity by someone unfamiliar with the domain, and writing consistency. Record which pass found or resolved each issue. [book:software-engineering-at-google], Documentation Reviews
- After every edit, run `python3 scripts/check_refs.py .`; it checks links and anchors against the reading copy. [book:continuous-delivery], Chapter 4: Implementing a Testing Strategy

## 4. Write the crosswalk

Check each important course claim against the factual library and assign one verdict in `templates/science-crosswalk.md`:

- **Agrees:** the source library supports the claim as stated.
- **Refines:** the claim works only with a correction; state the correction plainly.
- **Adds:** the library contributes something the method source does not cover.

The crosswalk names what is checked and how; do not merge an application-changing correction silently into a digest. Put short corrections that change the method into `SKILL.md`. [book:swebok], 2.3. Reviews and Audits

## 5. Rebuild execution and verification for agents

A source may teach inside one application. Its method tells the reader what to decide and in what order; it may not explain how an agent can make the artifact or prove it is sound. Build those execution and verification steps explicitly. (field rule)

### Execution: how the agent makes the artifact

- Name an editable, verifiable output medium for each deliverable. For visualizations, choose by interaction and data scale: interactive elements can use SVG while large, mostly static datasets can use canvas. Avoid assigning a medium from a broad deliverable label alone. [book:d3js-in-action], 11.2.3 Mixed mode rendering techniques
- Provide a script or template when a step recurs, needs exactness, agents often do badly, or can fail silently; leave the rest as clear instructions. [book:continuous-delivery], Principles and Practices of Build and Deployment Scripting
- Let domain conventions override the source's stylistic preferences; keep project-specific components in project code, not in the reusable skill. (field rule)
- Hand off only to skills the owner controls. Where neighboring work belongs to an unowned skill or a vendor feature, state the boundary by the artifact it produces. Do not name a tool available in only one agent; describe the task generically. [book:continuous-delivery], Principles and Practices of Build and Deployment Scripting
- Before finishing, search the skill for unowned skill names and agent-specific tool names; require an empty result. (field rule)
- Copy `scripts/check_refs.py` into every distilled skill so its link and anchor checks work without this source repository. (field rule)

### Verification: render and check

Render the artifact, check it, fix it, and render again. Run exact, cheap checks before visual review. [book:looks-good-to-me], Be your own first reviewer

1. **Code checks first.** Run checks that can measure a property exactly and cheaply.
2. **Vision second.** Give the rendered artifact and specific checklist questions to a reviewer who did not make it. Ask whether a defined property is present; do not ask only whether it “looks good.” If no reviewer can judge a visual property, report it as `not judged`, not as a pass. [book:looks-good-to-me], 2.2 How does a code review work?
3. **Report the result.** State what was measured, vision-judged, not judged, or skipped, and why. Separate automated checks from issues that need human judgment. [book:looks-good-to-me], You are responsible for what passes through your review

### Measurement outside the source's tool

For each review test, describe the source procedure and a tool-independent check. If a test needs a threshold the source does not provide, do not invent a default: justify the threshold as a product decision and obtain it from someone with authority and evidence to set it. [book:site-reliability-engineering], Objectives

Check proposed measurements against the factual library before using them; the source application's reading can mislead. Reliability and validity are properties of the measure, not just of the tool. [book:swebok], 3.3. Reliability and Validity

## 6. SKILL.md

Beyond the canonical skeleton:

- Give each principle a source anchor; show the method flow in a table with stage, decision, check, and linked reference. (field rule)
- Scale the flow for a quick question, a critique of existing work, and a recheck after a fix. (field rule)
- State the output medium, scripts and templates, the render-and-check loop, and when to open the factual library. List application-changing crosswalk corrections. (field rule)
- Anchor every method claim, and cite the science library for each factual claim. [book:swebok], 7.4. Requirements Tracing
- Cite anchors or pages in outputs. Report measured, vision-judged, not-judged, and skipped checks with reasons. [book:looks-good-to-me], You are responsible for what passes through your review
- Do not state an unanchored source principle or present a derived conclusion as if the source said it. (field rule)

## 7. Dogfood

Use `templates/dogfood-brief.md` on real work. A course-distilled skill uses the three tasks in that brief: a paired-goal plan, a critique using the full checklist without the source application, and a fact question routed to the factual library. At least one task must produce an artifact through the complete render-and-check loop. (field rule)

### Claim audit when the owner does not review the method

An independent auditor from a different lane checks every anchored claim beside its source. For the course-method audit, use `supported`, `overstated`, `unsupported`, or `derived-unlabelled`; return every claim that is not supported to the writer for at most three rounds. [book:looks-good-to-me], 2.2 How does a code review work?

- Later rounds replace earlier verdicts for the same claim. Drop rows for anchors no longer cited.
- Audit each method-file edit after it happens; make edits before the final audit or audit their diff. Dogfood fixes are labeled derived and the changed text is audited. [book:looks-good-to-me], Table 3.1 Code review functions
- Fix the source or generator as well as the emitted text so the defect does not recur. For recurring or unclear failures, use a root-cause technique such as a fishbone diagram to find contributing factors. [book:swebok], 7. Root Cause Analysis; [book:swebok], 7.1. Techniques for Conducting Root Cause Analysis

## 8. Privacy and install

- Paid course material means a **private** repository. `NOTICE.md` names the course and any vendored licenses; the license frontmatter is proprietary. Do not run public-publishing steps on paid material. (field rule)
- Install the skill as the single entry point; unlink absorbed standalone copies, update the owned routing table, and tell the prior sibling which skill now owns the method. (field rule)
- Check for account-synced copies you cannot remove locally; tell the user where to disable an unwanted copy in the relevant account settings, such as claude.ai. (field rule)

## 9. Record

Write the first `EVOLUTION.md` entry from the shared skeleton. Record the classification, sources, rule/crosswalk count, dogfood findings and fixes. Keep the verdict `PENDING` until two independent real uses; a distilled skill's borrowed confidence is not evidence. (field rule)

## Adding a second course to an existing distilled skill

Store the reading copy in its own folder, merge its claims into the current digests with its own anchors, record disagreements in the crosswalk, and configure `check_refs.py` to read both sources. (field rule)
