# Render and check

## Check every requested output

Mark HTML/SVG artifact regions with `data-rk-stage` and any intended focal area with `data-rk-focal`; run render-kit on each slide artifact and on the PDF when one is delivered. The kit reports code checks and reviewer questions separately. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop” and “Markup the checks read”.

For multi-slide work, check one HTML file per slide with one stage and one focal in each file using `rk check --root <project-root>`. Separately check the combined screen-grid deck and its print PDF. Keep each captured grid dimension below 16,384 px; the print view must stack the fixed-size slides as pages. Deliver the combined deck check's `render.pdf` as the handout. (derived: dogfood 2026-10-02, F1)

Fix every `fail`, then read each `skipped` and `incomplete` item before accepting the result. A skipped or incomplete item is not a pass; when a reviewer cannot see the render, leave the vision item not-judged. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”; [book:playwright-docs], “Accessibility testing”.

Ask an independent reviewer concrete yes-means-pass questions from [review-checklist.md](review-checklist.md); render-kit can prepare and verify its review answers, but does not itself make vision judgments. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”.

For videos, use scene-engine's validation and selected-frame check, then decode or inspect the actual output frames. An encoder success code establishes that encoding ran, not that the delivered frames are correct. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Check loop”; (field rule (screencast)).

For every app demo, review representative frames decoded from the final MP4 until scene-engine's check stages include the captured app frames. Its current app-layer check may pass on a stage containing only the demo label and captions. Use motion's `measure_storyboard.py` or cut frames with FFmpeg and review them through `rk brief`; scene-engine's app-layer result alone is not evidence that the app state appeared. (derived: dogfood 2026-10-02, F2)

For PPTX, inspect a rendered PDF or image set for layout issues as well as reopening the native file structurally; a LibreOffice render is a useful automated view but is not proof of PowerPoint rendering. [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; (field rule (pptx)).

Mark the element that carries the slide's intended point as focal: use an illustration only when its image carries that point, a screenshot when its interface state or evidence is the point, and a headline/callout for dense-text slides when that is the first takeaway. Do not mark a decorative image or an entire oversized text panel just to satisfy the check. If the required focal genuinely occupies over half the frame, `value` may return `incomplete`; leave it marked incomplete and obtain the named vision review rather than reporting a pass. If the owner approves a different minimum edge-share threshold, rerun with `--threshold value.min_edge_share=<number>` and record the exact threshold, rationale, owner, affected slides, and both default and override results in the review record. (derived: dogfood 2026-10-02, F7)

## Return defects to the stage that owns them

Return incorrect evidence to brief/story or data-slides; return hierarchy, typography, and palette issues to their design owners; return output conversion issues to output-by-medium; rerun the affected checks afterward. [visual-design/SKILL.md](../../../visual-design/SKILL.md#the-flow-at-a-glance); [information-design/SKILL.md](../../../information-design/SKILL.md#the-flow-at-a-glance). (derived: each failed check should name a repair stage and a verification path.)

## Report

Report the files rendered, code checks and their outcomes, vision questions reviewed, unresolved `fail` items, skipped or incomplete items, and any owner-check result. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”; [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.
