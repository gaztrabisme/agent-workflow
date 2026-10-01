
# scene-engine specification

Reader: the agent that builds scene-engine, and anyone who later changes it.

Grounded in the frontend research: `synthesis.md` sections “Verdicts by use case” and “Inputs for the scene engine”; `output-pipelines/report.md` UC1–UC3 and findings F1, F3–F5, F8, F8b and F9; and the experiments named in those findings. This spec follows the shape, terms and acceptance-test numbering of the render-kit `SPEC.md`.

## 1. What it is

scene-engine turns a storyboard into two deliverables: a PowerPoint-safe MP4 explainer or web-app demo, and an editable native PowerPoint deck. It compiles the same scene model into HTML for video, adds a Playwright capture stage for real web apps, and writes PPTX objects from scene data. HyperFrames is the default video renderer. A smaller renderer uses the same seek contract when HyperFrames is unavailable.

Terms used below:

- **Storyboard:** the versioned JSON document that lists scenes, timed layers, narration metadata and caption cues.
- **Scene:** a timed composition in the storyboard. For PPTX export it becomes one slide; for video it occupies its declared interval on the deck timeline.
- **Layer:** one positioned object in a scene, such as text, an image, a chart or captured app footage.
- **Timeline:** the deck-wide integer-millisecond time domain from zero to the storyboard duration.
- **Frame:** one output image at a fixed frame index and frame rate. At 30 fps, frame \(n\) is sampled at \(\lfloor n × 1000 / 30 \rfloor\) milliseconds.
- **Seek:** setting every animation and time-dependent layer to the state for an explicit timeline time, without waiting for real time to pass.
- **App-demo capture:** a scripted Playwright run against a local web app that records deterministic frames, cursor motion and highlights for use as a layer.
- **Native PPTX object:** editable PowerPoint text, shape, chart, picture or movie objects rather than a screenshot of the whole slide.
- **Fallback renderer:** the portable screenshot-per-frame and FFmpeg renderer used when HyperFrames cannot run.
- **Easing:** a function that maps progress between two keyframes to the interpolated progress used by a numeric property.
- **Animation adapter:** a registered function that sets an animation library or script-driven layer to an explicit frame time.
- **Fixture:** a recorded or authored HTTP response that Playwright serves instead of calling a live service.
- **PPTX:** the Office Open XML PowerPoint Presentation file format used for editable decks.
- **WebVTT:** the timed-text caption format used for the optional caption sidecar.
- **Morph:** PowerPoint's transition that moves matching named objects between adjacent slides.
- **Round trip:** opening an exported deck, editing and saving native objects, then reopening it and checking that edits persisted.

The video export is always normalized after rendering to MP4 with H.264 High@4.1, yuv420p limited range, BT.709 color tags, 1920×1080, constant 30 fps and AAC-LC audio at 48 kHz stereo. A poster image accompanies the MP4.

## 2. Scope

In scope:

- One JSON storyboard format shared by video, app capture and PPTX export.
- Seekable timelines with deterministic easing and integer frame sampling.
- HTML scene generation for HyperFrames and the fallback renderer.
- Imported narration audio, narration text metadata, optional local-TTS output as an input asset, and optional WebVTT and burned-in captions.
- A native PPTX writer based on python-pptx 1.0.2 plus narrowly-scoped DrawingML/XML additions.
- Capture of local web apps with Playwright, deterministic fixtures and scripted UI actions.
- MP4 normalization and verification with FFmpeg/ffprobe.
- A check command that calls render-kit (`rk check`) for key frames and rendered PPTX slides.

Out of scope:

- A public hosted service, cloud rendering, native desktop/mobile app capture, a general video editor, arbitrary HTML-to-PPTX conversion, or an audio recording studio.
- Playing unseekable WebGL, canvas, video, Rive state machines or history-dependent spring animations as if they were deterministic. Those require an external real-time recording; scene-engine reports them as unsupported.
- Music and sound-effect authoring, licensing and ducking; version one accepts narration audio only.
- Spatial motion paths, loop/repeat controls, analytic spring/elastic easing, motion blur, frame rates other than 30 fps, preview/scrub UI, custom PowerPoint themes/layouts/placeholders, slide-number/footer placeholders and Google Slides support are deferred to version 2. V1 uses straight interpolation between authored positions and the fixed PowerPoint-safe 30 fps delivery profile.
- Scene transitions are cuts unless authored scene intervals overlap with opacity tracks; push, wipe and other named transition blocks are deferred to version 2. Repeated `!!` layer names provide the PPTX Morph continuity described in §5.4.
- A bundled voice, paid cloud TTS calls, forced alignment, music licensing or a local TTS model installer. The research names local options (Kokoro-82M for English and VieNeu-TTS v3-Turbo for Vietnamese); callers may pass their WAV and timing JSON to the ordinary narration inputs. Their exact runtime/model revisions and listening quality were not established, so neither is a required dependency.
- Claiming actual PowerPoint playback compatibility solely from LibreOffice output. PowerPoint playback remains a manual verification item.

## 3. Environment and dependencies

Required runtime:

| Component | Pin or minimum | Use |
|---|---:|---|
| Node.js | 24 or later | CLI, storyboard compiler, Playwright orchestration |
| TypeScript | 5.9.3 | Development check; Node runs erasable TypeScript directly, with no build step |
| `hyperframes` | 0.8.78 exactly | Default HTML-to-video renderer |
| `playwright` | 1.63.0 exactly | App capture and fallback frame screenshots |
| Playwright Chromium | 153.0.8010.12, revision 1243 in the research run | Browser used by the pinned Playwright build |
| Python | 3 | PPTX writer subprocess |
| `python-pptx` | 1.0.2 exactly | Native PPTX text, shapes, pictures, notes and supported charts |
| FFmpeg and ffprobe | 8.0 | MP4 normalization, audio mix, probing and frame diagnostics |

The Node project must commit a lockfile and install pinned packages with `npm ci`. The package manifest must use exact dependency versions, including `hyperframes: 0.8.78` and `playwright: 1.63.0`; do not let `npx` fetch an unpinned latest release. The research installed browsers with:

```sh
npm install --save-exact hyperframes@0.8.78 playwright@1.63.0
npm ci
npx playwright install chromium chromium-headless-shell
```

For HyperFrames, resolve the installed Playwright `chrome-headless-shell` path and set `PRODUCER_HEADLESS_SHELL_PATH` to that executable for the HyperFrames process. The measured Linux path was `/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`. On macOS, use the executable under the Playwright browser cache; do not hard-code a user-specific cache path. HyperFrames is invoked from the local npm install:

```sh
HYPERFRAMES_NO_TELEMETRY=1 PRODUCER_HEADLESS_SHELL_PATH="<Playwright chrome-headless-shell path>" \
  ./node_modules/.bin/hyperframes lint <composition-dir>
HYPERFRAMES_NO_TELEMETRY=1 PRODUCER_HEADLESS_SHELL_PATH="<Playwright chrome-headless-shell path>" \
  ./node_modules/.bin/hyperframes render <composition-dir> -o <raw.mp4> --quality delivery
```

Set `HYPERFRAMES_NO_TELEMETRY=1` on every HyperFrames subprocess, including lint, render and diagnostics. Do not rely on a developer's global telemetry preference. scene-engine runs HyperFrames lint before each render. A static scene must be explicitly marked with `data-no-timeline`; an animated composition must register its seekable timelines so lint does not wait through the measured 45-second missing-timeline readiness poll.

The fallback and app capture use Playwright's installed Chromium, with its deterministic seek adapter. On Linux, the measured fast capture primitive is `HeadlessExperimental.beginFrame` after seeking; it is not the source of time. On macOS it is unavailable, so use `Page.captureScreenshot`. The portable fallback is screenshot-per-frame on all platforms.

Install `python-pptx==1.0.2` in the Python environment used by the writer. Use Python's standard `zipfile` and XML libraries for the DrawingML patches; do not add another PPTX library. FFmpeg 8.0 must provide libx264, AAC, loudnorm, blackdetect, freezedetect and libass (the latter is needed only for burned-in captions). LibreOffice's `soffice` is an optional PPTX render-check tool; the research does not provide its version, so the build must record the version actually used. The render-kit executable is configured by path and is not copied or reimplemented.

## 4. Scene model

Coordinates are CSS pixels on a 1920×1080 stage. Times are integer milliseconds. The project root is the storyboard's containing directory unless `--root <dir>` is supplied. Resolve the root and each asset with `realpath`; reject symlinks that escape it. This covers image/video/adapter sources, narration audio and word-timing files, fixture body files, and poster files. `--out`, `--out-dir` and report destinations may be outside the project root.

Scene `startMs` is storyboard-relative. A scene may instead declare `after: <earlier-scene-id>` and `gapMs` (default 0); its start is that scene's end plus the gap. This single-predecessor rule moves later scenes when an earlier duration changes. Root `durationMs` is optional: when present it must cover the latest scene end; otherwise the compiler derives it. Explicit scenes may overlap. At equal start time, scene array order is back-to-front (later entries paint over earlier entries).

Layer `startMs` and `durationMs` are local to their scene; group-child times are local to their parent group. A layer track's numeric `atMs` is local to its layer start; a camera track's numeric time is scene-local. A symbolic track time may instead be `{ "marker": "name", "offsetMs": 0 }` or `{ "wordIndex": 3, "offsetMs": 0 }`: marker events are storyboard-relative; word indexes are zero-based in the containing scene's word-timing file and resolve from the word start plus `audioOffsetMs`, then convert to layer-local time. Captions are scene-local; app steps, cursor points and highlights are app-layer-local. `pptxAtMs` is scene-local. CLI `check --at` values are storyboard-relative. §5.1 gives the complete time-origin table and a worked frame conversion.

