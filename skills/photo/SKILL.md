---
name: photo
description: "A course-distilled method for photographing and finishing portraits and social images: capture, RAW development, tone and colour correction, skin retouching, compositing, grading, batches and delivery. USE WHEN planning a portrait session, correcting or retouching a photo, matching a portrait set, preparing social crops, or reviewing edited images. color-theory owns color science; visual-design owns graphic composition and layout. Keywords: portrait photography, photo retouching, RAW, skin, dodge and burn, compositing, grading, batch editing, social images."
license: "Proprietary (private course-derived material, not for redistribution)"
---

# Photo

This skill produces edited portrait and social-image files with a clear record of scope, source files, review checks, and delivery settings. It combines the course methods for portrait sessions, phone photography, RAW and Photoshop editing with reusable photo grading and comparison scripts.

> Inherits the core kernel. See [../core/SKILL.md](../core/SKILL.md). Grounded: read core + color-theory + visual-design → reused their shared gates, kept color-science with color-theory, and handed graphic composition to visual-design. Owner decisions 2–7 and 11 set tool portability, code-first review, domain convention precedence, output medium, and photo-tool scope.

## When it fires — and when a sibling owns it

- **This skill:** planning a portrait session; photographing portrait, product, interior, or social images; developing RAW; correcting tone and color; retouching skin and features; compositing; matching a batch; exporting and reviewing photographs.
- **color-theory instead:** questions about color-science, palette relationships, color naming, contrast, or color-space conversions. Photo edits stay here; the sibling handles the broader color facts.
- **visual-design instead:** graphic composition, layout, typography, or story/post overlays. This skill supplies the photograph placed into that design.

> **Disambiguation by artifact:** photo means a captured or edited raster photograph and its delivery set. Color-theory produces color decisions and factual answers; visual-design produces a graphic structure or layout.

## Principles / anchoring rules

1. **Plan for the intended image.** Choose purpose, space, light, equipment, and output together. (669 · U1 · L03 · 00:00–00:37; 669 · U2 · L05 · 00:00–01:39; 669 · U2 · L05 · 01:39–03:59; 669 · U2 · L05 · 05:58–07:18)
2. **Build comfort with the portrait subject.** Listen, notice personal gestures, and let the person decide how much to share. (669 · U2 · L04 · 00:00–01:36; 669 · U2 · L04 · 01:36–03:24; 669 · U2 · L04 · 03:24–06:21; 669 · U2 · L04 · 06:21–08:07)
3. **Judge exposure from the scene, not a histogram shape alone.** A bright, dark, or small subject can produce a misleading full-frame histogram; inspect its region and protect useful detail. (1343 · U13 · L16 · 01:55–02:59; 1343 · U13 · L16 · 02:59–03:57; 1343 · U13 · L16 · 05:16–06:44; 1343 · U13 · L16 · 06:44–08:10)
4. **Correct the base before detailed retouch.** Stabilize tone before judging a color cast; keep creative color separate from neutral correction. (1343 · U14 · L17 · 00:00–01:05; 1343 · U14 · L17 · 02:33–03:55; 1343 · U14 · L17 · 03:55–04:57)
5. **Make local edits reversible and specific.** Use selections, masks, and separate adjustments to limit where changes occur. (1343 · U19 · L23 · 03:10–05:54; 1343 · U19 · L23 · 05:54–09:29; 1343 · U20 · L27 · 00:00–02:27; 1343 · U20 · L27 · 02:27–04:57; 1343 · U20 · L27 · 04:57–06:38)
6. **Let automation repeat a starting point, not approve the result.** Test a grading action and review each image; copy edits only between comparable shooting conditions. (1343 · U53 · L80 · 10:29–13:58; 227 · U4 · L12 · 18:15–20:06)
7. **Inspect the delivered image at its real size.** Compare the final crop, profile, dimensions, and visible edit regions with the delivery brief. (1343 · U54 · L81 · 01:19–04:29; 1343 · U54 · L81 · 04:29–07:57; field rules FR-06, FR-08)

## The flow

