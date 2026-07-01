# Dogfood Brief — template

The fresh-context dogfood is a **hard gate** (SKILL.md; checklist step 6). A weak brief produces a weak dogfood — so brief the critic well. Spawn a *fresh-context* subagent (no prior knowledge of the work) and give it this shape:

## Brief shape (fill and hand to the agent)

> You are dogfooding a newly authored skill `<name>` (location: `<path>`). Your job: (a) actually **USE** it on a real task, (b) report as a **harsh, honest critic**. Do not praise it — the point is finding real gaps. You have fresh context; that's the point.
>
> **Read first:** `<path>/SKILL.md` + all its `references/`, and the kernel `../core/SKILL.md`.
>
> **Use it on a real task** (not a toy): <the concrete task — for a refine, audit a real artifact/skill; for a new skill, run its flow end-to-end on real inputs>. Produce the real artifacts as **evidence** you used it, not just read it.
>
> **Judge it as a skill:** triggering/disambiguation (does it fire right; collide with a sibling?), gaps (what did you NEED it didn't give — missing step/template/reference?), friction/contradiction/over-reach, whether each gate is actionable as written, cross-references resolve, honesty (does it overclaim?).
>
> **Do NOT modify skill files.** Scratch allowed under `<scratchpad path>`.
>
> **Deliverable:** (1) Evidence — terse, what you produced by using it; (2) Findings — ranked most-severe-first, each `[high/med/low] <defect> — <why it bit you> — <specific fix>`, 5–12 of them, including the single most important MISSING thing; (3) What genuinely worked — 2–4 bullets, only things that actually helped.

## Pass condition (state it before running)
The skill **passes** when: it fired on the right task without a sibling collision, every mandated gate was actionable, all cross-refs resolved, and no `high`-severity finding survives after fixes. `PENDING → KEEP` still needs ≥2 independent real uses (per `../core/references/evolution-loop.md`).

## After the run
Fold findings back into the skill; record the pass as an Evolution entry (verdict `PENDING`); re-run if any `high` finding required a structural change.