The required schema is JSON Schema Draft 2020-12. Unknown properties are rejected except within an adapter's registry-validated `config` object. A storyboard has at least one scene and one of the specified layer types. The base schema below is completed by the normative amendments in §4.1; those amendments replace fields marked as superseded. Validation reports a JSON pointer, stable code and reason for each invalid field.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://scene-engine.invalid/schema/storyboard-1.json",
  "title": "scene-engine storyboard v1",
  "type": "object",
  "additionalProperties": false,
  "required": ["format", "title", "width", "height", "fps", "scenes"],
  "properties": {
    "format": { "const": "scene-engine/storyboard@1" },
    "title": { "type": "string", "minLength": 1 },
    "width": { "const": 1920 },
    "height": { "const": 1080 },
    "fps": { "const": 30 },
    "durationMs": { "type": "integer", "minimum": 1, "description": "Optional asserted storyboard end; derived from scene ends if omitted." },
    "background": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$", "default": "#FFFFFF" },
    "language": { "type": "string", "minLength": 2, "default": "en" },
    "markers": { "type": "array", "items": { "type": "object", "additionalProperties": false, "required": ["id", "sceneId", "atMs"], "properties": { "id": { "type": "string", "minLength": 1 }, "sceneId": { "type": "string" }, "atMs": { "type": "integer", "minimum": 0 } } } },
    "scenes": {
      "type": "array", "minItems": 1,
      "items": { "$ref": "#/$defs/scene" }
    }
  },
  "$defs": {
    "easing": {
      "oneOf": [
        { "type": "string", "enum": ["linear", "ease-in", "ease-out", "ease-in-out", "step-start", "step-end"] },
        {
          "type": "object", "additionalProperties": false,
          "required": ["cubicBezier"],
          "properties": {
            "cubicBezier": {
              "type": "array", "prefixItems": [
                { "type": "number", "minimum": 0, "maximum": 1 },
                { "type": "number" },
                { "type": "number", "minimum": 0, "maximum": 1 },
                { "type": "number" }
              ], "minItems": 4, "maxItems": 4
            }
          }
        }
      ]
    },
    "timeRef": {
      "oneOf": [
        { "type": "integer", "minimum": 0 },
        { "type": "object", "additionalProperties": false, "properties": {
          "marker": { "type": "string", "minLength": 1 }, "wordIndex": { "type": "integer", "minimum": 0 },
          "offsetMs": { "type": "integer", "default": 0 }
        }, "oneOf": [{ "required": ["marker"] }, { "required": ["wordIndex"] }] }
      ]
    },
    "propertyKeyframe": {
      "type": "object", "additionalProperties": false, "required": ["atMs", "value"],
      "properties": { "atMs": { "$ref": "#/$defs/timeRef" }, "value": { "oneOf": [{ "type": "number" }, { "type": "string" }] }, "easing": { "$ref": "#/$defs/easing", "default": "linear" } }
    },
    "propertyTrack": {
      "type": "object", "additionalProperties": false, "required": ["property", "keyframes"],
      "properties": {
        "property": { "type": "string", "minLength": 1 },
        "keyframes": { "type": "array", "minItems": 1, "items": { "$ref": "#/$defs/propertyKeyframe" } }
      }
    },
    "rangeTrack": {
      "type": "object", "additionalProperties": false, "required": ["start", "end", "property", "keyframes"],
      "properties": {
        "start": { "type": "integer", "minimum": 0 }, "end": { "type": "integer", "minimum": 1 },
        "property": { "enum": ["opacity", "color", "fontSize", "rotation", "x", "y"] },
        "keyframes": { "type": "array", "minItems": 1, "items": { "$ref": "#/$defs/propertyKeyframe" } }
      }
    },
    "camera": {
      "type": "object", "additionalProperties": false,
      "properties": {
        "x": { "type": "number", "default": 0 }, "y": { "type": "number", "default": 0 },
        "zoom": { "type": "number", "exclusiveMinimum": 0, "default": 1 }, "rotation": { "type": "number", "default": 0 },
        "anchorX": { "type": "number", "minimum": 0, "maximum": 1, "default": 0.5 },
        "anchorY": { "type": "number", "minimum": 0, "maximum": 1, "default": 0.5 },
        "tracks": { "type": "array", "items": { "$ref": "#/$defs/propertyTrack" } }
      }
    },
    "mask": {
      "type": "object", "additionalProperties": false, "required": ["sourceLayerId"],
      "properties": {
        "sourceLayerId": { "type": "string" }, "mode": { "enum": ["alpha", "luma"], "default": "alpha" },
        "inverted": { "type": "boolean", "default": false }, "featherPx": { "type": "number", "minimum": 0, "default": 0 }
      }
    },
    "chartStyle": {
      "type": "object", "additionalProperties": false,
      "properties": {
        "fontFamily": { "type": "string", "default": "Arial" }, "fontSize": { "type": "number", "default": 14 },
        "seriesColors": { "type": "array", "items": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" } },
        "axisTitleX": { "type": "string", "default": "" }, "axisTitleY": { "type": "string", "default": "" },
        "numberFormat": { "type": "string", "default": "#,##0.##" }, "gridColor": { "type": "string", "default": "#D9DDE3" }
      }
    },
    "chartBuild": {
      "type": "object", "additionalProperties": false, "required": ["mode"],
      "properties": { "mode": { "enum": ["grow", "draw", "reveal"] }, "durationMs": { "type": "integer", "minimum": 1, "default": 600 }, "staggerMs": { "type": "integer", "minimum": 0, "default": 0 } }
    },
    "chartState": {
      "type": "object", "additionalProperties": false, "required": ["atMs", "series"],
      "properties": { "atMs": { "$ref": "#/$defs/timeRef" }, "series": { "type": "array", "items": { "type": "object", "additionalProperties": false, "required": ["name", "values"], "properties": { "name": { "type": "string" }, "values": { "type": "array", "items": { "type": "number" } } } } } }
    },
    "layerBase": {
      "type": "object",
      "required": ["id", "type", "x", "y", "width", "height", "startMs", "durationMs"],
      "properties": {
        "id": { "type": "string", "pattern": "^[A-Za-z][A-Za-z0-9_.-]*$" },
        "name": { "type": "string", "description": "Stable PowerPoint morph name; repeated names start with !!." },
        "type": { "type": "string" },
        "x": { "type": "number" }, "y": { "type": "number" },
        "width": { "type": "number", "exclusiveMinimum": 0 },
        "height": { "type": "number", "exclusiveMinimum": 0 },
        "startMs": { "type": "integer", "minimum": 0 },
        "durationMs": { "type": "integer", "minimum": 1 },
        "z": { "type": "integer", "default": 0 },
        "opacity": { "type": "number", "minimum": 0, "maximum": 1, "default": 1 },
        "rotation": { "type": "number", "default": 0 },
        "scaleX": { "type": "number", "exclusiveMinimum": 0, "default": 1 },
        "scaleY": { "type": "number", "exclusiveMinimum": 0, "default": 1 },
        "effects": {
          "type": "object", "additionalProperties": false,
          "properties": {
            "blurPx": { "type": "number", "minimum": 0 },
            "backdropBlurPx": { "type": "number", "minimum": 0 },
            "blendMode": { "enum": ["multiply", "screen", "overlay", "darken", "lighten"] },
            "mask": { "$ref": "#/$defs/mask" },
            "transform3d": { "type": "array", "minItems": 16, "maxItems": 16, "items": { "type": "number" } }
          }
        },
        "tracks": { "type": "array", "items": { "$ref": "#/$defs/propertyTrack" } },
        "anchorX": { "type": "number", "minimum": 0, "maximum": 1, "default": 0.5 },
        "anchorY": { "type": "number", "minimum": 0, "maximum": 1, "default": 0.5 },
        "alt": { "type": "string", "default": "" },
        "decorative": { "type": "boolean", "default": false },
        "readingOrder": { "type": "integer" },
        "entrance": { "enum": ["none", "fade", "flyInLeft", "flyInRight", "flyInUp", "flyInDown", "wipeLeft"], "default": "none" },
        "entranceDurationMs": { "type": "integer", "minimum": 1, "default": 500 }
      }
    },
    "scene": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "durationMs", "layers"],
      "properties": {
        "id": { "type": "string", "pattern": "^[A-Za-z][A-Za-z0-9_.-]*$" },
        "startMs": { "type": "integer", "minimum": 0 },
        "after": { "type": "string", "minLength": 1 },
        "gapMs": { "type": "integer", "minimum": 0, "default": 0 },
        "durationMs": { "type": "integer", "minimum": 1 },
        "pptxAtMs": { "type": "integer", "minimum": 0, "description": "Scene-local pose time; defaults to durationMs - 1." },
        "background": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
        "camera": { "$ref": "#/$defs/camera" },
        "notes": { "type": "string", "description": "PowerPoint speaker notes; defaults to narration.text." },
        "layers": {
          "type": "array",
          "items": {
            "oneOf": [
              { "$ref": "#/$defs/textLayer" },
              { "$ref": "#/$defs/imageLayer" },
              { "$ref": "#/$defs/chartLayer" },
              { "$ref": "#/$defs/shapeLayer" },
              { "$ref": "#/$defs/tableLayer" },
              { "$ref": "#/$defs/appDemoLayer" },
              { "$ref": "#/$defs/videoLayer" },
              { "$ref": "#/$defs/adapterLayer" },
              { "$ref": "#/$defs/groupLayer" }
            ]
          }
        },
        "narration": { "$ref": "#/$defs/narration" },
        "captions": { "oneOf": [{ "type": "array", "items": { "$ref": "#/$defs/caption" } }, { "const": "fromWordTimings" }] }
      }
    },
    "textLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "text" }, "text": { "type": "string" },
          "style": { "type": "object", "additionalProperties": false, "properties": {
            "fontFamily": { "type": "string", "default": "Arial" }, "fontSize": { "type": "number", "exclusiveMinimum": 0, "default": 32 },
            "fontWeight": { "type": "integer", "minimum": 100, "maximum": 900, "default": 400 }, "italic": { "type": "boolean", "default": false },
            "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$", "default": "#111111" },
            "align": { "enum": ["left", "center", "right"], "default": "left" }, "lineHeight": { "type": "number", "exclusiveMinimum": 0, "default": 1.2 },
            "letterSpacing": { "type": "number", "default": 0 }, "background": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
            "wrap": { "type": "boolean", "default": true }, "autoFit": { "enum": ["none", "shrinkText"], "default": "none" }, "insetPx": { "type": "number", "minimum": 0, "default": 0 }
          } },
          "split": { "enum": ["none", "line", "word", "grapheme"], "default": "none" },
          "reveal": { "type": "object", "additionalProperties": false, "required": ["unit", "staggerMs"], "properties": { "unit": { "enum": ["line", "word", "grapheme"] }, "staggerMs": { "type": "integer", "minimum": 0 }, "mode": { "enum": ["reveal", "typewriter"], "default": "reveal" } } },
          "runs": { "type": "array", "items": { "type": "object", "additionalProperties": false, "required": ["text"], "properties": { "text": { "type": "string" }, "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }, "fontWeight": { "type": "integer", "minimum": 100, "maximum": 900 }, "italic": { "type": "boolean" } } } },
          "rangeTracks": { "type": "array", "items": { "$ref": "#/$defs/rangeTrack" } },
          "bullets": { "type": "array", "items": { "type": "object", "additionalProperties": false, "required": ["text"], "properties": { "text": { "type": "string" }, "level": { "type": "integer", "minimum": 0, "maximum": 8, "default": 0 }, "kind": { "enum": ["bullet", "number", "none"], "default": "bullet" } } } },
          "counter": { "type": "object", "additionalProperties": false, "required": ["from", "to"], "properties": { "from": { "type": "number" }, "to": { "type": "number" }, "decimals": { "type": "integer", "minimum": 0, "maximum": 6, "default": 0 }, "prefix": { "type": "string", "default": "" }, "suffix": { "type": "string", "default": "" } } }
        }, "required": ["type"], "anyOf": [{ "required": ["text"] }, { "required": ["bullets"] }, { "required": ["counter"] }] }
      ],
      "unevaluatedProperties": false
    },
    "imageLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "image" }, "src": { "type": "string", "minLength": 1 },
          "alt": { "type": "string" }, "fit": { "enum": ["contain", "cover", "fill"], "default": "contain" }
        }, "required": ["type", "src"] }
      ],
      "unevaluatedProperties": false
    },
    "chartLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "chart" },
          "kind": { "enum": ["column", "bar", "line", "area", "pie", "doughnut", "scatter", "columnStacked", "columnStacked100", "barStacked", "barStacked100", "areaStacked", "combo"] },
          "categories": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
          "series": {
            "type": "array", "minItems": 1,
            "items": {
              "type": "object", "additionalProperties": false, "required": ["name", "values"],
              "properties": {
                "name": { "type": "string" },
                "values": { "type": "array", "minItems": 1, "items": { "type": "number" } },
                "xValues": { "type": "array", "minItems": 1, "items": { "type": "number" } },
                "kind": { "enum": ["column", "line", "area"] },
                "axis": { "enum": ["primary", "secondary"], "default": "primary" }
              }
            }
          },
          "showLegend": { "type": "boolean", "default": true },
          "showValues": { "type": "boolean", "default": false },
          "style": { "$ref": "#/$defs/chartStyle" },
          "build": { "$ref": "#/$defs/chartBuild" },
          "dataStates": { "type": "array", "items": { "$ref": "#/$defs/chartState" } }
        }, "required": ["type", "kind", "categories", "series"] }
      ],
      "unevaluatedProperties": false
    },
    "shapeLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "shape" }, "shape": { "enum": ["rect", "roundRect", "ellipse", "line", "path"] },
          "fill": {
            "oneOf": [
              { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
              {
                "type": "object", "additionalProperties": false, "required": ["angleDeg", "stops"],
                "properties": {
                  "angleDeg": { "type": "number" },
                  "stops": { "type": "array", "minItems": 2,
                    "items": { "type": "object", "additionalProperties": false, "required": ["offset", "color"],
                      "properties": {
                        "offset": { "type": "number", "minimum": 0, "maximum": 1 },
                        "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
                        "opacity": { "type": "number", "minimum": 0, "maximum": 1, "default": 1 }
                      }
                    }
                  }
                }
              }
            ]
          },
          "stroke": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
          "strokeWidth": { "type": "number", "minimum": 0 },
          "strokeDash": { "enum": ["solid", "dash", "dot"] },
          "strokeDashOffset": { "type": "number", "default": 0 },
          "radiusPx": { "type": "number", "minimum": 0, "default": 0 },
          "trimStart": { "type": "number", "minimum": 0, "maximum": 1, "default": 0 },
          "trimEnd": { "type": "number", "minimum": 0, "maximum": 1, "default": 1 },
          "shadow": {
            "type": "object", "additionalProperties": false,
            "required": ["blurPx", "distancePx", "directionDeg", "color"],
            "properties": {
              "blurPx": { "type": "number", "minimum": 0 }, "distancePx": { "type": "number", "minimum": 0 },
              "directionDeg": { "type": "number" }, "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
              "opacity": { "type": "number", "minimum": 0, "maximum": 1, "default": 1 }
            }
          },
          "path": { "type": "string" }
        }, "required": ["type", "shape"] }
      ],
      "unevaluatedProperties": false
    },
    "tableLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "table" },
          "columns": { "type": "array", "minItems": 1, "items": { "type": "string" } },
          "rows": { "type": "array", "items": { "type": "array", "items": { "type": ["string", "number", "boolean", "null"] } } }
        }, "required": ["type", "columns", "rows"] }
      ],
      "unevaluatedProperties": false
    },
    "appDemoLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "appDemo" },
          "url": { "type": "string", "pattern": "^http://(127\\.0\\.0\\.1|localhost)(:[0-9]+)?/" },
          "appBuildId": { "type": "string", "minLength": 1, "description": "Caller-supplied immutable local app build identifier required for frame reuse." },
          "readySelector": { "type": "string", "minLength": 1 },
          "readyTimeoutMs": { "type": "integer", "minimum": 1, "default": 30000 },
          "locale": { "type": "string", "default": "en-US" },
          "timeZoneId": { "type": "string", "default": "UTC" },
          "deviceScaleFactor": { "const": 2 }, "viewport": { "const": "layer-box-css-pixels" },
          "steps": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["atMs", "action"],
              "properties": {
              "atMs": { "type": "integer", "minimum": 0 }, "timeoutMs": { "type": "integer", "minimum": 1, "default": 5000 },
                "action": { "enum": ["goto", "click", "fill", "press", "waitFor"] },
                "url": { "type": "string" },
                "locator": {
                  "type": "object", "additionalProperties": false,
                  "properties": {
                    "role": { "type": "string" }, "name": { "type": "string" },
                    "testId": { "type": "string" }, "css": { "type": "string" }
                  },
                  "oneOf": [
                    { "required": ["role"] }, { "required": ["testId"] }, { "required": ["css"] }
                  ]
                },
                "value": { "type": "string" }, "key": { "type": "string" }
              },
              "allOf": [
                { "if": { "properties": { "action": { "const": "goto" } } }, "then": { "required": ["url"] } },
                { "if": { "properties": { "action": { "const": "click" } } }, "then": { "required": ["locator"] } },
                { "if": { "properties": { "action": { "const": "fill" } } }, "then": { "required": ["locator", "value"] } },
                { "if": { "properties": { "action": { "const": "press" } } }, "then": { "required": ["locator", "key"] } },
                { "if": { "properties": { "action": { "const": "waitFor" } } }, "then": { "required": ["locator"] } }
              ]
            }
          },
          "fixtures": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["urlPattern", "status", "bodyFile"],
              "properties": {
                "urlPattern": { "type": "string", "description": "Playwright URL glob pattern; regular expressions are not accepted." }, "method": { "type": "string", "default": "GET" },
                "status": { "type": "integer", "minimum": 100, "maximum": 599 },
                "bodyFile": { "type": "string" }, "contentType": { "type": "string", "default": "application/octet-stream" }
              }
            }
          },
          "cursor": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["atMs", "x", "y"],
              "properties": {
                "atMs": { "type": "integer", "minimum": 0 }, "x": { "type": "number" },
                "y": { "type": "number" }, "click": { "type": "boolean", "default": false }, "easing": { "$ref": "#/$defs/easing", "default": "linear" }
              }
            }
          },
          "highlights": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false,
              "required": ["locator", "startMs", "durationMs"],
              "properties": {
                "locator": {
                  "type": "object", "additionalProperties": false,
                  "properties": {
                    "role": { "type": "string" }, "name": { "type": "string" },
                    "testId": { "type": "string" }, "css": { "type": "string" }
                  },
                  "oneOf": [
                    { "required": ["role"] }, { "required": ["testId"] }, { "required": ["css"] }
                  ]
                },
                "startMs": { "type": "integer", "minimum": 0 },
                "durationMs": { "type": "integer", "minimum": 1 },
                "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$", "default": "#FF3B30" }
              }
            }
          }
        }, "required": ["type", "url", "readySelector", "steps"] }
      ],
      "unevaluatedProperties": false
    },
    "videoLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "video" }, "src": { "type": "string", "minLength": 1 },
          "poster": { "type": "string" }, "muted": { "type": "boolean", "default": true },
          "playback": { "type": "object", "additionalProperties": false, "properties": { "autoplay": { "type": "boolean", "default": false }, "loop": { "type": "boolean", "default": false }, "hideUntilPlay": { "type": "boolean", "default": false }, "startDelayMs": { "type": "integer", "minimum": 0, "default": 0 }, "fullScreen": { "type": "boolean", "default": false } } }
        }, "required": ["type", "src"] }
      ],
      "unevaluatedProperties": false
    },
    "adapterLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "adapter" }, "adapterId": { "type": "string", "minLength": 1 },
          "source": { "type": "string", "minLength": 1 }, "config": { "type": "object" }
        }, "required": ["type", "adapterId"] }
      ],
      "unevaluatedProperties": false
    },
    "groupLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "group" },
          "stagger": { "type": "object", "additionalProperties": false, "required": ["eachMs"], "properties": { "eachMs": { "type": "integer", "minimum": 0 }, "from": { "enum": ["start", "end", "center"], "default": "start" } } },
          "children": { "type": "array", "minItems": 1, "items": { "oneOf": [
            { "$ref": "#/$defs/textLayer" }, { "$ref": "#/$defs/imageLayer" }, { "$ref": "#/$defs/chartLayer" },
            { "$ref": "#/$defs/shapeLayer" }, { "$ref": "#/$defs/tableLayer" }, { "$ref": "#/$defs/appDemoLayer" },
            { "$ref": "#/$defs/videoLayer" }, { "$ref": "#/$defs/adapterLayer" }
          ] } }
        }, "required": ["type", "children"] }
      ],
      "unevaluatedProperties": false
    },
    "narration": {
      "type": "object", "additionalProperties": false, "required": ["text"],
      "properties": {
        "text": { "type": "string" },
        "audio": { "type": "string", "description": "Optional supplied WAV/AIFF/MP3 narration input, relative to storyboard." },
        "audioOffsetMs": { "type": "integer", "minimum": 0, "default": 0 },
        "gainDb": { "type": "number", "default": 0 },
        "wordTimings": {
          "type": "string", "description": "Optional JSON file of word start/end times from an existing TTS or alignment tool."
        }
      }
    },
    "caption": {
      "type": "object", "additionalProperties": false,
      "required": ["startMs", "endMs", "text"],
      "properties": {
        "startMs": { "type": "integer", "minimum": 0 },
        "endMs": { "type": "integer", "minimum": 1 },
        "text": { "type": "string", "minLength": 1 },
        "language": { "type": "string", "description": "Defaults to storyboard language, then en." }
      }
    }
  }
}
```

### 4.1 Model semantics and validation

`layerBase.tracks` replaces the former layer-wide `keyframes` field. A track is independent and may target only a registered v1 path: `x`, `y`, `width`, `height`, `opacity`, `rotation`, `scaleX`, `scaleY`, `anchorX`, `anchorY`, `style.fontSize`, `style.letterSpacing`, `style.color`, `style.background`, `fill`, `fill.angleDeg`, `fill.stops[i].offset|color|opacity`, `stroke`, `strokeWidth`, `strokeDashOffset`, `radiusPx`, `trimStart`, `trimEnd`, `effects.blurPx`, `effects.backdropBlurPx`, `effects.mask.featherPx`, `shadow.blurPx`, `shadow.distancePx`, `shadow.directionDeg`, `shadow.color`, `shadow.opacity`, or scene-camera `x|y|zoom|rotation`. This is a closed allowlist: 3D matrices, path-string morphing and arbitrary style properties cannot be keyframed in v1. A track value is an absolute value for its property, not an offset; each property path appears at most once per layer and keyframe times are strictly increasing after symbolic resolution. Values must match their target type; opacity/shadow opacity and trim values are [0,1], width/height/font size/scale/zoom are positive, blur and stroke widths are nonnegative, and color values use `#RRGGBB`. Invalid values return `TRACK_VALUE_INVALID`. Before a property's first keyframe, its base value applies; after its last keyframe, its last value holds. Between two keyframes on that property, interpolate only that property using the earlier keyframe's easing. Missing values in another track have no effect. Numeric angles are degrees and interpolate directly; rotation and scale pivot around `(anchorX × width, anchorY × height)`, default center. Colors interpolate in OKLab with alpha linear. Gradient stop count/order is fixed for an animation; paths, mask mode and gradient topology are discrete and cannot be interpolated. `strokeDashOffset`, `trimStart` and `trimEnd` provide line draw-on/reveal controls.

