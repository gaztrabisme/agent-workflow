# Measurement: numbers behind the checks

Reader: an agent running the review tests on an image file, or computing contrast and ramps, without Photoshop. Everything here is derived. The course measures with Photoshop and by eye, and these are the equivalents this skill uses. The script is `scripts/checks.py` (Python 3, numpy, Pillow).

## Semantic-differential checks (T10–T12)

Course 5642 uses seven positions between two bipolar adjectives, groups candidate pairs under aesthetic, indicative-instrumental and symbolic-social dimensions, and averages audience profiles. The worked example uses 24 pairs. This skill’s adaptation lets a brief select relevant pairs (derived: the course says adjective choices should depend on the piece, communication intentions and audience, and demonstrates a 24-pair profile: 5642 · U3 · L43 · 03:44–04:34; 5642 · U3 · L43 · 10:21–11:57). (5642 · U3 · L43 · 02:41–03:16, 5642 · U3 · L43 · 03:44–04:34, 5642 · U3 · L43 · 10:21–11:57)

Record the left pole as 1, the midpoint as 4 and the right pole as 7. For pair j, with n respondents and rating rᵢⱼ:

- **Mean profile:** μⱼ = (Σ rᵢⱼ) / n.
- **Audience spread:** sⱼ = √[Σ(rᵢⱼ − μⱼ)² / (n − 1)], for n ≥ 2.
- **Variant shift:** Δⱼ = μ(B, j) − μ(A, j).

These are this skill's derived measurements of the plotted rating profiles. They are not thresholds supplied by the course. (derived from 5642 · U3 · L43 · 10:21–11:57)

| Test | Pass condition | Set before ratings |
|---|---|---|
| T10 — semantic target fit | Every critical pair's mean μⱼ is inside its target interval [aⱼ, bⱼ] on the 1–7 scale. | The relevant pairs, left/right direction and target intervals. |
| T11 — audience agreement | The respondent count meets nₘᵢₙ, and each critical pair's sⱼ is at or below its maximum sₘₐₓ,ⱼ. If spread exceeds the limit, mark inconclusive and investigate the different readings before acceptance. | nₘᵢₙ and sₘₐₓ,ⱼ, chosen for the project; the course defines neither. |
| T12 — variant distinction | For each named difference, Δⱼ has the intended sign and magnitude at least δⱼ. | Which profile should move toward which pole and the minimum meaningful δⱼ. |

The method is a way to summarize this audience's perceptions in this context; a mean is not a universal meaning for that color. (5642 · U3 · L43 · 00:26–01:52, 5642 · U3 · L43 · 11:57–12:55)

## Which quantity stands in for which course term

| Course term | Measure it as | Why |
|---|---|---|
| Value | OKLab L (0 = black, 1 = white) | Perceptual lightness. HSL L and HSB B misrank saturated colors: yellow and blue have the same HSL L but look very different in lightness. |
| Saturation | OKLCH C (chroma: distance from the grey of the same lightness) | Photoshop's HSB S reads dark colors as highly saturated. A dark navy sky can score S 0.5 while a glowing bulb scores 0.28, which inverts the saturation map on night scenes. |
| Hue, and warm or cool | OKLCH h, in degrees | Bands used by T7: warm 20–100, cool 200–320. The rest is the green or purple boundary, which can read either way in context. |
| Photoshop Hue/Saturation ranges | Red, yellow and green each show a 30° core plus a 30° falloff on each side, centered on 0°, 60° and 120°, respectively | Read from the course frames at 1140 · U4 · L18 · 05:09–07:27. |

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
