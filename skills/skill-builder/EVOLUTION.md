# Evolution Log — skill-builder

The loop that turns real skill-authoring into improvements to this meta-skill. Mechanism: `../evolution/references/loop.md`. Harvest source: skills authored/refined with it + their later EVOLUTION verdicts + dogfood runs.

---

## Evolution 1 — 2026-07-01 — Birth + first dogfood

### Harvest scope
- A fresh-context Opus subagent (~65k tokens) ran **both paths skill-builder claims to support**: a construction audit of `solution-architect` (REFINE) and an end-to-end checklist walk to author a hypothetical `presale-deck` skill (AUTHOR). Classify: **authored** (from the practice of building the constellation), verdict still `PENDING`.
- Representative because it exercised the two real use cases and, critically, tried to *build to the skill's own standard* — surfacing where the builder isn't built to it.

### Patterns found
Ranked, with the proof each bit:
1. **skill-builder (and core) shipped no `EVOLUTION.md` — the builder violated its own non-negotiable gate** — Impact: H, Effort: L. The dogfood *was* checklist step 6, and there was nowhere to record it. A "disciplined by construction" skill that isn't itself so constructed undercuts its authority.
2. **No disambiguation vs `core`, despite an identical trigger** — Impact: H, Effort: L. core's description said `USE WHEN authoring or refining a skill` — byte-identical to skill-builder — and skill-builder's own frontmatter contract *requires* a disambiguation line for sibling overlaps. Both would fire on "make me a skill."
3. **No SKILL.md skeleton to fill (the biggest gap)** — Impact: H, Effort: L. Step 4 listed 8 section names in prose but shipped no template; the agent reverse-engineered structure from an existing skill, and every skill invents its own headers (not greppable).
4. **The dogfood gate under-briefed the briefer** — Impact: M, Effort: L. Step 6 said what the critic does, not how to brief it (fresh-context how, artifacts to hand it, evidence location, pass condition). The brief the agent received was ~5× richer than step 6.
5. **skill-builder never linked `../evolution/references/loop.md`** — Impact: M, Effort: L. It mandated EVOLUTION.md but never pointed at the file defining its shape.
6. **Checklist step 5 linked 3 core gates, silently dropped the 4th (Approach)** — Impact: M, Effort: L. Correct-but-suspicious asymmetry (approach has no separate reference).
7. **"Reference, don't duplicate" had no checkable test** — Impact: M, Effort: L. The "cardinal sin" with no detector — and `dev` already duplicates the two spine files with nothing flagging it.
8. **Refine path softens "non-negotiable" dogfood to "or a real-use trace" with no rule for when** — Impact: L, Effort: L.
9. **No description length/format budget guidance** — Impact: L, Effort: L.
10. **"distill vs author" classification had no downstream mechanical consequence** — Impact: L, Effort: L.

### Hypotheses applied
1. Created **`EVOLUTION.md`** (this file) + **`core/EVOLUTION.md`**. (Pattern 1.)
2. Added a **`vs core` disambiguation** to skill-builder's description and **narrowed core's `USE WHEN`** to drop "authoring or refining a skill." (Pattern 2.)
3. Added **`references/templates/SKILL.md.skeleton`** with canonical headers; checklist step 4 points at it. (Pattern 3.)
4. Added **`references/templates/dogfood-brief.md`** with pass condition + evidence location; step 6 and the SKILL.md dogfood bullet point at it. (Pattern 4.)
5. Cited **`../evolution/references/loop.md`** in step 8 + References; added **`EVOLUTION.md.skeleton`**. (Pattern 5.)
6. Step 5 now annotates Approach as "(core SKILL.md §7 — no separate reference)." (Pattern 6.)
7. Added a checklist test: **grep the new skill for canonical gate prose; assert links, not copies.** (Pattern 7.)
8. Refine path now states the substitution rule: real-use trace may replace a fresh dogfood **only when the change is reversible and fails loud** (core gate 3). (Pattern 8.)
9. Step 3 notes the description budget. (Pattern 9.)
10. Distilled skills now carry an extra validation requirement before `KEEP`. (Pattern 10.)

Not modified (validated as genuinely strong): the "when to build / when NOT" decision test, the frontmatter trigger-contract spec, the grounding-gate-for-authoring step. The dogfood confirmed `solution-architect` passes every construction gate — the standard itself is sound.

### Validation results (fill after ≥2 more skills are built/refined with it)
- [ ] A new skill authored from the SKILL.md.skeleton ships with canonical, greppable headers.
- [ ] A dogfood run driven by dogfood-brief.md (not an ad-hoc brief) produces a strong critique.
- [ ] The "reference-don't-duplicate" grep test catches a real copy (or confirms none).
- **Verdict: PENDING** — all fixes from a single dogfood; needs real authoring cycles to confirm the templates and gates hold.
