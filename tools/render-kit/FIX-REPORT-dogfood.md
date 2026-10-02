# Dogfood fixes: render-kit (F3, F5, F10, F11)

## Findings and changes

- **F3 — value thresholds and data graphics.** Added `value.min_edge_share` (2×), `value.data_graphic_min_edge_share` (0.5×), `value.max_focal_area_share` (0.50), and `value.achromatic_chroma_max` (0.01 OKLCH C) to the `--threshold` registry and documented their origin and use in `SPEC.md`. A focal declared `data-rk-focal="data-graphic"` uses its own T1 target. An ordinary focal box covering over half the stage now produces an `incomplete` T1 item with a vision question instead of an automatic failure. This addresses the cited dashboard (0.78×) and weekly chart (0.63×) measurements.
- **F5 — zero-area stroked geometry.** CVD, fidelity, overflow and the shared text scan now treat SVG geometry with zero width or height as visible when it has a non-`none` stroke and computed stroke width above zero. Added a red/green horizontal-series fixture with zero-height bounds; its CVD check fails at the expected deuteranopia distance while fidelity passes.
- **F10 — PDF review briefs.** `rk brief --pdf` now renders and checks the PDF, creates a 96 dpi PNG for every PDF page with Poppler `pdftoppm`, and lists the PDF and page images in `brief.md` and the command result. A two-page fixture covers the page count and both images.
- **F11 — value result items and achromatic chroma.** Every `T<n> PASS`, `FAIL`, and `CHECK` line is retained as a report item with its preceding measurements and source result. An achromatic chart's T5 `CHECK` becomes item status `n/a` when its measured chroma is within the documented epsilon. Other `CHECK` results remain `incomplete` with a vision question.

## Verification

- Added acceptance tests AT31–AT34 and an in-repository `color-theory` output fixture for deterministic value parser tests.
- Confirmed the new horizontal series have bounding boxes `{width: 280, height: 0}` and the CVD/fidelity acceptance test reports the expected statuses.
- Confirmed the actual color-theory command on the new achromatic data-graphic fixture reports T1 pass at the 0.5 data-graphic threshold and records the achromatic T5 check as `n/a`.
- `npx tsc --noEmit`: passed.
- `node --test test/dogfood.test.ts`: 4 tests passed.
- `git diff --check`: passed.
- Final requested `npm test && ./bin/rk selftest` (with the temporary venv first on `PATH`): passed. `npm test` reports 40 tests passed; `rk selftest` reports all 19 sample expectations passed.

All changes remain uncommitted.

## F13 follow-up — 2026-10-02

### Findings and changes

- **Brief question groups.** `parseQuestions` now keeps each heading and its following questions together in `brief.md`; question IDs remain globally numbered for `answers.template.json` and `--verify`.
- **Whole-stage focal.** When the focal box covers the complete captured stage, `value` returns `incomplete` with a clear no-outside-pixels reason before calling color-theory. This avoids empty-array reductions for both the outside-value region and chroma rings.
- **Tall HTML pages.** HTML capture and stage-based checks now use the document scroll height by default while preserving the 1920 × 1080 layout viewport. Passing `--height` retains a fixed-height viewport and capture. `SPEC.md` records the behavior.

### Verification

- Regression coverage: brief grouping, tall-page capture plus explicit `--height`, and the whole-stage value guard. The value test instruments `python3` and confirms it is not called.
- `npm test`: exit 0, 44 tests passed.
- `./bin/rk selftest`: exit 0, all 19 sample expectations passed.
- Both acceptance commands used a temporary `/tmp/rk-f13-venv` with NumPy and Pillow because the default `python3` did not have the optional check dependencies.
- `git diff --check`: passed.

Current state: F13 complete; changes remain uncommitted.

## Frontend follow-up — F2, F4, F11 — 2026-10-02

### Findings and changes

- **F2 — expected failed requests.** Added repeatable `--expect-request '<url-pattern>=<status>'` for `rk check` and `rk brief`. `*` matches any sequence in the full URL. A matching HTTP 4xx/5xx appears with item status `expected` and does not fail `resources`; mismatched status or URL, network errors, and blocked requests still fail. No markup attribute is required.
- **F4 — accessibility patterns in visual scans.** Text scans and overflow checks skip closed `<details>` content while keeping its visible summary, positioned focusable content outside the viewport, and clipped visually-hidden text (`clip-path: inset(50%)` or the positioned 1 px clipped pattern). Wide descendants of an active horizontal scroller may pass beyond its left or right edge. The scroller itself and vertical overflow remain checked; axe still runs.
- **F11 — multi-state briefs.** `rk brief --state '<label>=<input>'` accepts repeated labelled files or local URLs. Each state receives its own report, render, simulation images, and optional PDF page renders; the brief shows separate labels and check summaries with shared review questions. The PDF sentence is omitted without `--pdf`.

### Verification

- Added CLI acceptance tests for expected request matching and both mismatch axes, visual exclusions and horizontal scrolling, and a two-state brief without PDF guidance. Updated brief API and type fixtures, help coverage, and the PDF guidance assertion.
- `npm test`: exit 0, 47 tests passed. `./bin/rk selftest`: exit 0, all 19 sample expectations passed. Both ran with `/tmp/rk-f13-venv/bin` first on `PATH` because the default `python3` lacks NumPy and Pillow; `AGENTS.md` lists these optional color-check dependencies.
- `git diff --check`: passed. All changes remain uncommitted.
