# Legibility — the model, the thresholds, and why the condition comes first

A font size in pixels is not a legibility claim. The same 16px is comfortable on a
printed A3 held at 50 cm and below the limit of what the eye can resolve in a
phone-sized social post. So this skill does not ask "is the type big enough"; it asks
"big enough **at what viewing condition**", and refuses to answer until told.

Instrument: `scripts/legibility.mjs`. Run it with no condition to list the named ones.

---

## The model

Legibility is governed by the angle a glyph subtends at the eye. A glyph of height *h*
viewed at distance *D* subtends, by the small-angle approximation:

> α = (h / D) radians = (h / D) × 3437.75 arcminutes

A design file has no physical size, so split that into a term the layout controls and a
term the reader controls:

> **α (arcmin) = (h_px / W_px) × (W_mm / D_mm) × 3437.75**
>
> where `h_px` is the glyph height in the design, `W_px` the canvas width,
> `W_mm` the physical width the sheet is shown at, and `D_mm` the viewing distance.

The second factor, **k = W_mm / D_mm**, is the whole of the viewing condition. Larger k
is easier to read. Everything the instrument reports is one of these two terms, so a size
can be judged against a named condition instead of by feel.

## The thresholds

Vision science measures **x-height**, not point size, because x-height predicts reading
performance and point size is not even comparable between typefaces.

**Mixed case — judged on x-height.** Legge, G. E. & Bigelow, C. A. (2011). "Does print
size matter for reading? A review of findings from vision science and typography."
*Journal of Vision* 11(5):8, 1–22. doi:10.1167/11.5.8

| Threshold | x-height | What it means |
|---|---|---|
| Acuity limit | **4.8′** | Smaller than this and the text cannot be read at all |
| Critical print size | **12′** | The smallest size that still supports *maximum* reading speed. Below it, reading slows. **This is the floor.** |
| Comfortable | **18′** | Where real-world typography mostly sits (18–24′) |

**ALL CAPS — judged on cap height.** ISO 9241-303:2011 and ANSI/HFES 100-2007.

| Threshold | Cap height |
|---|---|
| Minimum | **16′** |
| Preferred | **20–22′** |

**Contrast.** WCAG 2.2 SC 1.4.3: 4.5:1 below 24px (18.66px bold), 3:1 above. Separately,
Legge et al. (1987) found contrast below roughly 10% Weber raises the critical print size
— so low contrast makes text need to be *bigger*, not merely harder to like.

## Two measurement traps, both real

**`actualBoundingBoxAscent` rounds to integer device pixels.** Measuring a 12px font
directly returns 6 where the truth is 5.64 — an 8% error on exactly the quantity being
judged against a 12′ bar. The instrument therefore measures the x/em and cap/em ratios
once at 1000px and scales them to the real size. On one sheet this alone moved the body
reading from 9.9′ to 9.3′.

**SVG text is scaled by its own viewBox.** A label declared at 11px inside a 322-unit
viewBox shown 216px wide paints at 7.38px. CSS says 11px and every CSS-based checker
agrees. The instrument measures through `getScreenCTM()` and reports the size actually
painted; `scripts/check.mjs` fails the build if any SVG renders below its declared size.

## The named conditions

| id | sheet | distance | k | What it is |
|---|---|---|---|---|
| `phone-fit` | 71 mm | 350 mm | 0.203 | Phone, fit to width, 6.1″ at 35 cm |
| `laptop-fit` | 234 mm | 600 mm | 0.390 | PDF fit-to-window, 15.6″ laptop at 60 cm |
| `projected` | 2400 mm | 4000 mm | 0.600 | Projected on a 2.4 m screen, viewer at 4 m |
| `monitor-fit` | 429 mm | 700 mm | 0.613 | PDF fit-to-window, 27″ at 70 cm |
| `a4-print` | 297 mm | 400 mm | 0.743 | Printed A4 landscape, read at 40 cm |
| `monitor-100` | 485 mm | 600 mm | 0.808 | PDF at 100%, 24″ at 60 cm (it scrolls) |
| `a3-print` | 420 mm | 500 mm | 0.840 | Printed A3 landscape, read at 50 cm |

Anything not listed: `--sheet-mm N --distance-mm N`.

Note how close `a3-print` (0.840) and `monitor-100` (0.808) are — within 4%. A sheet
built for A3 is also right for a PDF opened at 100%. And note how far `laptop-fit`
(0.390) is from both: **fit-to-window on a laptop is less than half the viewing ratio of
a poster**, which is why a sheet that measures perfectly can still be unreadable when the
recipient opens it in a mail client.

## Turning a threshold into a type size

Rearranged, the floor for a given condition and canvas is:

> h_px = α × W_px / (k × 3437.75)

Worked, for a 1754px-wide canvas at `a3-print` (k = 0.840):

- x-height floor = 12 × 1754 / (0.840 × 3437.75) = **7.29 px**
- cap-height floor = 16 × 1754 / (0.840 × 3437.75) = **9.72 px**

Then divide by the typeface's own ratios. BR Omega has x/em = 0.470 and cap/em = 0.700:

- mixed case: 7.29 / 0.470 = 15.5 px → **16 px**
- all caps: 9.72 / 0.700 = 13.9 px → **14.5 px**

Those two numbers are the type scale's floor, and everything else is built up from them.
An x-height of 0.470 em is small for a grotesque, which is why BR Omega needs a larger
nominal size than the same measurement would demand of many other faces.

## When the page does not fit

Pay in **leading and chrome, never in glyph size**. On the founding engagement the first
build at the corrected type scale ran 125px past the canvas and was brought back inside
by trimming line-height (1.42 → 1.29 on body), callout discs (34 → 28px), zone rhythm
(12 → 6px) and footer slots (52 → 40px). Not one glyph got smaller. Body leading of 1.29
at 16px is at the tight end of normal and is the first thing to give back if the sheet
ever gets more room.

If it still does not fit, the sheet has too much on it. Cut content, or split the page.

## The honest limit

A sheet built to clear 12′ on A3 will **not** clear it opened fit-to-window on a laptop.
Measured on the worked example, which passes every gate at A3:

| | `a3-print` (k 0.840) | `laptop-fit` (k 0.390) |
|---|---|---|
| At or above the 12′ critical print size | **100%** | **1%** |
| Reading slowed (between 4.8′ and 12′) | 0% | 77% |
| Below the 4.8′ acuity limit — cannot be read | 0% | 23% |
| Smallest text | 12.3′ | 5.7′ |

Closing that gap needs about 3.9× the type, which is roughly fifteen times the area.
That is not a tuning problem, it is a different artefact.

So say how it should be read when you send it — "print A3, or view at 100%" — or split
the content across three pages. Do not quietly accept that most recipients will see it at
a third of the size it was measured for.
