# render-kit specification

Reader: the agent that builds render-kit, and anyone who later changes it. Agents that only *use* the kit read `AGENTS.md`.

Grounded in the frontend research (`~/Documents/Work/lab/frontend-2026/`): `synthesis.md` section "Inputs for the render kit", the four track reports, and the gap pass's testing-tools findings (`gaps/report.md`, G2).

## 1. What it is

render-kit (command `rk`) turns an HTML or SVG file into the PNG or PDF a reader will see, then checks that output with code. Producer skills (frontend, presentation, information design, photo) call it in a loop: render, check, fix, render again. After the code checks pass, `rk brief` writes specific questions for a reviewer who can see images and did not make the artifact, and `rk brief --verify` checks that reviewer's answers. The kit never calls a model itself, so it works with any agent.

Terms used below:
- **Stage:** the area that is the artifact. It is the element marked `data-rk-stage` when one exists; otherwise, HTML uses the viewport width and full document height unless `--height` fixes the viewport, and SVG uses its own size.
- **Check:** one code test. Its status is `pass`; `fail`; `incomplete` (it ran and found no failure, but could not measure some items, which it lists); `skipped` (it applies but could not run, for example because a tool is missing; a reason is always given); or `n/a` (the input has nothing for it to check, such as no chart markup or no PDF; a reason is always given).
- **Mark:** an SVG element that encodes a data value: a bar, a point, a line.
- **Data-graphic focal:** a focal area declared with `data-rk-focal="data-graphic"`; its value target is distinct from the ordinary composition target.
- **OKLab distance:** the Euclidean distance between two colours in the OKLab colour space (Björn Ottosson, 2020), where lightness L runs from 0 to 1.
- **Page clock:** Playwright's fake clock, which controls `Date`, timers and `requestAnimationFrame` inside the page.

## 2. Scope

In scope: rendering and checking one HTML page or SVG file per `render` or `check` invocation; a single `brief` can collect several labelled HTML or SVG inputs; the 11 checks in section 6; measuring and wrapping text; vision briefs; a self-test.

Out of scope: video encoding and PowerPoint output (the separate `scene-engine`, later); multi-slide decks in one call (render each slide file separately); Firefox and WebKit; native desktop or mobile apps; calling any vision or language model; bundling fonts.

## 3. Environment and dependencies

- **Node 24 or later**, running TypeScript directly through type stripping. Source files are `.ts` with erasable syntax only (no `enum`, `namespace`, parameter properties or decorators); imports name the `.ts` extension. There is no build step and no bundler. `bin/rk` exits 2 with a message on Node older than 24. `tsconfig.json` sets `noEmit`, `allowImportingTsExtensions`, `erasableSyntaxOnly`, `strict`, `module` and `moduleResolution` `nodenext`.
- **Runtime dependencies, exact versions:** `playwright` 1.63.0 and `@axe-core/playwright` 4.13.0. **Dev dependency:** `typescript` 5.9.3, used only for `tsc --noEmit`. Any further dependency needs an entry in section 10.
- **Browser:** Playwright's Chromium launched with `channel: 'chromium'`: full Chromium in the new headless mode, with GPU rasterisation and WebGL through ANGLE on Metal (verified on the build Mac, 2026-09-26). Playwright's Chromium build exposes no WebGPU in any mode (`navigator.gpu` is undefined, verified the same day), so WebGPU content is out of scope. The headless shell is never used: it rasterises WebGL on the CPU, and its frames differ from the new mode's by 3.6–8.1% of pixels (research: graphics-motion). Pages come from `browser.newContext()`, which `@axe-core/playwright` requires. Every report records the browser version and the mode.
- **Local server:** local files are never loaded over `file://`. For a file input, rk starts a static HTTP server (Node's `http` module, no dependency) on `127.0.0.1` with a free port, rooted at `--root` (default: the input file's folder), and loads the input over `http`. Requests for paths outside the root get 404. The server stops when the command ends. For a URL input, no server starts, `--root` is refused (exit 2), and the URL must serve an HTML page.
- **Network:** blocked by default. The page may request only its own origin: the rk server's for a file input, the URL's for a URL input. Every other request is aborted and recorded. `--allow-network` lifts the block.
- **Optional tools**, detected at run time; when a check dependency is missing, that check is `skipped` with the reason. A missing page-render tool makes `rk brief --pdf` exit 2 with the tool error:
  - `pdffonts` from poppler, for `pdf-fonts`;
  - `pdftoppm` from poppler, for PDF page previews in `rk brief --pdf`;
  - Python 3 with numpy and Pillow, plus `color-theory`'s `scripts/checks.py`, for `value`. The color-theory folder is the env var `RK_COLOR_THEORY` if set, else `../skills/color-theory` relative to the render-kit folder.
- **Platforms:** developed on macOS (Apple Silicon); must also run on Linux.

## 4. Command-line interface

`rk <command> [options]`. Normal command output is one JSON document on stdout (except `rk text wrap --format svg`, which prints SVG) and progress on stderr. `rk --help`, `rk help`, a bare `rk`, and `rk <command> --help` print usage to stdout and exit 0; command help lists its flags.

**Exit codes**
- `0`: success.
- `1`: a check failed, text overflowed, or a vision answer was `no`. With `--strict`, also any `skipped` or `incomplete` check, or any `unsure` or `not-judged` answer. `n/a` never affects the exit code.
- `2`: usage, input or render error. stderr carries the message; stdout carries `{"error": "<message>"}`.

