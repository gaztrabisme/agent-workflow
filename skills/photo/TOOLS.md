# Photo tools

These scripts provide deterministic grading and a guarded edit round trip. They use Python 3, NumPy and Pillow; there are no other third-party dependencies. For this workspace, the verified interpreter is `/Users/GaryT/miniconda3/bin/python3` (Python 3.11.5, NumPy 2.4.6, Pillow 11.3.0), confirmed by `python3 -c "import numpy, PIL"`. In shells where `python3` resolves elsewhere, prepend `/Users/GaryT/miniconda3/bin` to `PATH` or use the full path. Install the two runtime libraries into that environment with `/Users/GaryT/miniconda3/bin/python3 -m pip install numpy Pillow`.

## Grading

```sh
python3 scripts/grade.py apply input.png recipe.json graded.png
python3 scripts/grade.py measure input.png [--mask subject-mask.png] [--neutral-rect X0 Y0 X1 Y1 | --neutral-mask neutral-mask.png]
python3 scripts/grade.py compare before.png after.png [--mask region.png | --region X0 Y0 X1 Y1 --region-name "left eye"] --out review/
python3 scripts/grade.py deliver delivery.json --out delivered/
```

**Ingesting a camera card on this Mac.** `exiftool`, `magick` and `rawpy` are not installed; use `sips` and Pillow (`/Users/GaryT/miniconda3/bin/python3 -I`) for JPEG EXIF and thumbnails. Skip `._*` files when counting. Select a day by file modification time (`find -newermt D ! -newermt D+1`) and confirm against the EXIF DateTimeOriginal. Do not trust the DCIM folder name for the camera model (a Canon 550D shot into `114_FUJI`). Check EXIF orientation (tag 274) on a few frames. If it is 1 or missing everywhere, the camera did not record rotation; build numbered contact sheets, view them, and write the rotation per frame before making previews. (derived: 2026-10-17 outing card)

**Lifting underexposed frames in a batch.** Do not apply one fixed stop value to the whole set; a +1 stop lift took frames from under 0.1% to 4–7% blown highlights (and one from 2.4% to 11.9%). Per frame: measure with `grade.py measure`, try stops from 1.0 down in 0.2 steps, keep the largest value whose `clipped_highlights_pct` stays within about 1% above the original, and leave the frame as shot if even 0.2 stops fails. Report the per-frame values and any frame left unlifted. (derived: 2026-10-17 outing batch)

All commands print one JSON object to stdout. Failures print JSON to stderr and return 2. `apply` takes an ordered JSON array, or an object with an `operations` array. It refuses to replace an existing output or provenance file, including the input. Beside the output it writes `<output>.recipe.json` and `<output>.input.sha256`. Recipe LUT paths are resolved from the recipe file's directory. PNG output is RGB 16-bit; other Pillow-supported output formats are RGB 8-bit. The processing pipeline uses float64 values and clips only after the recipe, so intermediate operations do not wrap or quantize integer pixels. The custom 16-bit PNG decoder rejects decompressed image data over 512 MiB.

Each operation is an object with `type`:

| Type | Fields and behavior |
|---|---|
| `exposure` | `stops` (default 0); multiplies linear-light RGB by 2 to that power. |
| `white_balance` | `gains: [r,g,b]` positive linear-light multipliers (for a neutral measured by another tool; normalized like the other modes), or `temperature` in Kelvin (default 6500; valid 1000–40000), legacy `neutral: [x,y]` normalized coordinates, or `neutral_rect: [x0,y0,x1,y1]` pixel bounds whose channel means are averaged. Lower Kelvin cools and higher Kelvin warms in this tool's approximation. Temperature and neutral correction run in linear light; gains are normalized so an equal-channel neutral keeps its Rec.709 luminance. Optional signed `tint` (default 0) adjusts green gain. (derived: dogfood 2026-10-02, F7) |
| `levels` | `black` (0), `white` (1), `gamma` (1); normalizes the input range, clips to 0–1, then raises to `1/gamma`. |
| `tone_curve` | `points`: at least two increasing `[input, output]` pairs, usually in 0–1; linear interpolation. |
| `saturation` | `factor` (1); scales chroma around Rec.709 luma. |
| `vibrance` | `amount` (0, valid -1..1); selectively adjusts lower-chroma pixels. |
| `hsl` | `bands`: objects with `hue` center in degrees, optional `range` (30 degrees), `hue_shift` in degrees, and additive `saturation` / `lightness` adjustments in 0–1 units. |
| `lut` | `file`: a `.cube` 3D LUT with `LUT_3D_SIZE` and optional `DOMAIN_MIN` / `DOMAIN_MAX`. 1D LUT sections are rejected. |
| `vignette` | `strength` (0.25), `radius` (0.72), and normalized `center` ([0.5,0.5]); darkens a quadratic edge falloff. |