| Stage | Decide | Check | Reference |
|---|---|---|---|
| 1. Brief and session | Audience, image purpose, subject, setting, output, and permitted edits | Each input and requested change has an exact map; T1 | [brief-and-session.md](references/method/brief-and-session.md) |
| 2. Capture and compose | Light, framing, format, focus, exposure, and image coverage | Intended subject and important detail are usable; T2 | [capture-and-compose.md](references/method/capture-and-compose.md) |
| 3. Select keepers | Which frames add a distinct moment or viewpoint | Requested subjects are covered without unnecessary duplicates; T3 | [select-keepers.md](references/method/select-keepers.md) |
| 4. RAW and base correction | Geometry, tonal range, white balance, and local RAW edits | Crop, detail, tone, and color checks pass; T4–T6 | [raw-and-base-correction.md](references/method/raw-and-base-correction.md) |
| 5. Retouch and composite | Which specific local corrections or composites fit the approved scope | Change containment, texture, identity, and edges pass; T7–T9 | [retouch-and-composite.md](references/method/retouch-and-composite.md) |
| 6. Grade and batch | Shared look and which frames have matched conditions | Sample action tested; each image inspected; T10 | [grade-and-batch.md](references/method/grade-and-batch.md) |
| 7. Deliver and review | Approved files, crop, profile, dimensions, and ordering | Required outputs and gallery pass; T11–T12 | [deliver-and-review.md](references/method/deliver-and-review.md) |

### Scale the flow

- **One small edit:** map the image and edit scope, correct the base if needed, make the local change, then run T1 and T4–T9 as applicable.
- **Critique an existing photo:** start with T1–T12, then return to the earliest failed stage and name one concrete change.
- **Portrait session or social set:** use all stages. Keep an input map and edit ledger; test a batch operation on a sample, then inspect every image and the gallery.
- **After a fix:** rerun affected tests from [review-checklist.md](references/method/review-checklist.md); a retouch can change color, crop, or gallery fit.

## Execution

### Output medium

The photograph is a raster deliverable: PNG, JPEG, or TIFF as required by the brief. Preserve the original and an editable working file when available. Build multi-image comparison sheets or review reports as HTML/SVG and render them with the owner's render-kit.

### Make and verify

1. Map source filenames in the user's supplied order and label each as target, reference, or support. For a batch, copy [session-ledger.md](references/templates/session-ledger.md) into the task workspace. Follow [field-rules.md](references/field-rules.md).
2. Keep the requested edit scope explicit. Use a supported local or generative editing capability for the task; do not claim that a prompt or generated output preserved unedited pixels.
3. Run exact checks first: use [TOOLS.md](TOOLS.md) for scripts/grade.py measure, scripts/grade.py compare, and scripts/roundtrip.py verify; check output dimensions, profiles, file counts, and masks. These tools expose their readings and limitations.
4. For a comparison or contact sheet, use HTML/SVG with data-rk-stage and run the render-kit check. Fix code failures, render again, then prepare the specific visual questions from [measurement.md](references/method/measurement.md) for a fresh-context reviewer who can see the images.
5. Vision checks cover intent, likeness, expression, skin texture, plausible edits, composite seams, and gallery rhythm. Code checks cover measurable pixels, containment tolerances, crop/dimensions, profile, file presence, and render-kit resource/overflow issues. If a fresh visual review is unavailable, report it as **not judged**.
6. Report which checks were measured, vision-judged, not judged, or skipped, with the actual readings and reasons. Cite course anchors in the critique or handoff.

### Course disagreements and application corrections

- Courses place selection at different points: course 227 marks favorites before editing; course 669 compares exported candidates and revisits the shortlist later. Use an early technical shortlist followed by a final comparison after base edits when the set warrants it. (227 · U4 · L11 · 00:08–01:38; 669 · U4 · L11 · 08:22–12:37; 669 · U4 · L11 · 12:37–15:44; derived)
- Course 669 copies a scene base and adapts each image; course 227 copies edits only when light/background/conditions match; course 1343 tests an action before batch processing. Apply shared settings only across matched conditions and inspect every result. (669 · U4 · L10 · 03:49–05:57; 227 · U4 · L12 · 18:15–20:06; 1343 · U53 · L80 · 10:29–13:58; derived)
- Course 227's Snapseed lesson labels a Story crop 16:9, while its Story lesson says vertical 9:16. Follow the destination's current specification; 9:16 applies when the requested deliverable is explicitly a vertical Story. (227 · U4 · L11 · 14:31–16:48; 227 · U5 · L15 · 02:07–03:20)
- Course 1343 offers skin-tone percentage examples but says individual skin varies. Do not turn those values into universal targets; use the project standard or visual comparison. (1343 · U48 · L71 · 02:10–04:05; 1343 · U48 · L71 · 06:31–08:12; 1343 · U48 · L71 · 08:12–10:59)
- Domain and delivery conventions override course taste (owner decision 6). For color-science facts and broader color decisions, open [color-theory](../color-theory/SKILL.md); photo grading metrics are estimates and tool defaults, not a photography science library.

