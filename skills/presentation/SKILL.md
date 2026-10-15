---
name: presentation
description: "Produces planned, rendered and verified slide decks, handouts and recorded explanations across HTML, PDF, editable PowerPoint and MP4. USE WHEN planning, authoring or reviewing a presentation, printable deck, explainer video, or app demo. UX owns product flows and copy; information-design owns chart meaning; visual-design and color-theory own visual structure and color; motion owns choreography; frontend owns working web apps. Keywords: presentation, slides, slide deck, HTML deck, PDF handout, PowerPoint, PPTX, MP4 explainer, recorded demo, storyboard, speaker notes, captions, export, editability."
license: "Proprietary (private, not for redistribution)"
---

# Presentation

This skill produces a sourced story plan and the requested presentation deliverables: HTML slides, PDF handouts, editable PowerPoint, MP4 explainers, or app demos. It coordinates the owner's design skills and drives the existing render and scene tools; it does not replace their specialist decisions or reimplement their pipelines.

> Inherits the shared kernel. See [core](../core/SKILL.md) and its canonical gates.

## When it fires — and when a sibling owns it

- **This skill:** a deck, handout, narrated explainer, recorded product demo, or review of those artifacts.
- **UX:** owns product tasks, flows, audience research, and interface copy.
- **Information design:** owns chart questions, data mappings, and chart keys.
- **Visual design:** owns composition, hierarchy, typography, and visual systems.
- **Color theory:** owns palette, color meaning, and color checks.
- **Motion:** owns the motion story, storyboard, timing, and choreography.
- **Frontend:** owns functioning web interfaces and app changes; this skill owns a presentation or demo made from them.

> **Disambiguation:** choose by deliverable. This skill assembles a presentation; its siblings provide the task, chart, visual, color, motion, or app decisions that the presentation needs.

## Principles / anchoring rules

1. **Name the audience and outcome before building slides.** The brief and story references define what the reader should know, decide, or do.
2. **Keep each claim traceable to its supplied evidence.** Mark assumptions and limitations where the audience needs them.
3. **Use the governing client or company identity.** Use the owner's profile only when no governing identity applies, and treat it as a draft.
4. **Treat each medium as a separate deliverable contract.** A rendered PDF or movie does not establish PowerPoint editability or playback.
5. **Render the artifact and inspect it.** A clean tool exit is not visual evidence; report code checks, human review, and unjudged items separately.

## The flow (at a glance)

| Stage | Goal | Primary artifact |
|---|---|---|
| 1. Brief and audience | Fix audience, use, outcome, evidence, and delivery constraints | [brief-and-audience.md](references/method/brief-and-audience.md) |
| 2. Story and structure | Turn the evidence into a message-led sequence | [story-and-structure.md](references/method/story-and-structure.md) |
| 3. Slide design | Apply the governing identity and coordinate visual decisions | [slide-design.md](references/method/slide-design.md) |
| 4. Data slides | Specify chart meaning and keep data faithful | [data-slides.md](references/method/data-slides.md) |
| 5. Output by medium | Produce HTML, PDF, PPTX, explainer, or app demo | [output-by-medium.md](references/method/output-by-medium.md) |
| 6. Render and check | Fix mechanical defects and review the actual output | [render-and-check.md](references/method/render-and-check.md) |
| 7. Delivery and editability | Verify files, editability claims, and owner checks | [delivery-and-editability.md](references/method/delivery-and-editability.md) |

## Execution

1. Read the brief and any project guidance. Record the audience, purpose, decision or action, evidence, caveats, setting, requested media, and acceptance checks.
2. Draft and confirm the story outline before styling. Ask the relevant sibling skill for chart, composition, color, motion, or app decisions; preserve the source data and limitations.
3. Select a governing brand system. If the owner's profile is appropriate, consult its [README](../../tools/brand-profile/README.md) and [profile](../../tools/brand-profile/PROFILE.md); both identify it as a draft awaiting owner review.
4. Build the HTML/SVG source or storyboard. Use [render-kit](../../tools/render-kit/AGENTS.md) for visual checks and [scene-engine](../../tools/scene-engine/AGENTS.md) for native PowerPoint export, video rendering, and app capture.
5. Run applicable checks in [review-checklist.md](references/method/review-checklist.md) and [measurement.md](references/method/measurement.md). Fix failures, inspect skipped or incomplete results, and rerun affected checks.
6. Deliver the requested files with a short evidence record. Separate measured results, vision review, not-judged items, and owner checks.