`measure` reports 16-bin encoded RGB histograms, channel means/spreads, and the percentages of pixels with any encoded channel at or below 1% / at or above 99%. These clipping readings describe the saved encoded values; changing the recipe's output endpoints can lower them without restoring detail that was already clipped. `apply` flags tone-curve or levels endpoints that lift black or lower white; `compare` reports those warnings when the edited image has a recipe sidecar and reports null when the recipe is unavailable. (derived: dogfood 2026-10-02, F5)

Cast measurement uses every pixel in a supplied neutral rectangle or neutral mask, and reports its count and share of the full image. Without one, the tool falls back to Lab chroma below 12 and 15 < L* < 98, reports the selected share, and warns when that selection is very small or covers most of the frame. Positive a* points toward red/magenta and negative a* toward green; positive b* points toward yellow and negative b* toward blue. (derived: dogfood 2026-10-02, F2) With `--mask`, the tool also reports the masked region's L*, C*, encoded clipping shares, 16-bin L* histogram, and circular hue statistics. The mask is grayscale, must match the input dimensions, and selects values at least 50%. These readings are estimates, not semantic segmentation. (derived: dogfood 2026-10-02, F6)

`compare` aligns the second image to the first with bicubic resizing when dimensions differ and reports that in JSON. It writes `side-by-side.png`, a 4× amplified absolute RGB `difference.png`, a `close-up.png` made from an unscaled crop around the hard-mask bounding box, a named region rectangle, or a centre crop (when neither was supplied), and `compare.html`. The page uses a neutral mid-grey surround, names the two files in its title and labels, and collapses measurement JSON in `<details>`. Close-up pixels render at their natural dimensions inside a horizontal scroll area. (derived: dogfood 2026-10-02, F4) Hard-mask metrics use the consistent JSON key `mask` (values ≥0.5); the round-trip core uses `mask_core` for its feather-defined interior. (derived: dogfood 2026-10-02, F9)

`deliver` reads a JSON spec with an `items` array. Each item names `input` (relative to the spec or absolute), a simple output `file`, optional `crop: [x0,y0,x1,y1]`, optional `size: [width,height]`, `format` (`JPEG`, `PNG`, `WEBP`, or `TIFF`), and lossy `quality` (1–100) for JPEG/WEBP. It applies Lanczos resizing and embeds an sRGB ICC profile. If an input has an ICC profile it is converted to sRGB first; an untagged input is treated as sRGB, matching the grade pipeline. Resizing that enlarges either dimension fails unless that item explicitly sets `allow_upscale: true`. It refuses output collisions and writes `manifest.json`; the manifest reports the code checks for output count, dimensions, format, and sRGB profile. The exact workflow and presets are in [deliver-and-review.md](references/method/deliver-and-review.md). (derived: dogfood 2026-10-02, F3)

## Guarded edit round trip

```sh
python3 scripts/roundtrip.py prepare original.png --mask edit-mask.png \
  --brief "Soften the small blemish on the left cheek." --out work/edit/
python3 scripts/roundtrip.py merge original.png work/edit/edited-crop.png \
  --mask edit-mask.png --out work/merged.png
python3 scripts/roundtrip.py verify original.png edited.png \
  --mask edit-mask.png --out work/review/
```

`prepare` copies the original byte-for-byte, copies the mask, writes an 8-pixel-padded crop of the masked region, and writes an edit brief that records the permitted change and protected content. It will not replace an existing copied original. Keep edits as separate files; never overwrite originals.

`merge` requires an edited crop with the exact dimensions of that prepared 8-pixel-padded region. It alpha-composites through the supplied grayscale mask into a new full-frame output, refuses collisions, and reports the mask bounds. (derived: dogfood 2026-10-02, F9)

