
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

Coordinates are CSS pixels on a 1920×1080 stage. Times are integer milliseconds. All asset paths are relative to the storyboard file and must resolve inside its project directory. Scene intervals may overlap for crossfades; scene array order breaks equal-start ties. A layer's `startMs` and `durationMs` are local to its scene. Keyframe `atMs` values are local to that layer's start. A keyframe's easing controls the interval from that keyframe to the next one.

The required schema is JSON Schema Draft 2020-12. Unknown properties are rejected. A storyboard has at least one scene and one of the specified layer types. The schema below defines the version-one contract; implementation validation must report the JSON pointer and reason for every invalid field.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://scene-engine.invalid/schema/storyboard-1.json",
  "title": "scene-engine storyboard v1",
  "type": "object",
  "additionalProperties": false,
  "required": ["format", "title", "width", "height", "fps", "durationMs", "scenes"],
  "properties": {
    "format": { "const": "scene-engine/storyboard@1" },
    "title": { "type": "string", "minLength": 1 },
    "width": { "const": 1920 },
    "height": { "const": 1080 },
    "fps": { "const": 30 },
    "durationMs": { "type": "integer", "minimum": 1 },
    "language": { "type": "string", "minLength": 2 },
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
    "keyframe": {
      "type": "object", "additionalProperties": false,
      "required": ["atMs", "values"],
      "properties": {
        "atMs": { "type": "integer", "minimum": 0 },
        "easing": { "$ref": "#/$defs/easing", "default": "linear" },
        "values": {
          "type": "object", "minProperties": 1, "additionalProperties": false,
          "properties": {
            "x": { "type": "number" }, "y": { "type": "number" },
            "width": { "type": "number", "exclusiveMinimum": 0 },
            "height": { "type": "number", "exclusiveMinimum": 0 },
            "opacity": { "type": "number", "minimum": 0, "maximum": 1 },
            "rotation": { "type": "number" },
            "scaleX": { "type": "number", "exclusiveMinimum": 0 },
            "scaleY": { "type": "number", "exclusiveMinimum": 0 }
          }
        }
      }
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
            "mask": { "type": "boolean" },
            "transform3d": { "type": "array", "minItems": 16, "maxItems": 16, "items": { "type": "number" } }
          }
        },
        "keyframes": {
          "type": "array", "items": { "$ref": "#/$defs/keyframe" },
          "description": "Strictly increasing atMs values within durationMs."
        }
      }
    },
    "scene": {
      "type": "object", "additionalProperties": false,
      "required": ["id", "startMs", "durationMs", "layers"],
      "properties": {
        "id": { "type": "string", "pattern": "^[A-Za-z][A-Za-z0-9_.-]*$" },
        "startMs": { "type": "integer", "minimum": 0 },
        "durationMs": { "type": "integer", "minimum": 1 },
        "pptxAtMs": { "type": "integer", "minimum": 0, "default": 0 },
        "background": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
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
              { "$ref": "#/$defs/videoLayer" }
            ]
          }
        },
        "narration": { "$ref": "#/$defs/narration" },
        "captions": { "type": "array", "items": { "$ref": "#/$defs/caption" } }
      }
    },
    "textLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "text" }, "text": { "type": "string" },
          "style": {
            "type": "object", "additionalProperties": false,
            "properties": {
              "fontFamily": { "type": "string" }, "fontSize": { "type": "number", "exclusiveMinimum": 0 },
              "fontWeight": { "type": "integer", "enum": [400, 700] }, "italic": { "type": "boolean" },
              "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
              "align": { "enum": ["left", "center", "right"] }, "lineHeight": { "type": "number", "exclusiveMinimum": 0 },
              "letterSpacing": { "type": "number" }, "background": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }
            }
          }
        }, "required": ["type", "text"] }
      ],
      "unevaluatedProperties": false
    },
    "imageLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "image" }, "src": { "type": "string", "minLength": 1 },
          "alt": { "type": "string" }, "fit": { "enum": ["contain", "cover", "fill"] }
        }, "required": ["type", "src"] }
      ],
      "unevaluatedProperties": false
    },
    "chartLayer": {
      "allOf": [
        { "$ref": "#/$defs/layerBase" },
        { "type": "object", "properties": {
          "type": { "const": "chart" },
          "kind": { "enum": ["column", "bar", "line", "area", "pie", "doughnut", "scatter", "stacked", "combo"] },
          "categories": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
          "series": {
            "type": "array", "minItems": 1,
            "items": {
              "type": "object", "additionalProperties": false, "required": ["name", "values"],
              "properties": {
                "name": { "type": "string" },
                "values": { "type": "array", "minItems": 1, "items": { "type": "number" } },
                "kind": { "enum": ["column", "line", "area"] },
                "axis": { "enum": ["primary", "secondary"] }
              }
            }
          },
          "showLegend": { "type": "boolean", "default": true },
          "showValues": { "type": "boolean", "default": false }
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
          "radiusPx": { "type": "number", "minimum": 0 },
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
          "readySelector": { "type": "string", "minLength": 1 },
          "locale": { "type": "string", "default": "en-US" },
          "timeZoneId": { "type": "string", "default": "UTC" },
          "deviceScaleFactor": { "const": 2 },
          "steps": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["atMs", "action"],
              "properties": {
                "atMs": { "type": "integer", "minimum": 0 },
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
              }
            }
          },
          "fixtures": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["urlPattern", "status", "bodyFile"],
              "properties": {
                "urlPattern": { "type": "string" }, "method": { "type": "string", "default": "GET" },
                "status": { "type": "integer", "minimum": 100, "maximum": 599 },
                "bodyFile": { "type": "string" }, "contentType": { "type": "string" }
              }
            }
          },
          "cursor": {
            "type": "array", "items": {
              "type": "object", "additionalProperties": false, "required": ["atMs", "x", "y"],
              "properties": {
                "atMs": { "type": "integer", "minimum": 0 }, "x": { "type": "number" },
                "y": { "type": "number" }, "click": { "type": "boolean" }, "easing": { "$ref": "#/$defs/easing" }
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
                "color": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }
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
          "poster": { "type": "string" }, "muted": { "type": "boolean", "default": true }
        }, "required": ["type", "src"] }
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
        "language": { "type": "string" }
      }
    }
  }
}
```

Additional model validation not expressible in this schema: scene IDs and layer IDs are unique; scenes and layers end no later than storyboard duration; keyframes are strictly increasing and lie within their layer duration; chart series value count equals category count except scatter; caption cues satisfy `startMs < endMs`; app steps and overlay times lie within the app layer; and local assets cannot resolve outside the project directory. A failed validation lists all independent errors and exits 2.

## 5. Rendering and export parts

### 5.1 Timeline and easing

The compiler creates one timeline in milliseconds and one HTML composition. It assigns every scene, layer, narration cue, caption cue, app frame strip and keyframe a time relative to storyboard zero. For frame \(n\), the only renderer time is `tMs = floor(n × 1000 / 30)`. No layer may read `Date.now()`, `performance.now()`, real elapsed time, unseeded randomness or an uncontrolled timer to choose visible state.

Between numeric keyframes, interpolate the property after applying the easing on the earlier keyframe. `linear`, `ease-in`, `ease-out`, `ease-in-out` and CSS cubic Bézier control points are deterministic. `step-start` and `step-end` hold discrete transitions. Duplicate times, non-finite values and values outside the layer interval fail validation. For a layer with no keyframes, its base properties hold for its interval. Scene transitions are explicit overlap and opacity keyframes, not implicit wall-clock CSS transitions.

HTML must expose `window.__timelines` (one registered adapter per animated subsystem) and `window.__sceneEngine.seek(ms)`. The latter updates all script-driven state and redraws before capture. The adapter contract is `seekFrame(frameIndex)`; it computes time from the integer frame index. Capture `document.getAnimations()` once after the scene is ready, pause every returned animation and set its `currentTime` on every seek; do not re-query after seeking past the end because completed transitions can disappear from the query. Pause a page's animations before calling `startViewTransition()`, whose snapshot is taken at call time. Seek every root SVG's SMIL animations with `pauseAnimations()` and `setCurrentTime(seconds)`. A canvas layer must register a pure draw callback that accepts time. Library adapters must use paused seekable timelines (for example GSAP paused timeline/exportRoot, anime.js timeline.seek, Lottie frame setters or Three.js explicit update); history-dependent react-spring and Rive state-machine motion is rejected.

Before rendering with HyperFrames, run its `lint`; then render with local version 0.8.78 and telemetry disabled. HyperFrames owns normal clip scheduling, frame workers and audio muxing. scene-engine always transcodes its output with FFmpeg to the required delivery profile and probes it. Never rely on HyperFrames' raw encoding profile: the measured delivery render was High level 5.0, above this tool's 4.1 target. In `auto` mode, a missing HyperFrames CLI selects the fallback and records that choice; a lint or render failure is reported rather than silently retried with different semantics. Explicit `--renderer hyperframes` fails if the binary is missing.

### 5.2 Deterministic frames by seeking

For each requested frame, set the canonical time, seek every registered timeline and layer, await only explicit ready gates, and capture once the page reports `seekComplete`. The page clock is installed and paused before navigation when a capture depends on timers, but fake time alone does not control CSS or Web Animations. The seek call—not a real-time wait or CDP virtual-time tick—sets their state.

Use HyperFrames frame adapters for its normal renderer. For app capture and fallback, use Playwright screenshot-per-frame; on Linux the implementation may use BeginFrame after the seek to make capture atomic, while still using the same time mapping. On macOS use `Page.captureScreenshot`; BeginFrame is unavailable there. If any animation or scene cannot be set to an explicit time and then sought backward to an earlier time with the same result, report the offending adapter/layer and fail the render with a seekability error. Do not silently switch to wall-clock capture.

### 5.3 Narration and captions

The storyboard accepts narration text, optional supplied audio, an offset and optional word timings. Text is metadata for notes and caption creation; scene-engine itself does not call a hosted TTS API. A caller using the research-named local voice options passes their generated WAV and word-timing JSON as input files. The word-timing file format is `{"format":"scene-engine/word-timings@1","language":"en","words":[{"text":"Hello","startMs":0,"endMs":300}]}`; words are sorted and each end is later than its start. Video without supplied audio gets a silent AAC-LC stereo track so every deliverable has the same stream format. For supplied narration, run two-pass FFmpeg `loudnorm` with explicit `I=-16`, `TP=-1.5`, `LRA=11`, `linear=true`. Encode AAC-LC, 48 kHz stereo, 192 kb/s.

Caption cues live on the scene timeline and may be generated from supplied word timings or authored directly. `--captions sidecar` writes a WebVTT file next to the MP4; `--captions burn-in` renders cue text into the scene with libass; `--captions both` does both; `--captions none` writes neither. Default is `sidecar` when cues exist and `none` otherwise. Cues are sorted, non-overlapping and clipped to the storyboard duration. Lint against the researched caption profile: at most two lines, 42 characters per line, cue duration 5/6–7 seconds where timing permits, no more than 20 characters/second in English or 17 in Vietnamese. Shorter cue duration is allowed at scene boundaries and is reported. The generated WebVTT begins with `WEBVTT`; all cue times increase.

### 5.4 Native-PPTX writer

One scene produces one 13.333×7.5-inch slide. CSS px map to 6,350 EMU (0.5 pt); text px map to half as many points. The scene's PPTX pose is sampled at `pptxAtMs` (default 0). Native PowerPoint motion is emitted only for supported entrance presets and objects whose stable names begin `!!` and repeat across adjacent slides; those receive Morph XML with a fade fallback. Arbitrary keyframe animation is not falsely represented as editable PowerPoint motion and is listed in the export report. Charts cross-fade during Morph.

Map the one-to-one subset as follows:

| Scene element | PPTX representation |
|---|---|
| Positioned rectangle, rounded rectangle, ellipse, line; solid or dashed stroke; solid fill or supported linear gradient; one outer shadow; shape opacity | Native `p:sp` and DrawingML preset geometry/fills/effects; strip the theme `p:style` that adds unwanted shadows |
| Text with one family, 400/700 weight, italic, color, alignment, bullets, line-height and letter spacing | Native editable `txBody`; explicit line breaks; supported source font must be a PowerPoint cloud font or licensed for embedding |
| SVG path using M/L/H/V/C/S/Q/T/Z (arcs converted to cubics), SVG rect/circle/ellipse/line | Native custom geometry `a:custGeom` and DrawingML preset geometry |
| Raster image | Native editable-position `p:pic` |
| Whole SVG illustration | SVG picture `asvg:svgBlip` plus a Chromium PNG fallback |
| Table | Native `graphicFrame` table |
| Data chart (column, bar, line, area, pie, doughnut, scatter, stacked, combo) | Native chart `graphicFrame`, chart XML and an embedded workbook; preserve series, categories and values so Edit Data works |
| Captured or supplied video | Native movie picture, poster frame and autoplay timing XML where requested |
| Speaker notes | Native notes slide |

Use python-pptx 1.0.2 for its supported editable objects. Write custom geometry, SVG relationships/fallbacks, Morph transitions, autoplay timing and combo/mixed-axis chart XML with standard-library ZIP/XML patches where python-pptx has no API. Generate a valid embedded workbook for every native chart. If an unsupported combination cannot be written as valid native objects, use this ordered fallback and report it per slide: (1) rebuild CSS layout as positioned boxes, recording that flex/grid no longer reflows; (2) whole-element SVG picture with PNG fallback; (3) 2× Chromium PNG for unsupported visual effects while preserving separately rendered text as native text where it can remain legible. Rasterize filters, backdrop-filter, blend modes, masks, complex clip-paths, conic/multiple backgrounds, gradient text, text-on-path, 3D transforms, canvas/WebGL and fonts unavailable to PowerPoint or embedding. Do not rasterize data charts when the native chart writer can express the data.

The editability acceptance round trip opens the generated file with python-pptx, changes a native text value and shape position, replaces chart data, saves a second deck, and reopens it. The second read must find the changed text and geometry, a chart object with the changed category/value data, and an embedded workbook. Run `soffice --headless --convert-to pdf` on both decks as a layout smoke check when LibreOffice is installed. This proves object-level round-trip editability; it does not claim Microsoft PowerPoint playback was tested.

### 5.5 App-demo capture

The app-demo layer addresses only a real local web app with source access and a runnable development server. `url` must be localhost or 127.0.0.1 and the layer must name a `readySelector`. Register response fixtures before navigation with Playwright routing; use the app's MSW handlers if its project supplies them. Install and pause Playwright's clock before `goto`, pin locale and timezone, and keep scripted interactions in ascending timeline order. Supported actions are goto, click, fill, press and waitFor using role/name, test-id or CSS locators. Wait for selectors and explicit asset readiness; do not use sleeps to decide when a frame is ready. A page-load timeout or missing readiness selector fails capture.

Capture the app at device scale factor 2 (3840×2160) so the editor can crop to the 1920×1080 output without upscaling. Replace private data in route fixtures before display. Capture every frame in increasing frame-index order, set all seekable animations to that frame's time, then write an immutable frame sequence as the app-demo layer. This pre-captured sequence makes the stateful click path repeatable and lets the enclosing composition seek in either direction. Cursor positions and click ripples are separate seekable overlays; highlight overlays resolve their locators to rectangles for each captured frame. Both are rendered into the composition, not recorded from a real cursor. A network response, cursor position or step whose result depends on live external state is a capture error.

A canvas/WebGL/video animation that cannot be adopted by a seek adapter, an app that cannot be fixture-backed, or an app that fails its ready gate causes a clear nonzero result with the URL, step/frame and reason. This design does not silently produce a real-time screencast: research found Playwright's own screencast is real-time VP8 at 25 fps, suitable for run receipts but not the required MP4.

### 5.6 Fallback renderer

The fallback reads the same compiled scene HTML, JSON model, assets and seek adapters as HyperFrames. It uses Playwright to set `window.__sceneEngine.seek(tMs)`, captures one PNG per output frame, and pipes the ordered image sequence and audio inputs to FFmpeg. It must write the same MP4 profile, WebVTT options, poster and JSON report as the HyperFrames path. It may be slower; it may not change scene semantics, timeline, easing, caption timing or app-demo frames. For an identical pinned browser and fonts, test the same keyframes against both paths and require the frame comparison policy recorded in the report (byte equality where capture primitives match; otherwise per-pixel difference and a reviewer brief).

## 6. Command-line interface

Commands use `scene-engine <command> [options]`. Every command writes one JSON document to stdout; progress, HyperFrames output and FFmpeg logs go to stderr. No command prints human prose to stdout.

Exit codes:

- `0`: command completed and requested checks passed.
- `1`: visual, media-profile, caption, PPTX round-trip or seekability check failed.
- `2`: unknown command/flag, malformed JSON, invalid schema or missing storyboard/asset.
- `3`: required executable failed or is missing, HyperFrames is unavailable, app navigation/readiness failed, or a renderer process crashed.

All errors still print JSON such as `{"error":{"code":"HYPERFRAMES_MISSING","message":"..."}}` to stdout and a diagnostic to stderr.

| Command | Contract |
|---|---|
| `scene-engine validate <storyboard.json>` | Validate schema and cross-field rules. Output `{"valid":true,"scenes":n,"duration_ms":n,"errors":[]}`; exit 2 with pointer-coded errors on invalid input. |
| `scene-engine render <storyboard.json> --out <file.mp4> [--renderer auto|hyperframes|fallback] [--captions sidecar|burn-in|both|none] [--poster <file.png>] [--timeout <ms>]` | Capture app-demo layers, compile HTML, render, normalize with FFmpeg, emit optional VTT and poster, and verify via ffprobe. `auto` is the default: use HyperFrames when installed, otherwise use the fallback. Output includes files, duration, frame count, media streams, renderer/version and diagnostics. |
| `scene-engine capture <storyboard.json> --scene <id> --out-dir <dir> [--timeout <ms>]` | Capture one app-demo layer to an immutable frame sequence and metadata. Output includes URL origin, frame count, device scale, fixture count and content hashes. |
| `scene-engine export-pptx <storyboard.json> --out <file.pptx> [--embed-video <file.mp4>] [--report <file.json>] [--verify|--no-verify]` | Write one editable slide per scene; optionally embed the produced MP4 as a movie object with a poster and autoplay timing. Run the editability round trip by default and write per-slide native/raster mappings. `--no-verify` opts out of the structural round trip. |
| `scene-engine check <storyboard.json> [--at <ms,...>] [--pptx <file.pptx>] [--out-dir <dir>] [--rk <path-to-rk>]` | Seek and capture authored keyframes plus scene start/mid/end, serialize the selected state as a static HTML stage, and call configured render-kit `rk check`. If PPTX is supplied, render its slides through LibreOffice, wrap each actual slide PNG in an HTML image stage and call `rk check`; retain native-object and LibreOffice diagnostics separately. Output nests each `rk` report and status. Missing `rk` is reported as skipped; `--strict` turns skipped into exit 1. |
| `scene-engine selftest [--case ATnn] [--strict]` | Run the fixture and command named by each acceptance-test row. Output `{"cases":[{"id":"AT01","status":"pass"}],"ok":true}`. |

Render options:

| Option | Meaning | Default |
|---|---|---|
| `<storyboard.json>` | Local storyboard; all referenced files stay within its project directory | required |
| `--out <path>` | MP4 or PPTX destination | required for render/export |
| `--renderer <name>` | `hyperframes` or `fallback` | `hyperframes` |
| `--captions <mode>` | Sidecar, burn-in, both or none | sidecar when cues exist |
| `--poster <path>` | PNG poster extracted at the first non-empty frame | alongside the MP4 |
| `--timeout <ms>` | Bound app readiness and renderer calls | 30000 |
| `--at <ms,...>` | Additional explicit times for frame and visual checks | authored keyframes plus scene start/mid/end |
| `--rk <path>` | render-kit `bin/rk` executable | configured sibling checkout |
| `--strict` | Treat skipped external checks as failures | off for reports; on in CI |

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

## 9. Decisions

| ID | Choice | Alternative rejected | Why and research basis |
|---|---|---|---|
| D1 | HyperFrames 0.8.78 is the only default video engine; telemetry is disabled on every invocation | Build a renderer from scratch, use Remotion, or follow the npm latest tag | The researched HyperFrames composition/seek contract rendered deterministically in 5.8 s warm; it is Apache-2.0. Remotion needs a paid Company License above three employees and HyperFrames is already the chosen layer. The version is pre-1.0 and changes frequently, so pinning and fallback are mandatory. `synthesis.md` “Inputs for the scene engine”; `output-pipelines/report.md` F3 and `experiments/09-hyperframes`. |
| D2 | Integer frame time and explicit seek adapters are the only animation clock | Wall-clock playback, Playwright fake clock alone, or CDP virtual time alone | Measured wall-clock and fake-clock-only capture produced 0/60 identical frames; seek-driven capture produced 90/90 identical frames. `document.getAnimations()` must be captured once. `output-pipelines/report.md` F1 and `experiments/02-frame-capture`; `synthesis.md` “Inputs for the scene engine”. |
| D3 | Use Linux BeginFrame only after seek; use screenshot capture on macOS and portable fallback | BeginFrame as the source of animation time or BeginFrame on every OS | BeginFrame is unsupported on macOS, and by itself missed script-started animations; combined with seeking it produced 120/120 identical frames on Linux. `output-pipelines/report.md` F1 and `experiments/02-frame-capture`. |
| D4 | Always normalize HyperFrames output through FFmpeg to H.264 High@4.1/yuv420p/BT.709/30 fps/AAC | Ship HyperFrames' raw file | The tested HyperFrames file was High level 5.0; the PowerPoint recipe measured 4.1, limited-range yuv420p, BT.709, 30 fps and AAC-LC. `output-pipelines/report.md` F3, F5 and `experiments/01-mp4-for-powerpoint`, `experiments/09-hyperframes`. |
| D5 | Generate PPTX from scene data with native objects and explicit raster fallbacks | Convert arbitrary rendered HTML to PPTX or use a full-slide bitmap | Converters rasterized gradients, blur, SVG and charts; the one-to-one scene subset maps to editable PowerPoint elements, and python-pptx charts carry an embedded workbook. `output-pipelines/report.md` F8 and F8b; `experiments/04-pptx-native`, `experiments/07-html-to-pptx`. |
| D6 | Script local web-app capture with fixtures, paused clock, seeked animations and an injected cursor | Real-time Playwright screencast as the deck video | The fixture-backed path reproduced 120/120 4K frames; Playwright screencast is VP8/25 fps and real-time. Unseekable WebGL/canvas/video must fail this deterministic path. `output-pipelines/report.md` UC2 and F9; `experiments/08-app-capture`. |
| D7 | Supply narration audio and timings as assets; allow optional local model output to enter through that same file interface | Make a hosted TTS API or unpinned voice model a renderer dependency | Research names Kokoro-82M and VieNeu-TTS v3-Turbo as permissively licensed local choices but did not listen to the voices or validate Vietnamese alignment. Keeping synthesis outside the engine preserves local choice without claiming quality. `output-pipelines/report.md` F4 and Risks. |
| D8 | Write optional WebVTT sidecar and optional burned-in cues from the same cue model | Burn every caption into pixels or ship SRT only | WebVTT is accepted by PowerPoint across documented desktop/web versions and stays beside the video; the measured experiment also burned the VTT with libass. `output-pipelines/report.md` F4 and `experiments/06-audio`. |
| D9 | Invoke render-kit for scene keyframes and rendered PPTX slide images | Reimplement visual checks inside scene-engine | render-kit already owns HTML/SVG rendering and checking; this tool adds artifact production, not another checking rule set. `render-kit/SPEC.md` sections 4–7 and `output-pipelines/report.md` F8/F8b. |
| D10 | Keep Node/TypeScript orchestration with a Python PPTX subprocess | Implement the whole tool in Python or call a hosted service | HyperFrames and Playwright are local Node tools; python-pptx is the measured native PPTX writer. A JSON subprocess boundary keeps each dependency in its tested runtime. `output-pipelines/report.md` F3 and F8; `experiments/09-hyperframes` and `experiments/04-pptx-native`. |
| D11 | Limit version one to narration audio and captions; accept pre-rendered TTS output as narration input | Add soundtrack authoring, licensed music catalogues and automatic music ducking in this phase | The phase 4 acceptance row requires narration and captions but not music or effects. Research F4 contains useful music and loudness guidance, but soundtrack ownership and licensing are separate decisions. `design-programme/plan.md` “Phases: deliverables and acceptance”, phase 4; `output-pipelines/report.md` F4. |

## 10. Open questions

- Which exact Node 24 patch and Python 3 patch should the build image pin? The research gives Node 24+ in render-kit and Python 3, but no patch versions. Record both when the lockfile/build image is created.
- What is the installed macOS absolute path for Playwright's revision-1243 `chrome-headless-shell` on the build machine? Only the Linux path is recorded; resolve from the Playwright cache at install.
- Which LibreOffice version should be pinned for PPTX smoke rendering? Research records `soffice` use but not its version.
- Does actual Microsoft PowerPoint preserve the generated Morph, SVG fallback, embedded font, poster/autoplay timing and native movie playback? Research only read package XML and rendered with LibreOffice; a real PowerPoint open/play test is outstanding.
- How does PowerPoint store an imported WebVTT file inside a deck? The research deliberately ships it beside the video because this was not inspected.
- Does an actual Angular, React or Vue application capture with the same determinism as the stand-in? No framework-specific app was tested.
- What accuracy does Vietnamese forced alignment achieve on the chosen licensed local model, and which voices sound acceptable? These were not listening or alignment tests.
- Which exact revision/package version should package local TTS model weights? The research names model cards and dates, not immutable model hashes or package pins.
- Which capture APIs do real WebGL/canvas/video apps expose for a deterministic adapter? The research recommends real-time screen recording when they cannot be sought; that path is intentionally unsupported here.
- What cross-machine byte-identity guarantee should be required outside a pinned Docker image? Research says Chromium, fonts and FFmpeg must also be pinned; only one-machine frame identity was measured.
- Which final frame-difference tolerance should CI use between HyperFrames and the screenshot fallback when their capture primitives differ? The sources establish same-state seeking but do not measure a cross-renderer pixel tolerance; retain a comparison image and reviewer brief until a threshold is selected.
- The source experiment installed XlsxWriter without recording a version. This spec avoids a runtime dependency on it by requiring the PPTX writer to create the minimal embedded workbook with standard-library ZIP/XML; verify that this is practical before deleting the experiment helper.