### 4.1 Shared render options
Used by `render`, `check` and `brief`.

| Option | Meaning | Default |
|---|---|---|
| `<input>` | A local `.html` or `.svg` file, or a URL on `http://localhost:<port>/` or `http://127.0.0.1:<port>/` (a dev server). Any other URL, or a missing file, is exit 2 | required |
| `--root <dir>` | Folder the local server serves | the input file's folder |
| `--width`, `--height` | Browser viewport in CSS pixels | HTML: 1920 × 1080. If `--height` is omitted, capture extends to the full document height while the layout viewport remains 1080 px high. Passing `--height` fixes the capture to that viewport height. SVG: its `width`/`height` attributes, else its `viewBox` size |
| `--scale <n>` | Device pixel ratio | 1 |
| `--at <ms\|end>` | Scene time to render (section 5) | `end` |
| `--settle <ms>` | Page-clock time given to script-driven animation when `--at end` | 10000 |
| `--boot <ms>` | Page-clock time run after `load`, so code that draws in its first frames runs (section 5) | 100 |
| `--media <screen\|print>` | CSS media type for PDF output | `screen` |
| `--wait-for <selector>` | Wait for this CSS selector after load, advancing the page clock while waiting (section 5) | none |
| `--timeout <ms>` | Limit for load and waits; exceeding it is exit 2 | 30000 |
| `--allow-network` | Permit requests to other origins | off |

### 4.2 `rk render <input> --out <file.png|file.pdf> [render options] [--simulate <type>]`
Renders the stage. PNG: a screenshot clipped to the stage, using full-page capture when HTML `--height` is omitted so content below the initial viewport is included. PDF: `page.emulateMedia({ media })` with `--media` (default `screen`, so the PDF shows what the PNG shows; `page.pdf()` on its own uses `print` styles), then `page.pdf({ preferCSSPageSize: true, printBackground: true, tagged: true, outline: true })`; when the page sets no `@page` size, the PDF page size equals the stage size. `--simulate protanopia|deuteranopia|tritanopia|achromatopsia` renders the PNG as seen with that colour-vision deficiency, through Chromium's `Emulation.setEmulatedVisionDeficiency`; it is refused (exit 2) for PDF.

Output: `{"out", "format", "width", "height", "scale", "at_ms", "browser": {"version", "mode"}, "requests_blocked": []}`. `width` and `height` are the image's pixel size (PNG) or the page size in points (PDF).

### 4.3 `rk check <input> [render options] [--checks <ids>] [--expect-request <url-pattern>=<status>] [--pdf] [--out-dir <dir>] [--strict]`
Renders once, runs the checks, and writes `report.json` and `render.png` (plus `render.pdf` with `--pdf`) into `--out-dir` (default: a new temporary folder). Prints the report (section 7). `--checks` takes comma-separated check ids; an unknown id is exit 2. By default all 11 checks run and each appears in the report; one with nothing to check in this input is `n/a` (section 7), and `pdf-fonts` is `n/a` without `--pdf`. `--threshold <check>.<name>=<value>` (repeatable) overrides one of the named thresholds in the table at the start of section 6, for example `--threshold cvd.min_distance=0.08`; an unknown name, or a value that is not a number, is exit 2.
`--expect-request '<url-pattern>=<status>'` is repeatable. The pattern is matched against the full request URL; `*` matches any sequence and every other character is literal. The status must be a 4xx or 5xx HTTP status. A matching failed response is listed with item status `expected` and does not fail `resources`; every unmatched HTTP error, blocked request, and network failure still fails.

### 4.4 `rk text measure --font <css font> --text <string> [--font-file <path>]`
Measures one line of text in the browser with canvas `measureText`, after `document.fonts.load(font)`. `--font` is a CSS font shorthand such as `600 32px "Source Sans 3"`. `--font-file` registers that file with the FontFace API under the family named in `--font`. Before measuring, rk applies the font rule in 4.9. Output: `{"width", "ascent", "descent", "font"}` in CSS pixels.

### 4.5 `rk text wrap --font <css font> --text <string> --width <px> [--line-height <multiplier>] [--max-lines <n>] [--format json|svg] [--x <n> --y <n>] [--font-file <path>]`
Breaks text into lines no wider than `--width`, measuring in the browser (canvas `measureText`) and finding break opportunities with `Intl.Segmenter` (word granularity). A line may break at a whitespace segment, after a hyphen or slash, or between two adjacent word segments with no space between them, which is how Chinese and Japanese text breaks. Lines are filled greedily. Before measuring, rk applies the font rule in 4.9. Output JSON: `{"lines": [{"text", "width"}], "line_height", "height", "overflow": false}`; `--format svg` prints a `<text>` element with one `<tspan x=".." dy="..">` per line, positioned at `--x`, `--y` (defaults 0, 0), `font` set from `--font`. `overflow` is true, and the exit code 1, when one word is wider than `--width` or the line count exceeds `--max-lines`. Line height defaults to 1.2.

