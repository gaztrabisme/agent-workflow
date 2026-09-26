# render-kit specification

Reader: the agent that builds render-kit, and anyone who later changes it. Agents that only *use* the kit read `AGENTS.md`.

## 1. What it is

render-kit (command `rk`) turns an HTML or SVG file into the PNG or PDF a reader will see, then checks that output with code. Producer skills (frontend, presentation, information design, photo) call it in a loop: render, check, fix, render again. After the code checks pass, `rk brief` writes specific questions for a reviewer who can see images and did not make the artifact, and `rk brief --verify` checks that reviewer's answers. The kit never calls a model itself, so it works with any agent.

Terms used below:
- **Stage:** the area that is the artifact. It is the element marked `data-rk-stage` when one exists; otherwise the viewport for HTML input, or the SVG's own size for SVG input.
- **Check:** one code test. Its status is `pass`; `fail`; `incomplete` (it ran and found no failure, but could not measure some items, which it lists); or `skipped` (it could not run; a reason is always given).
- **Mark:** an SVG element that encodes a data value: a bar, a point, a line.
- **OKLab distance:** the Euclidean distance between two colours in the OKLab colour space (Björn Ottosson, 2020), where lightness L runs from 0 to 1.
- **Page clock:** Playwright's fake clock, which controls `Date`, timers and `requestAnimationFrame` inside the page.

## 2. Scope

In scope: rendering one HTML page or one SVG file to PNG or PDF; the 11 checks in section 6; measuring and wrapping text; vision briefs; a self-test.

Out of scope: video encoding and PowerPoint output (the separate `scene-engine`, later); multi-slide decks in one call (render each slide file separately); Firefox and WebKit; native desktop or mobile apps; calling any vision or language model; bundling fonts.

## 3. Environment and dependencies

- **Node 24 or later**, running TypeScript directly through type stripping. Source files are `.ts` with erasable syntax only (no `enum`, `namespace`, parameter properties or decorators); imports name the `.ts` extension. There is no build step and no bundler. `tsconfig.json` sets `noEmit`, `allowImportingTsExtensions`, `erasableSyntaxOnly`, `strict`, `module` and `moduleResolution` `nodenext`.
- **Runtime dependencies, exact versions:** `playwright` 1.63.0 and `@axe-core/playwright` 4.13.0. **Dev dependency:** `typescript` 5.9.3, used only for `tsc --noEmit`. Any further dependency needs an entry in section 10.
- **Browser:** Playwright's Chromium launched with `channel: 'chromium'`: full Chromium in the new headless mode, with GPU rasterisation, WebGL and WebGPU. The headless shell is never used: it rasterises WebGL on the CPU, lacks WebGPU, and its frames differ from the new mode's by 3.6–8.1% of pixels (research track 3, `lab/frontend-2026/graphics-motion`). Every report records the browser version and the mode.
- **Local server:** local files are never loaded over `file://`. rk starts a static HTTP server (Node's `http` module, no dependency) on `127.0.0.1` with a free port, rooted at `--root` (default: the input file's folder), and loads the input over `http`. Requests for paths outside the root get 404. The server stops when the command ends.
- **Network:** blocked by default. The page may request only the rk server's origin (and, for URL inputs, the input's own origin). Every other request is aborted and recorded. `--allow-network` lifts the block.
- **Optional tools**, detected at run time; when one is missing, the check that needs it is `skipped` with the reason:
  - `pdffonts` from poppler, for `pdf-fonts`;
  - Python 3 with numpy and Pillow, plus `color-theory`'s `scripts/checks.py`, for `value`. The color-theory folder is the env var `RK_COLOR_THEORY` if set, else `../skills/color-theory` relative to the render-kit folder.
- **Platforms:** developed on macOS (Apple Silicon); must also run on Linux.

## 4. Command-line interface

`rk <command> [options]`. Every command prints one JSON document to stdout (except `rk text wrap --format svg`, which prints SVG) and progress to stderr.

**Exit codes**
- `0`: success.
- `1`: a check failed, text overflowed, or a vision answer was `no`. With `--strict`, also any `skipped` or `incomplete` check, or any `unsure` or `not-judged` answer.
- `2`: usage, input or render error. stderr carries the message; stdout carries `{"error": "<message>"}`.

### 4.1 Shared render options
Used by `render`, `check` and `brief`.