## Gates (declared, inherited from core)

- **Grounding gate:** the brief, supplied photographs, course reading copies in references/course-*, and stated delivery requirements. Cite the course anchor for each method claim. See [grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract:** selected photo files, source/output map, required profile and dimensions, review results, and any limits. See [output-contract.md](../core/references/output-contract.md) and [wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach:** explain when an edit would alter identity, exceed the brief, or create a false claim about detail/fidelity; give a safer option and reason. See [pushback-and-teach.md](../core/references/pushback-and-teach.md).
- **Approach declaration:** for multiple images, revisions, or composite work, state the stages, editor/capabilities, and review questions before running the batch. A simple one-image correction can skip this declaration.

## Anti-patterns

- Applying a grade or action to images with different lighting without per-image review.
- Using the full-image histogram as a universal exposure target.
- Smoothing away pores, moles, natural variation, expression, or identity without a specific request.
- Reshaping faces or bodies substantially without clear scope and approval.
- Treating an automated fill, mask, comparison metric, or generated image as proof of photographic fidelity.
- Overwriting originals, misassigning numbered inputs, or delivering rejected variants.
- Calling a skipped or unavailable visual review a pass.
- Presenting a course example, tool default, or derived workflow as a universal photographic standard.

## Composition

- **Inherits:** core.
- **Works beside:** color-theory for color knowledge and visual-design for graphic framing, layout, and typography.
- **Domain rule:** the brief and current delivery specification govern over course examples or aesthetic preferences.

## References

- [references/method/claim-audit.md](references/method/claim-audit.md) — the independent claim audit of every course citation (evidence per scope in `audit/`).
- [references/method/brief-and-session.md](references/method/brief-and-session.md) — define audience, session direction, output, and permitted edits.
- [references/method/capture-and-compose.md](references/method/capture-and-compose.md) — use light, framing, and coverage to make the photograph.
- [references/method/select-keepers.md](references/method/select-keepers.md) — select a working set and compare finalists.
- [references/method/raw-and-base-correction.md](references/method/raw-and-base-correction.md) — establish reversible tone, geometry, and color corrections.
- [references/method/retouch-and-composite.md](references/method/retouch-and-composite.md) — plan local retouching and blend images with masks.
- [references/method/grade-and-batch.md](references/method/grade-and-batch.md) — match and inspect a repeatable grade.
- [references/method/deliver-and-review.md](references/method/deliver-and-review.md) — prepare delivery files and social previews.
- [references/method/review-checklist.md](references/method/review-checklist.md) — twelve tests and return stages.
- [references/method/measurement.md](references/method/measurement.md) — course checks, tool-independent measures, and threshold origins.
- [references/method/coverage.md](references/method/coverage.md) — lessons not cited by a method digest and why.
- [references/field-rules.md](references/field-rules.md) — input mapping, conservative edits, inspections, revisions, and delivery rules.
- [references/templates/session-ledger.md](references/templates/session-ledger.md) — reusable input, edit, review, and delivery ledger.
- [TOOLS.md](TOOLS.md) — grading, comparison, guarded edit verification, outputs, and limits.
- [scripts/check_refs.py](scripts/check_refs.py) — local-link and lesson-anchor validation.
- [references/course-669/README.md](references/course-669/README.md), [references/course-227/README.md](references/course-227/README.md), [references/course-1343/README.md](references/course-1343/README.md) — source lesson indexes and exclusions.
