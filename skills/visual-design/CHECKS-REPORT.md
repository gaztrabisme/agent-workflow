# Measurement script report

**Verdict: PASS.** Built `scripts/checks.py` with `grid`, `balance`, `space`, `scale` and `focal` JSON results; split the pure calculations into one-measure modules; and added `scripts/measure_boxes.mjs`, which uses render-kit's prepared Chromium page for stage-relative boxes and rendered type sizes. The helper and checker use the same rendered PNG dimensions, and the checker rejects mismatched box metadata.

Added five passing SVG samples and five isolated failing samples under `samples/`. `tests/test_checks.py` covers each pure measure and runs `bin/rk check`, the box helper and all five composition checks for every sample. The bad samples each fail only their named visual-design measure.

## Test run

Ran the acceptance command from this folder with render-kit's colour dependency configured:

```text
RK_COLOR_THEORY=/Users/GaryT/Documents/Work/tools/skills/color-theory python3 -m unittest discover -s tests
```

Last lines:

```text
Ran 15 tests in 42.393s

OK
```

## Measurement definition change

T6 now defines occupied area as the union of explicitly marked visible element bounding boxes (`data-vd-occupies`) and estimates negative space as the remaining stage area. This makes the measure deterministic from the boxes render-kit can expose through the documented helper. Pixel-only vacancy has no stable definition for arbitrary transparent, textured or photographic backgrounds. The estimate can overcount transparent and irregular elements; `measurement.md` documents that limitation and still requires vision review of the spaces' function.

## Open issues

- T6 depends on authors marking all content that should count as occupied. Its result is a box-based estimate, not a pixel segmentation.
- T5 reports `not_judged` unless the stage declares centered or asymmetric intent; asymmetric balance still needs a fresh visual reviewer.
- The box helper imports render-kit's internal TypeScript `prepare` modules and therefore requires Node 24 and the local render-kit source directory. It accepts render options that affect viewport, scale, page time and preparation; rerun it with the same options used by `rk check`.
