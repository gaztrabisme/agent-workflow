# scene-engine specification report

The research did not settle several design choices required for a buildable contract. SPEC.md §9 records the trade-offs: the version-one JSON storyboard and its fixed 1920×1080/30 fps canvas; millisecond time and interpolation rules; each PPTX slide's sampled pose at `pptxAtMs`; the app-demo frame-sequence boundary; CLI exit codes and JSON shape; render-kit invocation on key frames and rendered PPTX slides; raster fallback order; Node orchestration with a Python writer; and deferring soundtrack authoring while the phase 4 row requires narration and captions. These are implementation decisions, not claims from the research.

Questions left unanswered by the permitted sources are listed in SPEC.md §10. They include exact Node and Python patch versions, the macOS Playwright shell path, the LibreOffice pin, the FFmpeg build feature set, actual Microsoft PowerPoint playback and WebVTT storage, capture parity on a real framework app, local voice quality and Vietnamese alignment accuracy, immutable TTS model revisions, cross-machine identity, and a measured frame-difference tolerance between renderers. The experiment used XlsxWriter without an exact version; the spec avoids making it a dependency and records the risk of generating the small embedded workbook with standard-library ZIP/XML. Sources: `output-pipelines/report.md` F4, F8, F9 and Risks; `synthesis.md` “Inputs for the scene engine” and “Open questions”.

Acceptance command:

```text
test $(grep -c '^| AT' SPEC.md) -ge 15 && for p in 'scene model' 'timeline' 'seek' 'narration' 'PPTX' 'app-demo' 'fallback'; do grep -i '^| AT' SPEC.md | grep -qi "$p" || { echo "no AT for $p"; exit 1; }; done && git log --oneline -1
```

The test-count and part-name checks passed silently. The command then failed at its final `git log` check:

```text
fatal: your current branch 'master' does not have any commits yet
```

Exit code: 128. The requested commit could not be created because the workspace permission profile makes `.git` read-only: `git branch -m main` failed when Git attempted to write `.git/HEAD.lock` (`Operation not permitted`). The working tree remains on `master` with the four requested files uncommitted.


## Revision after the persona contest

**Artifact verdict: PASS for spec/register completeness; implementation acceptance is pending the coordinator.** `SPEC.md` now answers all 26 blocking rows. `contest/objections.md` records 26 blocking and 10 non-blocking rows as `answered`, and 7 non-blocking rows as `declined` with version-two reasons; no row remains open and no blocking row is declined. The acceptance table keeps the required `| AT | Part | Given | When | Then |` format, retains the original cases and adds AT23–AT39 for the new scene, timing, narration, app-demo, PPTX, CLI and owner-check contracts.

The revision defines property tracks, group/stagger behavior, text and chart animation, masks, a 2D camera, symbolic time, narration overflow, app-demo steps and fixtures, asset-root containment, explicit frame reuse, renderer defaults, command JSON and error codes. It also states the v1 limits for spatial paths, spring/repeat motion, high frame rates, preview, themes/layouts and partial draft rendering.

For the PowerPoint objection, the spec requires ECMA-376 validation of hand-written package parts, python-pptx and LibreOffice open/save/reopen checks, LibreOffice PDF renders, and a Keynote import/PDF smoke check through `osascript`. This Mac has Keynote and LibreOffice but no Microsoft PowerPoint. Those checks can catch malformed XML, round-trip loss and alternate-viewer import problems; they do **not** prove that PowerPoint opens without repair, that Edit Data works in its UI, or that Morph, SVG, timing and movie playback behave correctly. AT37 assigns the Windows/Mac PowerPoint check to the release owner.

The initial revision report recorded specification work only. Build validation and remaining implementation gaps are now tracked in `BUILD-REPORT.md`.

## Build decisions

| Open environment choice | Decision used in this build |
|---|---|
| Node patch version | Node.js 24.16.0; runtime requires Node 24 or later |
| Python patch version and writer path | Python 3.11.5; writer runs from repository `.venv/bin/python` |
| Node package pins | `hyperframes@0.8.78`, `playwright@1.63.0`, `ajv@8.17.1`, `gsap@3.13.0`, `typescript@5.9.3`; exact versions are in `package.json` and `package-lock.json`. GSAP supplies HyperFrames' seekable composition timeline. |
| Python package pin | `python-pptx==1.0.2` installed in `.venv/`; the system Python's 1.0.3 is not used by the writer |
| Chromium shell | Use the installed Playwright revision 1243 under `~/Library/Caches/ms-playwright/chromium_headless_shell-1243/`, choosing the `mac-arm64` or `mac-x64` executable at runtime |
| FFmpeg / ffprobe | Use the installed FFmpeg 8.0 and matching `ffprobe` from `/opt/homebrew/bin`; HyperFrames raw output is always normalized with FFmpeg |
| LibreOffice | Use installed LibreOffice 26.2.4.2 for PPTX PDF render checks |
| Keynote | Use installed Keynote 13.2 for the import and PDF export smoke check |
| render-kit | Call the sibling `../render-kit/bin/rk`; do not copy it |
| HyperFrames telemetry | Set `HYPERFRAMES_NO_TELEMETRY=1` in the renderer and sample process environments |
| Sample chart CSV | `samples/explainer/chart.csv` is parsed by `npm run samples` into the spec's inline chart data before validation/rendering |
| Sample narration | Captions use authored text cues; no voice recording is shipped, so MP4 output has the required silent AAC track |

The export patches python-pptx's speaker-notes reference in `presentation.xml`. Without that relationship entry, Keynote 13.2 rejects a notes-bearing deck as an invalid file even though LibreOffice and python-pptx accept it. The build validates package ZIP CRCs and internal relationship targets; an ECMA-376 XSD bundle was not selected or vendored, so full schema validation remains unbuilt and is reported as a gap.
