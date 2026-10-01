# scene-engine build report

## Verdict

FAIL — the acceptance suite reports 36 pass, 2 fail, and 1 owner-check skip. All requested implementation cases pass except the Keynote automation portions of AT33 and AT36: AppleScript timed out waiting for the currently unresponsive Keynote process. AT33's ECMA-376 schema, python-pptx, and LibreOffice checks pass. A request to restart Keynote is pending because it may contain unsaved work; no Keynote process was terminated. AT37 remains the explicit release-owner check because Microsoft PowerPoint is not installed on this Mac.

## Acceptance tests

`SPEC.md` and `tests/acceptance.test.mjs` define AT01–AT39. This report records test IDs individually. The full `npm test` run completed; AT33 and AT36 are the only failures, and AT37 is the only skipped case.

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
| AT19 | Run sibling render-kit checks on requested storyboard frames | PASS (round 1) |
| AT20 | Render PPTX slides and check each with render-kit | PASS (round 1) |
| AT21 | Verify H.264 High, frame size/rate, color tags, AAC-LC, and size profile | PASS (round 1) |
| AT22 | Validate CLI error codes and one-document JSON output | PASS (round 1) |
| AT23 | Validate registered adapters and reject unknown adapter IDs | PASS (round 1) |
| AT24 | Sample sparse property tracks, color interpolation, and anchor behavior | PASS (round 1) |
| AT25 | Sample nested groups, stagger, mask, and camera behavior | PASS (round 1) |
| AT26 | Sample rich text reveal, color range, counter, and paragraph order | PASS (round 1) |
| AT27 | Validate chart build modes, data states, and scatter data | PASS (round 1) |
| AT28 | Resolve scene dependencies, markers, word events, captions, and app-local time | PASS (round 1) |
| AT29 | Split narration cues by timing rules and reject overflow without publishing output | PASS (round 1) |
| AT30 | Apply optional defaults and reject a symlink that escapes the project root | PASS (round 1) |
| AT31 | Capture multiple app layers with locator, asset, and external-request handling | PASS (round 1) |
| AT32 | Export entrance timing, editable bullet formatting, pose warnings, and font substitution | PASS — timing duration, DrawingML bullets, invisible/clipped/reflow warnings, Arial substitution |
| AT33 | Validate ECMA-376 authored parts and round-trip through python-pptx, LibreOffice, and Keynote | FAIL — 57 package XML parts validate; python-pptx and LibreOffice pass; Keynote AppleScript timed out after 125.9 s |
| AT34 | Detect chart formula references that do not match embedded workbook cells | PASS — corrupted formula fails with `PPTX_WORKBOOK_MISMATCH` before publication |
| AT35 | Embed a whole-storyboard video slide and report caption placement | PASS — native movie object and python-pptx round trip |
| AT36 | Automate Keynote import/PDF export and LibreOffice render smoke checks | FAIL — Keynote AppleScript timed out after 120.7 s; smoke reports `PPTX_ROUNDTRIP_FAILED` |
| AT37 | Verify current Microsoft PowerPoint behavior on Windows and Mac | OWNER-CHECK — only non-pass row; see the manual steps below |
| AT38 | Validate command result shapes, errors, and cleanup of failed artifacts | PASS (round 1) |
| AT39 | Reuse only the selected immutable app capture when its manifest matches | PASS (round 1) |

## Commands and artifact checks

- Full acceptance command: `npm test 2>&1 | tee /tmp/se-test.log; grep -E '^# (pass|fail|skip|todo)' /tmp/se-test.log`.
- Full suite result: 39 tests; 36 passed, 2 failed (AT33 and AT36), 1 skipped (AT37 owner-check), 0 todo. The exact summary emitted for the requested `grep` was:

  ```text
  # pass 36
  # fail 2
  # skipped 1
  # todo 0
  ```

- `npm test` uses Node's TAP reporter so the requested summary grep emits the test totals. AT37 invokes `scene-engine selftest --case AT37`, asserts the JSON status is `owner-check` and checks the manual steps before marking the test skipped.
- AT33 direct export: `openXmlValidation.status=pass`, `partsChecked=57`; python-pptx edit/save/reopen passed; LibreOffice opened and saved the PPTX, reopened it and rendered original and round-trip PDFs. Keynote import/PDF export failed with `spawnSync osascript ETIMEDOUT`.
- AT36 Keynote import/PDF export failed with `spawnSync osascript ETIMEDOUT`; its selftest reports `PPTX_ROUNDTRIP_FAILED`.
- `npm run samples`: exit 0. It rendered both 32-second 960-frame videos and exported the three-slide editable explainer PPTX. HyperFrames 0.8.78 reported 0 lint errors and nested-scene structure warnings.
- Explainer MP4 ffprobe: H.264 High@4.1, 1920×1080, yuv420p, 30 fps, limited-range BT.709; AAC-LC, 48 kHz stereo; duration 32.000 seconds.
- App-demo MP4 ffprobe: H.264 High@4.1, 1920×1080, yuv420p, 30 fps, limited-range BT.709; AAC-LC, 48 kHz stereo; duration 32.000 seconds.
- Python-pptx sample check: `pptx ok 3` (three slides, native chart, non-empty editable text).
- Sample artifacts: `out/explainer.mp4`, `out/explainer.pptx`, `out/explainer.png`, `out/explainer.vtt`, `out/app-demo.mp4`, `out/app-demo.png`, `out/app-demo.vtt`. `out/` is git-ignored.

## AT37 release-owner steps

`scene-engine selftest --case AT37` returns `status: owner-check`, `ok: true` in non-strict mode, and these steps. It does not claim PowerPoint compatibility:

1. On current Microsoft PowerPoint for Windows and Mac, record the OS and PowerPoint build. Open `out/tests/at33-morph.pptx` and `out/tests/at35.pptx`; record whether either shows a repair prompt.
2. In the chart, use Edit Data to change a value, save, close, reopen, and confirm the edited value persists.
3. Run the AT33 Morph slides and AT32 entrance animation; record whether the title morphs and the text enters from the left.
4. Play the embedded video on the AT35 playback slide and record playback and audio results on each platform.

The TAP skip string is prefixed with `owner-check:` so this is the sole expected skip/todo, not a pass.

## Remaining verification

- Rerun the full acceptance command after Keynote responds to import/export Apple Events. The current Keynote processes respond to version queries but hang on document enumeration/import/export. The restart confirmation is pending because a forced quit could discard unsaved work.
- AT37 must be completed by the release owner on current Microsoft PowerPoint for Windows and Mac before claiming app compatibility.