| Option | Meaning | Default |
|---|---|---|
| `<input>` | A local `.html` or `.svg` file, or a URL on `http://localhost:<port>/` or `http://127.0.0.1:<port>/` (a dev server). Any other URL, or a missing file, is exit 2 | required |
| `--root <dir>` | Folder the local server serves | the input file's folder |
| `--width`, `--height` | Viewport in CSS pixels | HTML: 1920 × 1080. SVG: its `width`/`height` attributes, else its `viewBox` size |
| `--scale <n>` | Device pixel ratio | 1 |
| `--at <ms\|end>` | Scene time to render (section 5) | `end` |
| `--settle <ms>` | Page-clock time given to script-driven animation when `--at end` | 10000 |
| `--wait-for <selector>` | Wait for this CSS selector after load | none |
| `--timeout <ms>` | Limit for load and waits; exceeding it is exit 2 | 30000 |
| `--allow-network` | Permit requests to other origins | off |

### 4.2 `rk render <input> --out <file.png|file.pdf> [render options] [--simulate <type>]`
Renders the stage. PNG: a screenshot clipped to the stage. PDF: `page.pdf({ preferCSSPageSize: true, printBackground: true, tagged: true, outline: true })`; when the page sets no `@page` size, the PDF page size equals the stage size. `--simulate protanopia|deuteranopia|tritanopia|achromatopsia` renders the PNG as seen with that colour-vision deficiency, through Chromium's `Emulation.setEmulatedVisionDeficiency`; it is refused (exit 2) for PDF.

Output: `{"out", "format", "width", "height", "scale", "at_ms", "browser": {"version", "mode"}, "requests_blocked": []}`. `width` and `height` are the image's pixel size (PNG) or the page size in points (PDF).

### 4.3 `rk check <input> [render options] [--checks <ids>] [--pdf] [--out-dir <dir>] [--strict]`
Renders once, runs the checks, and writes `report.json` and `render.png` (plus `render.pdf` with `--pdf`) into `--out-dir` (default: a new temporary folder). Prints the report (section 7). `--checks` takes comma-separated check ids; by default every check that applies to the input runs. `pdf-fonts` applies only with `--pdf`. `--threshold <check>.<name>=<value>` (repeatable) overrides a *kit default* threshold from section 6, for example `--threshold cvd.min_distance=0.08`; an unknown name is exit 2.

### 4.4 `rk text measure --font <css font> --text <string> [--font-file <path>]`
Measures one line of text in the browser with canvas `measureText`, after `document.fonts.load(font)`. `--font` is a CSS font shorthand such as `600 32px "Source Sans 3"`. `--font-file` registers that file with the FontFace API under the family named in `--font`. Before measuring, rk confirms the font renders as requested, by the same rule as the `fonts` check (6.3); if it does not, exit 2 naming the font actually used. Output: `{"width", "ascent", "descent", "font"}` in CSS pixels.

### 4.5 `rk text wrap --font <css font> --text <string> --width <px> [--line-height <multiplier>] [--max-lines <n>] [--format json|svg] [--x <n> --y <n>] [--font-file <path>]`
Breaks text into lines no wider than `--width`, measuring in the browser (canvas `measureText`) and finding break opportunities with `Intl.Segmenter` (word granularity; breaks allowed at whitespace and after hyphens and slashes; CJK breaks between graphemes). Lines are filled greedily. Output JSON: `{"lines": [{"text", "width"}], "line_height", "height", "overflow": false}`; `--format svg` prints a `<text>` element with one `<tspan x=".." dy="..">` per line, positioned at `--x`, `--y` (defaults 0, 0), `font` set from `--font`. `overflow` is true, and the exit code 1, when one word is wider than `--width` or the line count exceeds `--max-lines`. Line height defaults to 1.2.

### 4.6 `rk brief <input> --questions <file> --out-dir <dir> [--purpose <text>] [--simulate <types>] [render options]`
Prepares a review for someone who can see images and did not make the artifact. It renders the PNG, plus one PNG per type in `--simulate` (comma-separated), runs `rk check`, and writes into `--out-dir`:
- `render.png` and `render-<type>.png`;
- `report.json`, the code-check report;
- `brief.md`: what the artifact is (`--purpose`), the image paths, a summary of the code checks (so the reviewer does not re-judge what code measured), the rules for answering, and the numbered questions `Q1`…`Qn`;
- `answers.template.json`: `{"reviewer": null, "answers": [{"id": "Q1", "question": "...", "answer": null, "where": null, "reason": null}]}`.

