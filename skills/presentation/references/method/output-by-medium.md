# Output by medium

Choose a final format from the audience's use and editing needs. The research groups a live HTML deck, PDF handout, and editable PowerPoint in one use case, and treats the MP4 app demo and narrated explainer as two more use cases with their own constraints. [src:output-pipelines/report.md], “Use case 1”; [src:output-pipelines/report.md], “Use case 2”; [src:output-pipelines/report.md], “Use case 3”. (derived: choose a path to match the audience’s use, timing, and reuse.)

## HTML slide deck

Author one 1920×1080 HTML/SVG scene per slide. Select a static HTML shell for a one-off deck or a presenter shell when speaker notes, fragments, a second screen, or presentation controls are required; research sources disagree about a universal shell default, while agreeing on fixed-size scenes. [src:synthesis.md], “Contradictions”; [src:output-pipelines/report.md], “F7. HTML presentation frameworks”. (derived: choose the shell from the required live-presenting features instead of hiding the unresolved source disagreement.)

Use semantic, media-independent, style-independent markup rather than presentational markup. [book:whatwg-html], “Conformance requirements for authors”. Keep source text, headings, and reading order in the document, and use the shell's render-kit stage markers. [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “Markup the checks read”. (derived from the source’s accessibility and maintenance rationale for semantic, media-independent markup.)

For a multi-slide deck, keep one HTML check file per slide, each with exactly one `data-rk-stage` and its own `data-rk-focal`. Run `rk check --root <project-root>` over that folder; `templates/deck-shell.html` is a one-slide starter to copy once per slide. Also build a combined deck file for browsing: use a screen grid whose captured width and height both remain below Chromium's 16,384 px limit, then use print CSS to stack one fixed-size slide per PDF page. The dogfood's 27 slides used three columns and `--width 5760` (5,760 × 9,720 px). Run `rk check <project-root>/deck.html --pdf --media print --width 5760`; deliver its `render.pdf` as the handout. If the deck grid would exceed the capture limit, divide the screen review into smaller grids while keeping the print document as one page per slide. (derived: dogfood 2026-10-02, F1)

## PDF handout

Print fixed-size slide pages with Chromium using a zero-margin 1920×1080 page rule, `preferCSSPageSize`, `printBackground`, tagged output, and outline where the export interface supports them. Use static font files for every weight used; a variable font and synthetic bold were measured as Type 3 fonts. Chromium does not claim PDF/UA or PDF/A conformance. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”; [src:output-pipelines/experiments/README.md], “05-html-pdf”.

Replace colour emoji with a monochrome SVG icon or a raster emoji image with meaningful alternative text, then recheck PDF fonts. (derived: dogfood 2026-10-02, F8)

Avoid blur effects when vector output matters: the measured Chromium print path rasterizes box-shadow blur and CSS blur filters, while basic SVG and gradients remained vector in the tested file. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”.

## Editable PowerPoint

Drive scene-engine's native PPTX export and verification path from its storyboard contract; do not substitute a screenshot converter when the brief requires editable text, shapes, or charts. [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “Commands”; [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

Run scene-engine with the presentation project as the current working directory. In the dogfood, invoking the CLI entry point directly from that folder kept export paths inside the CLI's working-directory guard; running the same command from the scene-engine checkout with absolute project output paths failed. Use this form from the presentation project folder: (derived: dogfood 2026-10-02, F4)

```sh
PROJECT=/path/to/presentation-project
cd "$PROJECT"
node ~/.agent-workflow/tools/scene-engine/src/cli.mjs validate deck.storyboard.json --root .
node ~/.agent-workflow/tools/scene-engine/src/cli.mjs export-pptx deck.storyboard.json --root . --out out/deck.pptx --verify
```