`verify` resizes the edited image to original dimensions with nearest-neighbour sampling for verification and bicubic interpolation for its compare preview when sizes differ; it records both dimensions and methods. It Gaussian-feathers the mask at radius 5 pixels. The protected region is feathered coverage ≤0.05; defaults are mean ΔE00 ≤1, p99 ≤3, and max ≤3. The separate outside-mask transition band is hard-mask coverage <0.5 with feathered coverage >0.05; defaults are mean ≤1, p99 ≤2, and max ≤3. The CLI allows these band limits to be set with `--band-mean-limit`, `--band-p99-limit`, and `--band-max-limit`. **All limits are tool choices**, not a published photographic or perceptual standard. The verifier reports both regions' distributions and the over-limit bounding boxes. No outside-mask pixel is omitted: unchecked outside-mask width is 0 px. Pixels inside the hard mask are the permitted edit area. (derived: dogfood 2026-10-02, F1)

When resizing was required, statistics are still reported and the compare page is written, but verification returns exit 1 with `manual_review_required` because resampling can hide localized changes. Any region threshold failure also returns exit 1. JSON reports `mask_core`, `transition_band`, and protected/outside-mask statistics, maximum-pixel coordinates and generated `compare.html`, `side-by-side.png`, `difference.png`, `close-up.png`, and `verify.json`. A pass reports measured differences within these tolerances; it does not establish exact pixel identity or prove the requested edit looks good.

Inspect edited results at full-frame size and at 100% around changed areas. Use the compare page for digital evidence, then review visual quality and identity details separately.

## Samples and render check

```sh
python3 scripts/make_samples.py
~/.agent-workflow/tools/render-kit/bin/rk check samples/out/compare.html --out-dir /tmp/photo-rk
```

`make_samples.py` builds a portrait-like image with a skin region and gray card, a landscape-like image, an ordered recipe, an edit mask, and good / leaking simulated edits. It runs the good edit through `verify` into `samples/out/`. It preserves existing files and refuses to replace generated review outputs; remove only the generated review files before rerunning. Generated source fixtures are kept in `samples/`; runtime review files in `samples/out/` are ignored by Git. 8-bit alpha is ignored when reading RGB; 16-bit RGB, RGBA, grayscale, and grayscale-alpha PNG are supported. EXIF orientation is applied to high-bit-depth PNGs too.

## Tools built in use

Built during the 2026-10-17 outing batch. These two need OpenCV as well as NumPy and Pillow (`/Users/GaryT/miniconda3/bin/python3` has it).

```sh
python3 scripts/straighten.py estimate IMG [IMG ...]        # JSON lines with rotate_by
python3 scripts/straighten.py apply IN OUT --angle DEG       # positive = counter-clockwise
python3 scripts/straighten.py selftest IMG [IMG ...]         # rotate by known angles, check the estimate follows
python3 scripts/colour_lock.py SOURCE EDITED OUT             # JSON with the a*/b* shift per lightness band
```

- `straighten.py` estimates roll from upright edges (walls, doors, screens) with OpenCV's line-segment detector, modelling lean as roll plus a keystone term. It rotates only between 0.5° and 5°, and not above 3° when the upright edges total under 2 units of length. Self-test on frames with straight uprights (16 known rotations): mean error 0.2°, max 0.46°. On a frame with only short edges (IMG_6787) the raw fit reported itself confident at 8–10° error; the 3° rule is what stops that one, so check `rotate_by`, not `confident`. Automatic tilt from gradient histograms on thumbnails was unreliable (4–5° on level photos).
- `colour_lock.py` shifts an AI edit's mean a*/b* back to its source in five lightness bands, keeping the edit's lightness.
- White balance from objects picked by eye: propose numbered bright, low-chroma regions outside faces and pick the white ones by eye, then pass `{"type":"white_balance","gains":[r,g,b]}`. A single object is unreliable on the yellow-blue axis, so correct green-magenta from one reference and yellow-blue only where two references agree within 2 b* units. The candidate tool (`white_candidates.py`) is tied to that project's folder layout and stays in `~/Pictures/2026-10-16-company-outing/tools/`.
- Putting real faces back over an AI edit: where the blurred structural similarity (SSIM) of a face against the source falls below 0.93, replace it with the source face, denoised and matched in lightness on the face centre, blended in an ellipse just inside the face box. This removed the halos an earlier, wider blend left. The tool (`face_guard.py`) is tied to that project's layout and stays in the same folder.