`group` layers contain child layers in `children`; child x/y are group-local, and position, scale, rotation and opacity compose through each parent. A group may have only leaf children in v1. Group children paint in array order, with `z` first and array order as the tie-break. `stagger.eachMs` adds `rank × eachMs` to child start time. `start` ranks array order; `end` reverses it; `center` sorts by distance from the center index with lower indexes first on ties. Group motion is inherited, so a card, icon and label can move together while child tracks add follow-through. Reusable named animation presets and direct `parent` references are outside v1; group containment and authored tracks are the supported composition model.

An `adapter` layer makes the seek adapter reachable from a storyboard without embedding executable code. `adapterId` must name an adapter registered by the host; `source` is a project-root asset and `config` is validated against that adapter's declared JSON Schema. The built-in `lottie` adapter requires a Bodymovin JSON `source` and accepts `{ "firstFrame": 0, "lastFrame": 60, "frameRate": 30, "playbackRate": 1 }`; it maps layer-local milliseconds to that frame interval and seeks through the Lottie frame setter. A registered adapter must implement `seekFrame(frameIndex)` and redraw synchronously. Unregistered IDs fail with `ADAPTER_NOT_REGISTERED`; arbitrary storyboard JavaScript is not supported. Static SVG remains available as the existing path/illustration input and is seek-independent.

Text defaults are Arial, 32 px, weight 400, `#111111`, left alignment, 1.2 line height, zero letter spacing, wrapping on, zero inset and no auto-fit. `autoFit: shrinkText` shrinks only at the sampled frame to fit the authored box; `none` keeps size and clips overflow. `runs` is the authored rich-text sequence; when present, concatenated run text must equal `text`. `rangeTracks` indexes Unicode grapheme clusters in the concatenated run text with a half-open `[start,end)` range, allowing color, font size, opacity and position changes on line/word/character spans. `split` selects the layer's unit (`none` means one unit); `reveal.unit` overrides it. Reveal creates units in reading order with each unit delayed by `staggerMs`; `typewriter` reveals grapheme clusters. `counter` interpolates the numeric value over the layer interval and formats it with decimals, prefix and suffix. Explicit `\n` stays a paragraph break; automatic wrapping is never converted into hard line breaks. `bullets` is an alternative paragraph list, not a string convention. For PPTX, `scaleX/scaleY` scale the editable box around the authored anchor and multiply run font size by `sqrt(scaleX × scaleY)`; non-uniform scale can change wrapping and is reported as a layout limitation.