Keep `--out`, `--out-dir`, and report paths inside the project folder for this command form. Apply the same `node ~/.agent-workflow/tools/scene-engine/src/cli.mjs <command> ... --root .` form to `capture` and `check`. [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “Commands”.

Write an export report naming which items became native text, shapes, charts, SVG pictures, or raster pictures, and why any fallback was used. The research maps a one-to-one subset and documents picture fallbacks for complex effects and unsupported geometry. [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

## MP4 explainer

Hand the approved message, evidence, narration/caption needs, and motion storyboard to motion; use scene-engine to validate, render, and check selected frames. [motion/SKILL.md](../../../motion/SKILL.md#execution); [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “Commands”.

```sh
npm run scene-engine -- validate <storyboard.json> --root <project-root>
npm run scene-engine -- render <storyboard.json> --out <project-root>/out/movie.mp4 --renderer auto --captions both
npm run scene-engine -- check <storyboard.json> --at 500,1000 --rk ../tools/render-kit/bin/rk
```

Use captions and an accessible alternative when the audience or delivery requires them. WCAG has a prerecorded-caption success criterion, and the output study specifies WebVTT alongside video for PowerPoint use. [book:wcag-22], “Success Criterion 1.2.2 Captions (Prerecorded)”; [src:output-pipelines/report.md], “F4. Audio: narration, timestamps, captions, music, loudness”.

Treat the requested encoder profile and output dimensions as a delivery contract, not an aesthetic decision; verify the file after render. [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”; [src:output-pipelines/experiments/README.md], “01-mp4-for-powerpoint”.

## Recorded app demo

When source access and a runnable app exist, capture the real app through scene-engine's capture path; keep app changes in the app's own implementation workflow. The research's reproducibility test used a stand-in app, so it does not establish coverage for every real application or rendering surface. [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “Commands”; [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”; [src:output-pipelines/report.md], “Risks and unknowns”.

```sh
npm run scene-engine -- capture <storyboard.json> --scene <scene-id> --layer <layer-id> --out-dir <project-root>/out/capture
```

Use fixtures or approved demo data, replace sensitive values, and distinguish a concept mockup from a live product wherever the footage could imply a real capability. (field rule (screencast)); [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access”.

Plan empty, loading, and error states explicitly. For empty, serve a valid empty response and drive the app's normal filter or route until its empty state appears. For loading, use a repeatable delayed response or controlled local server and capture while the real loading indicator is visible. For error, make the app's real request fail or return the documented error response, then capture its native error and recovery controls. Do not paint a fake state over the app. The dogfood-tested scene-engine fixture path only intercepted cross-origin requests; same-origin API calls reached the app server, and capture had no `selectOption` step. For those cases use buttons/keyboard navigation or an isolated local server/test copy, and record the limitation and fixture used. (derived: dogfood 2026-10-02, F5)

Until scene-engine composites captured app frames into its check stages, a passing `scene-engine check` does not verify app content. For every app demo, decode and review frames from the final MP4: compare them with capture/storyboard expectations using motion's `measure_storyboard.py`, or cut representative frames with FFmpeg and pass the contact sheet to `rk brief`. Include the actual empty/loading/error or success states that the demo claims to show. (derived: dogfood 2026-10-02, F2)

For a self-serve app demo, captions are required; narration is optional. A local macOS route is `say -o out/narration.aiff "..."` followed by `ffmpeg -i out/narration.aiff out/narration.wav`, then align/mix the WAV to storyboard cue times. Ask the project owner to listen to the final MP4 at normal playback speed and record intelligibility, pronunciation, pace, level, and caption/audio alignment; an image-only review cannot judge narration. (derived: dogfood 2026-10-02, F6)

## Return when

If the chosen medium cannot meet an editability or playback requirement, state the limitation and offer a medium that can. The research did not play its generated PPTX media in PowerPoint, and the scene-engine guide distinguishes a PowerPoint owner-check from a passing automated check. [src:output-pipelines/report.md], “Risks and unknowns”; [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”. (derived: do not upgrade structural evidence into a compatibility claim.)
