# Review checklist: twelve tests for portraits and social photographs

Run exact file and pixel checks first. Then inspect the rendered photograph or comparison sheet at full-frame and close-up scales, preferably with a fresh-context vision reviewer. Each failure names where to return.

| # | Test | Pass condition | Return to |
|---|---|---|---|
| T1 | Brief and edit scope | Each image maps to a named subject, requested change, protected details, and output. Any material ambiguity is resolved before editing. | Stage 1: brief and session |
| T2 | Capture quality | Intended subject and focus are usable; exposure preserves important detail; the background and light support the stated image. | Stage 2: capture and compose |
| T3 | Selection and coverage | Every chosen frame adds a distinct expression, gesture, viewpoint, or story role; requested subjects and moments are represented. | Stage 3: select keepers |
| T4 | Crop and geometry | Horizon, verticals, perspective, aspect ratio, and framing meet the brief; no required content is clipped. | Stage 4: RAW and base correction |
| T5 | Tone and detail | Important highlight/shadow detail is visible; clipping is limited to areas the brief or scene intends to lose. | Stage 4: RAW and base correction |
| T6 | Color and skin | White balance and skin color suit the subject and intended light; the grade does not create unwanted casts or color shifts. | Stage 4: RAW and base correction |
| T7 | Local edit containment | The roundtrip verifier passes both its protected-area check and its separate outside-mask transition-band check. The transition band has reported ΔE00 statistics and an over-limit bounding box; unchecked outside-mask width is 0 px. (derived: dogfood 2026-10-02, F1) | Stage 5: retouch and composite |
| T8 | Skin texture and identity | Skin retains plausible local texture and natural variation; identity, expression, moles, and defining features remain intact unless a requested edit says otherwise. | Stage 5: retouch and composite |
| T9 | Feature and composite integrity | Approved feature changes match scope; edges, anatomy, reflections, lighting, perspective, and repeated texture show no distracting artifacts. | Stage 5: retouch and composite |
| T10 | Grade and batch consistency | Every frame was inspected individually; images from matched conditions share the intended look without erasing useful scene differences. | Stage 6: grade and batch |
| T11 | File delivery | Required files, crops, formats, dimensions, and color profiles match the receiving brief; originals and working files are accounted for. | Stage 7: deliver and review |
| T12 | Gallery and social preview | The complete approved set is present; key content survives each destination crop; ordering has no accidental omissions or unwanted near-duplicate run. | Stage 7: deliver and review |

After a change, rerun affected tests. A geometry or crop change affects T3, T4, and T12; a tone or grade change affects T5, T6, and T10; a retouch or composite change affects T7–T9 and may affect T10–T12.

Thresholds and course procedures are in [measurement.md](measurement.md). Report each check as **measured**, **vision-judged**, **not judged**, or **skipped**, with the actual reading or reason.

For a hand-built photo review sheet, start from [review-sheet.html](../templates/review-sheet.html). Put `data-rk-stage="comparison"` on a full-width wrapper, keep the page within that stage, and do not declare a focal area; render-kit `value` n/a is expected for this photo grid. (derived: dogfood 2026-10-02, F10)
