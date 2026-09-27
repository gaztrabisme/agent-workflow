# Temperature and saturation: the two neglected contrasts

Reader: an agent using warm against cold, and saturated against desaturated, to place attention and build depth. Sources: [L16](../course/U04-L16-color-theory-finally-ii.md), [L17](../course/U04-L17-the-secret-ingredients-temperature-and-saturation.md), [L18](../course/U04-L18-bonus-solving-common-color-problems.md).

## Temperature

- **What it is.** The course splits the wheel into a warm half (reds, oranges, yellows) and a cold half (violets, blues, cyans). It calls this split "purely a human projection", not a physical property. (1140 · U4 · L17 · 01:30–02:37)
- **Why it is useful.** It is one of the most general contrasts. A whole family of cold colors against a whole family of warm ones works as a **super contrast**. After that, the normal harmony rules apply. (1140 · U4 · L17 · 02:37–04:32)
- **Keeping harmony inside the contrast.** In a teal forest with red caps, the reds are kept on the cooler side, away from orange, so the contrast works without being blunt. (1140 · U4 · L17 · 02:37–04:32)
- **Thinking in groups instead of complements.** Warm, cold and warm planes can replace working out "which color is complementary to which". (1140 · U4 · L17 · 05:51–07:09)
- **Lighting can establish the temperature groups.** In a stylized night scene, course 1560 uses a cool blue ambient field, warmer practical lights and a secondary rim light. Treat this as one scene recipe, not a universal rule for night. (1560 · U3 · L11 · 01:44–02:55, 1560 · U3 · L11 · 03:39–04:58)

### Classic temperature compositions

| Composition | Example | Source |
|---|---|---|
| Warm image, cold focal point | A monster's blue-violet mouth in warm sandstone. Shifting the blue to warm removes most of the focal pull. | 1140 · U4 · L17 · 04:32–05:51 |
| Cold image, warm protagonist | Said, not analysed; the slide shows a dark blue landscape with one peach accent (frame) | 1140 · U4 · L17 · 07:09–08:00 |
| Warm, cold, warm planes for depth | The Croods: warm foreground, cold middle ground, warm background. It works like black, grey and light grey. | 1140 · U4 · L17 · 05:51–07:09 |

- **Temperature is relative.**
  - The eye invents the missing temperature: a grey inside a red field looks blue-violet. (1140 · U4 · L17 · 08:00–09:13)
  - The same teal changes temperature with its surroundings. (1140 · U4 · L17 · 09:13–10:19)
  - Place the color, then adjust it in context.
- **Pushing temperature further on a finished image.** Mask everything outside the light and the focal point, then either:
  - lower Red in a Levels layer, or
  - use Hue/Saturation with Colorize toward a desaturated cool tone.

  (1140 · U4 · L17 · 14:44–16:57)

## Saturation

**Saturation** means how pure or intense a color is. Its opposite is grey. (1140 · U4 · L17 · 10:19–12:11)

### Compositions

| Composition | Effect | Source |
|---|---|---|
| Saturated context, desaturated protagonist | Attention through the opposite of the usual | 1140 · U4 · L17 · 10:19–12:11 |
| Desaturated context, saturated protagonist | The classic; the Peleng, Zbukvic and Misowski family works this way | 1140 · U4 · L17 · 13:10–14:44, 1140 · U1 · L02 · 08:14–09:44 |
| Saturated periphery, desaturating toward the antagonist | A fox in bright flowers; the threat sits in dull greens | 1140 · U4 · L17 · 12:11–13:10 |
| High saturation at the edges, dropping at the center | The terrifying version of the course poster | 1140 · U4 · L16 · 05:37–07:21 |

### Principles

- **Desaturation creates apparent temperature.**
  - A desaturated warm green inside saturated warm colors reads as cold. (1140 · U4 · L17 · 12:11–13:10)
  - A desaturated green next to saturated ochres reads as ochre. So it can repeat the dominant family without being that hue. (1140 · U4 · L17 · 10:19–12:11)
- **Colorful is an arrangement, not a level.** Images remembered as "super saturated" are often only moderately saturated. Saturation sits in key places against large desaturated areas. (1140 · U4 · L17 · 13:10–14:44)
- **Saturation should rise toward the protagonist.**
  - Check it in Photoshop's color picker in S mode, or measure OKLCH chroma with `scripts/checks.py chroma`. HSB S reads dark colors as saturated, so on night scenes use chroma. See [measurement.md](measurement.md).
  - A saturated shape at the edge is fine if it frames the image and does not touch the focal color.

  (1140 · U4 · L16 · 01:56–04:24)

## Failures

**Problem 2: contrast in the wrong place.**
- **The failure:** desaturating the focal area merges it with its neighbours, while new saturation and color contrast appear in the periphery. The eye goes where the layout did not intend. (1140 · U4 · L18 · 01:47–03:19)
- **The fix:** put color, saturation and temperature contrast where the value plan already sends the eye.

**Problem 5: saturation out of control.**
- **The failure:** everything saturated looks garish and creates unwanted contrasts, for example between sky and clouds. Saturated colors also separate from each other, while desaturation brings colors together. (1140 · U4 · L18 · 08:56–10:26)
- **The fix, in order:**
  1. desaturate the secondary areas;
  2. return the sky to "more human" saturation;
  3. saturate the focal point;
  4. only then raise the overall saturation, if the image looks grey.

**The final-pass version of the fix** (1140 · U3 · L13 · 13:17–16:28):
1. Raise saturation globally.
2. Remove it from the shadows, foreground and background, so the image keeps variation.
3. Darken slightly.
4. Pull back any color pushed too far.

"There is nothing worse than an image that feels very saturated; it feels visually aggressive."

Practice the teacher sets: make three versions of the PSD that move the focus using, in turn, value contrast, saturation contrast and color contrast. Ask people what they see first. See [U04-unit.md](../course/U04-unit.md).