### 4.6 `rk brief [<input> | --state <label>=<input> ...] --questions <file> --out-dir <dir> [--purpose <text>] [--simulate <types>] [--pdf] [render options]`
Prepares a review for someone who can see images and did not make the artifact. It renders the PNG, plus one PNG per type in `--simulate` (comma-separated), runs `rk check`, and writes into `--out-dir`:
- `render.png` and `render-<type>.png`; with `--pdf`, also `render.pdf` and `render-page-<n>.png` for every PDF page, rasterized with Poppler's `pdftoppm` at 96 dpi;
- with repeated `--state '<label>=<file-or-local-URL>'`, one labelled input per state, each rendered and checked independently in a `state-<n>-<slug>/` subfolder; use these options instead of the positional `<input>`;
- `report.json`, the code-check report;
- `brief.md`: what the artifact is (`--purpose`), the image paths, a summary of the code checks (so the reviewer does not re-judge what code measured), the rules for answering, and the numbered questions `Q1`…`Qn`;
- `answers.template.json`: `{"reviewer": null, "answers": [{"id": "Q1", "question": "...", "answer": null, "where": null, "reason": null}]}`.

The PDF sentence is included in `brief.md` only when `--pdf` is supplied. With several inputs, each label, input, file list, and check summary appears in its own section; questions and answer numbering are shared across the brief.

`--expect-request` is also accepted and applied to each input's `resources` check using its exact URL-pattern and HTTP-status matching rules from section 4.3.

The questions file has one question per line starting with `- ` or `1. `; lines starting with `#` are group headings and are copied into the brief. Questions are phrased so that **yes means the artifact passes**. The kit ships default sets in `questions/chart.md` and `questions/slide.md`. A questions file with no questions is exit 2.

Answering rules written into the brief: `answer` is `yes`, `no`, `unsure` or `not-judged` (for a reviewer that cannot see the image); `reason` is one sentence; `where` names the region or element for `yes` and `no`.

### 4.7 `rk brief --verify <answers.json> [--strict]`
Checks a filled answers file against the questions in the same folder's `brief.md`. Exit 2 when the file is malformed, a question is missing, an answer is not one of the four values, a `reason` is empty, or a `yes`/`no` lacks `where`. Otherwise prints `{"no": [ids], "unsure": [ids], "not_judged": [ids]}`; exit 1 when any answer is `no` (or, with `--strict`, any `unsure` or `not-judged`), else 0.

### 4.8 `rk selftest [--strict]`
Runs `rk check --pdf` on every sample listed in `samples/expectations.json` and compares the set of failing checks with the expected set. The comparison is by check, not by item. Good samples must fail nothing; each bad sample must fail exactly its expected checks. When a tool a check needs is missing on this machine, that check is `skipped`: on a good sample this is allowed, and on a bad sample that expects the check to fail it counts as an unmet but allowed expectation. Both are reported, and both fail the self-test under `--strict`. Prints `{"samples": [...], "ok": true|false}`; exit 0 when every expectation holds.

### 4.9 Font rule for the text commands
Both `text measure` and `text wrap` first draw the text in a hidden element set in `--font` and apply the `fonts` check's rule (6.3) to it. If any glyph comes from another font, they exit 2 naming the font actually used. They never measure with a fallback font.

## 5. Rendering and time

1. Before navigation, install the page clock at `2026-01-01T00:00:00Z` and pause it (`page.clock.install({ time })`, then `page.clock.pauseAt(time)`), so `Date`, timers and `requestAnimationFrame` are identical on every run and a page that shows "today" always shows that date. From here on, page time moves only in the steps below.
2. Load the input and wait for the `load` event.
3. Boot: `page.clock.runFor(boot)`, with `--boot` (default 100 ms). Code that draws in its first animation frames, such as deferred hydration or a chart that waits a frame before drawing, runs here. A page whose clock has been paused since before navigation still shows its pre-render placeholder at `load` (verified 2026-09-26), which is why this step exists. Scene time 0 is the end of boot.
4. Wait for `document.fonts.ready`. With `--wait-for`, check for the selector, and while it is absent call `page.clock.runFor(16)` and check again, until it appears or `--timeout` passes in page time or in real time, whichever comes first (exit 2). Then wait for network idle.
5. Seek to scene time T. Always advance with `page.clock.runFor`, never `fastForward`: `runFor` fires every timer and animation frame on the way, so frame-to-frame code (easing, springs, D3 timers) sees every step, while `fastForward` fires each due callback at most once (verified 2026-09-26: 62 frames against 1 over 1,000 ms).
   - Take the list of animations from `document.getAnimations()` once, before seeking, and seek every animation in that list. A fresh query after a seek drops finished CSS transitions (research: graphics-motion F3). View-transition pseudo-element animations are in the list and are seeked like the others.
   - `--at <ms>`: T = ms. Call `page.clock.runFor(T)`. Then pause every animation in the list (CSS animations, CSS transitions, Web Animations) and set its `currentTime` to boot + T, and call `pauseAnimations()` and `setCurrentTime((boot + T) / 1000)` on every `<svg>` root (SMIL). The page clock, the animations and SMIL then all stand at boot + T after `load`.
   - `--at end`: call `page.clock.runFor(settle)` with `--settle`, so script-driven animation completes. Then call `finish()` on every finite CSS or Web Animation, pause every infinite one at `currentTime` = boot + settle, and set SMIL time to (boot + settle) / 1000.
   - Animations are assumed to start at `load`. An animation a script starts later is seeked as if it had started at `load`; the kit cannot know its start.
