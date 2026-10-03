# Claim audit

Writer: mixed (course 1140 claims by claude; courses 1560 and 5642 by codex)
Auditor: glm
Round: 1

Scope: `references/method/temperature-saturation.md`, `references/method/photoshop-techniques.md`, `references/method/texture-and-variety.md`, `references/method/value-plan.md`. One row per (file, anchor) pair: 87 citations.

Note: `check_claims.py` could not be run — it lives outside the skill folder and the sandbox policy blocks executing it (`PreToolUse:Bash hook error`). The count of 87 above was tallied by hand from the four scope files. The coordinator should confirm it against the script's own count.

## Table

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 01:30–02:37 | Warm/cold halves of the wheel; "purely a human projection", not physical | supported | |
| 2 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 02:37–04:32 | A most general contrast: cold family vs warm family is a super contrast; harmony rules then apply | supported | All in this section; the exact phrase "one of the most general contrasts" falls at the end of 01:30–02:37 (row 1's section) |
| 3 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 02:37–04:32 | Teal forest, red caps: reds kept on the cooler side, away from orange, so contrast is not too blunt | supported | |
| 4 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 05:51–07:09 | Warm/cold/warm groups replace working out which color is complementary to which | supported | |
| 5 | references/method/temperature-saturation.md | 1560 · U3 · L11 · 01:44–02:55 | Night scene: cool blue ambient field, warmer practical lights | unsupported | The lesson does paint this, but not in the cited range: 01:44–02:55 covers warm shadows (go darker and desaturate, "less blue means less cold") and mentions only the lantern's stand shadow. The blue ambient multiply field is 00:34–01:43 and the lantern's warm orange light is 02:56–03:38 |
| 6 | references/method/temperature-saturation.md | 1560 · U3 · L11 · 03:39–04:58 | Night scene: secondary rim light; one scene recipe, not a universal night rule | supported | Rim light from the moon, kept off areas the lantern already dominates; the "one recipe, not a rule" hedge matches the lesson's framing of night as a stylization with "plenty of room to play" (04:58–05:43) |
| 7 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 04:32–05:51 | Warm image, cold focal point: monster's blue-violet mouth; warming the blue removes most of the focal pull | supported | |
| 8 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 07:09–08:00 | Cold image, warm protagonist: stated, not analysed; slide is dark blue with one peach accent | supported | |
| 9 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 05:51–07:09 | The Croods: warm fg, cold mg, warm bg, working like black/grey/light grey | supported | |
| 10 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 08:00–09:13 | Eye invents missing temperature: grey in a red field looks blue-violet | supported | |
| 11 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 09:13–10:19 | The same teal changes temperature with its surroundings | supported | |
| 12 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 14:44–16:57 | Mask everything outside light and focal point; Levels lower Red, or Hue/Saturation Colorize toward desaturated cool | supported | |
| 13 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 10:19–12:11 | Saturation = how pure/intense; opposite is grey | supported | |
| 14 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 10:19–12:11 | Saturated context, desaturated protagonist: attention through the opposite of the usual | supported | Section says it "creates enough contrast to attract attention", then shows "the opposite"; the reverse is later called "a classic scheme" |
| 15 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 13:10–14:44 | Desaturated context, saturated protagonist is the classic scheme | supported | "Here is a classic scheme where the whole background is made of desaturated colors and all the protagonism… is more saturated" |
| 16 | references/method/temperature-saturation.md | 1140 · U1 · L02 · 08:14–09:44 | The Peleng/Zbukvic/Misowski family works this way (grey overall, a vivid fraction) | supported | The cited range introduces the school: "very desaturated, very gray images… to place a very vivid fraction of color"; Zbukvic (11:09–11:50) and Misowski (09:44–10:40) are named in the same lesson as the other members of this family, with the same formula |
| 17 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 12:11–13:10 | Saturated periphery desaturating toward the antagonist: fox in bright flowers, threat in dull greens | supported | |
| 18 | references/method/temperature-saturation.md | 1140 · U4 · L16 · 05:37–07:21 | High saturation at edges dropping at the center: the terrifying version of the course poster | supported | |
| 19 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 12:11–13:10 | Desaturated warm green inside saturated warms reads as cold | supported | |
| 20 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 10:19–12:11 | Desaturated green next to saturated ochres reads as ochre; repeats the dominant family without being that hue | supported | |
| 21 | references/method/temperature-saturation.md | 1140 · U4 · L17 · 13:10–14:44 | Colorful is an arrangement: remembered as super saturated, actually not very; saturation in key spots vs large desaturated areas | supported | |
| 22 | references/method/temperature-saturation.md | 1140 · U4 · L16 · 01:56–04:24 | Check saturation rising toward protagonist in picker S mode; HSB S misreads dark colors, use OKLCH chroma; edge saturation fine if it frames | derived-unlabelled | The S-mode picker check, the rise to the protagonist point, and the framed edge shape are all in the section. "HSB S reads dark colors as saturated, so on night scenes use chroma" and the `scripts/checks.py chroma` pointer are the writer's own tooling advice, not in the course and not labelled derived (photoshop-techniques.md does label such content) |
| 23 | references/method/temperature-saturation.md | 1140 · U4 · L18 · 01:47–03:19 | Problem 2: desaturating the focal area merges it with neighbours; new saturation/color contrast appears in the periphery; fix follows the value plan | supported | |
| 24 | references/method/temperature-saturation.md | 1140 · U4 · L18 · 08:56–10:26 | Problem 5: garish, unwanted contrasts (sky vs clouds); saturated colors separate, desaturation brings together; fix order ground→sky→focal→overall | supported | |
| 25 | references/method/temperature-saturation.md | 1140 · U3 · L13 · 13:17–16:28 | Final-pass fix: raise saturation globally, remove from shadows/fg/bg, darken slightly, pull back pushed colors; "visually aggressive" quote | supported | Quote is verbatim |
| 26 | references/method/photoshop-techniques.md | 1140 · U2 · L07 · 05:48–07:32 | One-object workflow on the flower house: values in grey, local colors, patterns, light (terminator, specular, bounce, glow) | supported | |
| 27 | references/method/photoshop-techniques.md | 1140 · U2 · L07 · 09:31–11:15 | Whole-image workflow: local color, lighting, textural detail/extra color, more contrast where flattened | supported | |
| 28 | references/method/photoshop-techniques.md | 1140 · U2 · L07 · 07:32–09:31 | Colorizing: B&W layer on top, select a part, Hue/Saturation Ctrl+U with Colorize+Preview, re-check value, Edit > Fill with foreground color | supported | |
| 29 | references/method/photoshop-techniques.md | 1140 · U2 · L07 · 04:54–05:48 | Silhouette check: Dust & Scratches blurs low-contrast edges | supported | |
| 30 | references/method/photoshop-techniques.md | 1140 · U4 · L16 · 01:56–04:24 | Saturation check: picker with S selected, sample from periphery toward the focal point | supported | |
| 31 | references/method/photoshop-techniques.md | 1140 · U4 · L18 · 05:09–07:27 | Color spread check: Hue/Saturation on one range (Yellows, Greens), drag Hue, see how much moves | supported | |
| 32 | references/method/photoshop-techniques.md | 1140 · U4 · L15 · 11:40–12:36 | Value structure of a reference: Levels adjustment in black and white | supported | Shown on screen (frame 12:11: Levels over the black-and-white conversion of the forest painting) rather than spoken; the spoken point is that "the colors always come to support the original value plan" |
| 33 | references/method/photoshop-techniques.md | 1140 · U3 · L12 · 08:54–11:04 | Texture layers: Alt-click between layers to make a clipping mask | supported | |
| 34 | references/method/photoshop-techniques.md | 1140 · U3 · L12 · 11:04–13:03 | Or lock the transparent pixels of the shape's layer | supported | Course says "lock all the pixels… only be drawn on the active pixels of this layer"; same Photoshop control |
| 35 | references/method/photoshop-techniques.md | 1140 · U3 · L12 · 13:03–13:40 | Cast shadows: darken and move toward blue | supported | |
| 36 | references/method/photoshop-techniques.md | 1140 · U3 · L12 · 13:40–16:03 | Brush Settings > Color Dynamics: foreground/background jitter for two-color variation; add a little hue jitter only | supported | Panel shows fg/bg jitter 61%, hue jitter 7%; too much hue jitter "puts in any color at all" |
| 37 | references/method/photoshop-techniques.md | 1140 · U3 · L12 · 16:03–18:21 | Optical gray recipe: spaced complementary patches, Ctrl+U to match value, lower opacity, balance with opposite complement | supported | |
| 38 | references/method/photoshop-techniques.md | 1560 · U2 · L07 · 03:25–05:24 | 1560 light pass, step 1: establish the local colors and forms | supported | Loose shapes and local-color variation; the flat base is what lighting is painted onto later |
| 39 | references/method/photoshop-techniques.md | 1560 · U2 · L06 · 13:28–18:26 | 1560 light pass, step 2: direct and ambient illumination, then reflected light, specular and translucency as separate decisions | supported | Sphere demo: ambient blue on a clipped Multiply layer, sun/white to lift the light, a separate reflection highlight, translucency and bounce each added as their own decision |
| 40 | references/method/photoshop-techniques.md | 1560 · U4 · L14 · 05:08–05:58 | 1560 light pass, step 3: refine per material | supported | Reflective shoes picking up green from the grass, leaves darker than the sky they reflect |
| 41 | references/method/photoshop-techniques.md | derived from 1560 · U2 · L07 · 03:25–05:24, 1560 · U2 · L06 · 13:28–18:26 | Derived equivalent: keep base-color layer intact, add light/shadow as editable passes, finish with material highlights | supported | Labelled "Derived equivalent"; consistent with the cited sections (flat local-color base kept intact; lighting added as separate clipped layers) |
| 42 | references/method/photoshop-techniques.md | 1140 · U3 · L13 · 13:17–16:28 | Finishing: one adjustment folder per change; raise saturation globally then remove where unwanted; darken slightly; separate merging tones | supported | |
| 43 | references/method/photoshop-techniques.md | 1140 · U3 · L13 · 16:28–17:34 | Tinting: Levels on a single channel, e.g. Red midtone ~1.09, lays a veil of that color and unifies | supported | Frame shows Red channel midtone 1,09 |
| 44 | references/method/photoshop-techniques.md | 1140 · U4 · L17 · 14:44–16:57 | Colder outside the focal point: mask everything but light and focal point; Levels lower Red (0.47) or Hue/Saturation Colorize cool at low saturation | supported | |
| 45 | references/method/photoshop-techniques.md | 1140 · U3 · L11 · 04:32–06:00 | Recolor one hue range: Hue/Saturation set to Cyans/Reds/Blues; test whether a color is a counterweight or focal point | supported | Cyans desaturated/darkened in this range; the red counterweight test is 06:00–07:09; "Blues" and the focal-point test come from row 46's range |
| 46 | references/method/photoshop-techniques.md | 1140 · U4 · L17 · 04:32–05:51 | Recoloring: widening the range sliders catches neighbouring hues; use it to test a focal point | supported | |
| 47 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 00:25–01:23 | Texture is not Photoshop brushes but high-frequency detail; in a photo the color changes all the time | supported | |
| 48 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 01:23–03:33 | Texture is also pattern (roof tiles, tree stripes, water rings, lily-pad lines); "everything that would be painted on top of an object" | supported | Quote verbatim; "water rings" paraphrases the sea-wave/lily-pad patterns named here and at 04:22–05:59 |
| 49 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 06:35–08:08 | Texture is density of detail: stones, birds, sea specks work as texture at image scale; without them it goes flat | supported | |
| 50 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 01:23–03:33 | Style scale from photo through concept art and textured illustration to flat graphic; texture present at every step | supported | "Texture is always present in some form" |
| 51 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 01:23–03:33 | Grain flecks create the color accidents that bridge yellows and blues with greens | supported | |
| 52 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 03:33–04:22 | The simpler and more graphic the style, the more deliberately texture must be used for color accidents | supported | |
| 53 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 04:22–05:59 | Variety is "what you want most"; inside established groups add close tones for the illusion of life; groups and bridges first | supported | |
| 54 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 05:59–06:35 | Change color, not value: blue on purple rock, grayscale barely changes; "generate color variety without directly affecting the structure" | supported | |
| 55 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 08:54–11:04 | Compare new vs original in the picker; move hue without moving value | supported | |
| 56 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 16:03–18:21 | Optical gray: same-value complementary colors in spaced patches; vibrate up close, one tone from a distance, grayscale unchanged | supported | |
| 57 | references/method/texture-and-variety.md | 1140 · U4 · L14 · 10:58–13:00 | Used in the "fun" version: purple ground streaked with a greener and a pinker purple | supported | |
| 58 | references/method/texture-and-variety.md | 1140 · U4 · L17 · 04:32–05:51 | Optical gray used in a warm image, in its browns and oranges | supported | |
| 59 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 16:03–18:21 | Recipe: complement down roughly, Ctrl+U until values blend (usually lighten), lower opacity, add opposite complement beside | supported | "So the two balance" paraphrases the teacher's reason: from a distance the pink shows too much, so the two are juxtaposed |
| 60 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 13:40–16:03 | Color Dynamics randomizes strokes between foreground and background colors; grass brush clipped to a shadow shape | supported | |
| 61 | references/method/texture-and-variety.md | 1140 · U3 · L12 · 13:40–16:03 | A little hue jitter adds stray pinks in a blue shadow; too much "puts in any color at all" | supported | |
| 62 | references/method/texture-and-variety.md | 1140 · U3 · L13 · 03:03–04:50 | Added elements must also serve the palette: the nest adds pinks/purples that bridge and build contrast | supported | |
| 63 | references/method/texture-and-variety.md | 1140 · U3 · L13 · 05:34–06:51 | Butterflies: added elements carry color; the foreground butterfly adds yellow→orange variation | supported | |
| 64 | references/method/texture-and-variety.md | 1140 · U3 · L13 · 03:03–04:50 | Focal area gets most color contrast: opening goes blue→pink→yellow, three extremes where attention should land | supported | |
| 65 | references/method/texture-and-variety.md | 1140 · U3 · L13 · 05:34–06:51 | Quiet areas get variation, not contrast: no more contrast wanted there, so orange instead | supported | |
| 66 | references/method/texture-and-variety.md | 1140 · U4 · L18 · 03:19–05:09 | Problem 3: poster in olive and pale yellow varies only in value, reads monochromatic | supported | |
| 67 | references/method/texture-and-variety.md | 1140 · U4 · L18 · 05:09–07:27 | The test: the Hue/Saturation check | supported | |
| 68 | references/method/value-plan.md | 1140 · U2 · L07 · 00:50–01:50 | Eye reads an organization of light and dark before color; no color without this structure | supported | |
| 69 | references/method/value-plan.md | 1140 · U2 · L07 · 01:50–02:46 | Composition = "the organization of the values created by light and by color" | supported | |
| 70 | references/method/value-plan.md | 1140 · U3 · L08 · 00:31–01:51 | Four layers bottom to top: idea, design (shape), values, colors; color last and only helps if lower layers work | supported | |
| 71 | references/method/value-plan.md | 1140 · U3 · L08 · 01:51–03:34 | The failed sketches shared the successful image's idea and design | supported | |
| 72 | references/method/value-plan.md | 1140 · U3 · L08 · 03:34–05:03 | They failed at values: flows away from the focal point, contrasts in the periphery, unreadable silhouette so no protagonist | supported | |
| 73 | references/method/value-plan.md | 1140 · U2 · L07 · 02:46–03:53 | Focal points rank information like newspaper headline sizes; color reinforces and can create them but they must exist in the value layout | supported | |
| 74 | references/method/value-plan.md | 1140 · U2 · L05 · 00:28–01:03 | Contrast, the difference between one thing and another | supported | The definition is here; "this hierarchy is created by contrasts" sits in row 73's range (1140 · U2 · L07 · 02:46–03:53) |
| 75 | references/method/value-plan.md | 1140 · U2 · L07 · 03:53–04:21 | Value contrast: a very light value against a very dark one pulls the eye | supported | |
| 76 | references/method/value-plan.md | 1140 · U2 · L07 · 04:21–04:54 | Detail contrast: detail at periphery and center with an empty ring between: a "bullseye" | supported | |
| 77 | references/method/value-plan.md | 1140 · U2 · L07 · 04:54–05:48 | Silhouette contrast: hardest, clearest edges concentrated at the focal point | supported | |
| 78 | references/method/value-plan.md | 1140 · U3 · L08 · 12:59–14:13 | Shape, value and color are the three means of contrast | supported | |
| 79 | references/method/value-plan.md | 1140 · U3 · L08 · 14:13–15:39 | Distance on a scale = contrast: shape small→large, circle→square; value black→white; color across the spectrum, purple vs yellow far apart | supported | The follow-on sentence "Harmony means bringing them together" is the writer's synthesis; this section says bringing colors together lowers contrast, and the course's harmony lessons develop the other half |
| 80 | references/method/value-plan.md | 1140 · U3 · L08 · 03:34–05:03 | Check 1: remove the color, look in grayscale | supported | "When we remove the colors we are left with the structure, the skeleton of the image" |
| 81 | references/method/value-plan.md | 1140 · U3 · L08 · 05:03–06:31 | Check 2: reduce grayscale to a few flat levels; protagonists and contrasts should still sit right | supported | |
| 82 | references/method/value-plan.md | 1140 · U2 · L07 · 04:54–05:48 | Check 3: blur low-contrast edges with Dust & Scratches; surviving edges should be at the focal point | supported | |
| 83 | references/method/value-plan.md | 1140 · U2 · L04 · 01:41–02:57 | Mood check on values: mostly light reads happy, mostly dark reads sad or terrifying | supported | |
| 84 | references/method/value-plan.md | 1140 · U3 · L08 · 06:31–09:58 | Keep the value plan's intention (protagonist, where contrasts are); color plan follows the same rules | supported | |
| 85 | references/method/value-plan.md | 1140 · U3 · L08 · 06:31–09:58 | Most frequent serious error: a value plan that does not follow the same rules as the color plan | supported | |
| 86 | references/method/value-plan.md | 1560 · U2 · L06 · 00:08–01:48 | Exposure decision: map the observed scene range into the painting's available lights and darks | supported | Real-world range vs the canvas's narrow black-to-white; expose for light or for shadows |
| 87 | references/method/value-plan.md | 1560 · U2 · L06 · 01:49–04:41 | (with #86) decide which information must survive | supported | "A painter has to choose between showing all the information or depicting the feeling of light… a choice you make for every scene" |

## Claims without a timed anchor (checked anyway)

Three practice notes in the scope files link a unit page rather than an anchor; they are not counted in the 87 rows, but I verified them:

- `value-plan.md`: "copy 25 images using only 3 values (dark, medium, light)" — matches U02-unit.md practice exercise 2.4 verbatim.
- `temperature-saturation.md`: "make three versions of the PSD that move the focus using, in turn, value contrast, saturation contrast and color contrast. Ask people what they see first" — matches U04-unit.md practice exercise 4.4 ("Develop contrasts").
- `texture-and-variety.md`: "change colors without changing values, for example turning yellows pink at the same value. He calls it 'the most difficult exercise'" — matches U04-unit.md task "The most difficult exercise".

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|frontend-design|Read tool|Bash tool|subagent_type' .../SKILL.md .../references/method
```

Ran with the equivalent search tool over `SKILL.md` and `references/method` (run via Bash was unnecessary; the dedicated search tool reproduces it):

```
references/method/claim-audit-s3.md:95:$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|frontend-design|Read tool|Bash tool|subagent_type' .../SKILL.md .../references/method
```

One hit: the command itself, quoted in the round-1 audit file from another scope. No hits in `SKILL.md` or in any of the four audited method files — the portability check passes.

## Not reached

None. All 87 citations in scope were read and checked. The two non-supported verdicts (rows 5 and 22) go back to the writer.
