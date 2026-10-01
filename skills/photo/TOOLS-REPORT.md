# Photo tools build report

## Built

- Deterministic grading CLI with exposure, white balance, levels, curves, saturation, vibrance, HSL bands, 3D `.cube` LUTs, vignette, measurement, and comparison.
- CIE Lab and CIEDE2000 math, 16-bit RGB PNG read/write, output recipe and SHA-256 provenance sidecars.
- Guarded preparation and round-trip verification with explicit resize reporting, a feathered protected region, thresholds, and a render-kit comparison page.
- Synthetic sample builder, colour-math tests, and passing/failing round-trip test cases.

## Acceptance

**Status: PASS — 2026-10-02.** The successful acceptance chain used the verified Python 3.11.5 interpreter by prepending `/Users/GaryT/miniconda3/bin` to `PATH`. An unpinned attempt selected Homebrew Python 3.14 without NumPy and stopped at test discovery; the pinned run below completed all clauses.

Command:

```sh
PATH=/Users/GaryT/miniconda3/bin:$PATH python3 -m unittest discover -s tests && PATH=/Users/GaryT/miniconda3/bin:$PATH python3 scripts/make_samples.py && PATH=/Users/GaryT/miniconda3/bin:$PATH /Users/GaryT/Documents/Work/tools/render-kit/bin/rk check samples/out/compare.html --out-dir /tmp/photo-rk
```

Output:

```text
./Users/GaryT/Documents/Work/tools/skills/photo/tests/test_grade.py:44: DeprecationWarning: 'mode' parameter is deprecated and will be removed in Pillow 13 (2026-10-15)
  Image.fromarray(np.array([[[128, 0], [64, 255]]], dtype=np.uint8), "LA").save(path)
/Users/GaryT/Documents/Work/tools/skills/photo/scripts/png16.py:8: ResourceWarning: unclosed file <_io.BufferedReader name='/var/folders/yy/s3_y_d5x2_34qb0k9f6qvjqr0000gn/T/tmp92krkrpn/gray-alpha.png'>
  data = open(path, "rb").read()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
.....
----------------------------------------------------------------------
Ran 6 tests in 0.425s

OK
{"alignment":{"edited_resized_to_original":false,"edited_size":[192,128],"original_size":[192,128],"preview_method":null,"verification_method":null},"delta_e_2000":{"all":{"count":24576,"max":1.639315430525231,"mean":0.1959225774684017,"p99":1.6361093036859842},"inside_mask":{"count":1487,"max":1.6364147725205682,"mean":1.626618808559728,"p99":1.6357852304603078},"outside_mask":{"count":19861,"max":0.0,"mean":0.0,"p99":0.0}},"out":"/Users/GaryT/Documents/Work/tools/skills/photo/samples/out","roundtrip":{"bbox_delta_e_over_3_xyxy":null,"failure_reason":null,"feather_radius_px":5.0,"limits":{"max":3.0,"mean":1.0,"p99":3.0},"manual_review_required":false,"max_delta_e_2000":0.0,"max_limit":3.0,"max_pixel_xy":[0,0],"mean_delta_e_2000":0.0,"p99_delta_e_2000":0.0,"passed":true,"protected_definition":"feathered mask coverage <= 0.05","protected_pixels":19861,"statistics_passed":true}}
Checking samples/out/compare.html
  resources
  console
  fonts
  overflow
  collision
  contrast
  cvd
  fidelity
  a11y
  value
  pdf-fonts
{"rk_version":"0.1.0","markup_version":1,"input":"/Users/GaryT/Documents/Work/tools/skills/photo/samples/out/compare.html","created":"2026-10-01T21:12:21.069Z","browser":{"name":"chromium","version":"153.0.8010.12","mode":"new-headless"},"viewport":{"width":1920,"height":1080,"scale":1},"at_ms":10000,"outputs":{"png":"/tmp/photo-rk/render.png","pdf":null},"requests_blocked":[],"checks":[{"id":"resources","status":"pass","thresholds":{},"items":[],"reason":null},{"id":"console","status":"pass","thresholds":{},"items":[],"reason":null},{"id":"fonts","status":"pass","thresholds":{},"items":[],"reason":null},{"id":"overflow","status":"pass","thresholds":{"tolerance_px":1},"items":[],"reason":null},{"id":"collision","status":"pass","thresholds":{"min_overlap_px":1},"items":[],"reason":null},{"id":"contrast","status":"pass","thresholds":{"text_exclusion":0.1,"min_background_share":0.3},"items":[],"reason":null},{"id":"cvd","status":"n/a","thresholds":{"min_distance":0.06},"items":[],"reason":"fewer than two declared series"},{"id":"fidelity","status":"n/a","thresholds":{"tolerance_px":0.5},"items":[],"reason":"no chart marks"},{"id":"a11y","status":"pass","thresholds":{},"items":[{"engine":"axe-core","version":"4.13.0"}],"reason":null},{"id":"value","status":"n/a","thresholds":{},"items":[],"reason":"no focal element"},{"id":"pdf-fonts","status":"n/a","thresholds":{},"items":[],"reason":"no PDF produced"}],"summary":{"pass":7,"fail":0,"incomplete":0,"skipped":0,"n_a":4}}
```

An independent code review found an isolated protected-pixel leak that could evade the mean and 99th-percentile gates. Verification now also enforces maximum ΔE 3.0 and the tests include a one-pixel leak case. The review also prompted fixes for grayscale-alpha input, EXIF orientation on 16-bit PNGs, bounded PNG decompression, and sample-output deletion. Resized edits now produce comparison assets and measurements but return exit 1 for manual review, since resampling can hide localized changes.

A second review confirmed the resize/manual-review guard and found no material remaining issues in those findings.

## Open issues

- The neutral-patch and skin-region readings are statistical estimates; the mask is user-supplied and no semantic skin detector is included.
- Pillow output formats other than PNG are 8-bit RGB. PNG outputs retain 16-bit RGB precision.
- The custom high-bit-depth PNG decoder rejects decoded payloads above 512 MiB; the current pipeline uses full-frame float arrays, so unusually large source images need a future tiled implementation.
