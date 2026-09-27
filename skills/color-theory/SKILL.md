---
name: color-theory
description: "A course-distilled method for choosing and critiquing color in images, lighting and graphic design, with a color-science library for measurement, spaces, code and accessibility. USE WHEN planning or fixing color in illustration, painting, concept art, posters, brands, film, comics or UI themes; choosing or explaining a palette; critiquing an image's color; or answering color-science questions (OKLCH, CSS, contrast, naming, pigments, history). Not for photo edits (`batch-photo-retouching`), an interface's overall style, or choosing a chart type. Keywords: color theory, palette, harmony, complementary, value, contrast, saturation, temperature, mood, color script, focal point, OKLCH, WCAG, APCA."
license: "Proprietary (private course-derived material, not for redistribution); references/color-science is CC BY 4.0 by meodai"
---

# Color Theory

This skill gives an ordered method for deciding color in any image: illustration, concept art, poster, brand or sequence. It also covers critiquing color that does not work. Every step is traceable to a course lesson and time.

The method combines Domestika 1140, *Color Theory: How to Apply It to Your Images*; 1560, *Lighting Principles for Digital Painting*; and unit 3 of 5642, *Specialization in Graphic Design and Visual Communication*. Their lesson files and frames live in separate folders under `references/course*/`; the approved reading-copy PDF and page index in `references/course/` cover 1140. Underneath the method sits `references/color-science/`, the vendored `color-expert` library. It answers questions of fact: color spaces, CSS, contrast numbers, naming, pigments and history.

> Inherits the `core` kernel. See `../core/SKILL.md`. Obey its Integrity Constraints, declare its gates, and reference its files rather than copying them.

## When it fires, and when a sibling owns it
- **This skill:**
  - choosing, planning, explaining or critiquing color for an image, brand, sequence or theme;
  - any color-science question.
- **`batch-photo-retouching` instead:** editing photographs (relighting, white balance, retouching) where the colors must stay true to the original.
- **Not this skill:** the overall visual style of an interface (layout, typography, component styling). That belongs to the skill building the interface. This skill still answers the interface's palette, ramp and contrast questions.
- **Not this skill:** choosing a chart type and which data goes to which visual channel. This skill answers the color side of that choice: perceptual sequential and diverging ramps, color-vision deficiency and contrast.
- **`domestika-course-archive` instead:** archiving a course. Its `export` command is how another color course gets added here.

> **Disambiguation:** decide on the **artifact**. A color decision or color fact belongs here. Photo fidelity and course packaging belong to the siblings above. Overall interface style and chart choice belong to whichever skill builds the deliverable.

## Principles
1. **Values before color.** The eye reads light and dark before hue.
   - An image is built in four layers: idea, then shape, then value, then color.
   - Color is the last layer. It can only improve an image whose values already work.

   (1140 · U3 · L08 · 00:31–01:51)
2. **Color follows the value plan.** Where the grayscale has contrast, the color must have contrast. The course names a color plan that breaks the value plan as the most frequent serious error. (1140 · U3 · L08 · 06:31–09:58)
3. **Contrast is distance; harmony is closeness.** Value, hue, saturation and temperature are each a scale. Move things apart to attract attention, and bring them together to unify. Every decision trades one against the other. (1140 · U3 · L08 · 14:13–15:39, 1140 · U3 · L10 · 10:21–10:43)
4. **Harmony is interaction with clarity.** Each area has one dominant color and holds a little of the others. Bridge colors connect the areas. (1140 · U3 · L09 · 01:17–01:59)
5. **Color is relative.** Judge every color in place, next to its neighbours and in its sequence, never as a swatch. (1140 · U2 · L05 · 01:03–03:13, 1140 · U4 · L17 · 09:13–10:19)
6. **Feeling comes from value and saturation more than hue.** No color has a universal meaning; meaning comes from how the color is made and what it is associated with. (1140 · U2 · L04 · 04:17–05:30)
7. **Fewer colors, better decisions.** Limit the palette, then add variety inside each color group at the same value. (1140 · U3 · L08 · 09:58–11:48, 1140 · U3 · L12 · 05:59–06:35)
8. **The course is the system and the science is the check.** Follow the method for decisions. Open `color-science` for measurement, code and anything the course does not cover. Where they differ, apply the correction in `references/method/science-crosswalk.md`.

## The flow

The course teaches this in a deliberately reversed order: perception first, theory last. The working order is:

