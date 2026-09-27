# Evolution Log — color-theory

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: real color plans and critiques made with this skill, plus any further color course added through `domestika-course-archive` export.

---

## Evolution 1 — 2026-09-26 — Birth: course method as the system, color-expert as the science layer

### Harvest scope
- **Classification: distilled.** The method comes from one course, Domestika 1140 *Color Theory: How to Apply It to Your Images*. Its confidence is borrowed, so the skill ships PENDING.
- **Sources:**
  - The course as a checked reading copy: 17 lessons and 432 frames, translated from the Spanish captions, reviewed and approved by Gary.
  - `meodai/skill.color-expert`, a collection of 148 color-science references with no method of its own.
- **Grounded:** read `core` (gates), `skill-builder` (skeleton, checklist, dogfood brief), `color-expert` (SKILL.md, INDEX.md, the harmony and temperature references), `domestika-course-archive` (the reading copy and the new export), and the sibling descriptions that mention color. The trigger ownership that `conductor`'s routing table gave to `color-expert` moves to this skill.

### Patterns found
1. **The existing color skill had facts but no method.** Impact H, Effort M. `color-expert` answers "what is OKLCH" but cannot take a brief to a palette. The course supplies the ordered method (intent → values → light → color plan → harmony → rhythm → temperature and saturation → variety → review) and the checks at each step.
2. **The method must stay traceable.** Impact H, Effort L. Every method claim cites a course anchor (course · unit · lesson · time range). `scripts/check_refs.py` verifies that each cited anchor exists in `references/course/`.
3. **The course and the science disagree in places.** Impact M, Effort L:
   - value measured in HSB rather than as perceptual lightness;
   - wheel distance used as a contrast measure;
   - temperature treated as a hue half rather than a joint shift of hue and saturation;
   - grayscale treated as a proxy for accessibility.

   These are recorded as corrections in `references/method/science-crosswalk.md`, not silently merged.
4. **Forum prompts leaked into the unit tasks.** Impact L, Effort L. The course export carried "share it on the forum" prompts inside the unit task paragraphs. This was fixed upstream in `domestika-course-archive`: sentence-level cleaning of the exported unit text, and 4 new rules.

### Hypotheses applied
1. `SKILL.md` carries the 9-stage flow, 8 principles, science routing, gates and anti-patterns. Depth lives in 13 `references/method/` digests.
2. `references/course/` holds the exported lessons, 4 unit files and frames. `references/color-science/` holds the git subtree, unchanged.
3. `references/method/science-crosswalk.md` gives an Agrees, Refines or Adds verdict per claim, with links into color-science.
4. The standalone `color-expert` install is unlinked, so this skill is the single entry point for color work.

### Validation results
- [x] `npx -y skills-ref@latest validate .` passes.
- [x] `scripts/check_refs.py`: 15 files, 267 anchors cited, 0 problems.
- [x] Fresh-context dogfood (2026-09-26). The tester (a) planned a "warm but lonely" night-market illustration, built a flat mock and ran the tests on it, (b) critiqued the mock with the checklist, and (c) built a 9-step OKLCH accent ramp with WCAG AA from step 600 up. The method caught a real flaw: the vendor's head sat at the lightness of her lit wall (OKLab L 0.565 against 0.613). Routing into color-science was clean.

  Findings, all folded in:
  - **[high] No way to measure outside Photoshop.** Added `scripts/checks.py` (T1, T2, T5, T6, T7 and WCAG contrast) and `references/method/measurement.md` (formulas, Photoshop hue ranges, default thresholds). The checklist now has a column for working without Photoshop.
  - **[high] T5 in HSB S mode inverts on dark scenes.** T5 now measures OKLCH chroma.
  - **[high] The library's only luminance formula, APCA's pure 2.4 gamma, inflates WCAG ratios by 10–16%.** The WCAG 2 formula is in `measurement.md`, with a warning.
  - **[high] Trigger collision with `color-expert`.** The local link had already been removed. The remaining copies are Gary's claude.ai account skill (`anthropic-skills:color-expert`) and can only be disabled in claude.ai. A `dataviz` hand-off was added to the "When it fires" section.
  - **[med] The restrained-palette caveat was missing from T6, and the stage numbering disagreed.** T6 now carries the caveat and the range numbers (30° core, 30° falloff, read from the L18 frames). Stage numbering is fixed. The quick path now includes a one-line value target, matching the Output Contract.
  - **[med] T3 breaks on flat graphic work.** T3 is now skipped for flat styles.
  - **[med] No step to re-check after a fix.** Added "re-run T1 and T5 after any fix".
  - **[med] No recipe for mixed feelings.** Added a "combining two feelings" rule, labelled as derived.
  - **[low] Other gaps.** T7 now has warm and cool hue bands. A frame-derived example is marked "(frame)". Reports must now say which tests were measured, judged by eye, or skipped.
  - **Not changed:** a minified JavaScript scrape inside the vendored `colorandcontrast` reference. That is an upstream issue, and the vendored library is not edited here.
- [x] The reading-copy PDF (299 pages, rebuilt with the current rules) is in `references/course/`, with `pdf-index.md` giving the page for all 191 section anchors. One entry was checked against the rendered page (1140 · U3 · L09 · 03:57–05:00 → page 121).
- [ ] Two real uses on Gary's own images or briefs, with the plan or critique checked against the result.
- [ ] Validate the distilled claims against real use. Any principle that fails in practice is revised or marked with its limits.
- This build is the worked example for `../skill-builder/references/distill-course.md`, which turns its steps into a playbook for further courses. `scripts/check_refs.py` here is a copy of the general `../skill-builder/scripts/check_refs.py`.
- **Verdict: PENDING**: distilled from one course, and not yet used on a real task.

