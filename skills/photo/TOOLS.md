# Photo tools

These scripts provide deterministic grading and a guarded edit round trip. They use Python 3, NumPy and Pillow; there are no other third-party dependencies. For this workspace, the verified interpreter is `/Users/GaryT/miniconda3/bin/python3` (Python 3.11.5, NumPy 2.4.6, Pillow 11.3.0), confirmed by `python3 -c "import numpy, PIL"`. In shells where `python3` resolves elsewhere, prepend `/Users/GaryT/miniconda3/bin` to `PATH` or use the full path. Install the two runtime libraries into that environment with `/Users/GaryT/miniconda3/bin/python3 -m pip install numpy Pillow`.

## Grading

```sh
python3 scripts/grade.py apply input.png recipe.json graded.png
python3 scripts/grade.py measure input.png [--mask skin-mask.png]
python3 scripts/grade.py compare before.png after.png [--mask region.png] --out review/
```

All commands print one JSON object to stdout. Failures print JSON to stderr and return 2. `apply` takes an ordered JSON array, or an object with an `operations` array. It refuses to replace an existing output or provenance file, including the input. Beside the output it writes `<output>.recipe.json` and `<output>.input.sha256`. Recipe LUT paths are resolved from the recipe file's directory. PNG output is RGB 16-bit; other Pillow-supported output formats are RGB 8-bit. The processing pipeline uses float64 values and clips only after the recipe, so intermediate operations do not wrap or quantize integer pixels. The custom 16-bit PNG decoder rejects decompressed image data over 512 MiB.

Each operation is an object with `type`:

| Type | Fields and behavior |
|---|---|
| `exposure` | `stops` (default 0); multiplies linear-light RGB by 2 to that power. |
| `white_balance` | Either `temperature` in Kelvin (default 6500; valid 1000–40000) or `neutral: [x,y]` at normalized image coordinates; optional signed `tint` (default 0) adjusts green gain. Temperature uses a deterministic RGB approximation; tint is a simple green-channel control. |
| `levels` | `black` (0), `white` (1), `gamma` (1); normalizes the input range, clips to 0–1, then raises to `1/gamma`. |
| `tone_curve` | `points`: at least two increasing `[input, output]` pairs, usually in 0–1; linear interpolation. |
| `saturation` | `factor` (1); scales chroma around Rec.709 luma. |
| `vibrance` | `amount` (0, valid -1..1); selectively adjusts lower-chroma pixels. |
| `hsl` | `bands`: objects with `hue` center in degrees, optional `range` (30 degrees), `hue_shift` in degrees, and additive `saturation` / `lightness` adjustments in 0–1 units. |
| `lut` | `file`: a `.cube` 3D LUT with `LUT_3D_SIZE` and optional `DOMAIN_MIN` / `DOMAIN_MAX`. 1D LUT sections are rejected. |
| `vignette` | `strength` (0.25), `radius` (0.72), and normalized `center` ([0.5,0.5]); darkens a quadratic edge falloff. |

`measure` reports 16-bin encoded RGB histograms, channel means/spreads, percentages of pixels with any channel at or below 1% / at or above 99%, a heuristic neutral patch (Lab chroma below 12 and 15 < L* < 98), its mean/spread in a* and b*, and its cast vector. Positive a* points toward red/magenta and negative a* toward green; positive b* points toward yellow and negative b* toward blue. If a mask is supplied, it also reports the circular hue angle/spread of Lab a*b* vectors in masked pixels. The mask is a grayscale image matching the input; values at least 50% are selected. These neutral and skin measurements are estimates, not semantic segmentation.

`compare` aligns the second image to the first with bicubic resizing when dimensions differ and reports that in JSON. It writes `side-by-side.png`, a 4× amplified absolute RGB `difference.png`, and `compare.html`. Masked and unmasked CIEDE2000 distributions include count, mean, maximum and 99th percentile. Its output directory must not already contain those generated filenames; the page marks the visual area with `data-rk-stage="comparison"` for render-kit.

## Guarded edit round trip

```sh
python3 scripts/roundtrip.py prepare original.png --mask edit-mask.png \
  --brief "Soften the small blemish on the left cheek." --out work/edit/
python3 scripts/roundtrip.py verify original.png edited.png \
  --mask edit-mask.png --out work/review/
```

`prepare` copies the original byte-for-byte, copies the mask, writes an 8-pixel-padded crop of the masked region, and writes an edit brief that records the permitted change and protected content. It will not replace an existing copied original. Keep edits as separate files; never overwrite originals.

`verify` resizes the edited image to original dimensions with nearest-neighbour sampling for verification and bicubic interpolation for its compare preview when sizes differ; it records both dimensions and methods. It Gaussian-feathers the mask at radius 5 pixels and measures protected pixels where the feathered mask coverage is at most 0.05. Its chosen distribution defaults are mean CIEDE2000 ≤ 1.0 and 99th percentile ≤ 3.0 in that protected region. **These thresholds are the tool's chosen defaults**, not a published photographic or perceptual standard. It also rejects any single protected pixel above ΔE 3.0 so a severe isolated leak cannot hide below the percentile. All three checks must pass for same-size inputs. When resizing was required, statistics are still reported and the compare page is written, but verification returns exit 1 with `manual_review_required` because resampling can hide localized changes. A threshold failure also returns exit 1. JSON reports protected-region statistics, maximum-pixel coordinates, the bounding box of protected pixels above ΔE 3, and the generated `compare.html`, `side-by-side.png`, `difference.png`, and `verify.json`. Verification refuses to replace existing output files. A pass reports measured differences within these tolerances; it does not establish exact pixel identity or prove the requested edit looks good.

Inspect edited results at full-frame size and at 100% around changed areas. Use the compare page for digital evidence, then review visual quality and identity details separately.

## Samples and render check

```sh
python3 scripts/make_samples.py
/Users/GaryT/Documents/Work/tools/render-kit/bin/rk check samples/out/compare.html --out-dir /tmp/photo-rk
```

`make_samples.py` builds a portrait-like image with a skin region and gray card, a landscape-like image, an ordered recipe, an edit mask, and good / leaking simulated edits. It runs the good edit through `verify` into `samples/out/`. It preserves existing files and refuses to replace generated review outputs; remove only the generated review files before rerunning. Generated source fixtures are kept in `samples/`; runtime review files in `samples/out/` are ignored by Git. 8-bit alpha is ignored when reading RGB; 16-bit RGB, RGBA, grayscale, and grayscale-alpha PNG are supported. EXIF orientation is applied to high-bit-depth PNGs too.
