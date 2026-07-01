# Skill Authoring Checklist

Run top to bottom for a new skill; jump to the relevant steps for a refine. Each step is gate-by-artifact — name what you produced.

## 1. Decide it should exist
- [ ] The competency recurs, has its own trigger, and isn't already a sibling. (Else: add a reference to an existing skill instead.)
- [ ] If extracting shared machinery: there are **≥3 consumers** needing it (the measured trigger, per how `core` was extracted).
- [ ] Classify: **authored** (from your fire-tested practice) or **distilled** (from docs/methodology). Consequence: a **distilled** skill ships `PENDING` *and* its EVOLUTION validation list must include "validate the distilled claims against real use" — it cannot reach `KEEP` on internal consistency alone (borrowed confidence ≠ evidence).

## 2. Ground in what exists
- [ ] Read `../core/SKILL.md` + the sibling skills the new one touches.
- [ ] Record `Grounded: read core + <siblings> → <conventions/refs reused>`.
- [ ] Confirm you're **referencing** the spine (`../core/references/…`), not about to copy it.

## 3. Write the frontmatter (trigger contract)
- [ ] `name` matches the directory.
- [ ] `description` = what-it-is + `USE WHEN <situations>` + `Keywords: <typed terms>` + disambiguation vs any overlapping sibling. Mind the char budget — USE WHEN + Keywords are the retrieval surface; don't spend it on prose.
- [ ] **Sibling-collision check:** grep sibling descriptions for the same trigger verbs; if two skills would fire on the same turn, one *must* carry a disambiguation clause (this is how `skill-builder` and `core` were split — both once said "authoring a skill").
- [ ] Sanity: would this fire on the right turn and *not* collide with a sibling's trigger?

## 4. Write SKILL.md (the shape)
- [ ] Start from `references/templates/SKILL.md.skeleton` — fill the canonical headers rather than inventing your own (keeps the constellation greppable by section).
- [ ] Identity · when-it-fires-&-sibling-hand-offs · principles · flow-at-a-glance · gates (declared, pointing at `core`) · anti-patterns · composition · references.
- [ ] Disambiguate every trigger overlap on **artifact + audience**.
- [ ] Each reference/template you list actually exists and is pointed at (no orphans).

## 5. Declare the gates in the skill's terms
- [ ] Grounding gate (name the skill's substrate) → `../core/references/grounding-gate.md`.
- [ ] Output Contract / primary artifacts → `../core/references/wiki-protocol.md`.
- [ ] Pushback-and-teach → `../core/references/pushback-and-teach.md`.
- [ ] Approach declaration (mark skippable for single-actor work if apt). (core SKILL.md §7 — no separate reference file; this is intentional, not a missing link.)
- [ ] **Reference-don't-duplicate test:** grep the new skill for canonical gate prose (e.g. body text of `wiki-protocol`/`pushback-and-teach`/`grounding-gate`). Present as prose = you copied; assert *links*, not copies. (The cardinal sin; `dev` currently duplicates two spine files — the known exception, flagged in `core`'s provenance note.)

## 6. Dogfood with a fresh-context subagent (non-negotiable)
- [ ] Brief the agent with `references/templates/dogfood-brief.md` (defines fresh-context setup, the real task, what to judge, the **pass condition**, and where evidence is written) — don't improvise the brief; a thin brief yields a thin dogfood.
- [ ] Spawn a fresh agent; tell it to **use** the skill on a *real* task (not read it), producing real artifacts as evidence.
- [ ] Instruct it to report as a **harsh critic**: gaps, friction, contradictions, trigger ambiguity, broken cross-refs, over-reach — ranked, with the most important *missing* thing called out.
- [ ] Fold the findings back into the skill.
- [ ] Confirm every cross-reference resolves (grep the `../core/…` and sibling paths).

## 7. Wire into the constellation
- [ ] Add forward/back cross-links in the sibling skills so the pipeline reads from any entry point.
- [ ] Update this skill-builder's own references if a new convention emerged.

## 8. Ship + record
- [ ] `git init` (each skill is its own repo); `.gitignore` (`.DS_Store`).
- [ ] `EVOLUTION.md` with birth + the dogfood pass, from `references/templates/EVOLUTION.md.skeleton` (shape defined in `../core/references/evolution-loop.md`); **verdict `PENDING`** until ≥2 independent real uses → `KEEP`.
- [ ] Commit with a clear message.

## Refine (existing skill) — minimal path
- Steps 2 (ground), 6 (dogfood), 8 (record the evolution entry, keep verdict honest). Never let a refine skip the EVOLUTION entry — that's the shared-memory Output Contract for skills.
- **Substitution rule:** a real-use trace may stand in for a fresh-context dogfood **only when the change is reversible and fails loud** (core gate 3 — a planned gate skipped silently is an integrity miss). Irreversible or silent-when-wrong changes (a new gate, a trigger change, a distilled skill) require the full dogfood.