Chart data is inline only in v1. `categories` supplies labels; every non-scatter series has one value per category. Scatter requires equally sized numeric `xValues` and `values`. `stacked` is removed: `columnStacked`, `columnStacked100`, `barStacked`, `barStacked100` and `areaStacked` state orientation and normalization explicitly. A combo chart has per-series `kind` and axis; it requires at least one column or line series. Stacked charts allow only one orientation and no secondary axis. The deterministic HTML chart is SVG: axes, labels, grid, series and marks are emitted from the same normalized data used by PPTX. `build.mode` starts at layer-local time zero: it grows columns/bars from zero, draws line/area paths, or reveals series in order; it applies only to column, bar, line, area and combo charts. Default build duration is 600 ms and `staggerMs` defaults to zero. `dataStates[].atMs` is chart-layer-local and values interpolate linearly only when category order and series names/count match. The default palette is `#2563EB`, `#F97316`, `#10B981`, `#A855F7`, `#EF4444`, then repeated; defaults are Arial 14 px, axis titles empty, number format `#,##0.##`, and grid `#D9DDE3`.

`effects.mask` is an object naming a same-scene `shape` layer by `sourceLayerId`; supported mattes are alpha and luma, optionally inverted and feathered in CSS pixels. The source layer is hidden as a standalone visual and follows its own tracks, so animating it animates the reveal. Unsupported complex masks rasterize only the affected visual in PPTX; text remains native. A missing or non-shape source is `MASK_SOURCE_INVALID`.

An optional 2D scene camera applies `translate(anchor + (x,y)) rotate(rotation) scale(zoom) translate(-anchor)` to the stage, where anchor defaults to stage center, x/y are pixel pans, and rotation is degrees. Camera tracks use scene-local time and the same interpolation rules. PPTX samples the camera at `pptxAtMs` by transforming each native object's geometry and font size; unsupported effects follow the normal per-layer fallback.

The scene must provide exactly one of `startMs` and `after`. `after` must reference an earlier scene; `gapMs` is legal only with `after`. `durationMs` on each scene is required. Root `durationMs`, when supplied, cannot end before any scene. Scene gaps show the storyboard background (`#FFFFFF` by default); an absent scene background inherits it. Layer defaults are opacity 1, rotation 0 degrees, scale 1, anchor center, z 0, no fill/stroke/shadow, and non-decorative. Image fit is contain. Stable layer IDs are unique across the storyboard. A `pptxAtMs` outside `[0, scene.durationMs)` is invalid; when omitted it samples `durationMs - 1` and the report warns if a native layer is still transparent, off-slide, or has clipped text at that pose.

App-demo action requirements are conditional: `goto` needs a localhost `url`; `click` needs `locator`; `fill` needs locator and value; `press` needs locator and key; `waitFor` needs locator. Role locators require `name` and use exact matching; test-id and CSS locators require their corresponding value. Each action timeout is `timeoutMs` (default 5000); missing/ambiguous locators fail as `STEP_LOCATOR_NOT_FOUND` or `STEP_LOCATOR_AMBIGUOUS`. Step times must be strictly increasing. Fixture `urlPattern` uses Playwright URL glob syntax, method defaults to GET, and every external request must match a fixture; unmatched requests are blocked and fail with `FIXTURE_NOT_FOUND`. The CSS viewport equals the app layer's width and height, and device scale factor 2 produces a capture bitmap twice those dimensions. Cursor x/y are viewport CSS pixels with origin at top-left. `readySelector` uses `readyTimeoutMs` (default 30000), overridden by CLI `--timeout`. App content still must expose deterministic seek behavior.

Additional cross-field validation checks unique scene/layer/marker IDs; exactly one start mode per scene; scene ordering references; scene, layer, group-child, track and overlay bounds; strictly increasing resolved track times; chart dimensions/state compatibility; scatter x/y counts; caption `startMs < endMs`; app conditional fields, exact time ordering and overlay/layer bounds; mask sources; adapter schemas; and realpath asset containment. All independent validation failures are returned together.

## 5. Rendering and export parts

### 5.1 Timeline and easing

The compiler resolves one storyboard timeline and an HTML composition. Numeric track times are local to the layer start; group-child tracks are local to the child start; camera tracks and captions are scene-local; scene start and marker positions are storyboard-relative; app steps/overlays are app-layer-local; `check --at` is storyboard-relative. Narration `audioOffsetMs` is scene-local and each word time is audio-local before that offset is applied.

| Time field or option | Origin | Conversion |
|---|---|---|
| `scene.startMs` | Storyboard | Direct; `after` derives from predecessor end plus `gapMs` |
| `scene.durationMs` / root `durationMs` | Duration, not a timestamp | Root duration is optional and otherwise derived from latest scene end |
| layer `startMs`, `durationMs` | Containing scene | Add scene start for storyboard time |
| group child `startMs`, `durationMs` | Containing group | Add all parent starts, then scene start |
| `tracks[].keyframes[].atMs` integer | Layer | Add layer/parent/scene starts; object form resolves marker or word event first |
| scene `camera.tracks[].keyframes[].atMs` | Scene | Add scene start |
| `markers[].atMs` | Named scene | Add referenced scene start |
| chart `dataStates[].atMs` | Chart layer if integer | Add chart/parent/scene starts; symbolic object resolves marker/word then converts to chart-local time |
| narration `audioOffsetMs` | Scene | Add scene start; word-timing `startMs/endMs` are audio-local and add this offset |
| caption `startMs/endMs` | Scene | Add scene start |
| app `steps[].atMs`, `cursor[].atMs`, `highlights[].startMs` | App-demo layer | Add app layer/parent/scene starts |
| `pptxAtMs` | Scene | Sample that scene only; default `durationMs - 1` |
| CLI `check --at` | Storyboard | Direct absolute time |

Worked conversion: a scene starts at 1000 ms; its narration offset is 120 ms; word index 3 starts at 600 ms in the audio; an app/title layer starts at scene-local 200 ms. A track keyframe `{ "wordIndex": 3, "offsetMs": 40 }` resolves to storyboard time 1760 ms and layer-local time 760 ms. At 30 fps the first frame whose sample time is at or after that event is frame 53 (`floor(53×1000/30)=1766` ms). A caption at scene-local 720 ms is storyboard time 1720 ms and first appears at frame 52 (1733 ms).

For frame `n`, renderer time is exactly `tMs = floor(n × 1000 / 30)`. The frame count is `ceil(durationMs × 30 / 1000)`, with indexes from zero through count minus one. No layer reads wall time, unseeded randomness or an uncontrolled timer to choose visible state. Each property track is resolved independently as specified in §4.1. Named ease curves are fixed: `linear`=(0,0,1,1), `ease-in`=(0.42,0,1,1), `ease-out`=(0,0,0.58,1), `ease-in-out`=(0.42,0,0.58,1). Cubic Bézier uses the schema's four controls with x in [0,1]. `step-start` changes at interval start; `step-end` changes at interval end. Duplicate resolved times, non-finite values and values outside the layer interval fail validation.

HTML exposes `window.__timelines` (one registered adapter per animated subsystem) and `window.__sceneEngine.seek(ms)`. The latter updates every script-driven state and redraws before capture. The adapter contract is `seekFrame(frameIndex)`; it computes time from the integer frame index and supports backward seeks. Capture `document.getAnimations()` once after readiness, pause every returned animation and set its `currentTime` on each seek. Pause before `startViewTransition()`. Seek root SVG SMIL with `pauseAnimations()` and `setCurrentTime(seconds)`. Canvas adapters redraw from a pure time input. Built-in and registered adapters use paused seekable timelines; history-dependent simulations fail as `UNSEEKABLE`.

Scene intervals are composited back-to-front in scene array order. Non-overlapping adjacent intervals cut at the boundary; overlapping intervals show both scenes and have no implicit transition. Any crossfade is authored as explicit scene/layer opacity tracks. A repeated stable `!!` name requests PowerPoint Morph for that object only; video output does not inherit Morph.

Before rendering with HyperFrames, run its `lint`; then render with local version 0.8.78 and telemetry disabled. HyperFrames owns normal clip scheduling, frame workers and audio muxing. scene-engine always transcodes its output with FFmpeg to the required delivery profile and probes it. Never rely on HyperFrames' raw encoding profile: the measured delivery render was High level 5.0, above this tool's 4.1 target. In `auto` mode, a missing HyperFrames CLI selects the fallback and records that choice; a lint or render failure is reported rather than silently retried with different semantics. Explicit `--renderer hyperframes` fails if the binary is missing.

### 5.2 Deterministic frames by seeking

For each requested frame, set the canonical time, seek every registered timeline and layer, await only explicit ready gates, and capture once the page reports `seekComplete`. The page clock is installed and paused before navigation when a capture depends on timers, but fake time alone does not control CSS or Web Animations. The seek call—not a real-time wait or CDP virtual-time tick—sets their state.

Use HyperFrames frame adapters for its normal renderer. For app capture and fallback, use Playwright screenshot-per-frame; on Linux the implementation may use BeginFrame after the seek to make capture atomic, while still using the same time mapping. On macOS use `Page.captureScreenshot`; BeginFrame is unavailable there. If any animation or scene cannot be set to an explicit time and then sought backward to an earlier time with the same result, report the offending adapter/layer and fail the render with a seekability error. Do not silently switch to wall-clock capture.

### 5.3 Narration and captions

Each scene's narration supplies required descriptive text, optional WAV/AIFF/MP3 audio, a scene-local audio offset, gain and optional word-timing JSON. The word file is `{"format":"scene-engine/word-timings@1","language":"en","words":[{"text":"Hello","startMs":0,"endMs":300}]}`; times are audio-local, words are ordered, and every end is after its start. Text defaults into speaker notes, but the caller may override it with `scene.notes`. There is no hosted TTS call. The caller can pass locally generated audio/timings through these same inputs.

The audio duration is probed before render. If a narration file's `audioOffsetMs + duration` exceeds its scene duration, or its word times fall outside the audio, validation/render fails with `NARRATION_OVERFLOW`; audio is never truncated or allowed to overlap the next scene implicitly. No scene duration is inferred from narration: scene `durationMs` is authored, while `after` can shift later scenes. This makes timing ownership explicit.

Captions are authored as scene-local cue arrays or set to `"fromWordTimings"`. Generation requires `narration.wordTimings`; it greedily groups consecutive words, breaking at sentence punctuation, a silence over 500 ms, 7 seconds of cue span, or the point where text no longer fits two lines of 42 characters. Cue timestamps use word start/end plus scene `audioOffsetMs`, then convert to scene-local time. A cue crossing a scene boundary is split at that boundary. Shorter cues are allowed at boundaries and reported. Cues are sorted and non-overlapping. Lint also enforces at most 20 characters/second in English or 17 in Vietnamese. `--captions sidecar` writes WebVTT beside the MP4; `burn-in` renders with libass; `both` does both; `none` emits neither. Default is sidecar when cues exist, otherwise none. WebVTT starts with `WEBVTT` and has increasing cue times. Video without narration still has a silent AAC-LC stereo track. Supplied narration is mixed by two-pass FFmpeg `loudnorm` (`I=-16`, `TP=-1.5`, `LRA=11`, `linear=true`) and encoded AAC-LC, 48 kHz stereo, 192 kb/s.

### 5.4 Native-PPTX writer

One scene produces one 13.333×7.5-inch slide. CSS px map to 6,350 EMU (0.5 pt); text px map to half as many points. The scene's native pose is sampled at scene-local `pptxAtMs`, defaulting to `durationMs - 1` so entrance motion normally reaches its final visible state. The report warns if a native object is below 10% opacity, off-slide or has clipped text at the sampled pose. Arbitrary declarative tracks are sampled at that pose; they are not misrepresented as editable PowerPoint motion. Only `fade`, `flyInLeft`, `flyInRight`, `flyInUp`, `flyInDown` and `wipeLeft` write entrance timing XML; they start at the layer's scene-local `startMs` and last `entranceDurationMs` (default 500 ms). Stable names beginning `!!` that repeat across adjacent slides receive Morph XML with a fade fallback.

Map the one-to-one subset as follows:

| Scene element | PPTX representation |
|---|---|
| Positioned rectangle, rounded rectangle, ellipse, line; solid or dashed stroke; solid fill or supported linear gradient; one outer shadow; shape opacity | Native `p:sp` and DrawingML preset geometry/fills/effects; strip the theme `p:style` that adds unwanted shadows |
| Text, rich-text runs and bullet paragraphs | Native editable `txBody` with word wrap on, zero insets, authored paragraph breaks only and the declared autofit policy |
| SVG path using M/L/H/V/C/S/Q/T/Z (arcs converted to cubics), SVG rect/circle/ellipse/line | Native custom geometry `a:custGeom` and DrawingML preset geometry |
| Raster image | Native editable-position `p:pic` |
| Whole SVG illustration | SVG picture `asvg:svgBlip` plus a Chromium PNG fallback |
| Table | Native `graphicFrame` table |
| Data chart (column, bar, line, area, pie, doughnut, scatter, explicit stacked variants, combo) | Native chart `graphicFrame`, chart XML and a minimal embedded workbook with matching category/value cells; sample animated data at `pptxAtMs` |
| Captured app-demo or supplied video | Native movie picture, poster frame and supported playback timing from the layer's `playback` options |
| Speaker notes | Native notes slide from `scene.notes`, falling back to `scene.narration.text` |

Use python-pptx 1.0.2 for supported editable objects. Standard-library ZIP/XML patches write custom geometry, SVG relationships/fallbacks, Morph, entrance/autoplay timing, movie relationships and combo/mixed-axis charts where python-pptx has no API. No fonts are embedded. A requested font outside the writer's known set (`Arial`, `Aptos`, `Calibri`, `Georgia`, `Times New Roman`, `Verdana`) is emitted as Arial and reported as a substitution; all text remains native. The report lists requested and emitted font for every text layer and slide.

Every chart gets a minimal embedded workbook generated with standard-library ZIP/XML. Before export completes, validate every category/value formula range against the embedded sheet's actual cells and cached values. `Edit Data` compatibility on Microsoft PowerPoint is an owner check; the automated workbook consistency check does not prove Office's UI behavior. If an unsupported combination cannot be written as valid native objects, use this ordered fallback and report it per slide/layer: (1) rebuild CSS layout as positioned boxes, recording that flex/grid no longer reflows; (2) whole-element SVG picture with PNG fallback; (3) 2× Chromium PNG for unsupported visual effects. Text is excluded from fallback PNGs and emitted once as native text above the visual; unsupported text effects are dropped and reported rather than turning text into a picture. Rasterize filters, backdrop-filter, blend modes, masks, complex clip-paths, conic/multiple backgrounds, gradient text, text-on-path, 3D transforms and canvas/WebGL. Do not rasterize a data chart when the native chart writer can express its data.

Sort objects by ascending `z`, then source array order; later objects are above earlier objects. `readingOrder` controls screen-reader order; ties and unspecified values use ascending `z`, then array order. A group becomes one native `p:grpSp`, retaining editable children. Each layer has `alt`, `decorative` and `readingOrder`; decorative objects are marked as decorative, and non-decorative objects without alt text are reported. Raster fallback metadata carries source-layer alt text. This is metadata checking, not a claim that a slide passes Microsoft's full Accessibility Checker.

App-demo capture output is encoded per app-demo layer to the required 1920×1080 H.264 High@4.1/yuv420p/BT.709/30 fps/AAC profile with its poster frame; supplied `videoLayer.src` media is transcoded to the same profile before embedding. The movie object retains authored placement and uses contain-fit letterboxing when its aspect ratio differs. `--embed-video <file.mp4>` appends one 16:9 playback slide after all scene slides, with the movie filling the slide; it never duplicates the whole-storyboard movie onto every slide. V1 does not embed caption tracks in PPTX. The export report records `captionsEmbedded: false` and the available sidecar (if any) on every affected slide. Per-layer autoplay, looping, hide-until-play, start delay and full-screen map only to the declared video options; other keyframe animation remains a sampled static pose.

Slide advance timing is written from each scene's `durationMs`. Narration text feeds notes, but narration audio is not embedded in scene slides. The standard scene slides remain individually editable. V1 does not write a custom theme, master placeholders, slide-number placeholder or footer; those capabilities are deferred to v2.

The export report records every embedded media and fallback asset size. PNG fallbacks are optimized losslessly; warn when the final PPTX exceeds 256 MB, but do not silently recompress or omit authored content.

| Viewer | V1 support statement |
|---|---|
| Microsoft PowerPoint for Windows and Mac | Target format, but requires the manual owner check below; the automated suite does not prove playback compatibility |
| Apple Keynote | Degraded import only; `osascript` import/PDF smoke check when installed; SVG, Morph, combo charts and movie timing may change |
| Google Slides | Unsupported in v1; import may lose workbook links, Morph and embedded video |

Before publishing a PPTX, validate every package part written by scene-engine against vendored ECMA-376 schemas, including custom geometry, chart, SVG extension, Morph, movie relationship and timing XML; also verify internal relationship targets and content-type declarations. Then run the python-pptx edit/save/reopen round trip (change text, shape position and chart data, and verify the changed cells/ranges). On this Mac, LibreOffice is installed: use headless UNO automation to open and save the deck as a new PPTX, reopen that round-tripped file, then render both original and round-tripped decks to PDF. Keynote is installed: import the exported PPTX through `osascript`, confirm the document opens and export a PDF; record import warnings. These are structural and alternate-viewer smoke checks. They do **not** prove Microsoft PowerPoint opens without a repair prompt, preserves Edit Data behavior, Morph, SVGs, video playback or animation. PowerPoint is not installed on the build Mac. A manual owner check in current Microsoft PowerPoint for Windows and Mac remains required before release: open with no repair prompt, inspect native charts and Edit Data, play embedded/app-demo videos, and verify Morph/entrance timing.

The editability acceptance round trip opens the generated file with python-pptx, changes a native text value and shape position, replaces chart data, saves a second deck, and reopens it. The second read must find the changed text and geometry, a chart object with the changed category/value data, and an embedded workbook. Run `soffice --headless --convert-to pdf` on both decks as a layout smoke check when LibreOffice is installed. This proves object-level round-trip editability; it does not claim Microsoft PowerPoint playback was tested.

### 5.5 App-demo capture

The app-demo layer addresses a real local web app with source access and a runnable development server. `url` must be localhost or 127.0.0.1 and the layer must name a `readySelector`. Register response fixtures before navigation with Playwright routing; use the app's MSW handlers if its project supplies them. Fixture URL patterns use Playwright glob syntax. Requests to the local app origin may load its own app assets; any request to another origin must match a fixture. Unmatched external requests are blocked and return `FIXTURE_NOT_FOUND`, never passed through to the network. Install and pause Playwright's clock before `goto`, pin locale and timezone, and keep scripted interactions in ascending app-layer-local time. Action fields are conditional as defined in §4.1. Role/name matching is exact, test-id and CSS locators must resolve uniquely, and each action has its own `timeoutMs` (default 5000). A missing/ambiguous step locator is `STEP_LOCATOR_NOT_FOUND`/`STEP_LOCATOR_AMBIGUOUS`; missing readiness is `APP_LOAD_FAILED`. Wait for selectors and explicit asset readiness; never use sleeps to decide when a frame is ready.

The browser's CSS viewport is exactly the app layer's width and height; device scale factor 2 makes the capture bitmap twice those dimensions. Cursor coordinates are CSS pixels in that viewport, origin at top-left. Replace private data in route fixtures before display. Capture frames in increasing frame-index order, set every seekable animation to the corresponding time and write an immutable frame sequence. Its manifest hashes canonical storyboard JSON, selected layer JSON, fixture body bytes, browser version and the caller-supplied `appBuildId`. `appBuildId` is mandatory when reusing frames through `--frames-dir`; this lets the caller invalidate captures after rebuilding the local app. The manifest sequence makes the stateful click path repeatable and lets the enclosing composition seek in either direction. Cursor positions/click ripples and highlight rectangles are separate deterministic overlays. A live external response, unavailable locator or unseekable animation is a capture error.

A canvas/WebGL/video animation that cannot be adopted by a seek adapter, an app that cannot be fixture-backed, or an app that fails its ready gate causes a clear nonzero result with the URL, step/frame and reason. This design does not silently produce a real-time screencast: research found Playwright's own screencast is real-time VP8 at 25 fps, suitable for run receipts but not the required MP4.

### 5.6 Fallback renderer

The fallback reads the same compiled scene HTML, JSON model, assets and seek adapters as HyperFrames. It uses Playwright to set `window.__sceneEngine.seek(tMs)`, captures one PNG per output frame, and pipes the ordered image sequence and audio inputs to FFmpeg. It must write the same MP4 profile, WebVTT options, poster and JSON report as the HyperFrames path. It may be slower; it may not change scene semantics, timeline, easing, caption timing or app-demo frames. For an identical pinned browser and fonts, test the same keyframes against both paths and require the frame comparison policy recorded in the report (byte equality where capture primitives match; otherwise per-pixel difference and a reviewer brief).

## 6. Command-line interface

Commands use `scene-engine <command> [options]`. Every command writes one JSON document to stdout; progress, HyperFrames output and FFmpeg logs go to stderr. No command prints human prose to stdout.

Every stdout document has this common shape: `{"format":"scene-engine/result@1","command":"render","ok":true,"exitCode":0,"files":[],"errors":[],"warnings":[],"result":{}}`. `files[]` items are `{role,path,bytes,sha256}`. `errors[]` items are `{code,message,pointer,sceneId,layerId,frame,path,hint,severity:"error"}`; `warnings[]` use the same fields with severity `warning`; unavailable context fields are `null`, not omitted. Each command's `result` fields are listed below. The error `code`, not message text, is the branch key.

Exit codes are stable: `0` completed; `1` a requested visual/media/profile/caption/PPTX structural/seekability check failed; `2` malformed input, unknown flag, invalid schema, missing storyboard or missing project asset; `3` required executable/process failure, missing explicit renderer, app navigation/readiness/step/fixture failure, or timeout. `auto` renderer falls back only when HyperFrames is absent; it does not retry after a lint/render failure. Failed render/export artifacts are written to a temp directory and removed; an explicitly requested diagnostic report is retained and listed.

| Error code | Exit | Trigger and useful context |
|---|---:|---|
| `CLI_USAGE`, `STORYBOARD_MISSING`, `JSON_INVALID`, `SCHEMA_INVALID`, `TIME_REFERENCE_INVALID`, `TRACK_VALUE_INVALID`, `ASSET_MISSING`, `PATH_OUTSIDE_ROOT` | 2 | Unknown command/flag, missing storyboard, parse/schema/scene-time/track-value error, asset absent at validation or realpath escape; include pointer, path and hint |
| `NARRATION_OVERFLOW`, `CAPTION_LINT_FAILED`, `FFMPEG_PROFILE_MISMATCH`, `HYPERFRAMES_LINT_FAILED`, `UNSEEKABLE` | 1 | Contract check failure; include scene/layer/frame and corrective hint where applicable |
| `HYPERFRAMES_MISSING`, `HYPERFRAMES_RENDER_FAILED`, `FFMPEG_FAILED`, `RENDER_TIMEOUT`, `ASSET_MISSING_AT_RENDER` | 3 | Required renderer/tool failure or asset disappeared after validation; include path/timeout and process diagnostic |
| `APP_LOAD_FAILED`, `STEP_LOCATOR_NOT_FOUND`, `STEP_LOCATOR_AMBIGUOUS`, `FIXTURE_NOT_FOUND` | 3 | App step/readiness/fixture failure; include URL, scene/layer, step index and locator/path |
| `ADAPTER_NOT_REGISTERED`, `MASK_SOURCE_INVALID`, `CAPTURE_MANIFEST_MISMATCH` | 2 | Storyboard references an unavailable adapter/mask or supplied captures do not match the storyboard hash |
| `PPTX_SCHEMA_INVALID`, `PPTX_WORKBOOK_MISMATCH`, `PPTX_ROUNDTRIP_FAILED` | 1 | PPTX structural validation or editability check failed; include slide/part/path and hint |

