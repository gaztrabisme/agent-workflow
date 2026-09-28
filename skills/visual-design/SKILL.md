---
name: visual-design
description: "A course-distilled method for shaping visual form, composition, typography and identity systems. USE WHEN planning, making or critiquing a graphic, poster, editorial page, presentation, package, campaign or visual identity. Colour choices belong to color-theory. Keywords: visual design, graphic design, composition, visual hierarchy, negative space, Gestalt, balance, grids, typography, identity system, visual weight."
license: "Proprietary (private course-derived material, not for redistribution)"
---

# Visual Design

This skill turns a brief into a deliberate visual system: a clear concept, simple forms, an ordered composition, a typographic structure and applications that hold together across their real formats. It also reviews existing visual work and routes each failure back to the stage that can fix it.

> Inherits the core kernel — see [../core/SKILL.md](../core/SKILL.md). Obey its integrity constraints, declare its gates and reference its files rather than copying them.

## When it fires — and when a sibling owns it

- **This skill:** planning, making or reviewing graphic form, composition, negative space, visual hierarchy, typography, grids, identity systems and their applications.
- **color-theory:** choosing or explaining colours, palettes, colour meaning, colour-space values or colour contrast.

> **Disambiguation by artifact:** a visual-structure decision belongs here; a colour decision belongs to color-theory. In a composed artifact, keep each decision with its owner.

## Principles / anchoring rules

1. **The brief selects the visual register.** Decide how literal or subjective the response should be from the message and its audience; neither end is inherently better. (5642 · U2 · L07 · 03:57–05:07)
2. **Geometry is a vocabulary, not the concept.** Use shape and proportion to organize a concept; do not assume geometry alone supplies meaning. (5642 · U6 · L81 · 01:44–02:13; 5642 · U6 · L81 · 02:14–02:38)
3. **Design figure and ground together.** Negative space can carry the mark, group elements and set reading pace; it is an active shape. (5642 · U2 · L09 · 03:45–04:50; 5642 · U4 · L49 · 02:06–03:47; 5642 · U4 · L49 · 03:48–04:52; 5642 · U4 · L49 · 04:52–06:43)
4. **Give the eye a hierarchy.** Establish a dominant element, then subordinate elements and detail; competing “number ones” make a message unclear. (5642 · U4 · L55 · 00:08–01:27; 5642 · U5 · L75 · 06:39–07:37)
5. **Balance may be still or dynamic.** Use symmetry, asymmetry, counterweight and movement to fit the intended reading; do not mistake balance for centring. (5642 · U4 · L54 · 00:07–01:16; 5642 · U4 · L58 · 01:45–02:58; 5642 · U4 · L58 · 02:58–03:45)
6. **Build the system for its hardest application.** A mark and its supporting language must remain useful at the smallest or most constrained real use. (5642 · U7 · L96 · 01:48–02:32; 5642 · U7 · L103 · 02:24–03:14; 5642 · U7 · L103 · 03:14–04:24)
7. **Treat course conventions as choices.** A domain's reading order, standards, content rules and production constraints take precedence over an aesthetic convention from the course. (Owner decision 6.)
8. **Anchor the method.** Attribute course claims to lesson anchors; label cross-unit synthesis as derived. Do not present a derived rule as the teacher's wording.

## The flow (at a glance)

| Stage | Decide | Check before moving on | Reference |
|---|---|---|---|
| 1. Brief and intent | Audience, message, real use, constraints and desired reading | The concept and hardest application are named | [brief-and-intent.md](references/method/brief-and-intent.md) |
| 2. Research and concept | Literal-to-subjective and representative-to-abstract position; story and references | References support the intended register; key content survives abstraction | [research-and-concept.md](references/method/research-and-concept.md) |
| 3. Form and unity | Basic shapes, figure-ground, grouping and a recognizable visual vocabulary | The forms read together and their negative spaces are intentional | [form-and-unity.md](references/method/form-and-unity.md) |
| 4. Composition and movement | Grid, hierarchy, weight, balance, focal point, space and visual path | Grid, balance, space, focal point and path pass T4–T9 | [composition-and-movement.md](references/method/composition-and-movement.md) |
| 5. Type and system | Typographic hierarchy, scale, alignment, repeatable modules, constants and variables | Type scale and typography checks pass; named constants survive variants | [type-and-system.md](references/method/type-and-system.md) |
| 6. Medium and variants | Actual support, production constraints, variants and presentation | The hardest application reads at its real minimum size | [medium-and-variants.md](references/method/medium-and-variants.md) |
| 7. Review and handoff | Review every test, fix at its owning stage, prepare reusable files | Code checks have no unresolved failures; vision checks pass or are marked not judged | [review-checklist.md](references/method/review-checklist.md), [final-review-and-handoff.md](references/method/final-review-and-handoff.md) |

### Scale the flow

- **Quick composition question:** work stages 1, 3 and 4; state the intended hierarchy and name any visual convention supplied by the domain.
- **Critique of existing work:** start at stage 7, run T1–T12 in order and return to the stage named by each failed test.
- **Identity or campaign system:** run all seven stages. Test a base item, the most constrained application and the variants together.
- **After a fix:** rerun every affected code check, then the vision questions for that stage. A changed focal element can alter balance, spacing, typography and system consistency.
- **Small single-format piece:** combine research with concept and combine type with system, but keep the decisions and checks explicit.

## Execution

