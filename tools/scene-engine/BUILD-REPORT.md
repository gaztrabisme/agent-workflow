# scene-engine build report

## Motion dogfood repair (2026-10-02)

This run addresses motion dogfood findings F2, F3, F4, F6, F7, F8 and F14. The earlier 38-test baseline is historical and predates this repair; current status is recorded in the final run section below.

### Required red baseline before production changes

Command on the unchanged renderer after adding the MP4 comparison tests:

```sh
export PATH=/Users/GaryT/miniconda3/bin:$PATH
export HYPERFRAMES_NO_TELEMETRY=1
node --test --test-name-pattern='second-scene tracks|distinct tracks|one-scene burn-in' tests/acceptance.test.mjs
```

The command exited 1 with three intended regression failures. It rendered each short fixture using both `fallback` and `hyperframes`, cut RGB frames from the MP4 with FFmpeg, and compared them against the `generateStaticHtml` frames used by `check`. The comparator uses full-frame mean absolute RGB difference ≤ 8 and the stated layer/caption regions use the same ≤ 8 tolerance.

| Finding | Unchanged renderer evidence |
|---|---|
| F2 | At 1,500 ms in the second scene, MP4-to-check MAD was 15.48 (fallback) and 15.47 (HyperFrames), exceeding 8. |
| F3 | At 450 ms and 1,350 ms, the tracked-layer region MAD was 42.34 / 41.38 (fallback) and 42.37 / 41.40 (HyperFrames), exceeding 8. |
| F7 | The caption-band MAD was 19.10 / 19.31 (fallback) and 19.10 / 19.36 (HyperFrames) at active cues; at 1,350 ms the full-frame MAD was 15.63 / 15.84. |

The F4 check fixture also asserts the model-frame counter value, structured bullet text and SVG path. Separate assertions require the chart build/data-state and shape-mask fields to return the stable `FEATURE_UNSUPPORTED` validation code. F6, F8 and F14 have focused acceptance checks and the copied 57.5-second dogfood fixture.

After strengthening F4 to compare visible feature regions in the MP4 before the model assertions, the unchanged production sources were restored temporarily and the F4 case was run with the fallback renderer. It exited 1 as expected: at 300 ms, the video-entrance region MAD was 119.11, exceeding 8. With the repair restored, F4 was observed passing on fallback and HyperFrames. The later coordinator rerun showed that the check-frame screenshot was not paint-synchronized for video; that earlier pass did not establish a stable comparison for the video region. See the correction and evidence under Coordinator rerun below.

### Repair scope and dogfood renderer decision

F1 explains the test gap: `check` samples the storyboard model, so it can pass while the encoded MP4 has different motion. The new regression helper renders each available renderer, cuts RGB frames from the MP4 with FFmpeg at the authored check times, and compares them with the same `generateStaticHtml` model frames used by `check`. The full-frame mean absolute RGB tolerance is 8; moving-layer and caption regions also use 8.

Implemented: scene start is subtracted once when seeking later scenes; tracks are sampled together per layer with per-segment easing and end-value hold; counters, structured bullets, path/line shapes, trims/dashes and video entrances render; cue visibility is scene-local, caption duplication is omitted from check frames, and explicit caption line lint runs during validation. Chart `build`, `dataStates` and shape masks are intentionally rejected by storyboard validation with `FEATURE_UNSUPPORTED` in this release. The main sample now uses base chart data.

For F6, the report evidence records a 57.5-second, 1,725-frame, 95-layer single scene. A 3-second slice of the same storyboard completed in 5.6 seconds, while the full HyperFrames run still had captured no frames when its 580-second timeout elapsed. The evidence points to HyperFrames' long single-scene capture path rather than only the CLI's former 30-second timeout. The engine now selects fallback for auto-rendered single scenes at 1,200 frames or more and emits `HYPERFRAMES_LONG_SINGLE_SCENE`. This prevents the known stall for the requested 1,725-frame fixture; HyperFrames' underlying long-scene behavior remains unresolved. Default timeout scales to frame count, renderer progress is sent to stderr, Inter is embedded locally for the supported Arial/Inter aliases, and other HyperFrames font requests fail closed as `FONT_UNPINNED`.

F8 now resolves HyperFrames and GSAP from the engine install directory and permits render `--out` and `--poster` paths outside the repository. F14 now unions explicit `check --at` times with each scene's start/mid/end samples.

## Previous baseline (before the motion repair)

