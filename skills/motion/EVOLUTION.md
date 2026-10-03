# Evolution

## Evolution 1 — design run birth

- **Date:** 2026-10-02
- **Classification:** distilled course method.
- **Verdict:** PENDING. Do not change to KEEP until at least two independent real uses support the method.
- **Sources:** course 3762, *Animated Infographics with Illustrator and After Effects*; course 503, *Introduction to Motion Design and Animation Curves in After Effects*; course 433, *Storytelling for Animation and Motion Design*; course 561, *Creation of animated infographics*. Method claims are anchored in `references/method/`; unused lesson decisions are in `references/method/coverage.md`.
- **Grounded:** read `core` and its grounding, output and pushback references; read the `visual-design` and `color-theory` skill manuals and selected method references for staged digests, return-stage tests, measurement and code-first/vision-second reporting. Read all four course notes and `BLOCKED.md` files; opened the cited planning, premise, structure, storyboard, transition, animatic, curve, choreography, data-preservation, timing and animation-principle lesson sections. Read design decisions 2–7 and 16, `scene-engine/AGENTS.md` and SPEC §4, and `render-kit/AGENTS.md`.
- **Method shape:** six ordered stages, ten review tests, one measurement row per test; four courses supply method claims; no separate factual library is included.
- **Decisions:** keep storytelling and motion method in a new skill because no existing named skill owns the full ordered motion artifact; static chart choice, static composition and presentation artifacts hand off to their existing owners. Use scene-engine JSON and motion render; use render-kit for editable HTML/SVG visual assets and selected-frame checks. Keep course example durations as examples rather than defaults. Treat the 503 movement-system guidance and 561 decorative-motion guidance as distinct cases, resolved by the brief's purpose and reading needs.
- **Validation:** source-anchor, coverage, prohibited-name and official format checks are recorded in `DISTILL-REPORT.md`. No real-use dogfood or independent claim audit has been completed in this birth run; this is an open follow-up and the verdict stays PENDING.
- **Later-use signal:** in two independent real tasks, a fresh reviewer can explain the intended message and motion, and the full code/render/vision loop catches issues at the stage assigned by the checklist.
- **Open questions:** test whether the six-stage order works on a non-narrative interface animation and whether its source-ledger/data-preservation steps are appropriately scoped for non-infographic work.

## Evolution 2 — design run dogfood (2026-10-02)

### Harvest scope
- **Grounded:** dogfood report `/Users/GaryT/Documents/Work/lab/design-programme/dogfood/runs-3-5/motion/report.md` and its Larkspur-4 motion artifacts → confirmed that storyboard-model checks could pass while rendered MP4 motion/captions were wrong; identified missing narration, SVG, measurement and reviewer hand-off procedures.
- **Coverage:** one end-to-end, 57.5-second narrated explainer using scene-engine's fallback renderer; measured values, caption rates, panel holds, cut-offs and key frames were available. HyperFrames full render, engine npm tests/selftest and independent vision answers were unavailable.
- **Evidence limits:** this is one dogfood use and does not settle the birth entry's two-use floor. The review answers were not completed; renderer capability findings were handed to scene-engine/render-kit owners and are not claimed as tool fixes here.
- **Evidence class:** exercise.

### Settled verdicts
| Prior item | Verdict | Evidence and reason |
|---|---|---|
| Evolution 1 — design run birth | PENDING | One dogfood run exercised the stages but does not meet the two independent-use floor; the new changes also need later use. |

### Patterns found
Ranked by impact and effort; findings are recorded in the linked dogfood report.
1. **Rendered evidence gap** — Impact: H; Effort: M. F1 showed that storyboard check frames did not prove that motion or captions reached the MP4; F10 showed that repeated measurement checks had no shipped tool.
2. **Engine capability gaps need usable boundaries** — Impact: H; Effort: M. F2–F8 and F14 exposed renderer/schema gaps that need explicit skill-side workarounds while the engine owner addresses them.
3. **Production and reviewer hand-offs need concrete recipes** — Impact: M; Effort: M. F5, F9, F11–F13 and F15 exposed missing audio, asset, review, reference and residual guidance.

### Hypotheses applied
1. **Stage 6 rendered-output proof and current engine pointer — `SKILL.md` / `references/method/review-and-handoff.md`** — add MP4-to-check-frame comparison and direct readers to scene-engine's capability table; closes F1. Approved by the user's explicit request.
2. **Scene-engine v1 workaround notes — `SKILL.md` / `references/method/choreography.md`** — record the panel, track, unsupported-feature, renderer, caption, output-path and check-time workarounds; closes F2–F4, F6–F8 and F14. Approved by the user's explicit request.
3. **Narration and scene-engine artwork procedures — `references/method/storyboard-and-animatic.md`** — add measured one-clip-per-cue narration and standalone SVG checks; closes F5 and F9. Approved by the user's explicit request.
4. **Reusable measurements — `scripts/measure_storyboard.py`, `tests/test_measure_storyboard.py`, `references/method/measurement.md`** — ship proportions, caption-rate, hold, cutoff and frame checks with unit tests; closes F10. Approved by the user's explicit request.
5. **Motion review packet recipe — `references/method/review-and-handoff.md`, `references/method/review-checklist.md`** — require a contact sheet, clip path and playback labels, plus render-kit limitations; closes F11 and F13. Approved by the user's explicit request.
6. **Verified sibling routing and residual note — `SKILL.md`, `references/method/choreography.md`** — link the existing presentation skill, record the exact reference-check command and describe cosmetic leftovers; closes F12 and F15. Approved by the user's explicit request.

### Validation plan
| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| F1/F10 measurement loop | Later projects compare all MP4 check-time frames, report configured proportions and catch injected content differences without mistaking model checks for render proof. | Two independent motion tasks; metric output plus a fresh reviewer for playback questions. | exercise or natural | Motion skill owner | 2026-12-02 | PENDING |
| F2–F9/F14 capability, narration and asset notes | Workarounds accurately describe the current engine/render-kit behavior and are used where relevant until owners update their capability records. | Two independent motion tasks spanning narration/assets and at least one affected engine workaround. | exercise or natural | Motion skill owner | 2026-12-02 | PENDING |
| F11–F13/F15 reviewer, reference and residual notes | Reviewers receive frames and an accessible clip for playback questions; package checks pass; remaining visual limitations are not reported as fixes. | Two independent motion tasks with a fresh reviewer; record opened checklist sections and any friction. | exercise or natural | Motion skill owner | 2026-12-02 | PENDING |

**Verdict: PENDING** — the skill changes are applied, but one dogfood run and no independent vision review do not meet the two-use evidence floor. Revisit after two independent tasks or on 2026-12-02, whichever comes first.
