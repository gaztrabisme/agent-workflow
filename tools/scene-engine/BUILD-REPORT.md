# scene-engine build report

## Verdict

Partial pass. The implementation and required sample artifacts are built. Of the 39 acceptance rows actually enumerated in `SPEC.md`, 29 pass and 10 remain unbuilt or require an external owner check. The request refers to 40 numbered tests, but `SPEC.md` and `tests/acceptance.test.mjs` define only AT01–AT39; no AT40 row was invented.

## Acceptance tests

`npm test` result: 39 tests, 29 passed, 0 failed, 10 skipped; exit 0. Skips are reported as FAIL here because the corresponding acceptance behavior is not verified as complete.

| Test | Acceptance test | Result |
|---|---|---|
| AT01 | Validate a storyboard with text, image, shape, and chart layers | PASS |
| AT02 | Reject duplicate layer IDs and assets that escape the project root | PASS |
| AT03 | Sample linear, ease-in-out, and cubic-Bezier keyframes | PASS |
| AT04 | Render an explicit 300 ms scene opacity overlap | PASS |
| AT05 | Repeat non-monotonic seeks and compare deterministic frames | PASS |
| AT06 | Reject a registered animation adapter that cannot seek backward | FAIL — backward-unseekable adapter reporting is not implemented |
| AT07 | Render with pinned HyperFrames, telemetry disabled, and normalized profile | PASS |
| AT08 | Report `HYPERFRAMES_MISSING` when the locked executable is absent | FAIL — executable absence cannot be injected while the locked binary is installed |
| AT09 | Offset and normalize narration to AAC-LC | PASS |
| AT10 | Generate monotonic English and Vietnamese caption sidecar cues | PASS |
| AT11 | Burn matching captions into cue frames | PASS |
| AT12 | Export editable PPTX objects and verify its round trip | PASS |
| AT13 | Build a native combo chart with a secondary axis | FAIL — combo chart XML and secondary-axis workbook generation are not implemented |
| AT14 | Rasterize unsupported PPTX effects while retaining editable text | FAIL — per-layer DrawingML fallback is not implemented |
| AT15 | Capture a fixture app with deterministic frame hashes and timed overlays | PASS |
| AT16 | Report a fixture app that misses its ready selector | PASS |
| AT17 | Detect and reject an unseekable app canvas | FAIL — history-dependent canvas detection is not implemented |
| AT18 | Select and render the screenshot fallback when HyperFrames is absent | PASS |
| AT19 | Run sibling render-kit checks on requested storyboard frames | PASS — all selected times pass after fixing the static-check HTML to omit its optional composition script |
| AT20 | Render PPTX slides and check each with render-kit | PASS |
| AT21 | Verify H.264 High, frame size/rate, color tags, AAC-LC, and size profile | PASS |
| AT22 | Validate CLI error codes and one-document JSON output | PASS |
| AT23 | Validate registered adapters and reject unknown adapter IDs | PASS |
| AT24 | Sample sparse property tracks, color interpolation, and anchor behavior | PASS |
| AT25 | Sample nested groups, stagger, mask, and camera behavior | PASS |
| AT26 | Sample rich text reveal, color range, counter, and paragraph order | PASS |
| AT27 | Validate chart build modes, data states, and scatter data | PASS |
| AT28 | Resolve scene dependencies, markers, word events, captions, and app-local time | PASS |
| AT29 | Split narration cues by timing rules and reject overflow without publishing output | PASS |
| AT30 | Apply optional defaults and reject a symlink that escapes the project root | PASS |
| AT31 | Capture multiple app layers with locator, asset, and external-request handling | PASS |
| AT32 | Export PPTX entrance timing, editable bullets, pose warnings, and font substitution | FAIL — entrance XML, bullet formatting, and pose warnings are incomplete |
| AT33 | Validate authored parts against ECMA-376 and round-trip through python-pptx, LibreOffice, and Keynote | FAIL — ECMA-376 schemas and full LibreOffice/Keynote round trips are not implemented |
| AT34 | Detect chart formula references that do not match embedded workbook cells | FAIL — workbook formula-to-cell mismatch validation is not implemented |
| AT35 | Embed a whole-storyboard video slide and report caption placement | PASS |
| AT36 | Automate Keynote import/PDF export and LibreOffice render smoke checks | FAIL — the automated selftest is skipped; a manual Keynote 13.2 import and PDF export smoke check did complete |
| AT37 | Verify current Microsoft PowerPoint behavior on Windows and Mac | FAIL — PowerPoint is not installed on this build Mac; release-owner checks remain outstanding |
| AT38 | Validate command result shapes, errors, and cleanup of failed artifacts | PASS |
| AT39 | Reuse only the selected immutable app capture when its manifest matches | PASS |

## Acceptance command output

- `npm test`: 29 pass, 0 fail, 10 skipped, exit 0.
- `npm run samples`: exit 0; rendered the explainer MP4 and editable PPTX, then captured the local fixture app and rendered the app-demo MP4. HyperFrames 0.8.78 produced 960 frames per 32-second video. Lint had 0 errors and emitted nested-scene structure warnings.
- Explainer video ffprobe: `h264,1920,1080,yuv420p,30/1`; audio: `aac`; duration: `32.000000` seconds.
- App-demo video ffprobe: `h264,1920,1080,yuv420p,30/1`; audio: `aac`; duration: `32.000000` seconds.
- PPTX acceptance check: `pptx ok 3` (three slides; at least one non-empty text shape and one native chart).
- Files produced: `out/explainer.mp4`, `out/explainer.pptx`, `out/explainer.png`, `out/explainer.vtt`, `out/app-demo.mp4`, `out/app-demo.png`, and `out/app-demo.vtt`.
- Visual spot-check at 15 seconds showed the CSV-backed chart with both series in the explainer and the app-demo's closing title. `out/` is git-ignored.

## Build decisions

See `SPEC-REPORT.md` → “Build decisions” for the environment choices. Additional build facts:

- Pinned `gsap@3.13.0` and copied its local browser script into each HyperFrames composition so its composition timeline is seekable without a network request.
- The sample narrations are caption text only; no voice asset was authored, so sample MP4s carry the required silent AAC track.
- `npm ci` completed. npm reported one moderate dependency vulnerability; package pins were left unchanged.
- `npm run samples` builds the chart series from `samples/explainer/chart.csv` and starts the local fixture app only for the app-demo capture/render sequence.
- All HyperFrames processes run with `HYPERFRAMES_NO_TELEMETRY=1`. render-kit is called from `../render-kit/bin/rk` and is not copied into this repository.

## Remaining work and limits

- Complete AT06 adapter seekability checks, AT08 injectable missing-binary path, AT13 combo/secondary-axis charts, AT14 PPTX raster fallback, AT17 canvas seekability detection, AT32 PowerPoint entrance/bullet/pose features, AT33 package-schema and round-trip verification, AT34 chart workbook consistency checks, and AT36 automated Keynote smoke.
- Ask the release owner to perform AT37 in current Windows and Mac PowerPoint installations, including Edit Data and media playback.
- The exporter validates ZIP CRCs and package relationship targets, but does not validate all authored XML parts against ECMA-376 XSD schemas. Python-pptx round-trip and LibreOffice PDF checks cover portions of the PPTX path; they do not complete AT33.
- HyperFrames' nested-scene warnings do not block rendering. Both sample MP4s passed profile checks; the sample AAC tracks are silent because the storyboards include captions but no narration recording.