The earlier suite had 38 pass, 0 fail, and one AT37 owner-check skip. This is historical; the current `npm test` result is recorded in the final run section below. AT33 and AT36 previously reported the Keynote import/PDF portion as a nested owner check because the 10-second Apple Events probe timed out. Microsoft PowerPoint remains the separate AT37 release-owner check.

## Previous acceptance test results

`SPEC.md` defines AT01–AT39. The MP4 comparison and motion regression cases are additional acceptance gates because the prior IDs did not inspect encoded video pixels.

| Test | Acceptance test | Result |
|---|---|---|
| AT01 | Validate a storyboard with text, image, shape, and chart layers | PASS (round 1) |
| AT02 | Reject duplicate layer IDs and assets that escape the project root | PASS (round 1) |
| AT03 | Sample linear, ease-in-out, and cubic-Bezier keyframes | PASS (round 1) |
| AT04 | Render an explicit 300 ms scene opacity overlap | PASS (round 1) |
| AT05 | Repeat non-monotonic seeks and compare deterministic frames | PASS (round 1) |
| AT06 | Reject a registered animation adapter that cannot seek backward | PASS — high/zero/high/zero adapter probe reports `UNSEEKABLE`, adapter, layer and frame |
| AT07 | Render with pinned HyperFrames, telemetry disabled, and normalized profile | PASS (round 1) |
| AT08 | Report `HYPERFRAMES_MISSING` when the executable path points to a missing file | PASS — `SCENE_ENGINE_HYPERFRAMES_BIN` injects the missing path |
| AT09 | Offset and normalize narration to AAC-LC | PASS (round 1) |
| AT10 | Generate monotonic English and Vietnamese caption sidecar cues | PASS (round 1) |
| AT11 | Burn matching captions into cue frames | PASS (round 1) |
| AT12 | Export editable PPTX objects and verify its round trip | PASS — schema checks, python-pptx edit/reopen and LibreOffice round trip |
| AT13 | Build a native combo chart with a secondary axis and embedded workbook | PASS — column/line plots, right-side secondary value axis, and workbook validated |
| AT14 | Rasterize unsupported PPTX effects while retaining editable text | PASS — 2× Chromium picture fallback; title remains native text |
| AT15 | Capture a fixture app with deterministic frame hashes and timed overlays | PASS (round 1) |
| AT16 | Report a fixture app that misses its ready selector | PASS (round 1) |
| AT17 | Detect and reject an unseekable animated app canvas | PASS — reports `UNSEEKABLE` and does not publish capture output |
| AT18 | Select and render the screenshot fallback when HyperFrames is absent | PASS (round 1) |
| AT19 | Run sibling render-kit checks at default scene samples plus explicit `--at` frames | PASS — covers start/mid/end plus an additional explicit time |
| AT20 | Render PPTX slides and check each with render-kit | PASS (round 1) |
| AT21 | Verify H.264 High, frame size/rate, color tags, AAC-LC, and size profile | PASS (round 1) |
| AT22 | Validate CLI error codes and one-document JSON output | PASS (round 1) |
| AT23 | Validate registered adapters and reject unknown adapter IDs | PASS (round 1) |
| AT24 | Sample sparse property tracks, color interpolation, and anchor behavior | PASS (round 1) |
| AT25 | Check group/camera output and reject unsupported or invalid masks | PASS — reports `FEATURE_UNSUPPORTED`; invalid source also reports `MASK_SOURCE_INVALID` |
| AT26 | Sample rich text reveal, color range, counter, and paragraph order | PASS (round 1) |
| AT27 | Validate base chart data and unsupported build/dataStates | PASS — feature fields return `FEATURE_UNSUPPORTED`; scatter length constraints remain checked |
| AT28 | Resolve scene dependencies, markers, word events, captions, and app-local time | PASS (round 1) |
| AT29 | Split narration cues by timing rules and reject overflow without publishing output | PASS (round 1) |
| AT30 | Apply optional defaults and reject a symlink that escapes the project root | PASS (round 1) |
| AT31 | Capture multiple app layers with locator, asset, and external-request handling | PASS (round 1) |
| AT32 | Export entrance timing, editable bullet formatting, pose warnings, and font substitution | PASS — timing duration, DrawingML bullets, invisible/clipped/reflow warnings, Arial substitution |
| AT33 | Validate ECMA-376 authored parts and round-trip through python-pptx, LibreOffice, and Keynote | PASS — 57 package XML parts validate; python-pptx and LibreOffice pass; Keynote probe times out and records a nested owner check |
| AT34 | Detect chart formula references that do not match embedded workbook cells | PASS — corrupted formula fails with `PPTX_WORKBOOK_MISMATCH` before publication |
| AT35 | Embed a whole-storyboard video slide and report caption placement | PASS — native movie object and python-pptx round trip |
| AT36 | Automate Keynote import/PDF export and LibreOffice render smoke checks | PASS — Keynote probe times out and records a nested owner check; LibreOffice PDF render passes |
| AT37 | Verify current Microsoft PowerPoint behavior on Windows and Mac | OWNER-CHECK — only top-level owner-check; see the manual steps below |
| AT38 | Validate command result shapes, errors, and cleanup of failed artifacts | PASS (round 1) |
| AT39 | Reuse only the selected immutable app capture when its manifest matches | PASS (round 1) |

