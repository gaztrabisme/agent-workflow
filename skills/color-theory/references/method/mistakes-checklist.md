# Review checklist: six mistakes and the tests that catch them

Reader: an agent critiquing an existing image, or doing the last pass on its own work. Source: [L18](../course/U04-L18-bonus-solving-common-color-problems.md), plus the checks taught across the course.

Run the tests in this order. Each one names the stage of the method to go back to when it fails.

## Tests

| # | Test | In Photoshop | Without Photoshop | Pass condition | Back to |
|---|---|---|---|---|---|
| T1 | Grayscale | Black & White adjustment layer | `checks.py value IMG --focal x0,y0,x1,y1` (OKLab L, not HSL) | The focal point carries the strongest value contrast and the flows lead to it. Script default: the focal box holds at least 2× its area share of value edges. (1140 · U3 · L08 · 03:34–05:03, 1140 · U3 · L13 · 04:50–05:34) | Value plan |
| T2 | Fewer levels | Posterize the grayscale to 3–5 levels | The `-levels4.png` that `checks.py value` writes | The protagonists and contrasts are still where planned. (1140 · U3 · L08 · 05:03–06:31) | Value plan |
| T3 | Dust & Scratches | Filter > Noise > Dust & Scratches on a copy | A median filter on the grayscale at a radius of about 1% of the image width | The surviving hard edges cluster at the focal point. **Skip for flat or graphic styles**, where every edge is hard; T1's edge share replaces it. (1140 · U2 · L07 · 04:54–05:48) | Value plan |
| T4 | Mood board | Place the image beside references for the target feeling, with alternative versions | Same; needs reference images | The chosen version sits in the references' range. (1140 · U4 · L18 · 07:27–08:56) | Intent |
| T5 | Saturation map | Color picker in S mode, sampling from the edges inward (unreliable on dark colors) | `checks.py chroma IMG --focal …` (OKLCH C by ring) | Chroma rises toward the protagonist; saturated edges only frame. An inverted layout is allowed when deliberate, as in the terrifying recipe. (1140 · U4 · L16 · 01:56–04:24, 1140 · U4 · L16 · 05:37–07:21) | Temperature and saturation |
| T6 | Hue/Saturation spread | Adjustment layer: move the dominant range (for example Yellows), then a secondary range (Greens) | `checks.py spread IMG` (Photoshop's ranges: 30° core, 30° falloff) | The dominant range does not move almost everything, and a secondary range responds. Script default: fails if one range moves more than 80% and no other moves 5%. A deliberately restrained or pastel palette may fail; the teacher allows it. (1140 · U4 · L18 · 05:09–07:27) | Texture and variety |
| T7 | Light coherence | Sample a lit side and a shadow side of the key objects | `checks.py sample IMG x,y x,y` (warm h 20–100, cool 200–320) | Lit sides carry the light's temperature and shadows the ambient temperature; compare the pair, not absolute bands. (1140 · U4 · L18 · 10:26–12:20) | Light |
| T8 | Area clarity | Squint, or look at a thumbnail | Downscale to about 64 px wide and view it | Each large area has one clear dominant color, with only chosen interruptions. (1140 · U4 · L18 · 00:30–01:47) | Harmony |
| T9 | Counterweight | Temporarily desaturate the strongest color patch | Desaturate the patch in a copy and compare side by side | If the image loses balance, the patch is load-bearing: keep it. (1140 · U3 · L11 · 04:32–06:00) | Rhythm and balance |
| T10 | Semantic target fit | Use a seven-position bipolar rating form for the proposal; choose pairs relevant to the brief | Paper/web form and spreadsheet; the target audience rates the actual proposal | Before collecting ratings, name the required adjective pairs, pole direction and acceptable 1–7 interval. Pass when every brief-critical pair's audience mean falls inside its predeclared interval. (derived from 5642 · U3 · L43 · 02:41–03:16, 5642 · U3 · L43 · 03:44–04:34) | Intent and functional color |
| T11 | Audience agreement | Collect independent ratings from the intended audience and calculate each pair's spread | Spreadsheet: count, mean and sample standard deviation by pair | Pass when the predeclared minimum response count is met and each critical pair's standard deviation is within the brief's stated limit. Otherwise mark inconclusive and investigate the split before approval. The course supplies no universal sample-size or spread threshold. (derived from 5642 · U3 · L43 · 10:21–11:57, 5642 · U3 · L43 · 11:57–12:55) | Intent and functional color |
| T12 | Variant distinction | Rate each proposal on the same bipolar pairs and overlay the profiles | Spreadsheet: subtract each pair's means between variants | For each difference named in the brief, the second proposal's mean moves at least the predeclared amount in the intended direction. Skip when there are no alternatives. (derived from 5642 · U3 · L43 · 10:21–11:57) | Intent and functional color |

Formulas, thresholds and when to override them: [measurement.md](measurement.md). T4, T8 and T9 are judged by eye. T10–T12 require audience ratings; their target bands, sample count and minimum differences come from the brief, because the course does not set universal numeric thresholds. When reporting, say which tests were measured, which were judged by eye, and which were skipped and why.

**After any fix, re-run T1 and T5.** A value fix often flattens the chroma gradient, and a chroma fix often moves the value contrast.

## The six problems

| Problem | Symptom | Fix | Source |
|---|---|---|---|
| 1. Harmonizing until the areas dissolve | Dirty look; one area's color scattered everywhere | Keep each area coherent; interrupt it only on purpose | 1140 · U4 · L18 · 00:30–01:47 |
| 2. Color contrast in the wrong place | The layout points one way, and saturation or hue contrast pulls the eye elsewhere | Move the color, saturation and temperature contrast onto the focal point; desaturate what competes | 1140 · U4 · L18 · 01:47–03:19 |
| 3. Lack of color variety | Only value changes; reads monochromatic (fails T6) | Two color groups, then variation in hue and saturation within them, then a temperature contrast | 1140 · U4 · L18 · 03:19–05:09 |
| 4. Color does not fit the story | Pretty but the wrong feeling (fails T4) | Restate the feeling, build a mood board, compare versions, choose | 1140 · U4 · L18 · 07:27–08:56 |
| 5. Saturation out of control | Garish; unwanted contrasts everywhere | Desaturate secondary areas, saturate the focal point, then raise everything slightly if it looks grey | 1140 · U4 · L18 · 08:56–10:26 |
| 6. Color not coherent with the light | Lit side cooler than the shadow under a warm light (fails T7) | Decide the light and ambient colors first, and follow them on every object | 1140 · U4 · L18 · 10:26–12:20 |

## Other failures the course names

- **A value plan that does not follow the same rules as the color plan.** The course calls this one of the most frequent and serious errors. (1140 · U3 · L08 · 06:31–09:58)
- **Two tones merging at the focal point.**
  - The example is the pink body bleeding into the yellow rim.
  - The fix is to push them apart in hue and value until a clear line separates them.

  (1140 · U3 · L13 · 13:17–16:28)
- **A payoff-less focal point**: everything leads to the protagonist, and nothing is there. Add a story detail. (1140 · U3 · L13 · 01:43–03:03)

## Reporting a critique

For each failure, report:
- the test that failed;
- what was seen;
- the stage of the method to return to;
- one concrete change.

Quote the course anchor so the reader can check the principle. Keep what works: say which contrasts and bridges are already doing their job, so a fix does not destroy them.

For graphic-communication tasks, classify the role before revising the color: representation, psychological or cultural evocation, or a functional sign/code. See [functional-color.md](functional-color.md). (5642 · U3 · L26 · 00:55–01:40)
