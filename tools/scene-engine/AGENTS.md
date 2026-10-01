# Agent guide

## Commands

- Install locked Node dependencies with `npm ci`; prepare `.venv` with `python-pptx==1.0.2`.
- Validate: `npm run scene-engine -- validate <storyboard.json> --root <project-root>`.
- Render: `npm run scene-engine -- render <storyboard.json> --out out/movie.mp4 --renderer auto --captions both`.
- Capture one app layer: `npm run scene-engine -- capture <storyboard.json> --scene <scene-id> --layer <layer-id> --out-dir out/capture`.
- Export slides: `npm run scene-engine -- export-pptx <storyboard.json> --out out/deck.pptx --verify`.
- Check key frames: `npm run scene-engine -- check <storyboard.json> --at 500,1000 --rk ../render-kit/bin/rk`.
- Build both samples: `npm run samples`; run acceptance tests: `npm test`.

Each command writes one JSON result to stdout. Diagnostics use stable codes and JSON pointers. A storyboard's project root is its directory unless `--root` is supplied; asset paths resolve inside that root. Keep output paths inside the repository; the build and sample commands write under `out/`.

## PowerPoint owner check

AT37 is the sole expected owner check because Microsoft PowerPoint is not installed on the build Mac. `scene-engine selftest --case AT37` reports `status: owner-check` and the manual steps; it is not a passing compatibility test. On current Microsoft PowerPoint for Windows and Mac, record each OS and PowerPoint build, open `out/tests/at33-morph.pptx` and `out/tests/at35.pptx` and record repair prompts, edit a chart value and confirm it survives save/reopen, verify the AT33 Morph and AT32 entrance animation, and play the AT35 embedded video. `npm test` reports that one owner check as skipped until the release owner records the results.

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
2. Render a short clip while iterating. `auto` uses pinned HyperFrames when installed and the screenshot fallback otherwise; the engine always normalizes with FFmpeg.
3. Run `npm run scene-engine -- check <storyboard.json> --at <ms,...> --rk ../render-kit/bin/rk` to check selected frames through render-kit.
4. Probe the actual MP4 artifact:

   ```sh
   ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,level,pix_fmt,width,height,r_frame_rate,color_range,color_primaries,color_transfer,color_space -of default=nw=1 out/movie.mp4
   ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,profile,sample_rate,channels -of default=nw=1 out/movie.mp4
   ffprobe -v error -show_entries format=duration -of csv=p=0 out/movie.mp4
   ```

5. For PPTX, inspect native text/chart objects with `python-pptx` and open a LibreOffice PDF render. PowerPoint playback, Morph, SVG import and Edit Data remain manual owner checks on a Microsoft PowerPoint installation.