## Previous commands and artifact checks

- Full acceptance command: `npm test`.
- Full suite result: 39 tests; 38 passed, 0 failed, 1 skipped (AT37 owner-check), 0 todo; duration 131.3 seconds. The exact summary was:

  ```text
  # pass 38
  # fail 0
  # skipped 1
  # todo 0
  ```

- `npm test` uses Node's TAP reporter. AT37 invokes `scene-engine selftest --case AT37`, asserts the JSON status is `owner-check` and checks the manual steps before marking the test skipped. AT33 and AT36 assert the nested Keynote status and emit the required `owner-check:` diagnostic while passing.
- AT33 direct export: `openXmlValidation.status=pass`, `partsChecked=57`; python-pptx edit/save/reopen passed; LibreOffice opened and saved the PPTX, reopened it and rendered original and round-trip PDFs. The 10-second Keynote document-enumeration probe timed out and returned the Automation owner check.
- `npm run selftest -- --case AT36`: exit 0; AT36 status `pass`, nested Keynote status `owner-check` with the prescribed manual step, and LibreOffice status `pass` with a non-empty PDF at `out/tests/AT36/libreoffice.pdf`.
- `pgrep -x Keynote` after the full test suite: no processes found. Cleanup requests Keynote to quit, then signals only the PIDs observed after the test launched Keynote; a Keynote process present before a smoke is left untouched.
- `npm run samples`: exit 0. It rendered both 32-second 960-frame videos and exported the three-slide editable explainer PPTX. HyperFrames 0.8.78 reported 0 lint errors and nested-scene structure warnings.
- Explainer MP4 ffprobe: H.264 High@4.1, 1920×1080, yuv420p, 30 fps, limited-range BT.709; AAC-LC, 48 kHz stereo; duration 32.000 seconds.
- App-demo MP4 ffprobe: H.264 High@4.1, 1920×1080, yuv420p, 30 fps, limited-range BT.709; AAC-LC, 48 kHz stereo; duration 32.000 seconds.
- Python-pptx sample check: `pptx ok 3` (three slides, native chart, non-empty editable text).
- Sample artifacts: `out/explainer.mp4`, `out/explainer.pptx`, `out/explainer.png`, `out/explainer.vtt`, `out/app-demo.mp4`, `out/app-demo.png`, `out/app-demo.vtt`. `out/` is git-ignored.

## Previous AT36 Keynote Automation owner check

When the 10-second `osascript` document-enumeration probe times out or reports `Not authorized to send Apple events`, AT33/AT36 report this nested result and do not fail for the Keynote portion:

`owner-check: grant Automation permission (Terminal/Codex → Keynote) and rerun npm run selftest -- --case AT36`

After the owner grants Automation permission, rerun the command above. If the probe succeeds, Keynote import/PDF errors are real smoke failures. AT36 must still produce its LibreOffice PDF, and AT33 must still pass ECMA-376, python-pptx and LibreOffice checks.

## AT37 release-owner steps

`scene-engine selftest --case AT37` returns `status: owner-check`, `ok: true` in non-strict mode, and these steps. It does not claim PowerPoint compatibility:

1. On current Microsoft PowerPoint for Windows and Mac, record the OS and PowerPoint build. Open `out/tests/at33-morph.pptx` and `out/tests/at35.pptx`; record whether either shows a repair prompt.
2. In the chart, use Edit Data to change a value, save, close, reopen, and confirm the edited value persists.
3. Run the AT33 Morph slides and AT32 entrance animation; record whether the title morphs and the text enters from the left.
4. Play the embedded video on the AT35 playback slide and record playback and audio results on each platform.

The TAP skip string is prefixed with `owner-check:`. This is the only skipped test; AT33 and AT36 keep their Keynote owner check inside passing tests.

## Remaining owner checks

- AT33 and AT36 completed their Keynote import/PDF checks in the final run. AT37 still requires the release owner on current Microsoft PowerPoint for Windows and Mac before claiming app compatibility.

