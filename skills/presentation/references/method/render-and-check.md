# Render and check

## Check every requested output

Mark HTML/SVG artifact regions with `data-rk-stage` and any intended focal area with `data-rk-focal`; run render-kit on each slide artifact and on the PDF when one is delivered. The kit reports code checks and reviewer questions separately. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop” and “Markup the checks read”.

Fix every `fail`, then read each `skipped` and `incomplete` item before accepting the result. A skipped or incomplete item is not a pass; when a reviewer cannot see the render, leave the vision item not-judged. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”; [book:playwright-docs], “Accessibility testing”.

Ask an independent reviewer concrete yes-means-pass questions from [review-checklist.md](../../review-checklist.md); render-kit can prepare and verify its review answers, but does not itself make vision judgments. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”.

For videos, use scene-engine's validation and selected-frame check, then decode or inspect the actual output frames. An encoder success code establishes that encoding ran, not that the delivered frames are correct. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Check loop”; (field rule (screencast)).

For PPTX, inspect a rendered PDF or image set for layout issues as well as reopening the native file structurally; a LibreOffice render is a useful automated view but is not proof of PowerPoint rendering. [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; (field rule (pptx)).

## Return defects to the stage that owns them

Return incorrect evidence to brief/story or data-slides; return hierarchy, typography, and palette issues to their design owners; return output conversion issues to output-by-medium; rerun the affected checks afterward. [visual-design/SKILL.md](../../../visual-design/SKILL.md#the-flow-at-a-glance); [information-design/SKILL.md](../../../information-design/SKILL.md#the-flow-at-a-glance). (derived: each failed check should name a repair stage and a verification path.)

## Report

Report the files rendered, code checks and their outcomes, vision questions reviewed, unresolved `fail` items, skipped or incomplete items, and any owner-check result. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “The loop”; [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.
