# Delivery and editability

## Report what the recipient can change

For a native PowerPoint deliverable, reopen the `.pptx` with python-pptx and inventory non-empty text frames, editable shape objects, chart objects, tables, pictures, and any exported fallbacks. A chart built from data can carry its workbook; a picture of a chart cannot provide that data editing path. [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

List editability by slide or object group in the export report. Do not promise that all elements are native if effects, masks, unsupported text treatments, or complex paths fell back to a picture. [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

For a PDF, record page count, dimensions, fonts, and tagged status when available; do not describe Chromium tagging as PDF/UA certification. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”; [src:output-pipelines/experiments/README.md], “05-html-pdf”.

For an MP4, report verified streams, dimensions, duration, frame rate, caption sidecar, and whether its playback in the target presentation app was manually checked. The measured H.264/AAC recipe in the source study was not played inside PowerPoint. [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”; [src:output-pipelines/report.md], “Risks and unknowns”.

For a demo, label mockups or synthetic data when viewers could mistake them for a live system, and note any sensitive-value substitution that affects what the footage represents. (field rule (screencast)); [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”.

## Scene-engine owner checks

Scene-engine marks AT37 as a PowerPoint release-owner check; `scene-engine selftest --case AT37` reports `owner-check`, not a compatibility pass. The owner procedure opens `out/tests/at33-morph.pptx` and `out/tests/at35.pptx` in current PowerPoint on Windows and Mac, records OS and build and any repair prompt, edits a chart value and verifies it survives save/reopen, checks AT33 Morph and AT32 entrance animation, and plays the AT35 embedded video. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.

The scene-engine guide also names AT33 and AT36 as Keynote import/PDF smoke checks; when Apple Events times out or authorization is absent, the nested `owner-check` remains an owner check even if the enclosing test passes. After the owner grants Automation permission, rerun `npm run selftest -- --case AT36`. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.

Only report PowerPoint or Keynote compatibility after the named owner check has been performed on the target application and build. If it has not, give the structural, PDF, or other available evidence and say the application check remains open. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”; [src:output-pipelines/report.md], “Risks and unknowns”. (derived: compatibility depends on opening and using the exported artifact in the named application.)
