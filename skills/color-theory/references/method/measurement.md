# Measurement: numbers behind the checks

Reader: an agent running the review tests on an image file, or computing contrast and ramps, without Photoshop. Everything here is derived. The course measures with Photoshop and by eye, and these are the equivalents this skill uses. The script is `scripts/checks.py` (Python 3, numpy, Pillow).

## Which quantity stands in for which course term

| Course term | Measure it as | Why |
|---|---|---|
| Value | OKLab L (0 = black, 1 = white) | Perceptual lightness. HSL L and HSB B misrank saturated colors: yellow and blue have the same HSL L but look very different in lightness. |
| Saturation | OKLCH C (chroma: distance from the grey of the same lightness) | Photoshop's HSB S reads dark colors as highly saturated. A dark navy sky can score S 0.5 while a glowing bulb scores 0.28, which inverts the saturation map on night scenes. |
| Hue, and warm or cool | OKLCH h, in degrees | Bands used by T7: warm 20–100, cool 200–320. The rest is the green or purple boundary, which can read either way in context. |
| Photoshop Hue/Saturation ranges | HSB hue, 30° core plus a 30° falloff each side, centred on Reds 0, Yellows 60, Greens 120, Cyans 180, Blues 240, Magentas 300 | Read from the dialog in the course frames at 1140 · U4 · L18 · 05:09–07:27. |

## Formulas

**sRGB to linear** (per channel c in 0–1): c / 12.92 if c ≤ 0.04045, else ((c + 0.055) / 1.055)^2.4.

**Linear sRGB to OKLab** (Björn Ottosson):
1. lms = M1 · rgb, where M1 = [[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]].
2. Take the cube root of each component.
3. Lab = M2 · lms′, where M2 = [[0.2104542553, 0.7936177850, −0.0040720468], [1.9779984951, −2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, −0.8086757660]].

Then C = √(a² + b²) and h = atan2(b, a).

**WCAG 2 contrast:**
1. Relative luminance Y = 0.2126 R + 0.7152 G + 0.0722 B, computed on the **linear** channels above.
2. Ratio = (Y_light + 0.05) / (Y_dark + 0.05).
3. AA needs 4.5:1 for body text and 3:1 for large text. AAA needs 7:1.

**Warning:** do not reuse the pure 2.4-gamma linearization from the APCA reference ([apca-myndex-contrast.md](../color-science/references/techniques/apca-myndex-contrast.md)) for WCAG 2. On a warm ramp it overstates the WCAG ratio by 10–16%, which can pass a color that fails AA. APCA and WCAG 2 are different models; report which one you used.

Sanity values: #767676 on white is 4.54:1. #AA581E on white is 5.09:1.

## Default thresholds in `checks.py`

These are this skill's working defaults, not the teacher's numbers:

| Test | Default | Override when |
|---|---|---|
| T1 | The focal box holds at least 2× its area share of value-edge energy (gradient of OKLab L) | The focal element is large or has deliberately low contrast; judge by eye instead |
| T5 | The focal box's mean C is at least that of every ring outside it | The image uses an inverted saturation layout on purpose, as in the terrifying recipe (1140 · U4 · L16 · 05:37–07:21) |
| T6 | Fails if one range moves more than 80% of the image and no other range moves 5% | A restrained or pastel palette is the intent; the teacher allows it (1140 · U4 · L18 · 05:09–07:27) |

For ramps and design tokens, use the ramp guidance in [color-science SKILL.md](../color-science/SKILL.md): flat perceptual steps in OKLCH, and every text pair verified. Check the numbers with `checks.py contrast`.