| Command | Contract |
|---|---|
| `scene-engine validate <storyboard.json>` | `result` is `{valid:boolean,sceneCount:number,layerCount:number,durationMs:number,frameCount:number}`; invalid entries appear in common `errors[]`. |
| `scene-engine render <storyboard.json> --out <file.mp4> [--renderer auto|hyperframes|fallback] [--captions sidecar|burn-in|both|none] [--poster <file.png>] [--frames-dir <dir>] [--timeout <ms>]` | Capture app-demo layers, compile, render, normalize and probe. `result` is `{durationMs,frameCount,renderer:{name,version},streams:[{type,codec,width,height,frameRate,sampleRate,channels}],diagnostics}`; `files[]` lists MP4, poster and VTT. Default renderer is `auto`: HyperFrames when installed, fallback otherwise. |
| `scene-engine capture <storyboard.json> --scene <id> [--layer <id>] --out-dir <dir> [--timeout <ms>]` | Capture the named app-demo layer to immutable frames and a manifest. If `--layer` is omitted, the scene must contain exactly one app-demo layer. `result` is `{sceneId,layerId,appBuildId:string|null,cssViewport:{width,height},deviceScaleFactor,frameCount,fixtureCount,hashes,manifestPath,storyboardHash,layerHash,browserVersion}`. |
| `scene-engine export-pptx <storyboard.json> --out <file.pptx> [--embed-video <file.mp4>] [--report <file.json>] [--verify|--no-verify]` | Write one editable scene slide; optional whole-storyboard MP4 goes on an appended 16:9 playback slide. `result` is `{slideCount,slideAdvanceMs,mappings:[{sceneId,slide,layerId,representation,reason,alt,decorative}],fontReport,workbookChecks,openXmlValidation,roundTrip,captionsEmbedded,captionsBySlide:[{slide,embedded,sidecarPath}]}`. `--verify` is default; `--no-verify` skips python-pptx/LibreOffice round trips only. ECMA-376 schema validation always runs. |
| `scene-engine check <storyboard.json> [--at <ms,...>] [--pptx <file.pptx>] [--out-dir <dir>] [--rk <path-to-rk>] [--strict]` | Capture authored keyframes plus scene start/mid/end, staticize and call `rk check`. If PPTX is supplied, render slides through LibreOffice and call `rk check --pdf`. `result` is `{timesMs,reports:[{target,status,reason,rkReportPath}],pptxDiagnostics}`. Missing `rk` is skipped unless strict. |
| `scene-engine selftest [--case ATnn] [--strict]` | `result` is `{cases:[{id,status,errors}],ok:boolean}`; expected negative cases pass when the specified stable code/exit pair matches. |

Render options:

| Option | Meaning | Default |
|---|---|---|
| `<storyboard.json>` | Local storyboard; all referenced inputs stay within its project root | required |
| `--root <dir>` | Explicit asset project root; outputs are not restricted to it | storyboard directory |
| `--out <path>` | MP4 or PPTX destination | required for render/export |
| `--renderer <name>` | `auto`, `hyperframes` or `fallback` | `auto` |
| `--captions <mode>` | Sidecar, burn-in, both or none | sidecar when cues exist |
| `--poster <path>` | PNG poster extracted at the first non-empty frame | alongside the MP4 |
| `--timeout <ms>` | Bound app readiness and renderer calls | 30000 |
| `--frames-dir <dir>` | Reuse a prior `capture` output only when canonical storyboard/layer JSON, fixture body hashes, caller `appBuildId` and browser version all match; otherwise fail with `CAPTURE_MANIFEST_MISMATCH` | absent; capture afresh |
| `--layer <id>` | Select one app-demo layer for `capture` | required if scene has multiple app-demo layers |
| `--at <ms,...>` | Additional explicit times for frame and visual checks | authored keyframes plus scene start/mid/end |
| `--rk <path>` | render-kit `bin/rk` executable | `SCENE_ENGINE_RK`, then `rk` on PATH; otherwise skipped |
| `--strict` | Treat skipped external checks as failures | enabled when `CI=true`, otherwise off |