| # | Stage | Decide | Check before moving on | Reference |
|---|---|---|---|---|
| 1 | Intent | The feeling, as keywords; the story and its payoff at the focal point; references | A mood board exists; the value, color and saturation targets are written down | `method/intent-and-meaning.md`, `method/artist-references.md` |
| 2 | Value plan | Focal hierarchy; value, detail and silhouette contrast; flows | Grayscale, fewer-levels and Dust & Scratches tests pass | `method/value-plan.md` |
| 3 | Light | Direction, source quality, exposure, light color, ambient or shadow color, and how stylized (1560 · U2 · L05 · 01:04–03:43; 1560 · U2 · L06 · 00:08–01:48) | Lit sides take the light's temperature and shadows the ambient's | `method/light.md` |
| 4 | Color plan | Main contrast pair or families; each color's role (representation, evocation or code; 5642 · U3 · L26 · 00:55–01:40); the focal color; palette type; a color script for sequences | Every value contrast has a matching color contrast; any semantic target is named before testing | `method/palettes.md`, `method/contrast-and-context.md`, `method/functional-color.md` |
| 5 | Harmony | Blocks, then bridges (a third hue or desaturation), then spreading colors by bounced light and repetition | Each area is still clearly its own color | `method/harmony-bridges.md` |
| 6 | Rhythm, balance and flow | Placing colors with sound and silence; color counterweights; color families as paths to the focal point | Removing a key patch shows it is load-bearing | `method/rhythm-balance-flow.md` |
| 7 | Temperature and saturation | Warm and cold groups; the saturation layout rising toward the protagonist | S-mode saturation map; the focal point holds the strongest temperature and saturation contrast | `method/temperature-saturation.md` |
| 8 | Variety and finish | Texture, same-value hue shifts, optical gray, story details that carry color; final saturation and tint pass | Hue/Saturation spread test; grayscale unchanged by the texture | `method/texture-and-variety.md`, `method/photoshop-techniques.md` |
| 9 | Review | The six mistakes, plus a semantic profile for graphic communication when meaning is a brief requirement | Tests T1–T12 | `method/mistakes-checklist.md`, `method/functional-color.md` |

Scale the flow to the task:
- **A quick palette question:** stages 1, 4 and 7, plus a one-line value target from stage 2 (which area is lightest and darkest).
- **A critique of an existing image:** stage 9 first, then go back to the stage each failed test names.
- **After any fix:** re-run T1 and T5. A value fix often flattens the chroma gradient, and a chroma fix often moves the value contrast.
- **Measuring without Photoshop:** `scripts/checks.py` runs T1, T2, T5, T6 and T7 on an image file and computes WCAG contrast. Formulas and thresholds are in `references/method/measurement.md`.
- **Brand or identity work:**
  1. Fix a color code of 3 colors or fewer.
  2. Tie it to form.
  3. Choose the elegant or fun recipe from `method/intent-and-meaning.md`.
- **Graphic-communication meaning:** identify whether color represents, evokes, or functions as a sign/code (5642 · U3 · L26 · 00:55–01:40). When the intended audience's reading matters, use T10–T12 to test the semantic profile and compare alternatives (5642 · U3 · L43 · 10:21–11:57).
- **UI or data work:** use the method for the hierarchy (dominant, bridge and accent colors, saturation at the focal point). Use `color-science` for ramps, OKLCH and contrast numbers.

**Output.** For a plan, state each decision with the stage it belongs to. For a critique, report each failure as: test, what was seen, stage to return to, one concrete change. Cite lesson anchors, for example `1140 · U3 · L09 · 05:00–06:14`, `1560 · U3 · L13 · 06:30–07:57` or `5642 · U3 · L43 · 10:21–11:57`. Say which tests were measured, which were judged by eye, and which were skipped and why. Deliver the plan or critique in the reply, or in a file when the user names one.

## When to open color-science

Open `references/color-science/SKILL.md` first, then `references/color-science/references/INDEX.md`, when the task involves any of these:
- numbers: contrast ratios, OKLCH or CIELAB values, ΔE;
- code or CSS;
- color spaces and conversions;
- accessibility and color-vision deficiency;
- pigment or paint mixing;
- color names or naming systems;
- history of color theory;
- palette-generation libraries.

`references/method/science-crosswalk.md` lists where the course and the science agree and where they differ. Apply these corrections:
- **Measure value as perceptual lightness** (OKLCH L or CIELAB L\*), not HSL or HSB. HSL L is especially misleading.
- **Wheel distance is approximate.** Equal hue angles are not equal perceptual steps.
- **Temperature is a joint shift of hue and saturation.** Green and purple sit on the boundary between warm and cool.
- **Keep the two taught color wheels distinct.** Course 1140's screen complements use RGB/CMY; course 5642's harmony lesson uses a traditional RYB wheel. Follow the crosswalk for the task.
- **Grayscale does not prove accessibility.** For text and UI, verify WCAG or APCA contrast.

