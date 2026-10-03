# Agent guide

## Commands

- Install locked Node dependencies with `npm ci`; prepare `.venv` with `python-pptx==1.0.2`.
- Validate: `npm run scene-engine -- validate <storyboard.json> --root <project-root>`.
- Render: `npm run scene-engine -- render <storyboard.json> --out out/movie.mp4 --renderer auto --captions both`.
- Capture one app layer: `npm run scene-engine -- capture <storyboard.json> --scene <scene-id> --layer <layer-id> --out-dir out/capture`.
- Export slides: `npm run scene-engine -- export-pptx <storyboard.json> --out out/deck.pptx --verify`.
- Check key frames: `npm run scene-engine -- check <storyboard.json> --at 500,1000 --rk ../render-kit/bin/rk`.
- Build both samples: `npm run samples`; run acceptance tests: `npm test`.

Each command writes one JSON result to stdout. Diagnostics use stable codes and JSON pointers. A storyboard's project root is its directory unless `--root` is supplied; asset paths resolve inside that root. All CLI output paths (`--out`, `--poster`, `--out-dir`, `--report`) may be anywhere writable, from any working directory. Relative output paths resolve from the invoking process's current working directory. Build and sample commands write under `out/`.

## What renders today

| Storyboard feature | Video support today | Validation or rendering behavior |
|---|---|---|
| Text, rich text and counters | Supported; counters interpolate over the layer interval and keep the final value | Text uses engine-bundled Inter for the Arial/Inter aliases; HyperFrames returns `FONT_UNPINNED` for another requested family before render. |
| Structured bullets | Supported with bullet, numbered or marker-free items and indentation levels 0–8 | Authored item order is preserved. |
| Property tracks | Supported for registered properties; multiple properties on one layer are combined | Easing is evaluated per keyframe interval; values hold before/after their track; times stay layer-local within scene-local time. |
| Shapes | Rectangles, rounded rectangles, ellipses, lines and SVG paths; solid/gradient fill, solid/dash/dot stroke, stroke offset and path trim | PPTX rounded rectangles write `radiusPx` into DrawingML `adj`; `effects.mask` is rejected by `validate` with `FEATURE_UNSUPPORTED`; an invalid mask source also reports `MASK_SOURCE_INVALID`. |
| Charts | Base inline SVG charts render from their authored data | Native PPTX charts write series colors in authored order, axis titles, number format, gridline color and font size from `style`; `build` and `dataStates` are rejected by `validate` with `FEATURE_UNSUPPORTED`. |
| App demos | Local app capture, deterministic steps, cursor and highlight overlays; `check` captures active app layers and composites their matching frames into check stages with the sampled scene-camera pose | Fixtures may override same-origin requests and accept Playwright glob alternatives; `selectOption` chooses a `<select>` value. Highlights draw only a padded outline and do not tint the app frame. Unmatched external requests fail with `FIXTURE_NOT_FOUND`. |
| Video layers | Supported with `fade`, `flyInLeft`, `flyInRight`, `flyInUp`, `flyInDown` and `wipeLeft` entrances | Media seek and entrance progress use the containing scene's local time. |
| Captions | Burn-in cue visibility follows each scene-local `[startMs,endMs)` interval; sidecar and both modes write WebVTT | `validate` enforces at most two explicit lines and 42 characters per line. `check` omits a duplicate cue when matching author text is active in the bottom caption area. |
| Long single-scene renders | `auto` selects the fallback renderer at 1,200 frames and above | Emits `HYPERFRAMES_LONG_SINGLE_SCENE`; default timeout scales with frame count and fallback progress is reported to stderr. |

`tests/acceptance.test.mjs` compares FFmpeg-cut MP4 frames with `check` frames for both available renderers. App-demo comparison uses a local fixture app and the captured frame composed into the actual `check` stage; a static-stage regression checks its sampled camera pose. Full-frame mean absolute RGB difference must be at most 8; feature tests also check the moving layer or caption region at the same tolerance. The F3 test reopens PPTX charts with python-pptx and inspects chart and shape XML, including combo-series color order; F4 runs export, capture and check from a foreign working directory.

