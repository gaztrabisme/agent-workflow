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