## Final motion acceptance run (2026-10-02)

| Gate | Result |
|---|---|
| `npm test` | PASS — final TAP run reports 48 tests, 47 pass, 0 fail, one skip (AT37 owner check); duration 260.6 seconds. AT33 and AT36 passed. |
| `npm run samples` | PASS — explainer MP4, fixture app MP4 and editable explainer PPTX completed; both videos are 32 seconds and HyperFrames 0.8.78 was used. |
| Copied storyboard validation | PASS — one scene, 95 layers, 57,500 ms, 1,725 frames. |
| Default dogfood render | PASS — `out/tests/motion-dogfood.mp4`, renderer selected fallback with `HYPERFRAMES_LONG_SINGLE_SCENE`; H.264 High@4.1, yuv420p, 1920×1080, 30 fps, limited-range BT.709 and AAC-LC 48 kHz stereo. Render completed in about 149 seconds. |
| `check --at` plus render-kit | PASS — all ten times passed: defaults 0, 28,750, 57,499 ms plus 3,500, 12,300, 18,000, 24,800, 37,800, 43,800 and 57,300 ms. |
| MP4/check-frame comparison | PASS — full-frame mean absolute RGB difference, tolerance 8: 3,500 ms 2.732; 12,300 ms 2.754; 18,000 ms 2.750; 24,800 ms 2.808; 37,800 ms 2.751; 43,800 ms 2.759; 57,300 ms 2.776. |

The final check used the exact rendered `render.png` frames produced by `scene-engine check` and cut each comparison frame from the MP4 with FFmpeg. No Google Fonts fetch was observed in the acceptance log; generated video HTML embeds the local font. The HyperFrames long-single-scene stall remains unmodified internally; `auto` avoids that path for single scenes of at least 1,200 frames and reports its choice. Changes remain uncommitted.

One intervening full-suite attempt had a transient AT15 app-capture failure; AT15 passed in isolation, and the subsequent full-suite run passed all required gates.

## Coordinator rerun (2026-10-02)

### Coordinator failures and corrections

- **F4 HyperFrames video comparison:** The coordinator reported a 73.39 mean absolute RGB difference in the video region at 300 ms. Inspection of that HyperFrames MP4 showed the video present with the authored 60% fade. The check screenshot could still be blank: `readyState >= 2` confirmed decoded media data but did not guarantee the paused frame had reached the compositor. The runtime now waits for pending media seeks; the MP4/check test waits for two browser paint frames outside the HyperFrames composition. Static check frames also seek to the video source time sampled by the storyboard. F4 now renders a red-to-blue source and asserts red at 300 ms with the 60% fade and blue at 900 ms. Both visible-pixel assertions and the existing region comparison keep the original tolerance of 8 for fallback and HyperFrames.
- **Sample app `compare` locator:** The fixture HTML contains `data-testid="compare"`; its step timing is valid (period fill at 250 ms, compare click at 850 ms, highlight from 650 ms). The sample runner previously spawned a server on fixed port 4178 and treated any HTTP 200 there as proof its child server was serving the fixture. If another listener already owned that port, readiness could accept that page and the capture then failed to find `compare`. The prior listener identity is not retained in the coordinator log. The sample runner now starts the fixture server in-process on an OS-assigned port and writes that owned port into a temporary storyboard before capture.

### Clean rerun summaries

Before each numbered command, its preceding `out/` was moved aside; no output directory was deleted. The original outputs, three test runs and first sample run are preserved under `/tmp/scene-engine-coordinator-rerun-20261002/`; the second sample run remains in the repository's `out/`. Each `npm test` used `PATH=/Users/GaryT/miniconda3/bin:$PATH HYPERFRAMES_NO_TELEMETRY=1`.

| Run | Recorded summary |
|---|---|
| `npm test` 1 | `# tests 48; # pass 47; # fail 0; # skipped 1; # todo 0; # duration_ms 173452.980041` |
| `npm test` 2 | `# tests 48; # pass 47; # fail 0; # skipped 1; # todo 0; # duration_ms 178302.97325` |
| `npm test` 3 | `# tests 48; # pass 47; # fail 0; # skipped 1; # todo 0; # duration_ms 200644.0105` |
| `npm run samples` 1 | `[samples] all requested artifacts are in out/` — explainer MP4, editable PPTX and app-demo MP4 all returned `ok: true`. |
| `npm run samples` 2 | `[samples] all requested artifacts are in out/` — explainer MP4, editable PPTX and app-demo MP4 all returned `ok: true`. |