The following output schema is the machine contract for all six commands; each `oneOf` branch is the command-specific schema. Unrecognized command flags and malformed output documents are errors, not extensions.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "oneOf": [
    { "$ref": "#/$defs/validate" }, { "$ref": "#/$defs/render" },
    { "$ref": "#/$defs/capture" }, { "$ref": "#/$defs/exportPptx" },
    { "$ref": "#/$defs/check" }, { "$ref": "#/$defs/selftest" }
  ],
  "$defs": {
    "base": { "type": "object", "required": ["format", "command", "ok", "exitCode", "files", "errors", "warnings", "result"], "properties": {
      "format": { "const": "scene-engine/result@1" }, "command": { "type": "string" }, "ok": { "type": "boolean" }, "exitCode": { "enum": [0,1,2,3] },
      "files": { "type": "array", "items": { "type": "object", "required": ["role", "path", "bytes", "sha256"], "properties": { "role": { "type": "string" }, "path": { "type": "string" }, "bytes": { "type": "integer", "minimum": 0 }, "sha256": { "type": "string" } } } },
      "errors": { "type": "array", "items": { "$ref": "#/$defs/diagnostic" } }, "warnings": { "type": "array", "items": { "$ref": "#/$defs/diagnostic" } }
    } },
    "diagnostic": { "type": "object", "required": ["code", "message", "pointer", "sceneId", "layerId", "frame", "path", "hint", "severity"], "properties": {
      "code": { "type": "string" }, "message": { "type": "string" }, "pointer": { "type": ["string", "null"] }, "sceneId": { "type": ["string", "null"] }, "layerId": { "type": ["string", "null"] }, "frame": { "type": ["integer", "null"] }, "path": { "type": ["string", "null"] }, "hint": { "type": ["string", "null"] }, "severity": { "enum": ["error", "warning"] }
    } },
    "validate": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "validate" }, "result": { "type": "object", "required": ["valid", "sceneCount", "layerCount", "durationMs", "frameCount"], "properties": { "valid": { "type": "boolean" }, "sceneCount": { "type": "integer" }, "layerCount": { "type": "integer" }, "durationMs": { "type": "integer" }, "frameCount": { "type": "integer" } } } } }] },
    "render": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "render" }, "result": { "type": "object", "required": ["durationMs", "frameCount", "renderer", "streams", "diagnostics"], "properties": { "durationMs": { "type": "integer" }, "frameCount": { "type": "integer" }, "renderer": { "type": "object", "required": ["name", "version"], "properties": { "name": { "enum": ["hyperframes", "fallback"] }, "version": { "type": ["string", "null"] } } }, "streams": { "type": "array", "items": { "type": "object", "properties": { "type": { "type": "string" }, "codec": { "type": "string" }, "width": { "type": ["integer", "null"] }, "height": { "type": ["integer", "null"] }, "frameRate": { "type": ["string", "null"] }, "sampleRate": { "type": ["integer", "null"] }, "channels": { "type": ["integer", "null"] } } } }, "diagnostics": { "type": "array", "items": { "type": "object" } } } } } }] },
    "capture": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "capture" }, "result": { "type": "object", "required": ["sceneId", "layerId", "appBuildId", "cssViewport", "deviceScaleFactor", "frameCount", "fixtureCount", "hashes", "manifestPath", "storyboardHash", "layerHash", "browserVersion"], "properties": { "sceneId": { "type": "string" }, "layerId": { "type": "string" }, "appBuildId": { "type": ["string", "null"] }, "cssViewport": { "type": "object", "required": ["width", "height"], "properties": { "width": { "type": "number" }, "height": { "type": "number" } } }, "deviceScaleFactor": { "const": 2 }, "frameCount": { "type": "integer" }, "fixtureCount": { "type": "integer" }, "hashes": { "type": "array", "items": { "type": "string" } }, "manifestPath": { "type": "string" }, "storyboardHash": { "type": "string" }, "layerHash": { "type": "string" }, "browserVersion": { "type": "string" } } } } }] },
    "exportPptx": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "export-pptx" }, "result": { "type": "object", "required": ["slideCount", "slideAdvanceMs", "mappings", "fontReport", "workbookChecks", "openXmlValidation", "roundTrip", "captionsEmbedded", "captionsBySlide"], "properties": { "slideCount": { "type": "integer" }, "slideAdvanceMs": { "type": "array", "items": { "type": "integer" } }, "mappings": { "type": "array", "items": { "type": "object", "required": ["sceneId", "slide", "layerId", "representation", "reason", "alt", "decorative"], "properties": { "sceneId": { "type": "string" }, "slide": { "type": "integer" }, "layerId": { "type": "string" }, "representation": { "type": "string" }, "reason": { "type": ["string", "null"] }, "alt": { "type": "string" }, "decorative": { "type": "boolean" } } } }, "fontReport": { "type": "array", "items": { "type": "object", "required": ["sceneId", "layerId", "requested", "emitted", "status"], "properties": { "sceneId": { "type": "string" }, "layerId": { "type": "string" }, "requested": { "type": "string" }, "emitted": { "type": "string" }, "status": { "enum": ["exact", "substituted"] } } } }, "workbookChecks": { "type": "array", "items": { "type": "object" } }, "openXmlValidation": { "type": "object", "required": ["status", "partsChecked", "relationshipErrors"], "properties": { "status": { "enum": ["pass", "fail", "skipped"] }, "partsChecked": { "type": "integer" }, "relationshipErrors": { "type": "array", "items": { "type": "object" } } } }, "roundTrip": { "type": "object", "required": ["status", "text", "geometry", "chartData", "libreOffice"], "properties": { "status": { "enum": ["pass", "fail", "skipped"] }, "text": { "type": "string" }, "geometry": { "type": "string" }, "chartData": { "type": "string" }, "libreOffice": { "type": "string" } } }, "captionsEmbedded": { "const": false }, "captionsBySlide": { "type": "array", "items": { "type": "object", "required": ["slide", "embedded", "sidecarPath"], "properties": { "slide": { "type": "integer" }, "embedded": { "const": false }, "sidecarPath": { "type": ["string", "null"] } } } } } } } }] },
    "check": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "check" }, "result": { "type": "object", "required": ["timesMs", "reports", "pptxDiagnostics"], "properties": { "timesMs": { "type": "array", "items": { "type": "integer" } }, "reports": { "type": "array", "items": { "type": "object", "required": ["target", "status", "reason", "rk"], "properties": { "target": { "type": "string" }, "status": { "enum": ["pass", "fail", "skipped"] }, "reason": { "type": ["string", "null"] }, "rk": { "type": ["object", "null"], "required": ["exitCode", "reportPath", "report"], "properties": { "exitCode": { "type": ["integer", "null"] }, "reportPath": { "type": ["string", "null"] }, "report": { "type": ["object", "null"] } } } } } }, "pptxDiagnostics": { "type": "object" } } } } }] },
    "selftest": { "allOf": [{ "$ref": "#/$defs/base" }, { "properties": { "command": { "const": "selftest" }, "result": { "type": "object", "required": ["cases", "ok"], "properties": { "cases": { "type": "array", "items": { "type": "object", "required": ["id", "status", "errors"], "properties": { "id": { "type": "string", "pattern": "^AT[0-9]{2}$" }, "status": { "enum": ["pass", "fail", "skipped"] }, "errors": { "type": "array", "items": { "$ref": "#/$defs/diagnostic" } } } } }, "ok": { "type": "boolean" } } } } }] }
  }
}
```

## 7. Reuse render-kit

scene-engine does not reimplement render-kit checks. For each keyframe and selected scene start/mid/end, the engine seeks the composition using the canonical frame time, serializes that selected state as a static HTML stage marked with `data-rk-stage`, and emits the existing `data-rk-chart`, series, mark and data-value markup when the scene contains charts. It then calls the configured `rk check` on that static stage and stores each `report.json` and PNG. Staticizing the frame first avoids asking render-kit to drive scene-engine's script and canvas adapters.

For PPTX slides, convert the generated PPTX to PDF and PNG with the configured LibreOffice `soffice`, place each rendered PNG in a fixed-size HTML stage and run `rk check --pdf` on that stage. Checks that cannot inspect image pixels or apply to a single image stay `n/a` or are reported as skipped; retain all statuses and reasons. Native editability, embedded workbook and XML checks remain the PPTX writer's separate structural round trip; do not duplicate `rk`'s checks.

## 8. Acceptance tests

Each row is runnable with its named command. `scene-engine selftest --case ATnn` runs the same row using checked-in fixtures.

| AT | Part | Given | When | Then |
|---|---|---|---|---|
| AT01 | scene model | A valid storyboard with text, image, shape and chart layers | `scene-engine validate fixtures/at01/storyboard.json` | Exit 0; JSON reports four layers and the declared 30 fps, 1920×1080 canvas |
| AT02 | scene model | A storyboard with a duplicate layer id and an asset path escaping its project directory | `scene-engine validate fixtures/at02/storyboard.json` | Exit 2; JSON names both JSON pointers and validation reasons |
| AT03 | timeline | A layer with linear, ease-in-out and cubic-Bézier keyframes | `scene-engine selftest --case AT03` | Sampled property values match the easing reference values within 0.01 px at each asserted frame |
| AT04 | timeline | Two scenes with an explicit 300 ms opacity overlap | `scene-engine render fixtures/at04/storyboard.json --out out/at04.mp4 --renderer fallback` | Mid-overlap frame contains both scenes with the specified interpolated opacity; no implicit transition is added |
| AT05 | seek | A page with CSS animation, CSS transition, WAAPI, SVG SMIL and registered canvas motion | `scene-engine selftest --case AT05` | Seeking 0→900→200→900 ms produces byte-identical PNGs for both 900 ms captures |
| AT06 | seek | A scene uses an animation adapter that cannot seek backward | `scene-engine render fixtures/at06/storyboard.json --out out/at06.mp4 --renderer fallback` | Exit 1; JSON identifies the layer/adapter and reports the unsupported seek; no MP4 is published |
| AT07 | HyperFrames | A valid animated scene, HyperFrames 0.8.78 installed | `scene-engine render fixtures/at07/storyboard.json --out out/at07.mp4 --renderer hyperframes` | Telemetry is off; lint passes before render; normalized MP4 passes the profile probe |
| AT08 | HyperFrames | HyperFrames is absent from the local locked install | `scene-engine render fixtures/at07/storyboard.json --out out/at08.mp4 --renderer hyperframes` | Exit 3 with `HYPERFRAMES_MISSING`; no network fallback fetch occurs |
| AT09 | narration | A narration WAV, matching text and an offset cue | `scene-engine render fixtures/at09/storyboard.json --out out/at09.mp4 --captions none --renderer fallback` | Output contains AAC-LC 48 kHz stereo; voice starts at its offset; measured mix is normalized to the specified targets |
| AT10 | narration captions | Authored cues in English and Vietnamese | `scene-engine render fixtures/at10/storyboard.json --out out/at10.mp4 --captions sidecar --renderer fallback` | `at10.vtt` starts with WEBVTT, is monotonic, and meets the two-line and per-language character-rate limits or reports boundary exceptions |
| AT11 | narration captions | The same cues with the burn-in option | `scene-engine render fixtures/at10/storyboard.json --out out/at11.mp4 --captions burn-in --renderer fallback` | No VTT is emitted; sampled cue frames visibly contain the matching caption and non-cue frames do not |
| AT12 | PPTX | A scene with editable text, a native shape, SVG picture and supported chart | `scene-engine export-pptx fixtures/at12/storyboard.json --out out/at12.pptx --verify` | Round trip changes text, position and chart data; reopen reads those changes and an embedded workbook; LibreOffice renders all slides |
| AT13 | PPTX chart | A combo chart requiring bar and line series, which python-pptx's public chart API cannot create as one native chart | `scene-engine export-pptx fixtures/at13/storyboard.json --out out/at13.pptx --verify` | Hand-written chart XML contains both chart types, and values/categories match the embedded workbook cells |
| AT14 | PPTX fallback | A scene uses blur, blend mode and a 3D transform | `scene-engine export-pptx fixtures/at14/storyboard.json --out out/at14.pptx --report out/at14.json` | Unsupported pixels are rasterized at 2×; retained text stays native; the report lists each rasterized layer and reason |
| AT15 | app-demo capture | A local fixture-backed app with a ready selector, two scripted actions and cursor/highlight overlays | `scene-engine capture fixtures/at15/storyboard.json --scene demo --out-dir out/at15` | Two captures produce the same ordered frame hashes at 3840×2160; overlays land at their authored seek times |
| AT16 | app-demo capture | A local app never reaches its ready selector | `scene-engine capture fixtures/at16/storyboard.json --scene demo --out-dir out/at16 --timeout 1000` | Exit 3 with `APP_LOAD_FAILED`, the failing URL/selector is reported, and no partial sequence is marked complete |
| AT17 | app-demo seek | A local app draws an unsupported history-dependent canvas animation | `scene-engine capture fixtures/at17/storyboard.json --scene demo --out-dir out/at17` | Exit 1 with `UNSEEKABLE` and the exact frame/layer; no real-time capture is substituted |
| AT18 | fallback | HyperFrames is absent; storyboard has a golden frame and stream manifest | `scene-engine render fixtures/at18/storyboard.json --out out/at18.mp4 --renderer auto` | Exit 0; auto selects fallback and its frame states match the fixture manifest, with the declared captions and media streams |
| AT19 | render-kit key frames | Animated storyboard and configured sibling `rk` | `scene-engine check fixtures/at19/storyboard.json --at 500,1000 --rk ../render-kit/bin/rk` | `rk check` runs at both times; nested reports identify each frame and no check logic is reimplemented |
| AT20 | render-kit PPTX slides | Generated PPTX and LibreOffice available | `scene-engine check fixtures/at12/storyboard.json --pptx out/at12.pptx --rk ../render-kit/bin/rk` | Every rendered slide PNG is wrapped as a stage and checked by `rk check --pdf`; skipped checks retain their reasons |
| AT21 | MP4 PowerPoint profile | Any successful render with a poster and AAC track | `scene-engine selftest --case AT21` | ffprobe reports MP4, H.264 High level ≤4.1, yuv420p 1920×1080, 30/1 fps, BT.709 tags, AAC-LC 48 kHz stereo; file is below 256 MB |
| AT22 | CLI | Unknown command, malformed JSON, missing ffmpeg and renderer crash fixtures | `scene-engine selftest --case AT22` | Exit codes are respectively 2, 2, 3 and 3; each stdout value is one JSON document and progress stays on stderr |
| AT23 | scene model | A storyboard invokes registered Lottie and custom seek adapters with schema-valid config | `scene-engine validate fixtures/at23/storyboard.json` then seek fixture frames | Exit 0; adapter IDs/config are resolved, frame mapping is deterministic, and an unknown adapter returns `ADAPTER_NOT_REGISTERED` with its layer pointer |
| AT24 | timeline | One layer has independent sparse x, opacity, fill-color and trim tracks with different easing | `scene-engine selftest --case AT24` | Before the first keyframe the base value applies; only the keyed property changes; OKLab color and anchor-pivot samples match the reference values |
| AT25 | scene model | Nested group children use inherited transforms, stagger, an animated alpha matte and a moving 2D camera | `scene-engine selftest --case AT25` | Child order/delay and camera/mask poses match the golden frames; invalid/missing mask source reports `MASK_SOURCE_INVALID` |
| AT26 | scene model | Rich text uses line/word/grapheme reveal, range color change, a numeric counter and bullet paragraphs | `scene-engine selftest --case AT26` | Sample frames reveal and recolor only the authored grapheme ranges; counter formatting and paragraph order match the fixture |
| AT27 | scene model | SVG chart has grow/draw/reveal build modes, compatible data states, and a scatter series with xValues | `scene-engine selftest --case AT27` | HTML chart samples follow the normalized inline data; invalid stacked/combo constraints and mismatched scatter x/y counts fail validation |
| AT28 | timeline | Two scenes use `after`, a marker, a word-index track event, a local caption and an app-layer-local step | `scene-engine selftest --case AT28` | Later scene shifts by the predecessor duration; symbolic time resolves to 1760 ms/layer-local 760 ms; caption/app times convert per §5.1 and frame numbers match the worked example |
| AT29 | narration captions | Word timings have punctuation, a long gap, a 42-character boundary and an audio file that also overflows its scene | `scene-engine render fixtures/at29/storyboard.json --out out/at29.mp4 --captions sidecar` | Cues split by the specified greedy rules, offsets are applied once, and the overflow case exits 1 with `NARRATION_OVERFLOW`; no partial MP4 is published |
| AT30 | scene model | Storyboard omits optional root duration and scene background, and includes a symlink escaping the root | `scene-engine validate fixtures/at30/storyboard.json --root fixtures/at30` | Duration derives from scene ends, background defaults to white, and the realpath escape exits 2 with `PATH_OUTSIDE_ROOT` and the offending pointer/path |
| AT31 | app-demo capture | Two app-demo layers share one scene; fixtures include local assets and an external API; one step has a missing locator | `scene-engine capture fixtures/at31/storyboard.json --scene demo --layer checkout --out-dir out/at31 --timeout 5000` | Viewport equals layer CSS dimensions at DPR 2; exact role matching and cursor coordinates are correct; unmatched external requests and missing/ambiguous locators return their documented codes |
| AT32 | PPTX | Text has a `flyInLeft` entrance and non-uniform scale; default PPTX pose is omitted; native text uses bullets and an unavailable font | `scene-engine export-pptx fixtures/at32/storyboard.json --out out/at32.pptx --verify` | Pose samples at `durationMs - 1`; entrance timing is 500 ms from layer start; report warns on remaining invisible/clipped objects and scale-related reflow; bullets remain editable and text stays native with Arial substitution recorded |
| AT33 | PPTX | Deck contains every hand-written DrawingML part, a supported chart, SVG, Morph and movie timing | `scene-engine export-pptx fixtures/at33/storyboard.json --out out/at33.pptx --verify` | ECMA-376 validation passes every authored part and relationship; python-pptx and LibreOffice UNO open/save/reopen round trips pass; LibreOffice renders original and round-tripped decks to PDF |
| AT34 | PPTX chart | Native chart workbook contains values/categories and a combo chart with a secondary axis | `scene-engine export-pptx fixtures/at34/storyboard.json --out out/at34.pptx --verify` | Every chart formula points to cells with matching categories/values; workbook mismatch reports `PPTX_WORKBOOK_MISMATCH` and does not publish the deck |
| AT35 | PPTX | Deck has video/app-demo layers, a whole-storyboard `--embed-video` option and captions | `scene-engine export-pptx fixtures/at35/storyboard.json --out out/at35.pptx --embed-video out/story.mp4` | Every embedded stream passes the fixed PowerPoint profile; whole-story MP4 is on one appended slide; each slide reports `captionsEmbedded:false` and the sidecar path or null |
| AT36 | PPTX | On this Mac, Keynote and LibreOffice are installed; exported deck includes SVG, chart, Morph and video | `scene-engine selftest --case AT36` | `osascript` imports the deck into Keynote and exports a PDF; import warnings are reported; LibreOffice renders too. Result is labeled an import/render smoke check, not proof of PowerPoint behavior |
| AT37 | PPTX owner check | Release owner has current Microsoft PowerPoint for Windows and Mac | Manually open AT33/AT35 decks in both apps | Record app version, no-repair result, Edit Data cell edit, Morph/entrance behavior and video playback. This check remains outstanding on the build Mac because PowerPoint is not installed; no automated proxy can mark it pass |
| AT38 | CLI | All command success and failure fixtures, including missing asset at render, caption lint, renderer lint/timeout and PPTX failure | `scene-engine selftest --case AT38` | Each result validates against the command output schema; code and exit pairs match §6; failed render/export removes partial artifacts but retains an explicitly requested diagnostic report |
| AT39 | app-demo capture | Scene has multiple app-demo layers and a previously captured manifest from an exact storyboard/layer/browser build | `scene-engine capture fixtures/at39/storyboard.json --scene demo --layer checkout --out-dir out/at39` then render with `--frames-dir out/at39` | Only selected layer is captured; matching immutable frames with matching appBuildId are reused explicitly; mismatched storyboard, layer, fixture, app build or browser manifest fails with `CAPTURE_MANIFEST_MISMATCH`; no hidden cache is consulted |

All fixture paths in this table are relative to the scene-engine repository root. `fixtures/example/storyboard.json` and `fixtures/example/word-timings.json` below provide a complete starter shape; test fixtures live under the corresponding `fixtures/atNN/` directories.

### Example storyboard

This annotated example uses scene-local audio/captions and a second scene sequenced after the first. Asset files are project-root relative; the sample inputs are illustrative and may be replaced by the caller's files.

```json
{
  "format": "scene-engine/storyboard@1",
  "title": "From signal to decision",
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "durationMs": 5000,
  "language": "en",
  "scenes": [
    {
      "id": "intro",
      "startMs": 0,
      "durationMs": 3000,
      "background": "#FFFFFF",
      "pptxAtMs": 2999,
      "narration": { "text": "Signals become decisions.", "audio": "assets/voice.wav", "audioOffsetMs": 100, "wordTimings": "assets/word-timings.json" },
      "captions": "fromWordTimings",
      "layers": [
        { "id": "headline", "type": "text", "x": 120, "y": 90, "width": 1000, "height": 100, "startMs": 0, "durationMs": 3000, "text": "From signal to decision", "style": { "fontFamily": "Arial", "fontSize": 54, "fontWeight": 700, "color": "#111111", "align": "left" }, "reveal": { "unit": "word", "staggerMs": 70 } },
        { "id": "chart", "type": "chart", "x": 120, "y": 260, "width": 980, "height": 560, "startMs": 0, "durationMs": 3000, "kind": "column", "categories": ["Jan", "Feb", "Mar"], "series": [{ "name": "Signals", "values": [18, 31, 47] }], "build": { "mode": "grow", "durationMs": 900 }, "showLegend": false },
        { "id": "illustration", "type": "image", "x": 1220, "y": 300, "width": 520, "height": 430, "startMs": 0, "durationMs": 3000, "src": "assets/decision-map.png", "alt": "Three signal paths converge on one decision", "fit": "contain" }
      ]
    },
    {
      "id": "closing",
      "after": "intro",
      "durationMs": 2000,
      "layers": [
        { "id": "closing-title", "type": "text", "x": 160, "y": 350, "width": 1600, "height": 180, "startMs": 0, "durationMs": 2000, "text": "Make the next decision visible.", "style": { "fontFamily": "Arial", "fontSize": 62, "fontWeight": 700, "color": "#2563EB", "align": "center" } }
      ]
    }
  ]
}
```

`fixtures/example/word-timings.json`:

```json
{"format":"scene-engine/word-timings@1","language":"en","words":[{"text":"Signals","startMs":0,"endMs":430},{"text":"become","startMs":460,"endMs":820},{"text":"decisions.","startMs":850,"endMs":1450}]}
```

## 9. Decisions

| ID | Choice | Alternative rejected | Why and research basis |
|---|---|---|---|
| D1 | `auto` selects pinned HyperFrames 0.8.78 when installed and fallback only when it is absent; telemetry is disabled | Build a renderer from scratch, use Remotion, or follow the npm latest tag | The researched HyperFrames composition/seek contract rendered deterministically in 5.8 s warm; it is Apache-2.0. Pinning preserves the tested path, and fallback is explicit. A lint/render failure never changes renderer semantics. `synthesis.md` “Inputs for the scene engine”; `output-pipelines/report.md` F3 and `experiments/09-hyperframes`. |
| D2 | Integer frame time, independent property tracks and registered seek adapters define all motion | Wall-clock playback, one shared keyframe curve, Playwright fake clock alone, or CDP virtual time alone | Measured wall-clock and fake-clock-only capture produced 0/60 identical frames; seek-driven capture produced 90/90 identical frames. `document.getAnimations()` must be captured once. Property tracks and symbolic time references are v1 scene-engine design decisions. `output-pipelines/report.md` F1 and `experiments/02-frame-capture`; `synthesis.md` “Inputs for the scene engine”. |
| D3 | Use Linux BeginFrame only after seek; use screenshot capture on macOS and portable fallback | BeginFrame as the source of animation time or BeginFrame on every OS | BeginFrame is unsupported on macOS, and by itself missed script-started animations; combined with seeking it produced 120/120 identical frames on Linux. `output-pipelines/report.md` F1 and `experiments/02-frame-capture`. |
| D4 | Always normalize HyperFrames output through FFmpeg to H.264 High@4.1/yuv420p/BT.709/30 fps/AAC | Ship HyperFrames' raw file | The tested HyperFrames file was High level 5.0; the PowerPoint recipe measured 4.1, limited-range yuv420p, BT.709, 30 fps and AAC-LC. `output-pipelines/report.md` F3, F5 and `experiments/01-mp4-for-powerpoint`, `experiments/09-hyperframes`. |
| D5 | Generate PPTX from scene data with native objects, a small explicit fallback, schema validation and workbook range checks | Convert arbitrary rendered HTML to PPTX or use a full-slide bitmap | Converters rasterized gradients, blur, SVG and charts; the one-to-one scene subset maps to editable PowerPoint elements. OOXML, workbook and alternate-renderer checks reduce package risk but do not replace the PowerPoint owner check. `output-pipelines/report.md` F8 and F8b; `experiments/04-pptx-native`, `experiments/07-html-to-pptx`. |
| D6 | Script local web-app capture with fixtures, paused clock, seeked animations and an injected cursor | Real-time Playwright screencast as the deck video | The fixture-backed path reproduced 120/120 4K frames; Playwright screencast is VP8/25 fps and real-time. Unseekable WebGL/canvas/video must fail this deterministic path. `output-pipelines/report.md` UC2 and F9; `experiments/08-app-capture`. |
| D7 | Supply narration audio and timings as assets; allow optional local model output to enter through that same file interface | Make a hosted TTS API or unpinned voice model a renderer dependency | Research names Kokoro-82M and VieNeu-TTS v3-Turbo as permissively licensed local choices but did not listen to the voices or validate Vietnamese alignment. Keeping synthesis outside the engine preserves local choice without claiming quality. `output-pipelines/report.md` F4 and Risks. |
| D8 | Write optional WebVTT sidecar and optional burned-in cues from the same cue model | Burn every caption into pixels or ship SRT only | WebVTT is accepted by PowerPoint across documented desktop/web versions and stays beside the video; the measured experiment also burned the VTT with libass. `output-pipelines/report.md` F4 and `experiments/06-audio`. |
| D9 | Invoke render-kit for scene keyframes and rendered PPTX slide images | Reimplement visual checks inside scene-engine | render-kit already owns HTML/SVG rendering and checking; this tool adds artifact production, not another checking rule set. `render-kit/SPEC.md` sections 4–7 and `output-pipelines/report.md` F8/F8b. |
| D10 | Keep Node/TypeScript orchestration with a Python PPTX subprocess | Implement the whole tool in Python or call a hosted service | HyperFrames and Playwright are local Node tools; python-pptx is the measured native PPTX writer. A JSON subprocess boundary keeps each dependency in its tested runtime. `output-pipelines/report.md` F3 and F8; `experiments/09-hyperframes` and `experiments/04-pptx-native`. |
| D11 | Limit version one to narration audio and captions; accept pre-rendered TTS output as narration input | Add soundtrack authoring, licensed music catalogues and automatic music ducking in this phase | The phase 4 acceptance row requires narration and captions but not music or effects. Research F4 contains useful music and loudness guidance, but soundtrack ownership and licensing are separate decisions. `design-programme/plan.md` “Phases: deliverables and acceptance”, phase 4; `output-pipelines/report.md` F4. |
| D12 | Keep the stage at 1920×1080/30 fps and use 2D camera, deterministic groups, reveals, masks and data-driven SVG charts; defer spatial paths, springs, repeat and blur sampling | Claim a general-purpose motion editor | PowerPoint's delivery profile fixes 30 fps. The richer v1 motions remain seekable through declarative state. Advanced motion work is explicitly outside the v1 promise. This is a scope decision in response to M1–M14, not a research finding. |
| D13 | Treat Open XML validation, python-pptx/LibreOffice round trips and Keynote import as structural/import smoke evidence; require a manual Microsoft PowerPoint owner check | Claim Office compatibility from a non-Office application | The build Mac has Keynote and LibreOffice but no Microsoft PowerPoint. These checks can catch malformed XML and import/layout damage; they cannot prove PowerPoint's repair, editing, playback or animation behavior. The owner check remains a release requirement. |
| D14 | Keep command outputs versioned JSON with stable error codes and atomic artifact publication | Free-text diagnostics or leaving partial deliverables after failed checks | Storyboard-driving agents need machine-readable branches and useful pointers. Atomic publication prevents a failed profile or seek probe from looking like a valid final artifact. This is a v1 CLI contract decision. |
| D15 | Keep all text editable; do not embed fonts, and substitute unlisted source families to Arial with a per-layer report | Rasterize live text or assume each recipient has every font installed | Font embedding and cross-platform font availability were not established. Native text plus a visible named substitution preserves editing and makes reflow risk explicit. |
| D16 | Keep scene durations authored, allow `after` links to shift later scenes, and fail narration overflow instead of truncating or overlapping | Infer timing from audio or silently clip narration | This keeps narration and animation origins deterministic while still allowing storyboard revisions to propagate through sequenced scenes. This is a v1 semantics decision. |
| D17 | Sample native PPTX scene state at `durationMs - 1` by default and report accessibility metadata without claiming a Microsoft accessibility pass | Export at time zero or claim full Accessibility Checker equivalence | Explainers commonly animate in from transparent/off-slide states. End sampling improves the initial editable slide; metadata checks do not substitute for Microsoft's checker. |

## 10. Open questions

- Which exact Node 24 patch and Python 3 patch should the build image pin? The research gives Node 24+ in render-kit and Python 3, but no patch versions. Record both when the lockfile/build image is created.
- What is the installed macOS absolute path for Playwright's revision-1243 `chrome-headless-shell` on the build machine? Only the Linux path is recorded; resolve from the Playwright cache at install.
- Which LibreOffice version should be pinned for PPTX smoke rendering? Research records `soffice` use but not its version.
- Which current Microsoft PowerPoint versions should the release owner record for the Windows and Mac manual check? Microsoft PowerPoint is not installed on this build Mac. Until that owner check runs, opening without repair, Edit Data behavior, Morph, SVG, timing and movie playback remain unproven.
- Which exact ECMA-376 schema bundle revision and validator version should the build pin? V1 requires the schemas to be vendored and records per-part validation, but this research did not select a validator package.
- Does this Mac's Keynote import smoke check preserve every feature? It is an alternate-viewer diagnostic only; Keynote compatibility remains degraded and is not a PowerPoint proxy.
- How does PowerPoint store an imported WebVTT file inside a deck? The research deliberately ships it beside the video because this was not inspected.
- Does an actual Angular, React or Vue application capture with the same determinism as the stand-in? No framework-specific app was tested.
- What accuracy does Vietnamese forced alignment achieve on the chosen licensed local model, and which voices sound acceptable? These were not listening or alignment tests.
- Which exact revision/package version should package local TTS model weights? The research names model cards and dates, not immutable model hashes or package pins.
- Which capture APIs do real WebGL/canvas/video apps expose for a deterministic adapter? The research recommends real-time screen recording when they cannot be sought; that path is intentionally unsupported here.
- What cross-machine byte-identity guarantee should be required outside a pinned Docker image? Research says Chromium, fonts and FFmpeg must also be pinned; only one-machine frame identity was measured.
- Which final frame-difference tolerance should CI use between HyperFrames and the screenshot fallback when their capture primitives differ? The sources establish same-state seeking but do not measure a cross-renderer pixel tolerance; retain a comparison image and reviewer brief until a threshold is selected.
- The source experiment installed XlsxWriter without recording a version. This spec avoids a runtime dependency on it by requiring the PPTX writer to create the minimal embedded workbook with standard-library ZIP/XML; verify that this is practical before deleting the experiment helper.
