# Evolution Log — core

The kernel's own loop. Mechanism: `references/evolution-loop.md`. Harvest source: how the role-skills that inherit core actually consume it — where inheritance reduces duplication, where a gate is too abstract to apply, where drift creeps in.

---

## Evolution 1 — 2026-07-01 — Extraction from dev; constellation wired to the kernel

### Harvest scope
- Not a usage harvest — the **extraction event**. The general spine (integrity, gate-by-artifact, Output Contract, grounding, pushback, approach, evolution loop, Wu Wei) was lifted out of `dev` (where it was fire-tested but coupled) once three non-dev consumers (BI, SA, ms-ai-discovery) needed it. `skill-builder` was then built on top. Classify: authored, from dev's proven practice — but core *as a standalone kernel* is unproven.

### Patterns found
1. **General discipline was trapped inside `dev`** — Impact: H, Effort: M. BI/SA/MS reached into `../dev/references/` for non-engineering rules; the third consumer was the measured trigger to extract. (Fixed: core created; non-dev skills repointed.)
2. **Two spine files now exist in both `dev` and `core`** — Impact: M, Effort: M. `wiki-protocol.md` and `pushback-and-teach.md` were copied byte-identical; `dev` was left unrepointed to avoid editing ~15 internal references in a fire-tested skill. **Known drift risk** — the clean end-state is migrating dev to reference core.
3. **KB-grounding was a dev-specific gate** — Impact: M, Effort: L. Generalized to a substrate-by-role Grounding Gate (KB / graded sources / internal docs) so every role can honor it. (Fixed: `references/grounding-gate.md`.)
4. **core shipped no EVOLUTION.md** — Impact: M, Effort: L. It told others to ship one and didn't. (Fixed: this file, added during the skill-builder dogfood pass.)

### Hypotheses applied
1. `SKILL.md` — the 9-point spine, "how a role-skill consumes core," provenance note. (Pattern 1.)
2. `references/wiki-protocol.md` + `pushback-and-teach.md` (canonical copies) + provenance note flagging the dev duplication. (Patterns 1, 2.)
3. `references/grounding-gate.md` — substrate-by-role + honesty corollary. (Pattern 3.)
4. `references/evolution-loop.md` — role-agnostic loop + PENDING discipline.
5. This `EVOLUTION.md`. (Pattern 4.)

### Open items / validation (fill after the constellation runs on real work)
- [ ] **Migrate `dev` to reference core** (retire the two duplicated files) — resolves Pattern 2. Deferred: high-touch on a fire-tested skill.
- [ ] Confirm the Grounding Gate's per-role substrate is actually recorded in real traces (dev/BI/SA).
- [ ] Confirm no gate is too abstract to apply in a role skill without re-deriving it.
- **Verdict: PENDING** — core is a same-day extraction; it earns `KEEP` once ≥2 skills demonstrably run on the kernel without re-deriving or duplicating it.