6. Capture. Do not wait on `requestAnimationFrame` after seeking: the page clock is paused. For HTML without `--height`, the stage extends to the maximum of the viewport and document scroll heights; capture it with full-page screenshot mode while keeping the layout viewport at its configured size. With explicit `--height`, the stage is limited to that viewport. A marked `data-rk-stage` remains the capture area, including when it extends below the viewport.
7. SVG input is wrapped by the server in an HTML page (`<!doctype html>`, zero margins, transparent background) with the SVG inline, served from the SVG's own folder so relative references resolve. Nothing is written next to the input.
8. When a second CDP session is opened (for font or vision-deficiency queries), send `Emulation.setDeviceMetricsOverride` on it with the same size and scale; otherwise screenshots from that session come back at scale 1 (research: output-pipelines F1 item 8; verified 2026-09-26). This includes `--simulate` at any `--scale` (AT01).

The same input and options must give a byte-identical PNG on repeated runs on one machine, for HTML, CSS and SVG content. Content drawn with WebGL is excluded: GPU rasterisation is not guaranteed to repeat bit for bit.

## 6. Checks

Every check skips elements inside `[data-rk-ignore]`, and elements that are not visible: zero area, `display: none`, `visibility: hidden`, or opacity 0. SVG geometry with a zero-width or zero-height bounding box remains visible when it has a computed stroke width above 0 and a stroke other than `none`.

Visual text scans and the `overflow` offstage scan also skip descendants hidden by a closed `<details>` element, except for its visible direct `<summary>` subtree; focusable elements positioned outside the viewport before focus, such as an offscreen skip link; and clipped visually-hidden patterns using `clip-path: inset(50%)` or a positioned box of at most 1 px with `clip` or `clip-path`. These are visual-check exclusions, not accessibility exemptions: `a11y` still runs, and hidden states should be opened and checked in a browser when they are part of the product. A horizontal child that overflows an active `overflow-x: auto` or `scroll` ancestor is allowed beyond that scrollport's left or right edge; the scroll container itself and vertical overflow remain subject to the stage and clipping checks.

- A **text element** is a visible HTML element with at least one non-empty text node as a *direct* child, or an SVG `<text>` element.
- A **text box** is, for HTML, the union of the client rectangles of a DOM `Range` over the element's direct text nodes. For SVG, each `<tspan>` is its own text box, and a `<text>` without `<tspan>` children is one box. Boxes are in screen coordinates.

The thresholds below are the kit's defaults, set by judgment or calibration. Each can be changed with `--threshold <check>.<name>=<value>`, and the report states every threshold used. The WCAG contrast ratios (4.5 and 3) are fixed.

| Name | Default | Where it came from |
|---|---|---|
| `overflow.tolerance_px` | 1 CSS px | Judgment: sub-pixel rounding |
| `collision.min_overlap_px` | 1 CSS px, in both width and height | Judgment: anti-aliased edges |
| `contrast.text_exclusion` | 0.1 OKLab distance | Judgment: removes the text's own anti-aliased pixels from the background sample |
| `contrast.min_background_share` | 0.30 | Judgment: below it the background is an image or a gradient |
| `cvd.min_distance` | 0.06 OKLab distance | Calibrated 2026-09-26 (6.7) |
| `fidelity.tolerance_px` | 0.5 CSS px | Judgment: half a pixel at scale 1 |
| `value.min_edge_share` | 2× area share | color-theory T1 default; focal value-edge energy compared with its area share |
| `value.data_graphic_min_edge_share` | 0.5× area share | Judgment for a data-layer focal area: chart labels and surrounding copy also contribute value edges |
| `value.max_focal_area_share` | 0.50 of the stage | Dogfood finding F3: a larger ordinary focal box cannot pass the general prominence comparison |
| `value.achromatic_chroma_max` | 0.01 OKLCH C | Judgment: maximum chroma treated as achromatic for T5 on data graphics |

### 6.1 `resources` (all inputs)
Fail when any request was blocked by the network rule or failed (network error, or HTTP status 400 or above), except for a request declared with `--expect-request` whose full URL pattern and HTTP status both match. Expected response items have `status: "expected"`, `expected_status` and the matching `pattern`; unmatched items have `status: "unexpected"`. The check passes when it has no unexpected items. Items include the URL and reason.

`requests_blocked` in the report remains the raw record of all observed failed requests, including ones classified as expected by this check.

### 6.2 `console` (all inputs)
Fail on any uncaught page exception or `console.error` message between navigation and capture. Items: the first 200 characters of each message.