### Output medium

- Draw shapes, marks, diagrams and visualizations as SVG.
- Compose pages, slides and visual systems in HTML; embed SVG where needed.
- Use raster images for photographs and textures.
- Follow the project's and domain's required delivery format when it overrides this working medium. Keep project-specific components in project code.

### Render-and-check loop

1. Add render-kit markup to the HTML/SVG: mark artifact regions with data-rk-stage and the intended focal region with data-rk-focal. Declare the grid, occupied content (`data-vd-occupies`), type levels (`data-vd-type`) and intended balance on the stage using the attributes documented in [measurement.md](references/method/measurement.md).
2. Render and run render-kit checks with bin/rk check. Fix every failure and render again. A skipped or incomplete check is not a pass; record why it cannot apply.
3. Get stage-relative boxes from the same Chromium render with `node scripts/measure_boxes.mjs <artifact.html|svg> --render-kit <render-kit-folder> --out boxes.json` (repeat any non-default render options), then run `python3 scripts/checks.py <grid|balance|space|scale|focal> <out-dir>/render.png --boxes boxes.json`. Balance can run without boxes when the frame is the whole PNG. Each command prints JSON with the measure, threshold, status and source; thresholds are skill defaults where the course gives no number.
4. After code checks, prepare a render-kit review brief from the checklist questions. Give the rendered images and questions to a fresh-context reviewer who did not make the artifact and can see images. Verify the answers. A vision check without such a reviewer is reported as not judged.
5. Report measured, vision-judged, not-judged and skipped checks separately. Never turn a skipped or not-judged result into a pass.

**Code checks:** render-kit checks resource loading, console errors, font fallback, overflow, text collisions, contrast, colour-vision deficiency, data fidelity, accessibility, value and chroma where applicable. The visual-design measures cover grid alignment, visual-weight centre, occupied-box negative-space estimate, type-scale ratio and focal-area luminance-gradient energy.

**Vision checks:** message and motif recognition, figure-ground reading, optical balance, the function of negative space, movement, system coherence and whether a real-world application feels legible and appropriate. Give the reviewer the specific question from each test, not a generic “does it look good?”

## Gates (declared, inherited from core)

- **Grounding gate.** The substrate is the brief, supplied visual material, the course lessons in references/course and the rendered artifact. Keep course claims anchored and mark synthesis as derived. See [../core/references/grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract.** A plan names the decisions needed for its stages; a critique reports each failed test, what was seen, the return stage and one concrete change. State which checks were measured, judged, not judged or skipped. See [../core/references/wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach.** When a requested change would break the brief, domain convention, hierarchy or system, explain the consequence and cite the method anchor. See [../core/references/pushback-and-teach.md](../core/references/pushback-and-teach.md).
- **Approach declaration.** A single, small composition question can skip it. State the stages and reviewers for multi-piece systems, campaigns or work with several applications. (Core SKILL.md §7.)

## Anti-patterns

- Choosing a visual treatment before identifying the message, audience and use.
- Treating geometry or a grid as a substitute for a concept.
- Designing a positive mark without checking its ground and surrounding space.
- Leaving an element almost aligned or centred when the placement should read as deliberate.
- Making all elements equally prominent, or calling an unbalanced arrangement “dynamic” without an intentional path.
- Filling empty space with decoration, stock imagery or clichés that do not support the concept.
- Stretching type, pairing faces that are too similar, or using a display face for small running text.
- Assuming one logo lockup, format, text face or support will work at every size.
- Treating the course's proportional scales or compositional schemes as universal laws.
- Reporting code metrics as proof of meaning, balance or audience understanding.
- Calling an unavailable vision review a pass.
- Stating a course principle without its anchor or presenting a derived synthesis as the teacher's wording.
- Copying paid course material outside this private skill; see [NOTICE.md](NOTICE.md).

## Composition

- **Inherits:** core.
- **Works beside:** color-theory for colour decisions. Keep the artifact's form, hierarchy and colour decisions distinct when both are needed.
- **Domain rule:** project and audience conventions govern over course taste.

## References

- [references/method/brief-and-intent.md](references/method/brief-and-intent.md) — turn the brief into audience, message, constraints and an intended reading.
- [references/method/research-and-concept.md](references/method/research-and-concept.md) — gather non-derivative references and choose a conceptual register.
- [references/method/form-and-unity.md](references/method/form-and-unity.md) — build a visual vocabulary from shape, figure-ground and grouping.
- [references/method/composition-and-movement.md](references/method/composition-and-movement.md) — compose hierarchy, balance, space, focus and movement.
- [references/method/type-and-system.md](references/method/type-and-system.md) — set type and make a flexible, repeatable system.
- [references/method/medium-and-variants.md](references/method/medium-and-variants.md) — adapt the system to real supports and variants.
- [references/method/review-checklist.md](references/method/review-checklist.md) — numbered tests, pass conditions and return stages.
- [references/method/measurement.md](references/method/measurement.md) — course checks, tool-independent measures and defaults for T1–T12.
- [references/method/final-review-and-handoff.md](references/method/final-review-and-handoff.md) — run the review and make the work usable by someone else.
- [references/method/coverage.md](references/method/coverage.md) — lessons not cited by a method digest and why.
- [references/course/README.md](references/course/README.md) — source index for course 5642.
- [scripts/check_refs.py](scripts/check_refs.py) — resolve local references and verify course anchors.
