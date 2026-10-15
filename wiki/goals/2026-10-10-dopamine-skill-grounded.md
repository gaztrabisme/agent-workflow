# Grounded — dopamine/reward skill (run 2026-10-10-reward-skill)

## Request
Owner wants a skill for "hitting the dopamine release" in presentations, videos, UI and infographics: visual, auditory and other channels, sourced from research, with a buy-list of books and industry practice.
- Claim: a scientific method exists for triggering reward responses through media design.
- Context: owner already has `presentation`, `motion`, `visual-design`, `color-theory`, `information-design`, `ux`, `frontend` skills; none covers reward, anticipation, novelty, curiosity or sound design (grep of all SKILL.md files for dopamine/reward/engagement: no method hits).
- Implication: a new skill fits as a cross-medium layer that plans and critiques "reward beats" and hands rendering to the carrier skills.
- Missing: (1) whether "dopamine" framing is kept literally — the research meaning of dopamine is anticipation and prediction error, not pleasure, so a literal "release dopamine" skill would overclaim; (2) ethical line versus dark patterns; (3) standalone vs folded into existing skills; (4) buy-list format.

## Project state
- `skills.txt`: 28 skills; adding one requires folder + `skills.txt` line + `./install.sh` (AGENTS.md).
- skill-builder owns birth; distill path in `skills/skill-builder/references/distill-course.md`.
- Knowledge base (320 books): relevant hit only `storytelling-in-design` (Dahlström, ch. 4 emotional design, Schmid's eight positive-emotion factors). Most sources must come from the web.
- Lanes (subagent doctor, 2026-10-10): codex and bppc open; glm, deepseek, omlx, epi, bppc-lfm down.
- Uncommitted change in `skills/conductor/references/lane-plan.md` from a prior session: left untouched.

Grounded: request, sibling skills, skill-builder rules, KB coverage, lane status read; four missing items carried to the interview.

## Intent (2026-10-10)
| Question | Default | Owner answer |
|---|---|---|
| Name and literalness of "dopamine" | `reward-design`, "dopamine" as keyword, evidence tiers on every technique | skipped → default |
| Engaging vs manipulative line | teach dark patterns to recognise, never recommend | skipped → default |
| Standalone vs folded in | standalone, hands rendering to carrier skills, one-line pointers in siblings | skipped → default |
| Book list format | ranked `references/reading-list.md` + private page | skipped → default |
| Lanes | Claude subagents for research, Codex for check | **Owner: "You orchestrate Codex only."** All units on Codex. |
