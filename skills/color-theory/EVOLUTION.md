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
- [x] `scripts/check_refs.py`: 14 files, 262 anchors cited, 0 problems.
- [ ] Fresh-context dogfood on (a) a color plan from a brief and (b) a science question routed to color-science.
- [ ] Two real uses on Gary's own images or briefs, with the plan or critique checked against the result.
- [ ] Validate the distilled claims against real use. Any principle that fails in practice is revised or marked with its limits.
- **Verdict: PENDING**: distilled from one course, and not yet used on a real task.