The questions file has one question per line starting with `- ` or `1. `; lines starting with `#` are group headings and are copied into the brief. Questions are phrased so that **yes means the artifact passes**. The kit ships default sets in `questions/chart.md` and `questions/slide.md`.

Answering rules written into the brief: `answer` is `yes`, `no`, `unsure` or `not-judged` (for a reviewer that cannot see the image); `reason` is one sentence; `where` names the region or element for `yes` and `no`.

### 4.7 `rk brief --verify <answers.json> [--strict]`
Checks a filled answers file against the questions in the same folder's `brief.md`. Exit 2 when the file is malformed, a question is missing, an answer is not one of the four values, a `reason` is empty, or a `yes`/`no` lacks `where`. Otherwise prints `{"no": [ids], "unsure": [ids], "not_judged": [ids]}`; exit 1 when any answer is `no` (or, with `--strict`, any `unsure` or `not-judged`), else 0.

### 4.8 `rk selftest [--strict]`
Runs `rk check --pdf` on every sample listed in `samples/expectations.json` and compares the set of failing checks with the expected set. Good samples must fail nothing; each bad sample must fail exactly its expected checks. A `skipped` check whose tool is missing on this machine is reported and allowed, unless `--strict`. Prints `{"samples": [...], "ok": true|false}`; exit 0 when every expectation holds.

## 5. Rendering and time

1. Before navigation, install the page clock at `2026-01-01T00:00:00Z` and pause it, so `Date`, timers and `requestAnimationFrame` are identical on every run and a page that shows "today" always shows that date.
2. Load the input and wait for, in order: the `load` event, `document.fonts.ready`, `--wait-for` if given, and network idle.
3. Seek to scene time T:
   - `--at <ms>`: T = ms. Advance the page clock by T, then pause every animation in `document.getAnimations()` (CSS animations, CSS transitions, Web Animations) and set its `currentTime` to T, then call `pauseAnimations()` and `setCurrentTime(T / 1000)` on every `<svg>` root (SMIL).
   - `--at end`: advance the page clock by `--settle`, so script-driven animation such as D3 transitions completes. Then call `finish()` on every finite CSS or Web Animation, pause every infinite one with `currentTime` = `--settle`, and set SMIL time to `--settle` / 1000.
   - Animations are assumed to start at load. The kit does not detect animations started later by script at other times.
4. Capture. Do not wait on `requestAnimationFrame` after seeking: the page clock is paused.
5. SVG input is wrapped by the server in an HTML page (`<!doctype html>`, zero margins, transparent background) with the SVG inline, served from the SVG's own folder so relative references resolve. Nothing is written next to the input.
6. When a second CDP session is opened (for font or vision-deficiency queries), send `Emulation.setDeviceMetricsOverride` on it with the same size and scale; otherwise screenshots from that session come back at scale 1 (research track 3, finding F1 item 8).

The same input and options must give a byte-identical PNG on repeated runs on one machine.

## 6. Checks

Every check skips elements inside `[data-rk-ignore]`, and elements that are not visible: zero size, `display: none`, `visibility: hidden`, or opacity 0. A **text element** is a visible element with a non-empty direct text node, or an SVG `<text>` element. A **text box** is the union of its text's client rectangles (a DOM `Range` over its text nodes); for SVG `<text>`, its bounding box mapped to screen coordinates.

Thresholds marked *kit default* were set by judgment or calibration and can be changed with `--threshold <check>.<name>=<value>`; the report states every threshold used.

### 6.1 `resources` (all inputs)
Fail when any request was blocked by the network rule or failed (network error, or HTTP status 400 or above). Items: the URL and the reason.

### 6.2 `console` (all inputs)
Fail on any uncaught page exception or `console.error` message between navigation and capture. Items: the first 200 characters of each message.