## PowerPoint and Keynote owner checks

AT37 is the Microsoft PowerPoint release-owner check because PowerPoint is not installed on the build Mac. `scene-engine selftest --case AT37` reports `status: owner-check`; it is not a passing compatibility test. On current PowerPoint for Windows and Mac, record each OS and PowerPoint build, open `out/tests/at33-morph.pptx` and `out/tests/at35.pptx` and record repair prompts, edit a chart value and confirm it survives save/reopen, verify the AT33 Morph and AT32 entrance animation, and play the AT35 embedded video.

AT33 and AT36 also run a Keynote import/PDF smoke. Before importing, the smoke probes Apple Events for 10 seconds. A probe timeout, `Not authorized to send Apple events`, or a 30-second import/PDF timeout returns a nested `owner-check` inside the passing test; other import/PDF errors fail the Keynote smoke. The AT33 schema, python-pptx and LibreOffice checks and the AT36 LibreOffice render must still pass. After the owner grants Automation permission for Terminal/Codex to control Keynote, rerun `npm run selftest -- --case AT36`. Test-launched Keynote processes are tracked by PID and quit in `finally`; a pre-existing Keynote process is left alone.

## Storyboard example

```json
{
  "format": "scene-engine/storyboard@1",
  "title": "A small explanation",
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "scenes": [{
    "id": "intro",
    "startMs": 0,
    "durationMs": 3000,
    "narration": { "text": "Read the trend." },
    "captions": [{ "startMs": 500, "endMs": 1800, "text": "Read the trend." }],
    "layers": [
      {
        "id": "title", "type": "text", "x": 120, "y": 100,
        "width": 900, "height": 120, "startMs": 0, "durationMs": 3000,
        "text": "Read the trend", "style": { "fontFamily": "Arial", "fontSize": 56 },
        "tracks": [{ "property": "opacity", "keyframes": [
          { "atMs": 0, "value": 0 }, { "atMs": 500, "value": 1 }
        ] }]
      },
      {
        "id": "chart", "type": "chart", "x": 120, "y": 260,
        "width": 1000, "height": 600, "startMs": 0, "durationMs": 3000,
        "kind": "column", "categories": ["Jan", "Feb"],
        "series": [{ "name": "Visits", "values": [12, 24] }]
      }
    ]
  }]
}
```

Scenes occupy the deck timeline; layer and caption times are local to their scene. At 30 fps, frame `n` is sampled at `floor(n × 1000 / 30)` ms. Use `after` plus optional `gapMs` to sequence scenes. Tracks target one property each; times are layer-local and values are absolute. Image and narration assets use project-root-relative paths.

## Check loop

1. Run `npm test`, then `npm run scene-engine -- validate <storyboard.json>`.
2. Render a short clip while iterating. `auto` uses pinned HyperFrames when installed, except single scenes of 1,200 frames or more use the screenshot fallback with a warning; the engine always normalizes with FFmpeg. Fonts are local and unbundled HyperFrames fonts fail closed.
3. Run `npm run scene-engine -- check <storyboard.json> --at <ms,...> --rk ../render-kit/bin/rk` to check the default scene start/mid/end frames plus the requested times through render-kit.
4. Probe the actual MP4 artifact:

   ```sh
   ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,level,pix_fmt,width,height,r_frame_rate,color_range,color_primaries,color_transfer,color_space -of default=nw=1 out/movie.mp4
   ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,profile,sample_rate,channels -of default=nw=1 out/movie.mp4
   ffprobe -v error -show_entries format=duration -of csv=p=0 out/movie.mp4
   ```

5. For PPTX, inspect native text/chart objects with `python-pptx` and open a LibreOffice PDF render. PowerPoint playback, Morph, SVG import and Edit Data remain manual owner checks on a Microsoft PowerPoint installation; Keynote automation permission may require the owner check described above.
