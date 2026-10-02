# Output by medium

Choose a final format from the audience's use and editing needs. The research groups a live HTML deck, PDF handout, and editable PowerPoint in one use case, and treats the MP4 app demo and narrated explainer as two more use cases with their own constraints. [src:output-pipelines/report.md], “Use case 1”; [src:output-pipelines/report.md], “Use case 2”; [src:output-pipelines/report.md], “Use case 3”. (derived: choose a path to match the audience’s use, timing, and reuse.)

## HTML slide deck

Author one 1920×1080 HTML/SVG scene per slide. Select a static HTML shell for a one-off deck or a presenter shell when speaker notes, fragments, a second screen, or presentation controls are required; research sources disagree about a universal shell default, while agreeing on fixed-size scenes. [src:synthesis.md], “Contradictions”; [src:output-pipelines/report.md], “F7. HTML presentation frameworks”. (derived: choose the shell from the required live-presenting features instead of hiding the unresolved source disagreement.)

Use semantic, media-independent, style-independent markup rather than presentational markup. [book:whatwg-html], “Conformance requirements for authors”. Keep source text, headings, and reading order in the document, and use the shell's render-kit stage markers. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “Markup the checks read”. (derived from the source’s accessibility and maintenance rationale for semantic, media-independent markup.)

## PDF handout

Print fixed-size slide pages with Chromium using a zero-margin 1920×1080 page rule, `preferCSSPageSize`, `printBackground`, tagged output, and outline where the export interface supports them. Use static font files for every weight used; variable fonts and synthetic bold were measured as Type 3 fonts, and Chromium does not claim PDF/UA or PDF/A conformance. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”; [src:output-pipelines/experiments/README.md], “05-html-pdf”.

Avoid blur effects when vector output matters: the measured Chromium print path rasterizes box-shadow blur and CSS blur filters, while basic SVG and gradients remained vector in the tested file. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”.

## Editable PowerPoint

Drive scene-engine's native PPTX export and verification path from its storyboard contract; do not substitute a screenshot converter when the brief requires editable text, shapes, or charts. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Commands”; [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

Run these from the scene-engine repository, passing the presentation project as root so inputs, assets, and outputs stay with that project. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Commands”.

```sh
npm run scene-engine -- validate <storyboard.json> --root <project-root>
npm run scene-engine -- export-pptx <storyboard.json> --out <project-root>/out/deck.pptx --verify
```

Write an export report naming which items became native text, shapes, charts, SVG pictures, or raster pictures, and why any fallback was used. The research maps a one-to-one subset and documents picture fallbacks for complex effects and unsupported geometry. [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

## MP4 explainer

Hand the approved message, evidence, narration/caption needs, and motion storyboard to motion; use scene-engine to validate, render, and check selected frames. [motion/SKILL.md](../../../motion/SKILL.md#execution); [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Commands”.

```sh
npm run scene-engine -- validate <storyboard.json> --root <project-root>
npm run scene-engine -- render <storyboard.json> --out <project-root>/out/movie.mp4 --renderer auto --captions both
npm run scene-engine -- check <storyboard.json> --at 500,1000 --rk ../render-kit/bin/rk
```

Use captions and an accessible alternative when the audience or delivery requires them. WCAG has a prerecorded-caption success criterion, and the output study specifies WebVTT alongside video for PowerPoint use. [book:wcag-22], “Success Criterion 1.2.2 Captions (Prerecorded)”; [src:output-pipelines/report.md], “F4. Audio: narration, timestamps, captions, music, loudness”.

Treat the requested encoder profile and output dimensions as a delivery contract, not an aesthetic decision; verify the file after render. [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”; [src:output-pipelines/experiments/README.md], “01-mp4-for-powerpoint”.

## Recorded app demo

When source access and a runnable app exist, capture the real app through scene-engine's capture path; keep app changes in the app's own implementation workflow. The research's reproducibility test used a stand-in app, so it does not establish coverage for every real application or rendering surface. [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “Commands”; [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”; [src:output-pipelines/report.md], “Risks and unknowns”.

```sh
npm run scene-engine -- capture <storyboard.json> --scene <scene-id> --layer <layer-id> --out-dir <project-root>/out/capture
```

Use fixtures or approved demo data, replace sensitive values, and distinguish a concept mockup from a live product wherever the footage could imply a real capability. (field rule (screencast)); [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”.

## Return when

If the chosen medium cannot meet an editability or playback requirement, state the limitation and offer a medium that can. The research did not play its generated PPTX media in PowerPoint, and the scene-engine guide distinguishes a PowerPoint owner-check from a passing automated check. [src:output-pipelines/report.md], “Risks and unknowns”; [scene-engine AGENTS.md](../../../../scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”. (derived: do not upgrade structural evidence into a compatibility claim.)
