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