---

## Evolution 2 — 2026-09-26 — Hand-offs only to owned skills

### Harvest scope
- **Trigger:** the design-skills programme (run 1, unit 0.1) requires every skill to run with any agent. Hand-offs go only to skills Gary owns, and no text names a tool that exists in one agent only.

### Hypotheses applied
1. The hand-offs to `dataviz` (built into one vendor's app) and to the third-party `design-taste-frontend`, `minimalist-ui` and `high-end-visual-design`, and the composition line naming `pptx`, `docx` and "the frontend skills", now state the boundary by artifact: interface style and chart choice belong to the skill that builds the deliverable, and this skill supplies the palette, ramps and contrast checks.
2. `references/course/pdf-index.md` no longer tells the reader to open pages "with the Read tool". The wording was fixed at its source, `domestika-course-archive/scripts/reading_copy.py`, and the course was re-exported; every other exported file came out byte-identical.

### Validation results
- [x] No match for `dataviz`, `design-taste-frontend`, `minimalist-ui`, `high-end-visual-design` or `Read tool` in `SKILL.md` or `pdf-index.md`.
- [x] `scripts/check_refs.py`: 267 anchors cited, 0 problems. `skills-ref validate` passes. Description 971 characters.
- **Verdict: PENDING**, unchanged: the skill has not yet been used on a real task.

---

## Evolution 3 — 2026-09-28 — Merge lighting and functional-colour courses

### Harvest scope
- **Classification: distilled.** Added two audited exports: Domestika 1560, *Lighting Principles for Digital Painting* (Samuel Smith), and unit 3 of Domestika 5642, *Specialization in Graphic Design and Visual Communication*.
- **Method claim:** course 1560 sequences exposure, source quality, local-color setup, ambient and secondary light, bounce and material cues (1560 · U2 · L06 · 00:08–01:48, 1560 · U2 · L06 · 01:49–04:41, 1560 · U2 · L07 · 03:25–05:24, 1560 · U3 · L13 · 06:30–07:57, 1560 · U4 · L14 · 05:08–05:58).
- **Method claim:** course 5642 groups graphic color into denotative, connotative and sign functions, with nine variables (5642 · U3 · L26 · 00:55–01:40, 5642 · U3 · L26 · 01:40–04:06, 5642 · U3 · L26 · 04:06–05:14).
- **Excluded:** 1560 U3 L08 was removed as blocked and is not cited; see `references/course-1560/BLOCKED.md`.

### Patterns found
1. **Lighting decisions need a usable order.** The added light pass links exposure and softness decisions to scene demonstrations and the existing 1140 reflection, temperature and light-coherence rules (1560 · U2 · L05 · 01:04–03:43, 1560 · U2 · L06 · 00:08–01:48, 1560 · U2 · L06 · 01:49–04:41, 1140 · U4 · L18 · 10:26–12:20).
2. **A graphic color's function precedes its hue family.** Course 5642 distinguishes representation, psychological or cultural evocation, and sign/coding functions; the categories can overlap (5642 · U3 · L26 · 00:55–01:40, 5642 · U3 · L26 · 09:10–10:58).
3. **The courses teach different wheel models.** 1140's screen-complement exercise uses RGB/CMY, while 5642's harmony unit teaches RYB primary, secondary and tertiary colors (1140 · U3 · L08 · 14:13–15:39, 5642 · U3 · L24 · 05:49–06:28). The distinction is explicit in `science-crosswalk.md`.
4. **Association tables carry a context limit.** Course 5642 calls yellow universally cheerful, then separately says psychological and symbolic readings are not universal; course 1140 also rejects fixed meanings (5642 · U3 · L33 · 11:31–18:00, 5642 · U3 · L31 · 07:34–08:45, 5642 · U3 · L32 · 09:05–10:00, 5642 · U3 · L32 · 10:00–10:52, 1140 · U2 · L04 · 04:17–05:30).
5. **The semantic differential has a scale but no pass threshold.** Course 5642 uses seven-point scales and audience profiles, but gives no required sample size or acceptance band; these are set by the brief in derived T10–T12 (5642 · U3 · L43 · 02:41–03:16, 5642 · U3 · L43 · 10:21–11:57).

### Hypotheses applied
1. Merge course 1560's scene-light decisions into `light.md`, with exposure and workflow notes in the related value, temperature and digital-painting digests.
2. Add `functional-color.md` for the nine-variable classification and family examples, with all meanings treated as hypotheses to test in context.
3. Add T10–T12 and formulas to measure semantic target fit, audience agreement and variant distinction; project owners set thresholds.
4. Extend the flow, course provenance, source coverage and science crosswalk while preserving the private-repository notice.

### Validation results
- [x] `python3 scripts/check_refs.py --sources 'references/course*/*.md'`: 17 files, 414 anchors cited, 616 known, 0 problems.
- [x] `python3 /Users/GaryT/Documents/Work/lab/design-programme/checks/check_coverage.py .`: 52 lessons, 52 covered (44 cited).
- [x] Required `grep` restriction check: exit 0, no matches.
- `npx -y skills-ref@latest validate .` is delegated to the coordinator, which has network access.
- No real design task was used to dogfood this merged method.
- **Verdict: PENDING** — the new method is distilled from course material and awaits real use.