## Gates (declared, inherited from core)
- **Grounding gate.** The substrate is:
  - the course lessons in `references/course/`, `references/course-1560/` and `references/course-5642/`, cited by anchor;
  - the image or brief itself.

  Do not state a method claim without an anchor. Do not state a science fact without a `color-science` reference. See `../core/references/grounding-gate.md`.
- **Output Contract.** A color plan names a decision for stages 1, 2, 4 and 7 at minimum; a quick palette answer meets stage 2 with a one-line value target. A critique reports every failed test from `mistakes-checklist.md` with its fix. See `../core/references/wiki-protocol.md`.
- **Pushback and teach.** Push back when a request would break the value plan, for example "make everything more saturated" or "add the brand color everywhere". Explain which principle it breaks and cite the anchor. See `../core/references/pushback-and-teach.md`.
- **Approach declaration.** This can be skipped for a single palette answer. Declare it for a multi-image system or a brand system. (core SKILL.md §7.)

## Anti-patterns
- Choosing a harmony rule (complementary, triadic) before the value plan and the feeling exist.
- Judging colors as isolated swatches, or approving a palette without seeing it on the image.
- Adding a color "for harmony" everywhere until the areas dissolve (Problem 1).
- Putting saturation or hue contrast away from the focal point (Problem 2).
- Raising saturation everywhere instead of laying it out (Problem 5).
- Quoting a color-meaning chart ("blue is sad") as a rule.
- Reporting value from HSL lightness, or calling a grayscale check an accessibility pass.
- Stating a course principle without its anchor, or presenting a derived summary as the teacher's words.
- Copying course text into public places. The course material is private: see `NOTICE.md`.

## Composition
- **Inherits:** `core`.
- **Contains:** `references/color-science/`, the upstream `meodai/skill.color-expert` vendored as a git subtree. It is the secondary source and is not edited here. Update it with `git subtree pull --prefix=references/color-science https://github.com/meodai/skill.color-expert main --squash`.
- **Fed by:** course exports in their own folders. Course claims are merged into `method/` with lesson anchors.
- **Hands off to:** `batch-photo-retouching` for photo edits. When the palette goes into a deck, document or interface, the skill that builds that deliverable applies it; this skill supplies the palette, the ramps and the contrast checks.

## References
- `references/method/intent-and-meaning.md`: feeling to value, color and saturation targets; mood recipes; identity; story payoff.
- `references/method/value-plan.md`: four layers, focal hierarchy, the three black-and-white contrasts, structure checks.
- `references/method/light.md`: reflection, local color and specularity, direct and indirect light, bounces, stylization, light coherence.
- `references/method/functional-color.md`: the 5642 functional classification, color-family examples and semantic-differential review.
- `references/method/contrast-and-context.md`: relativity of perception, making one color stronger, color script, local color.
- `references/method/harmony-bridges.md`: interaction with clarity, bridge colors, spreading colors, the unique focal color.
- `references/method/rhythm-balance-flow.md`: sound and silence, color counterweights, color families as paths.
- `references/method/texture-and-variety.md`: texture as detail, same-value variety, optical gray, Color Dynamics.
- `references/method/palettes.md`: the wheel, the three ingredients, palette types as amounts of contrast.
- `references/method/temperature-saturation.md`: warm and cold groups, relative temperature, saturation layouts.
- `references/method/mistakes-checklist.md`: tests T1–T12 and the six problems, for critique and final review.
- `references/method/measurement.md`: OKLab and WCAG formulas, semantic-differential measures, Photoshop hue ranges, and default thresholds for the tests.
- `references/method/photoshop-techniques.md`: the teacher's Photoshop steps, with equivalents in other tools.
- `references/method/artist-references.md`: artist families and the films analysed, for mood boards.
- `references/method/science-crosswalk.md`: course claims checked against color science, with links.
- `references/course/README.md`: index of the 17 lessons and 4 unit files, with anchors.
- `references/course-1560/README.md`: source index for *Lighting Principles for Digital Painting*.
- `references/course-5642/README.md`: source index for unit 3, *Color applied to graphic design*.
- `references/course/Color Theory - reading copy.pdf`: the approved 299-page reading copy, with all figures in place.
- `references/course/pdf-index.md`: the PDF page for every section anchor, for opening the PDF at a given lesson.
- `scripts/checks.py`: measures an image for T1, T2, T5, T6 and T7, and computes WCAG contrast.
- `scripts/check_refs.py`: verifies every relative link and cited course anchor. Run it after editing any method file.
- `references/color-science/SKILL.md`: the color-science library's entry point.