Scale the stages to the task: a quick slide critique starts at render and check; a new deck or explainer uses the full sequence; after a fix, rerun every check that could be affected.

## Gates (declared, inherited from core)

- **Grounding gate** — substrate: brief, source material, approved brand inputs, storyboard, and rendered/exported artifacts. Keep evidence, assumptions, and limitations distinct. See [grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract** — deliver the requested medium, source/editability evidence where applicable, and a record of measured, reviewed, not-judged, and skipped checks. See [output-contract.md](../core/references/output-contract.md) and [wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach** — explain when a requested treatment would obscure evidence, misstate capability, or imply unverified compatibility; offer a concrete option. See [pushback-and-teach.md](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Styling slides before the audience, outcome, and evidence are clear.
- Treating the owner's draft profile as a settled identity or applying it over a client brand.
- Making up chart meanings, changing sourced proportions, or hiding selection rules and caveats.
- Calling a picture-only export editable without disclosing its limits.
- Treating structural checks or a LibreOffice render as proof of PowerPoint or Keynote playback.
- Declaring quality from the first render or from an encoder's exit code.
- Calling unavailable vision review a pass, or burying an owner-check result as passed.
- Adding movement, captions, or decoration that competes with the message or reading time.

## Composition

- **Inherits:** [core](../core/SKILL.md) for shared gates.
- **Consumes:** [UX](../ux/SKILL.md), [information-design](../information-design/SKILL.md), [visual-design](../visual-design/SKILL.md), [color-theory](../color-theory/SKILL.md), [motion](../motion/SKILL.md), and [frontend](../frontend/SKILL.md) when their decisions are needed.
- **Uses:** [scene-engine](../../tools/scene-engine/AGENTS.md) for video, app capture, and native PPTX; [render-kit](../../tools/render-kit/AGENTS.md) for HTML/SVG/PDF rendering and code checks; [brand-profile](../../tools/brand-profile/README.md) as a draft owner-specific input.
- **Boundary:** this skill owns the presentation story, medium choice, coordination, and delivery review. The named siblings and tools retain their specialist methods.

## References

- [references/method/brief-and-audience.md](references/method/brief-and-audience.md) — audience, outcome, evidence, and delivery context.
- [references/method/story-and-structure.md](references/method/story-and-structure.md) — message and sequence before slide styling.
- [references/method/slide-design.md](references/method/slide-design.md) — governing identity, owner profile status, and design handoffs.
- [references/method/data-slides.md](references/method/data-slides.md) — chart and evidence handoff to information-design.
- [references/method/output-by-medium.md](references/method/output-by-medium.md) — medium-specific production contracts.
- [references/method/render-and-check.md](references/method/render-and-check.md) — render-kit, scene-engine, and visual-review loop.
- [references/method/speaker-script-pass.md](references/method/speaker-script-pass.md) — internal speaker script walked in slide order, and a repeat check by a second reviewer, before a deck is shown.
- [references/method/delivery-and-editability.md](references/method/delivery-and-editability.md) — source and export checks, editability, and owner checks.
- [references/method/claim-audit.md](references/method/claim-audit.md) — source decisions and limits, with evidence index in [audit/](audit/).
- [review-checklist.md](references/method/review-checklist.md) — T1–T18 pass conditions and return stages.
- [measurement.md](references/method/measurement.md) — reproducible code checks and vision questions.
- [templates/deck-shell.html](templates/deck-shell.html) — standalone one-slide 1920×1080 HTML shell with render-kit markup and copied draft tokens.
- [questions/deck.md](questions/deck.md), [questions/demo.md](questions/demo.md), and [questions/pptx.md](questions/pptx.md) — ready yes-means-pass review questions for deck, demo, and PowerPoint briefs.
- [NOTICE.md](NOTICE.md) — private status and source notices.
- [EVOLUTION.md](EVOLUTION.md) — design-run birth and pending real-use validation.
- [DISTILL-REPORT.md](DISTILL-REPORT.md) — source coverage, validation results, and open review items.
- [scripts/check_refs.py](scripts/check_refs.py) — verify local package paths and references.
