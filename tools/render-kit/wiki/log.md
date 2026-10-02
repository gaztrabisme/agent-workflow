# Work log

## 2026-10-02 — Presentation F1 closed

- Grounded in F1 from `/Users/GaryT/Documents/Work/lab/design-programme/dogfood/runs-3-5/presentation/report.md`: a stacked stage could exceed Chromium's 16,384 px screenshot bound without a capture-limit diagnostic, and extra `[data-rk-stage]` elements were mistaken for separately checked slides.
- `overflow` now measures the first stage, or the document page when no stage exists, in output pixels after `--scale`; an over-limit target produces a `capture-limit` failure. `rk check` crops oversized diagnostic PNGs to the limit and completes the report.
- Review caught that an inline SVG inside HTML must not be treated as an SVG-file capture target; the SVG fallback now follows `session.svgInput`, with regression coverage.
- Added exact-boundary and over-boundary samples plus integration coverage for tall stages and wide pages. Updated `AGENTS.md` with first-stage semantics and a per-slide checking loop; updated `SPEC.md` and this file.
- Verified with `npm test` (48 passed), `./bin/rk selftest` (21 sample expectations passed), and `git diff --check`. Both acceptance runs used a temporary venv with NumPy and Pillow because the default Python lacked the optional color-check dependencies.
- Changes remain uncommitted.

## 2026-10-02 — F13 closed

- Grounded: F13 in the motion dogfood report and the existing render-kit contract in `../SPEC.md` → fixed the three observed defects without adding dependencies.
- Added acceptance coverage for heading/question order, tall HTML capture with fixed-height override, and whole-stage value guarding.
- Verified with `npm test` (44 passed) and `./bin/rk selftest` (19 sample expectations passed), using a temporary venv with the optional NumPy and Pillow dependencies. `git diff --check` passed.

## 2026-10-02 — Frontend F2, F4, and F11 closed

- Grounded: frontend findings F2, F4, and F11 in `/Users/GaryT/Documents/Work/lab/design-programme/dogfood/runs-3-5/frontend/report.md` and the linked check evidence → added expected-request matching, visual-check exclusions and horizontal-scroll handling, and labelled multi-input briefs.
- Added regression coverage for exact request URL/status matching, the documented hidden and scrolling patterns, and two labelled states with no PDF.
- Updated the CLI help, `../SPEC.md`, `../AGENTS.md`, and `../FIX-REPORT-dogfood.md`.
- Verified with `npm test` (47 passed) and `./bin/rk selftest` (19 sample expectations passed), using `/tmp/rk-f13-venv/bin` first on `PATH` because the default Python lacks NumPy and Pillow. `git diff --check` passed.
