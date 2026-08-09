---
name: skill-builder
description: "Author or refine an agent skill so it inherits the shared spine and earns its place in the constellation. USE WHEN creating a new skill, splitting/merging skills, distilling a methodology or documents into a skill, or fixing an existing one's structure (frontmatter, references, templates, gates, wiring, publishing). Bakes in the core kernel so every skill built is disciplined by construction. Not `core` — that's the kernel a skill *references*; this is the authoring *workflow* that produces skills. Not `evolution` — lessons from a *completed engagement or real traces* go there; distilling *documents/methodology* into structure is here. Keywords: skill, agent skill, build a skill, author skill, skill design, SKILL.md, frontmatter, distill, dogfood, publish skill, scrub, compose skills, split skill."
---

# Skill-builder

Build skills that are **disciplined by construction** and **compose** rather than sprawl. Every skill authored here inherits the `core` spine, ships with an evolution loop, and is fire-tested before it's trusted.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## When to build a skill (and when not)

**Build one when:** a competency recurs, has its own trigger, and is currently either improvised each time or awkwardly wedged into another skill. A third consumer needing the same machinery is the measured trigger to *extract* (as `core` was extracted once dev, BI, SA, MS all needed the spine).

**Don't build one when:** it's a one-off, it duplicates an existing skill's trigger, or it's really a *reference* inside an existing skill. Prefer adding a reference to an existing skill over spawning a near-synonym. Skills earn existence by being referenced (Wu Wei).

**Distill vs author:** a skill *distilled from documents/methodology* (like `ms-ai-discovery`, `solution-architect`) carries borrowed confidence — it ships at verdict `PENDING` and must be fire-tested. A skill *authored from your own fire-tested practice* (like `dev`) is stronger but still runs the loop.

## Anatomy of a good skill

```
<skill>/
├── SKILL.md              # operating manual: identity, when-it-fires, principles, flow, gates, anti-patterns, references
├── references/           # tight digests — each earns its place by being referenced from SKILL.md
├── references/templates/ # fill-in artifacts the skill produces (optional)
├── EVOLUTION.md          # the loop's ledger; verdict PENDING until fire-tested
└── .gitignore            # each skill is its OWN git repo (.DS_Store etc.)
```

### Frontmatter — the trigger contract
`name` + `description`. The description is a **retrieval and disambiguation** surface, not marketing. It must contain:
- one line of *what it is*,
- a **`USE WHEN`** clause naming the concrete situations it fires on,
- **`Keywords:`** the terms a user would actually type,
- and, when it overlaps a sibling, a one-line **disambiguation** ("… vs `X` which does Y").

Anti-pattern: a vague description → the skill never fires, or fires on the wrong turn.

### SKILL.md body — the shape that works
1. **Identity** — what buildable/sellable/knowable thing it produces, in one paragraph.
2. **When it fires — and when a sibling owns it** — explicit hand-offs; kill trigger collisions on *artifact + audience*.
3. **Principles / anchoring rules** — the load-bearing judgments, opinionated.
4. **The flow** — phases/modes at a glance (a table), scaled to the task; point to references for depth.
5. **Gates** — declare the `core` gates in this skill's terms (grounding, output-contract, pushback, approach). Reference `../core/references/…`.
6. **Anti-patterns** — the hard no-list.
7. **Composition** — what it consumes / hands off to; where it sits in the pipeline.
8. **References** — each with a one-line purpose.

## The build gates (this skill's own flow)

- **Grounding.** Before authoring, read `core` and the sibling skills the new one will touch — ground conventions in what exists, don't reinvent. Record `Grounded: read core + <siblings> → <what you reused>`. See `../core/references/grounding-gate.md`.
- **Reference, don't duplicate.** The spine lives in `core`. Copying `wiki-protocol`/`pushback`/gates into a new skill is the cardinal sin — reference them. New content only for what's genuinely unique to the skill.
- **Compose, don't merge.** Keep skills narrow and well-triggered; wire them via cross-links and hand-offs. A mega-skill triggers on everything and disambiguates nothing.
- **Dogfood before trust (Output Contract).** A skill is not done when written — it's done when a **fresh-context subagent has used it on a real task** and its findings are folded back. Brief the critic with `references/templates/dogfood-brief.md` (it also defines the *pass condition* and where evidence goes — a thin brief yields a thin dogfood); have it *use* the skill (not just read it); apply the fixes; record the pass in `EVOLUTION.md` at verdict `PENDING`. (This is `references/authoring-checklist.md` step 6, and it's non-negotiable — it's the gate-by-artifact rule applied to skills.)
- **Spec validation.** Run the official validator before calling a skill done — it catches what a human read misses (unquoted `description:` containing colons silently breaks the frontmatter, and the skill then loads wrong or not at all):
  ```bash
  npx -y skills-ref@latest validate <skill-path>
  ```
  Conform to the [Agent Skills spec](https://agentskills.io/specification): `name` matches the directory, `description` ≤1024 chars with `USE WHEN` + keywords, SKILL.md under ~500 lines, and declare `license` in frontmatter for anything public — a public repo with no license is all-rights-reserved and cannot be reused.
- **Own repo + EVOLUTION.md.** `git init` the skill; ship `EVOLUTION.md` with the birth + first dogfood recorded, verdict `PENDING` until ≥2 real uses.
- **Scrub gate (only when publishing publicly).** A skill authored inside real work carries the client detail that made it good. Before any public push: generalize identifiers to *shapes*, sever any reference to private traces, run `scripts/scrub_check.py --history`, and **verify by cloning the published repo and re-scanning it**. A clean working tree above a dirty history publishes the dirty history. Full procedure: `references/publishing.md`.

## Anti-patterns (hard no-list)
- Duplicating `core` instead of referencing it.
- Mega-skill / trigger collision with a sibling (no disambiguation).
- Marketing-prose description with no `USE WHEN` / keywords → never fires.
- Shipping a distilled skill as `KEEP` without fire-testing (borrowed confidence ≠ evidence).
- No `EVOLUTION.md` / no dogfood → the skill can never learn or be trusted.
- Speculative references/templates that nothing points at.

## Composition
- **Inherits:** `core` (spine, gates, evolution loop, wiki protocol).
- **Peers it builds/refines:** `dev`, `business-intelligence`, `solution-architect`, `ms-ai-discovery`, and future role-skills.
- **Its harvest:** the skills it authored + their later EVOLUTION verdicts → convention/checklist edits here.

## References
- `references/authoring-checklist.md` — the step-by-step build/refine checklist, including the fresh-context dogfood.
- `references/templates/SKILL.md.skeleton` — canonical section headers to fill (keeps the constellation greppable by section).
- `../evolution/references/templates/EVOLUTION.md.skeleton` — the evolution-ledger a new skill ships with. Lives in the `evolution` skill, which owns the ledger's shape and the loop behind it.
- `references/templates/dogfood-brief.md` — the fresh-context critic brief + pass condition + evidence location.
- `references/publishing.md` — the gate between "the skill works" and "the skill is public": generalization, the no-linkage rule, denylist construction, orphan-branch history, verify-from-a-clean-clone.
- `scripts/scrub_check.py` — the denylist gate itself; reads a per-skill `.scrub-denylist`, scans the working tree and (with `--history`) every blob in git history.
