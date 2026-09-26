# Photoshop techniques used in the course

Reader: an agent giving step-by-step instructions to someone working in Photoshop, or translating these steps to another editor. Every step is the teacher's own. The last section gives equivalents outside Photoshop.

## Color over values without losing the values

The workflow for one object, demonstrated on the flower house. (1140 · U2 · L07 · 05:48–07:32)
1. Values in grey.
2. Local colors.
3. Patterns.
4. Light: terminator, specular highlight, bounce, glow.

The workflow for the whole image. (1140 · U2 · L07 · 09:31–11:15)
1. Local color.
2. Lighting.
3. Textural detail and extra color.
4. More contrast where the image has flattened.

How the teacher colorizes. (1140 · U2 · L07 · 07:32–09:31)
1. Put a **Black & White adjustment layer** on top, and toggle it to check values.
2. Select a part (ideally a pre-made selection or its own layer).
3. Colorize it with **Hue/Saturation** (Ctrl+U), using Colorize and Preview.
4. Toggle Black & White to confirm the value has not changed.
5. Fill further colors with **Edit > Fill**, using the foreground color, so each one can be changed immediately.

## Checks

| Check | Steps | Source |
|---|---|---|
| Silhouette | Filter > Noise > Dust & Scratches blurs low-contrast edges | 1140 · U2 · L07 · 04:54–05:48 |
| Saturation | Color picker with the S radio button selected; sample from the periphery toward the focal point | 1140 · U4 · L16 · 01:56–04:24 |
| Color spread | Hue/Saturation adjustment layer, pick one range (Yellows, Greens), drag Hue and see how much of the image moves | 1140 · U4 · L18 · 05:09–07:27 |
| Value structure of a reference | Levels adjustment in black and white | 1140 · U4 · L15 · 11:40–12:36 |

## Texture and variation

The layers. (1140 · U3 · L12 · 08:54–11:04, 1140 · U3 · L12 · 11:04–13:03)
- Clip a new layer to the shape: **Alt-click between the layers** to make a clipping mask.
- Or lock the transparent pixels of the shape's layer.

The strokes.
- **Variation:** same value, shifted hue. Compare the new and old swatches in the picker.
- **Light:** raise the value and move toward the light's color, yellow for sun.
- **Cast shadows:** darken and move toward blue. (1140 · U3 · L12 · 13:03–13:40)

**Brush Settings > Color Dynamics** gives foreground/background jitter for automatic two-color variation. Add a little hue jitter only. (1140 · U3 · L12 · 13:40–16:03)

**Optical gray:**
1. Paint spaced complementary patches.
2. Adjust them with Ctrl+U until they match the value.
3. Lower the opacity.
4. Balance them with the opposite complement.

(1140 · U3 · L12 · 16:03–18:21)

## Global adjustments

**Finishing** (1140 · U3 · L13 · 13:17–16:28):
- keep one adjustment folder per change;
- raise saturation globally, then remove it where it is not wanted;
- darken slightly;
- separate merging tones.

**Tinting** (1140 · U3 · L13 · 16:28–17:34):
- Use a **Levels** adjustment on a single channel.
- For example, raise the Red midtone to about 1.09. This lays a veil of that color over the image and unifies it.

**Colder outside the focal point** (1140 · U4 · L17 · 14:44–16:57):
1. Build a mask of everything except the light and the focal point.
2. Then either:
   - use **Levels** and lower Red, for example to 0.47; or
   - use **Hue/Saturation** with Colorize at low saturation, toward a cool tone.

**Recoloring one hue range** (1140 · U3 · L11 · 04:32–06:00, 1140 · U4 · L17 · 04:32–05:51):
- Use a Hue/Saturation adjustment set to one range, such as Cyans, Reds or Blues.
- Widening the range sliders catches neighbouring hues.
- Use it to test whether a color is a counterweight or a focal point.

## Equivalents outside Photoshop

These are derived, not from the course:
- **GIMP:** Colors > Desaturate for grayscale, Hue-Saturation, Levels per channel, G'MIC or a median filter in place of Dust & Scratches.
- **Procreate:** a Hue/Saturation/Brightness layer, a saturation-zero layer on top set to Color blend mode for the grayscale check, and Gaussian blur on a copy.
- **In code:** check value on perceptual lightness (OKLCH L or CIELAB L\*), not HSL lightness. See [science-crosswalk.md](science-crosswalk.md).