### 6.3 `fonts` (all inputs)
For every text element, ask Chromium which fonts drew its glyphs (`CSS.getPlatformFontsForNode` over CDP). Let F be the first family in its computed `font-family`.
- F is a CSS generic family (`serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, `system-ui`, `ui-serif`, `ui-sans-serif`, `ui-monospace`, `ui-rounded`, `math`, `emoji`, `fangsong`): pass.
- F matches a family in `document.fonts` (an `@font-face` or FontFace font): pass when that font's status is `loaded` and every glyph was drawn by a custom font (`isCustomFont: true`).
- Otherwise F is a system font: pass when every glyph was drawn by a platform font whose `familyName` equals F, ignoring case.

Fail items: the element's selector, F, and each font actually used with its glyph count. A font that draws some glyphs but not all (for example, Vietnamese diacritics falling back to another font) fails.

### 6.4 `overflow` (all inputs)
Fail when any of these holds, by more than `overflow.tolerance_px`:
- a text box extends beyond its element's padding box;
- a text box extends beyond the padding box of the nearest ancestor that clips (`overflow` other than `visible`);
- an element with `text-overflow: ellipsis` has `scrollWidth > clientWidth` (truncated text), unless it or an ancestor has `data-rk-allow-truncate`;
- a visible element's box, or an SVG `<text>` box, extends beyond the stage (item kind `offstage`);
- an SVG `<text>` box extends beyond its nearest `<svg>` viewport.

An active horizontal scroll container (`overflow-x: auto` or `scroll` and `scrollWidth > clientWidth`) is a deliberate viewport for its wide descendants; its horizontal clipping is accepted.

The screenshot capture bound is 16,384 output pixels per dimension (presentation dogfood F1; Chromium full-page captures above this size can wrap). Measure the first `data-rk-stage` when present, otherwise the document page (or the SVG root for an SVG input); use full document height unless `--height` fixes the viewport, multiply by `--scale`, and round up. Fail with a `capture-limit` item when width or height exceeds the bound. The item names the target, measured dimensions, and limit. When the requested PNG capture exceeds the bound, `rk check` crops its diagnostic PNG to the bound so a report can still be written.

Items: kind, selector, overflow in pixels on each side; `capture-limit` items carry `target`, `width_px`, `height_px`, `limit_px` and a message.

### 6.5 `collision` (all inputs)
Fail when two text boxes overlap by more than `collision.min_overlap_px` in both width and height. Not compared: two boxes of the same element, `<tspan>` boxes of the same `<text>`, an element and its descendant, and any pair where either element or an ancestor has `data-rk-allow-overlap`. Find candidate pairs by sorting boxes by their left edge and sweeping, not by testing every pair. Items: both selectors and the overlap rectangle.

### 6.6 `contrast` (all inputs)
WCAG 2.2 success criterion 1.4.3: contrast ratio at least 4.5:1, or 3:1 for large text (font size at least 24 CSS px, or at least 18.66 CSS px at weight 700 or more).
- HTML text: axe-core's `color-contrast` rule.
- SVG `<text>`, and every item axe-core reports as incomplete: measured on the rendered PNG. The text colour is the computed `fill` (SVG) or `color` (HTML). The background is the most frequent colour in the text box after removing pixels within `contrast.text_exclusion` of the text colour. The ratio uses the WCAG 2 relative-luminance formula.
- When the most frequent background colour covers less than `contrast.min_background_share` of the remaining pixels (text over an image or a gradient), the item is `incomplete`.

Items: selector, text colour, background colour, ratio, required ratio.

### 6.7 `cvd` (inputs with `[data-rk-series]`)
Checks that categorical colours stay distinguishable for colour-vision deficiency. Each series' colour is the most common computed `fill` (else `stroke`) among elements with that `data-rk-series` value. Fewer than two series: `n/a`. For normal vision and for protanopia, deuteranopia and tritanopia (Machado, Oliveira and Fernandes 2009 matrices at severity 1.0, applied in linear sRGB and clamped to [0, 1]), compute the smallest OKLab distance between any two series. Fail when any is below `cvd.min_distance`. Normal vision is included on purpose: two series too close for anyone to tell apart is the same failure.

A stroked SVG geometry with a zero-width or zero-height box counts as visible when its computed stroke width is above 0. For such a mark, the stroke supplies the series colour even if its computed fill is not `none`.

The default, 0.06, was calibrated on 2026-09-26 with this method: the Okabe–Ito palette, designed for colour-vision deficiency, keeps at least 0.076 under all three (passes); the pair `#d62728`/`#2ca02c` falls to 0.039 under deuteranopia (fails); `#1f77b4`/`#ff7f0e` keeps 0.246 (passes). Items: vision type, the closest pair and its distance.

### 6.8 `fidelity` (inputs with `[data-rk-chart]`)
Checks that each mark sits where its data says, using markup the chart declares (section 8). The marks are the elements matching `[data-rk-chart] [data-rk-mark]`; value attributes on any other element are ignored. Expected positions come from the chart's declared scales, in the chart root's user space. Actual positions are read in the same space: a mark's geometry is mapped through the inverse of the root's `getCTM()` times the mark's `getCTM()`. Both are then mapped to screen coordinates, and their difference is compared with `fidelity.tolerance_px`, so the tolerance does not depend on the chart's `viewBox`.
- The scale for an axis is `linear` (dates are given as epoch milliseconds on a linear scale) or `band`. A `band` axis is not checked. Any other scale type (for example `log`) makes each mark on that axis an `incomplete` item, "scale type not supported".
- `<rect>` with `data-rk-y` (vertical bar): its top and bottom edges must equal `scaleY(data-rk-y)` and `scaleY(base)`, in either order, where `base` is `data-rk-y0` if given, else 0 if 0 lies in the domain, else the domain minimum. `<rect>` with `data-rk-x` (horizontal bar): the same with left and right edges and the x scale.
- `<circle>` or `<ellipse>` with `data-rk-x` and/or `data-rk-y`: its centre must equal the scaled value on each linear axis given.
- `<polyline>`, or `<path>` whose `d` uses only absolute `M` and `L` commands, with `data-rk-points="x1,y1 x2,y2 …"` in data values: its vertices must equal the scaled points, in order and equal in number. A path with any other command is an `incomplete` item ("curved path not checked").
- No `[data-rk-chart]`: `n/a`. A mark whose chart lacks a needed scale attribute: fail item "missing scale".

Items: selector, expected, actual.

### 6.9 `a11y` (all inputs; SVG input is checked in its HTML wrapper)
axe-core (the only engine; see section 12) with the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` and `wcag22aa`, with `color-contrast` disabled because `contrast` owns it. The check's result names the engine and its version. Fail on any violation. Items: rule id, impact, selectors. When there are no violations but axe-core reports incomplete results, the status is `incomplete` with those as items.

### 6.10 `value` (inputs with `[data-rk-focal]`)
Runs color-theory's image checks on the rendered PNG: `python3 <color-theory>/scripts/checks.py value <png> --focal x0,y0,x1,y1 --out <tmpdir>` and `... chroma <png> --focal x0,y0,x1,y1`, where the box is the focal element's bounding box in PNG pixels (CSS pixels × scale). The kit records every `T<n> PASS`, `FAIL` or `CHECK` line and the measurement lines before it as an item.

For T1, the kit compares the measured value-edge ratio with `value.min_edge_share` (default 2×). When the focal element is marked `data-rk-focal="data-graphic"`, it uses `value.data_graphic_min_edge_share` (default 0.5×) instead, so the chart's data layer can be the focal area. The target used is included in the result line and both values are reported as thresholds. An ordinary focal area larger than `value.max_focal_area_share` (default 0.50 of the stage) makes T1 `incomplete` with the question “Does the focal area remain an effective visual entry point at this scale?” instead of failing the automatic test. The explicit data-graphic mode is exempt from this area rule.

For chroma T5, `CHECK` on a data graphic becomes item status `n/a` when all reported ring and focal chroma values are at or below `value.achromatic_chroma_max` (default 0.01 OKLCH C). Other `CHECK` outcomes are `incomplete` with a vision question. If the focal element covers the entire captured stage, the check is `incomplete` with a reason because no outside pixels exist for the value-rest or chroma-ring comparison. The value check fails if any item fails, is incomplete if any item is incomplete or a partial tool error prevents a judgement, and passes when all returned T-lines pass or are `n/a`. Missing Python, numpy, Pillow or the script, a non-zero exit with no T-lines, or no result line is `skipped` with a reason. No `[data-rk-focal]`: `n/a`.

### 6.11 `pdf-fonts` (when a PDF was produced)
Runs `pdffonts <pdf>`. Fail when any font's type contains `Type 3` or its `emb` column is `no`. Chromium turns variable fonts and synthetic bold into Type 3 fonts, which render poorly and cannot be edited (research track 3, finding F6). Items: font name, type, embedded. No `pdffonts`: `skipped`. No PDF produced: `n/a`.

## 7. Report

`report.json`, printed by `rk check`:

```json
{
  "rk_version": "0.1.0",
  "markup_version": 1,
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
  "summary": {"pass": 8, "fail": 1, "incomplete": 0, "skipped": 1, "n_a": 1}
}
```

All 11 checks (or those named in `--checks`) appear exactly once. A check with nothing to check in this input has status `n/a`. `reason` is required for `skipped`, `incomplete` and `n/a`. `markup_version` is the version of the section 8 conventions the checks read. Selectors are unique CSS selectors that `document.querySelector` resolves to the element.

## 8. Markup conventions

Producer skills and chart templates add these attributes; the checks read them.

| Attribute | On | Meaning |
|---|---|---|
| `data-rk-stage` | one element | The artifact's area; PNG capture and the offstage test use it |
| `data-rk-focal` | one element | The focal area, for `value`; set its value to `data-graphic` when the plotted data layer is the intended focal area and should use the separate T1 threshold |
| `data-rk-series="<name>"` | marks, legend swatches | Categorical series, for `cvd` |
| `data-rk-chart` | a `<g>` or `<svg>` | Chart root, with `data-rk-x-scale`, `data-rk-x-domain="d0,d1"`, `data-rk-x-range="r0,r1"` and the same three for y. Ranges are in the root's user units; a reversed range (for depth increasing downward) is allowed |
| `data-rk-mark` | `<rect>`, `<circle>`, `<ellipse>`, `<polyline>`, `<path>` | A data mark, with `data-rk-x`, `data-rk-y`, `data-rk-x0`, `data-rk-y0` or `data-rk-points` as in 6.8 |
| `data-rk-allow-overlap` | any | Exempt from `collision` |
| `data-rk-allow-truncate` | any | Exempt from the truncation test in `overflow` |
| `data-rk-ignore` | any | Exempt the subtree from all checks |

## 9. Code layout

One concern per file, at most 120 lines of logic each; a check that needs more is split into two files:

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
src/pdf-pages.ts           PDF page rasterization for review briefs (`pdftoppm`)
src/selftest.ts            runs samples/expectations.json
questions/chart.md, questions/slide.md
samples/good/              raf.html (a requestAnimationFrame loop, AT23), print-media.html (AT24), dense.svg (1,500 labels, AT26), slide.html (1920×1080: title, body text, an inline SVG chart with every data-rk attribute, a focal element), chart.svg, animated.html (a CSS animation, a Web Animation and a SMIL animation)
samples/bad/<id>.html|svg  one sample per check, built to fail that check only. Every sample is a complete document (`<!doctype html>`, `<html lang>`, `<title>`, or an SVG with `<title>`) so it fails nothing else
samples/expectations.json  [{"input": "bad/contrast.html", "fail": ["contrast"]}, …]
samples/fonts/             font files the samples need (OFL-licensed, with their licence files)
test/*.test.ts             node:test unit and integration tests
```

`npm test` runs `tsc --noEmit` and then `node --test`.

## 10. Decisions

| # | Decision | Rejected, and why |
|---|---|---|
| D1 | TypeScript run directly by Node 24 (type stripping) | A build step or `tsx`: extra machinery for no gain. Python: Playwright's primary platform is Node, and in-page code is JavaScript anyway |
| D2 | One browser mode: full Chromium, new headless | The headless shell: WebGL on the CPU. Mixing modes: frames differ by 3.6–8.1% of pixels. (Neither mode exposes WebGPU in Playwright's build.) |
| D3 | A local HTTP server instead of `file://` | `file://`: an opaque origin, which blocks fonts and scripts in ways that differ from real hosting |
| D4 | Network blocked by default | Open network: a failed CDN request fails silently and makes renders irreproducible |
| D5 | Font fallback read from Chromium (`CSS.getPlatformFontsForNode`) | `document.fonts.check()`: returns true for families with no `@font-face` rule whether or not they are installed |
| D6 | Contrast from axe-core for HTML, and pixel measurement for SVG and axe's incomplete items | DOM-only contrast: cannot see backgrounds made of images, gradients or SVG shapes |
| D7 | Colour-vision check by matrices on declared series colours; emulated images for the vision brief | Sampling pixels of an emulated render for the check: depends on mark shapes and anti-aliasing |
| D8 | Data fidelity through declared scales and values (`data-rk-*`) | Inferring scales from axis ticks: fragile and silent when wrong |
| D9 | Value and chroma through color-theory's `checks.py` | Re-implementing them in TypeScript: two sources of truth for one method |
| D10 | Vision is a brief plus answer validation; the kit calls no model | Calling a vendor's vision API: ties every skill that uses the kit to that vendor |
| D11 | Text measured in the same browser that renders | Pretext (`@chenglou/pretext`, pre-1.0), which research track 2 (graphics-motion F2) recommends as the layout step for wrapped SVG and Canvas labels: rejected here because the kit already runs the browser that draws the result, so measuring there needs no dependency and cannot disagree with the render. opentype.js: the same objection, plus different shaping |
| D12 | PDF fonts checked with poppler's `pdffonts` | `pdf-lib`: last released 2022 |
| D13 | One accessibility engine, axe-core | Adding IBM Equal Access now: the evidence that two engines catch more is one 30-defect benchmark (synthesis claim audit: evidence only) |
| D14 | The page clock is paused before navigation and run for a fixed boot period after `load` | Playwright's documented order (install the clock running, pause after load): how many frames run during load would then depend on load speed, so script-driven animation would differ between runs |
| D15 | PDF uses `screen` media by default | `print` media, `page.pdf()`'s default: the PDF would differ from the checked PNG with no check noticing |
| D16 | `rk brief --pdf` rasterizes every output PDF page with Poppler `pdftoppm` at 96 dpi | A viewport PNG alone cannot review page breaks or PDF content outside the first page |

## 11. Acceptance tests

Each test names its sample or setup and its expected result. All run from the render-kit folder. "Fails X" means the report shows `X` with status `fail`, and `rk check` exits 1.

| AT | Setup and command | Expected |
|---|---|---|
| AT01 | `bin/rk render samples/good/slide.html --out /tmp/rk-at01.png` | Exit 0; a PNG of 1920 × 1080 pixels. With `--scale 2`: 3840 × 2160. With `--scale 2 --simulate deuteranopia`: also 3840 × 2160 |
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
| AT19 | `bin/rk render missing.html --out x.png`; `bin/rk render https://example.com --out x.png`; `bin/rk frobnicate`; `bin/rk render samples/good/slide.html --out x.pdf --simulate deuteranopia`; `bin/rk check samples/good/slide.html --threshold cvd.nope=1`; `bin/rk check samples/good/slide.html --checks nope` | Each exits 2 with a message on stderr and `{"error": …}` on stdout |
| AT20 | `bin/rk selftest` | Exit 0; every bad sample fails exactly its expected checks and every good sample fails none |
| AT21 | `npm test` | Exit 0. Unit tests include: OKLab of `#ffffff` is (1, 0, 0) within 1e-4; the WCAG ratio of `#000000` on `#ffffff` is 21; the deuteranopia distance of `#d62728`/`#2ca02c` is 0.039 ± 0.002; linear-scale mapping with a reversed range; parsing an M/L path; greedy wrapping with a fake measuring function; every exit-code rule in section 4 |
| AT22 | `time bin/rk check samples/good/slide.html` on the build machine | Finishes in under 20 s |
| AT23 | `bin/rk render samples/good/raf.html --at 1000 --out /tmp/rk-at23.png`. The page draws a 10 × 10 px square only inside `requestAnimationFrame` callbacks, at x = 0.1 × (`Date.now()` − 2026-01-01T00:00:00Z in ms); before its first frame it shows a placeholder text instead | The square's left edge is at x = 110 ± 1 px (boot 100 ms + 1,000 ms). With `--at 0`: the square is at x = 10 ± 1 px and the placeholder is gone. A build that advances with `fastForward`, or skips the boot step, fails this test |
| AT24 | `bin/rk render samples/good/print-media.html --out /tmp/rk-at24.pdf` (an element with the text "screen-only" hidden by `@media print`) | `pdftotext` output of the PDF contains "screen-only"; with `--media print` it does not |
| AT25 | `bin/rk check samples/bad/cvd.svg --threshold cvd.min_distance=0.03` | `cvd` passes (0.039 is above 0.03) and the report states the threshold used; exit 0 |
| AT26 | `time bin/rk check samples/good/dense.svg` (1,500 non-overlapping text labels in a grid) | Exit 0 in under 60 s on the build machine |
| AT27 | Serve `samples/good/` with `python3 -m http.server` on a free port on 127.0.0.1, then `bin/rk check http://127.0.0.1:<port>/slide.html`; then the same with `--root samples/good` | First: exit 0 with the same check statuses as AT03 without `--pdf`. Second: exit 2 |
| AT28 | `bin/rk brief samples/good/slide.html --questions questions/slide.md --out-dir /tmp/rk-at28 --simulate protanopia,deuteranopia,tritanopia` | Exit 0; `render.png` is the base image and one `render-<type>.png` exists for each requested type |
| AT29 | Brief the same slide with `--simulate protanopia`, then compare `render.png` and `render-protanopia.png` | Both files exist and differ; the base render is unsimulated |
| AT30 | `bin/rk --help`, bare `bin/rk`, `bin/rk help`, and `bin/rk <command> --help` | Each exits 0 and prints usage listing all commands and their flags; command help lists that command's flags |
| AT31 | `bin/rk check samples/good/cvd-12.svg` | Exit 0; `cvd` passes at its default `cvd.min_distance` of 0.06 for all 12 declared series |
| AT32 | `bin/rk check samples/bad/horizontal-series.svg` (two red and green horizontal stroked paths, each with zero-height bounds) | Exit 1; `cvd` fails with both series and the 0.039 deuteranopia distance; `fidelity` checks both marks and passes |
| AT33 | Check `samples/bad/value.html` with `--threshold value.min_edge_share=0.1`; check a copy of `samples/good/data-graphic.svg` with its data-graphic marker removed; then check the original with `--threshold value.min_edge_share=100 --threshold value.data_graphic_min_edge_share=0.5` | The override is reported and T1 passes at 0.1; the ordinary focal area over 50% is `incomplete` with a vision question; the data graphic uses 0.5 and is not failed by the ordinary target; achromatic T5 is recorded as `n/a`, with the original `CHECK` line retained in its item |
| AT34 | `bin/rk brief samples/good/pdf-pages.html --questions questions/slide.md --out-dir /tmp/rk-at34 --pdf` | Exit 0; the brief lists `render.pdf` and both page PNGs; the PDF has two pages and both page images exist |
| AT35 | Write a questions file with two headings and one question under each, then call `writeBrief` | Exit 0; each heading immediately precedes its numbered question group, and numbering remains global |
| AT36 | Check a 1,400 px HTML document without `--height`, then check it with `--height 900` | Default capture is 1,400 px tall and `overflow` passes for text at the bottom; the explicit-height capture is 900 px and reports the bottom text as offstage |
| AT37 | Check an HTML artifact whose `[data-rk-focal]` covers `[data-rk-stage]` entirely while `python3` is instrumented to fail if called | `value` is `incomplete` with a clear no-outside-pixels reason; the external value/chroma script is not called |
| AT38 | Check a page that fetches a missing same-origin JSON file with `--expect-request '*/missing.json=404'`, then with a wrong URL pattern and a wrong status | The exact URL/status match is listed as `expected` and `resources` passes; either mismatch is `unexpected` and fails; malformed syntax exits 2 |
| AT39 | Check a page containing a closed-details paragraph, an offscreen focusable skip link, both clipped visually-hidden patterns, and wide text in an active horizontal scroller | `fonts`, `overflow`, and `collision` pass for excluded hidden text and intentional horizontal scrolling; ordinary offstage content remains covered by AT08 |
| AT40 | Build one brief from repeated labelled `--state` inputs without `--pdf` | Each state has its own labelled section, report and render; questions are shared; the PDF sentence is absent |

## 12. Open questions

- Fonts are not bundled, so renders on two machines can differ when their installed fonts differ; the `fonts` check makes a fallback loud, not impossible. Revisit when the brand profile fixes the type families.
- GPU rasterisation can differ between machines; byte-identical output is required on one machine only.
- Multi-slide decks, video frames and PowerPoint belong to `scene-engine`, which will reuse `src/server.ts`, `src/browser.ts` and `src/seek.ts` rather than copy them.
- WebGPU: Playwright's Chromium exposes no WebGPU adapter in any mode (verified 2026-09-26). Whether branded Chrome (`channel: 'chrome'`) does is untested; decide when a producer needs WebGPU output.
- `value` reads color-theory's `checks.py` text output (`T<n> PASS|FAIL` lines). If that format changes, `value` becomes `skipped` with the unparsed output as its reason; a JSON output mode in `checks.py` would remove the coupling.
- The section 8 attributes are a contract other skills write against. Reports carry `markup_version` 1; a breaking change to section 8 raises it.
- A second accessibility engine (IBM Equal Access) may catch defects axe-core misses; revisit when a larger comparison than the gap pass's one benchmark exists.
- PDF/UA conformance (veraPDF, `--flavour ua1`) for exported decks is deferred to the presentation skill; Chromium claims no PDF/UA conformance, and veraPDF checks structure, not reading order.
