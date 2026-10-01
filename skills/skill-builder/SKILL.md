---
name: skill-builder
description: "A workflow for building and maintaining role-skill packages. USE WHEN creating a skill, changing its structure or trigger, distilling a book/course/method into a skill, or preparing a skill to publish. Not `core` (shared gates), `evolution` (trace-based changes to a working skill), `conductor` (cross-skill routing), or `ceric` (general claim audits). Not `domestika-course-archive` (exports purchased course media and captions); this skill builds the reusable role-skill package. Keywords: skill authoring, build a skill, SKILL.md, frontmatter, distill, dogfood, references, validate skill, publish skill."
---

# Skill-builder

Produces a discoverable, reviewable role-skill package for the author maintaining a skill set: a `SKILL.md` operating manual, only the useful references and templates it needs, an evolution record, and evidence that the skill works. The package names its artifact and audience, composes with the shared kernel, and keeps source-backed method claims traceable.

Shared gate definitions live in `../core/SKILL.md`. Quality plans name the practices and how each is checked; declare the relevant gates in this workflow's terms and link to the canonical definitions. [book:swebok], 2.1. Software Quality Assurance

## When it fires — and when a sibling owns it

- **This skill:** creating a role-skill; splitting, merging, or structurally refining one; distilling a source method; repairing references or trigger boundaries; preparing a skill for publication.
- **`core` instead:** the need is a shared operating gate or cross-skill contract, rather than a role-skill authoring workflow.
- **`evolution` instead:** the skill already works and a change must be harvested from real traces or an open verdict settled. Skill-builder creates the initial evolution record and owns structural authoring; evolution owns later trace-based updates.
- **`conductor` instead:** the work is to decide how a request should be routed or composed across the skill set. Skill-builder supplies a skill's trigger and hand-offs.
- **`ceric` instead:** the task is a general audit of claims and evidence. Skill-builder keeps only the source-fidelity checks needed to build a method skill.
- Split concerns out before a shared skill swallows them; do not let one skill accumulate every capability. [book:facilitating-software-architecture], Chapter 4. The Architecture Advice Process

> **Disambiguation:** choose by artifact and audience. Skill-builder produces or reshapes the skill package for its author; its siblings own the shared kernel, later trace harvest, constellation routing, or general argument audit.

> **Specific boundary:** `domestika-course-archive` exports a user's purchased course media and captions; skill-builder creates or structurally refines the reusable skill package. (derived: dogfood 2026-10-01)

## Principles / anchoring rules

1. **Give a recurring competency its own trigger.** Create a skill only when it has a distinct audience and trigger that a sibling does not already own. Extract shared machinery when at least three consumers need it; otherwise add a reference or hand-off. [book:infrastructure-as-code], Pattern: Bundle Module; [book:infrastructure-as-code], Antipattern: Unshared Module
2. **Reference the shared source.** Role-skills point to canonical, versioned core material instead of copying it. Keep new content specific to the skill's artifact and audience. [book:building-design-systems], Define the Sources of Truth
3. **Every skill has a learning loop.** A real-use dogfood comes before reliance, and `PENDING` remains until at least two independent real uses support the change. [book:site-reliability-engineering], Progressive Rollouts. Keep the loop running for authored skills too. (field rule)
4. **Make the operating manual easy to retrieve and scan.** Write the long version so unfamiliar readers can follow it, then edit repetition without losing needed detail. [book:software-engineering-at-google], Types of Audiences. Name the output, trigger, audience and boundaries; keep references as tight digests, include each only when it does useful work, and link to each from this manual. [book:software-engineering-at-google], WHO, WHAT, WHEN, WHERE, and WHY; [book:software-engineering-at-google], Guiding Principles. Fill-in artifact templates are optional; include them when useful. [book:looks-good-to-me], 5.4.1 PR templates
5. **Scale the shape to the task.** Keep the skill narrow, show its flow at a glance, and put detailed procedures in linked references. Readers should be able to stop after the section they need. [book:swebok], Chapter 2: Software Design; [book:facilitating-software-architecture], Chapter 6. Architectural Decision Records

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Scope and ground | Fix the proposed artifact, audience, trigger and dependencies; read the kernel and touched siblings | `Grounded:` note and scope decision |
| Author | Fill the canonical skeleton; write the trigger contract, principles, flow, gates and hand-offs | `SKILL.md`, focused references and templates |
| Distill, when needed | Separate method from source; anchor claims and crosswalk material that changes application | Method digests, claim map and crosswalk |
| Validate | Check structure and references, use the skill on a real task, fold findings back | Checker output, dogfood evidence and fixes |
| Publish, when requested | Generalize examples, break private linkage, scan files and history, verify a clean clone | Scrub results and release record |
| Record and hand off | Add the initial evolution entry and route later trace harvests to the right sibling | `EVOLUTION.md` and clear composition links |