### 6.3 `fonts` (all inputs)
For every text element, ask Chromium which fonts drew its glyphs (`CSS.getPlatformFontsForNode` over CDP). Let F be the first family in its computed `font-family`.
- F is a CSS generic family (`serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, `system-ui`, `ui-serif`, `ui-sans-serif`, `ui-monospace`, `ui-rounded`, `math`, `emoji`, `fangsong`): pass.
- F matches a family in `document.fonts` (an `@font-face` or FontFace font): pass when that font's status is `loaded` and every glyph was drawn by a custom font (`isCustomFont: true`).
- Otherwise F is a system font: pass when every glyph was drawn by a platform font whose `familyName` equals F, ignoring case.

Fail items: the element's selector, F, and each font actually used with its glyph count. A font that draws some glyphs but not all (for example, Vietnamese diacritics falling back to another font) fails.

### 6.4 `overflow` (all inputs)
Fail when any of these holds, by more than 1 CSS pixel:
- a text box extends beyond its element's padding box;
- a text box extends beyond the padding box of the nearest ancestor that clips (`overflow` other than `visible`);
- an element with `text-overflow: ellipsis` has `scrollWidth > clientWidth` (truncated text), unless it or an ancestor has `data-rk-allow-truncate`;
- a visible element's box, or an SVG `<text>` box, extends beyond the stage (item kind `offstage`);
- an SVG `<text>` box extends beyond its nearest `<svg>` viewport.

Items: kind, selector, the overflow in pixels on each side.

### 6.5 `collision` (all inputs)
Fail when the text boxes of two different text elements, neither containing the other, overlap by more than 1 CSS pixel in both width and height. Pairs where either element or an ancestor has `data-rk-allow-overlap` are exempt. Items: both selectors and the overlap rectangle.

### 6.6 `contrast` (all inputs)
WCAG 2.2 success criterion 1.4.3: contrast ratio at least 4.5:1, or 3:1 for large text (font size at least 24 CSS px, or at least 18.66 CSS px at weight 700 or more).
- HTML text: axe-core's `color-contrast` rule.
- SVG `<text>`, and every item axe-core reports as incomplete: measured on the rendered PNG. The text colour is the computed `fill` (SVG) or `color` (HTML). The background is the most frequent colour in the text box after removing pixels within OKLab distance 0.1 of the text colour. The ratio uses the WCAG 2 relative-luminance formula.
- When the most frequent background colour covers less than 30% of the remaining pixels (text over an image or a gradient), the item is `incomplete` (*kit default* 30%).

Items: selector, text colour, background colour, ratio, required ratio.

### 6.7 `cvd` (inputs with `[data-rk-series]`)
Checks that categorical colours stay distinguishable for colour-vision deficiency. Each series' colour is the most common computed `fill` (else `stroke`) among elements with that `data-rk-series` value. Fewer than two series: `skipped`. For normal vision and for protanopia, deuteranopia and tritanopia (Machado, Oliveira and Fernandes 2009 matrices at severity 1.0, applied in linear sRGB and clamped to [0, 1]), compute the smallest OKLab distance between any two series. Fail when any is below **0.06**.

The threshold is a *kit default* calibrated on 2026-09-26 with this method: the Okabe–Ito palette, designed for colour-vision deficiency, keeps at least 0.076 under all three (passes); the pair `#d62728`/`#2ca02c` falls to 0.039 under deuteranopia (fails); `#1f77b4`/`#ff7f0e` keeps 0.246 (passes). Items: vision type, the closest pair and its distance.

### 6.8 `fidelity` (inputs with `[data-rk-chart]`)
Checks that each mark sits where its data says, using markup the chart declares (section 8). Coordinates are read in the chart root's user space: a mark's geometry is mapped through the inverse of the root's `getCTM()` times the mark's `getCTM()`.
- The scale for an axis is `linear` (dates are given as epoch milliseconds on a linear scale) or `band`. A `band` axis is not checked.
- `<rect>` with `data-rk-y` (vertical bar): its top and bottom edges must equal `scaleY(data-rk-y)` and `scaleY(base)`, in either order, where `base` is `data-rk-y0` if given, else 0 if 0 lies in the domain, else the domain minimum. `<rect>` with `data-rk-x` (horizontal bar): the same with left and right edges and the x scale.
- `<circle>` or `<ellipse>` with `data-rk-x` and/or `data-rk-y`: its centre must equal the scaled value on each linear axis given.
- `<polyline>`, or `<path>` whose `d` uses only absolute `M` and `L` commands, with `data-rk-points="x1,y1 x2,y2 …"` in data values: its vertices must equal the scaled points, in order and equal in number. A path with any other command is an `incomplete` item ("curved path not checked").
- Tolerance: 0.5 user units (*kit default*).
- No `[data-rk-chart]`: `skipped`. A mark whose chart lacks a needed scale attribute: fail item "missing scale".

Items: selector, expected, actual.

### 6.9 `a11y` (all inputs; SVG input is checked in its HTML wrapper)
axe-core with the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` and `wcag22aa`, with `color-contrast` disabled because `contrast` owns it. Fail on any violation. Items: rule id, impact, selectors. When there are no violations but axe-core reports incomplete results, the status is `incomplete` with those as items.

### 6.10 `value` (inputs with `[data-rk-focal]`)
Runs color-theory's image checks on the rendered PNG: `python3 <color-theory>/scripts/checks.py value <png> --focal x0,y0,x1,y1 --out <tmpdir>` and `... chroma <png> --focal x0,y0,x1,y1`, where the box is the focal element's bounding box in PNG pixels (CSS pixels × scale). stdout lines matching `^(T\d+) (PASS|FAIL)\b` are the results. Fail when any is `FAIL`. Items: each T-line with the measurement lines printed before it. Missing Python, numpy, Pillow or the script, a non-zero exit, or no T-line: `skipped` with stderr's last 300 characters. No `[data-rk-focal]`: `skipped`.

### 6.11 `pdf-fonts` (when a PDF was produced)
Runs `pdffonts <pdf>`. Fail when any font's type contains `Type 3` or its `emb` column is `no`. Chromium turns variable fonts and synthetic bold into Type 3 fonts, which render poorly and cannot be edited (research track 3, finding F6). Items: font name, type, embedded. No `pdffonts`: `skipped`.

## 7. Report

`report.json`, printed by `rk check`:

```json
{
  "rk_version": "0.1.0",
  "input": "<path or URL>",
  "created": "<ISO time>",
  "browser": {"name": "chromium", "version": "<version>", "mode": "new-headless"},
  "viewport": {"width": 1920, "height": 1080, "scale": 1},
  "at_ms": 10000,
  "outputs": {"png": "<path>", "pdf": "<path or null>"},
  "requests_blocked": [],
  "checks": [
    {
      "id": "contrast",
      "status": "fail",
      "thresholds": {"normal": 4.5, "large": 3},
      "items": [{"selector": "…", "detail": "…", "measured": 3.1, "required": 4.5}],
      "reason": null
    }
  ],
  "summary": {"pass": 8, "fail": 1, "incomplete": 0, "skipped": 2}
}
```

Every check that applies appears exactly once. `reason` is required for `skipped` and `incomplete`. Selectors are unique CSS selectors that `document.querySelector` resolves to the element.

## 8. Markup conventions

Producer skills and chart templates add these attributes; the checks read them.

| Attribute | On | Meaning |
|---|---|---|
| `data-rk-stage` | one element | The artifact's area; PNG capture and the offstage test use it |
| `data-rk-focal` | one element | The focal area, for `value` |
| `data-rk-series="<name>"` | marks, legend swatches | Categorical series, for `cvd` |
| `data-rk-chart` | a `<g>` or `<svg>` | Chart root, with `data-rk-x-scale`, `data-rk-x-domain="d0,d1"`, `data-rk-x-range="r0,r1"` and the same three for y. Ranges are in the root's user units; a reversed range (for depth increasing downward) is allowed |
| `data-rk-mark` | `<rect>`, `<circle>`, `<ellipse>`, `<polyline>`, `<path>` | A data mark, with `data-rk-x`, `data-rk-y`, `data-rk-x0`, `data-rk-y0` or `data-rk-points` as in 6.8 |
| `data-rk-allow-overlap` | any | Exempt from `collision` |
| `data-rk-allow-truncate` | any | Exempt from the truncation test in `overflow` |
| `data-rk-ignore` | any | Exempt the subtree from all checks |

## 9. Code layout

One concern per file, at most 120 lines of logic each:

```
bin/rk                     #!/usr/bin/env node; imports src/cli.ts
src/cli.ts                 argument parsing (node:util parseArgs), dispatch, exit codes
src/server.ts              static HTTP server on 127.0.0.1, SVG wrapper
src/browser.ts             launch, context (viewport, scale, locale en-US, time zone UTC), network rule, page clock, error capture
src/render.ts              load, waits, PNG and PDF output, --simulate
src/seek.ts                scene-time seeking (section 5)
src/text.ts                measure and wrap
src/color.ts               sRGB, linear RGB, OKLab, WCAG luminance and ratio, Machado matrices
src/checks/<id>.ts         one file per check, each exporting run(ctx) → CheckResult
src/report.ts              report assembly, validation, exit code
src/brief.ts               brief writer and verifier
src/selftest.ts            runs samples/expectations.json
questions/chart.md, questions/slide.md
samples/good/              slide.html (1920×1080: title, body text, an inline SVG chart with every data-rk attribute, a focal element), chart.svg, animated.html (a CSS animation, a Web Animation and a SMIL animation)
samples/bad/<id>.html|svg  one sample per check, built to fail that check only
samples/expectations.json  [{"input": "bad/contrast.html", "fail": ["contrast"]}, …]
samples/fonts/             font files the samples need (OFL-licensed, with their licence files)
test/*.test.ts             node:test unit and integration tests
```

`npm test` runs `tsc --noEmit` and then `node --test`.

## 10. Decisions

| # | Decision | Rejected, and why |
|---|---|---|
| D1 | TypeScript run directly by Node 24 (type stripping) | A build step or `tsx`: extra machinery for no gain. Python: Playwright's primary platform is Node, and in-page code is JavaScript anyway |
| D2 | One browser mode: full Chromium, new headless | The headless shell: WebGL on the CPU, no WebGPU. Mixing modes: frames differ by 3.6–8.1% of pixels |
| D3 | A local HTTP server instead of `file://` | `file://`: an opaque origin, which blocks fonts and scripts in ways that differ from real hosting |
| D4 | Network blocked by default | Open network: a failed CDN request fails silently and makes renders irreproducible |
| D5 | Font fallback read from Chromium (`CSS.getPlatformFontsForNode`) | `document.fonts.check()`: returns true for families with no `@font-face` rule whether or not they are installed |
| D6 | Contrast from axe-core for HTML, and pixel measurement for SVG and axe's incomplete items | DOM-only contrast: cannot see backgrounds made of images, gradients or SVG shapes |
| D7 | Colour-vision check by matrices on declared series colours; emulated images for the vision brief | Sampling pixels of an emulated render for the check: depends on mark shapes and anti-aliasing |
| D8 | Data fidelity through declared scales and values (`data-rk-*`) | Inferring scales from axis ticks: fragile and silent when wrong |
| D9 | Value and chroma through color-theory's `checks.py` | Re-implementing them in TypeScript: two sources of truth for one method |
| D10 | Vision is a brief plus answer validation; the kit calls no model | Calling a vendor's vision API: ties every skill that uses the kit to that vendor |
| D11 | Text measured in the same browser that renders | Pretext (`@chenglou/pretext`, pre-1.0) or opentype.js: another dependency, and a different text engine from the one that draws the result |
| D12 | PDF fonts checked with poppler's `pdffonts` | `pdf-lib`: last released 2022 |

## 11. Acceptance tests

Each test names its sample or setup and its expected result. All run from the render-kit folder. "Fails X" means the report shows `X` with status `fail`, and `rk check` exits 1.

| AT | Setup and command | Expected |
|---|---|---|
| AT01 | `bin/rk render samples/good/slide.html --out /tmp/rk-at01.png` | Exit 0; a PNG of 1920 × 1080 pixels. With `--scale 2`: 3840 × 2160 |
| AT02 | `bin/rk render samples/good/chart.svg --out /tmp/rk-at02.pdf` | Exit 0; a one-page PDF whose page size equals the SVG's size in points (1 CSS px = 0.75 pt), and `pdfimages -list` shows no raster image |
| AT03 | `bin/rk check samples/good/slide.html --pdf` | Exit 0; every check `pass` or, when its tool is missing, `skipped` with a reason; `report.json`, `render.png` and `render.pdf` exist |
| AT04 | Render `samples/good/animated.html` twice with `--at 500`, and once with `--at 0` | The two `--at 500` PNGs are byte-identical; the `--at 0` PNG differs from them |
| AT05 | `bin/rk check samples/bad/resources.html` (it links a stylesheet on `https://example.com`) | Fails `resources` only; the item names the URL; no network request left the machine |
| AT06 | `bin/rk check samples/bad/console.html` (a script throws) | Fails `console` only; the item carries the exception message |
| AT07 | `bin/rk check samples/bad/fonts.html` (text set in a family that is not installed and has no `@font-face`) | Fails `fonts` only; the item names the requested family and the font actually used |
| AT08 | `bin/rk check samples/bad/overflow.html` (text longer than its fixed-size box with `overflow: hidden`, plus an element placed past the stage's right edge) | Fails `overflow` only, with one clipped-text item and one `offstage` item |
| AT09 | `bin/rk check samples/bad/collision.svg` (two chart labels drawn over each other) | Fails `collision` only; adding `data-rk-allow-overlap` to one label makes it pass |
| AT10 | `bin/rk check samples/bad/contrast.html` (`#777777` text on `#888888`) | Fails `contrast` only; the item's measured ratio is below 1.5 |
| AT11 | `bin/rk check samples/bad/cvd.svg` (series `#d62728` and `#2ca02c`) | Fails `cvd` only, under deuteranopia, with a distance of 0.039 ± 0.002 |
| AT12 | `bin/rk check samples/bad/fidelity.svg` (a bar chart where one bar's height is 20 user units off its `data-rk-y`) | Fails `fidelity` only; the item names that bar with expected and actual edges; the other bars pass |
| AT13 | `bin/rk check samples/bad/a11y.html` (a `<button>` with no accessible name and an `<img>` with no `alt`) | Fails `a11y` only, with rule ids `button-name` and `image-alt` |
| AT14 | `bin/rk check samples/bad/value.html` (the `data-rk-focal` area is flat mid-grey while the brightest contrast is elsewhere). Then again with `RK_COLOR_THEORY=/nonexistent` | First run fails `value` only. Second run: `value` is `skipped` with a reason; exit 0, and exit 1 with `--strict` |
| AT15 | `bin/rk check samples/bad/pdf-fonts.html --pdf` (text in a variable font, or a static font forced to a bold it lacks) | Fails `pdf-fonts` only; the item shows a `Type 3` font |
| AT16 | `bin/rk text wrap --font '400 20px sans-serif' --text '<the 60-word sample paragraph in test/fixtures/wrap.txt>' --width 300 --format svg`, then render that SVG and read the `<text>` box | Exit 0; every line narrower than 300 px, and the rendered box at most 301 px wide. With `--width 20`: exit 1 and `overflow: true`. With `--font '400 20px "No Such Font"'`: exit 2 |
| AT17 | `bin/rk brief samples/good/slide.html --questions questions/slide.md --out-dir /tmp/rk-at17 --simulate deuteranopia` | Exit 0; `brief.md` lists every question as Q1…Qn and both PNG paths; `answers.template.json` has one entry per question |
| AT18 | `bin/rk brief --verify` on: a complete answers file with all `yes`; one with a `no`; one with a missing question; one with an empty `reason` | Exit 0; exit 1 listing the `no`; exit 2; exit 2 |
| AT19 | `bin/rk render missing.html --out x.png`; `bin/rk render https://example.com --out x.png`; `bin/rk frobnicate`; `bin/rk render samples/good/slide.html --out x.pdf --simulate deuteranopia`; `bin/rk check samples/good/slide.html --threshold cvd.nope=1` | Each exits 2 with a message on stderr and `{"error": …}` on stdout |
| AT20 | `bin/rk selftest` | Exit 0; every bad sample fails exactly its expected checks and every good sample fails none |
| AT21 | `npm test` | Exit 0. Unit tests include: OKLab of `#ffffff` is (1, 0, 0) within 1e-4; the WCAG ratio of `#000000` on `#ffffff` is 21; the deuteranopia distance of `#d62728`/`#2ca02c` is 0.039 ± 0.002; linear-scale mapping with a reversed range; parsing an M/L path; greedy wrapping with a fake measuring function; every exit-code rule in section 4 |
| AT22 | `time bin/rk check samples/good/slide.html` on the build machine | Finishes in under 20 s |

## 12. Open questions

- Fonts are not bundled, so renders on two machines can differ when their installed fonts differ; the `fonts` check makes a fallback loud, not impossible. Revisit when the brand profile fixes the type families.
- GPU rasterisation can differ between machines; byte-identical output is required on one machine only.
- Multi-slide decks, video frames and PowerPoint belong to `scene-engine`, which will reuse `src/server.ts`, `src/browser.ts` and `src/seek.ts` rather than copy them.