AT37 is the one documented PowerPoint owner-check skip in each test run. Both samples runs produced 32-second H.264 1920×1080, 30 fps videos through HyperFrames 0.8.78. The explainer and app-demo MP4, PNG and VTT output hashes matched across the two sample runs; both PPTX files passed their Open XML, python-pptx and LibreOffice round trips. The PPTX package hashes differ only because the embedded workbook's `docProps/core.xml` created/modified timestamps differ between run times.

Artifact inspection of the second run's `out/app-demo.mp4` at 1,500 ms showed the filled `2026 Q2` period, the highlighted Compare periods button and the resulting “Compared 2026 Q2 with the prior period” status. Its probed duration is 32.000 seconds. Run logs are `npm-test-{1,2,3}.log` and `npm-run-samples-{1,2}.log` in the preserved rerun directory. Changes remain uncommitted.

## Presentation dogfood fixes (F2, F3, F4, F5, F12; 2026-10-02)

### Red baseline

Before implementation, the added regressions reproduced the requested gaps:

| Finding | Baseline evidence |
|---|---|
| F2 | The captured app was visible in the MP4 but absent from its check stage; full-frame MP4/check mean absolute RGB difference was 22.64, over the limit of 8. |
| F3 | The reopened chart XML contained no authored series colors (`[]`); chart titles, number format, gridline color, chart font size and rounded-rectangle adjustment were also absent. |
| F4 | `export-pptx`, `capture` and `check` returned exit code 2 when output destinations were outside the repository and command working directory. |
| F5 | Schema validation rejected `selectOption` with exit code 2, so the same-origin fixture path could not reach the staged error state. |
| F12 | The highlight overlay used a full-layer box-shadow tint and did not provide the requested padded outline-only treatment. |

### Changes

- F2 captures each active app-demo layer at the requested check time and embeds its matching frame in the check stage. The stage samples the scene-camera pose at that same time. A fallback MP4/check regression compares the full frame at 500 ms with the existing 8-level tolerance.
- F3 writes authored chart style into chart XML, maps combo-series colors by authored series index, and writes `radiusPx` to the rounded rectangle DrawingML `adj`. The regression reopens both native charts with python-pptx and checks chart and slide XML.
- F4 resolves `--out`, `--out-dir` and `--report` from the invoking process working directory without restricting their destination to the repository. PPTX temporary work is created next to its output so an external destination does not depend on repository writes.
- F5 fixtures run before same-origin pass-through. The URL matcher handles Playwright `*`, `**`, `?`, brace alternatives and backslash escaping; `selectOption` is accepted by the schema and runs in the capture. F12 draws only a 6-pixel-padded outline, with no viewport tint.
- The full suite initially exposed AT33/AT36 Keynote import timeouts after their Apple Events probe succeeded. The import/PDF call is now bounded at 30 seconds and reports that timeout as the documented nested Keynote owner-check; other import/PDF errors still fail. AT33 schema, python-pptx and LibreOffice checks and the AT36 LibreOffice render remain required.
- SPEC and AGENTS document the output-path, check-stage, chart XML, fixture, select action, highlight and Keynote owner-check behavior.

### Required clean validation

Before the first run, the existing `out/` was moved to `/tmp/scene-engine-presentation-fixes-20261002/out-before-clean-validation`. Focused debugging output and each full-suite output were also moved aside; the samples build produced the current repository `out/`. Every full test run began with no `out/` directory. Commands used `PATH=/Users/GaryT/miniconda3/bin:$PATH HYPERFRAMES_NO_TELEMETRY=1`.

| Gate | Recorded summary |
|---|---|
| `npm test` 1 | `# tests 53; # pass 52; # fail 0; # skipped 1; # todo 0; # duration_ms 259494.535542` |
| `npm test` 2 | `# tests 53; # pass 52; # fail 0; # skipped 1; # todo 0; # duration_ms 259180.923667` |
| `npm test` 3 | `# tests 53; # pass 52; # fail 0; # skipped 1; # todo 0; # duration_ms 296794.383917` |
| `npm run samples` | `[samples] all requested artifacts are in out/` |

The sole skip in each suite is AT37's documented Microsoft PowerPoint release-owner check. AT33 and AT36 pass; their Keynote portions report nested owner checks for the 30-second import/PDF timeout, while their LibreOffice checks pass. Logs and preserved test artifacts are under `/tmp/scene-engine-presentation-fixes-20261002/` (`npm-test-{1,2,3}.log`, `npm-run-samples.log`, and `out-test-{1,2,3}`). The sample artifacts remain in `out/`. Changes remain uncommitted.