The checklist gives the ordered build and refine paths. For a course, book, or talk-series distillation, follow `references/distill-course.md` with `references/authoring-checklist.md`. The course playbook and publishing reference carry the longer procedures. The flow table is an index; scale it for a quick question, a critique of existing work, or a recheck after a fix. For a critique or structural refine, use `references/refine-review.md` and its report template. [book:continuous-delivery], Chapter 3: Continuous Integration

For a course distillation, specify the output medium, recurring scripts or templates, and the render-and-check loop. Say when to open the factual library, list application-changing crosswalk corrections, and cite source anchors or pages in outputs. Report what was measured, vision-judged, not judged, or skipped and why.

## Gates (declared here, defined in core)

- **Grounding gate** — read the relevant source, `core`, and every sibling the new skill touches; record what conventions or references were reused. See `../core/references/grounding-gate.md`.
- **Output Contract** — the result is the skill package and its evidence: files exist, checks name their results, and an unfinished gate is reported. See `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- **Pushback and teach** — explain a substantive recommendation and give a better next move. See `../core/references/pushback-and-teach.md`.

## Anti-patterns (hard no-list)

- Copying core gate prose into a role-skill instead of linking the canonical references.
- A one-off, duplicate-trigger, reference-only, or mega-skill that a sibling already owns.
- A description with no concrete retrieval terms, trigger, or needed disambiguation.
- Calling a distilled skill `KEEP` before its claims have been checked in real use.
- Shipping without an evolution record or the required dogfood; adding a reference or template that nothing points to.

These failures are easier to catch when the workflow names its gates and checks early. [book:continuous-delivery], Some Common Release Antipatterns; [book:swebok], 2.1. Software Quality Assurance

## Composition

- **Core reference:** link to `core` for shared gate definitions; keep skill-specific procedures here.
- **Consumes / hands off to:** `conductor` for constellation routing and multi-skill approach declarations; `evolution` for real-trace harvesting and verdict settlement; `ceric` for general claim-evidence audits.
- **Pipeline position:** after `conductor` scopes and routes an authoring request, this workflow consumes the request brief and existing skill-set conventions; a distillation also consumes the complete source and factual library. It produces the skill package and its validation and dogfood evidence. Later trace harvesting and verdict settlement go to `evolution`; general claim audits go to `ceric`. [book:continuous-delivery], Chapter 3: Continuous Integration
- Keep each skill narrow, give it a distinct trigger, and connect neighboring skills with forward and return links plus explicit hand-offs. [book:swebok], Chapter 2: Software Design
- **Canonical reference rule:** keep shared material in one authoritative source and link to it from the role-skill. [book:building-design-systems], Define the Sources of Truth

## References

- `references/authoring-checklist.md` — decide, ground, write, validate, dogfood, refine and record a skill.
- `references/refine-review.md` — inspect an existing skill, map build checks to review checks, and report evidence-backed findings.
- `references/templates/refine-review-report.md` — record a critique or structural-refine review.
- `references/templates/EVOLUTION.md.skeleton` — minimal local starter if the shared evolution template is unavailable.
- `references/templates/SKILL.md.skeleton` — canonical section headers and frontmatter shape.
- `references/distill-course.md` — source approval, method digests, crosswalk, execution, checks and privacy for book/course distillation.
- `references/rebuild-from-sources.md` — the agent-neutral source-ledger, coverage, claim-audit, dogfood, fix and swap method used in this programme.
- `references/templates/dogfood-brief.md` — brief a fresh-context reviewer to use the skill on a real task and report evidence.
- `references/templates/method-digest.md` — one anchored digest for each method stage.
- `references/templates/science-crosswalk.md` — compare a course method with its factual or measurement library.
- `references/publishing.md` — prepare a skill for public release and verify the published artifact.
- `scripts/check_refs.py` — check package paths, named files, sibling pointers, optional skeleton headings, format, and source anchors.
- `scripts/scrub_check.py` — scan a working tree and, when requested, the full Git history against a private denylist.
- Every skill ships with `EVOLUTION.md`; use `../evolution/references/templates/EVOLUTION.md.skeleton` when the shared sibling is available, or `references/templates/EVOLUTION.md.skeleton` as the local minimum fallback. (derived: dogfood 2026-10-01)
