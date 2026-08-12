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

---

## Evolution 2 — 2026-08-12 — the skill that builds skills is almost never in the room

First harvest by the `evolution` loop. Window: since Evolution 1 (2026-07-01) — the oldest
unsettled ledger in the constellation.

### Harvest scope

All 8 commits in the repo (full diffs for the 6 in-window); the skill's own files; and the
sharpest available substrate — **its products**. Every skill born or majorly revised in the
window was read for whether skill-builder's prescribed shape was actually followed:
`media-gen` (07-05), `delivery` + `solution-architect` (07-27), `omlx` (07-30), `gsheets`
(08-02), `harness-operator` (08-03), `conductor` (08-06), `zalo-platform` (08-06),
`evolution` (08-09), `ai-discovery-workshop` (08-10). Plus `read-once` (13,120 events, both
path arms), `history.jsonl`, six transcripts streamed and filtered, and live `gh` state on 11
public repos.

### Patterns found

1. **2 invocations, 10 skills born** — Impact: H, Effort: M. The `zalo-platform` build session
   opens with *"I need to build a skill that is a specialist in Zalo OA/Miniapp"* and mentions
   skill-builder **zero times**. The `omlx` build was entered as `/dev` and only reached this
   skill because the agent went and read it 15 seconds later.
2. **Every structural deviation in a newborn skill is a skill-builder no-show** — Impact: H,
   Effort: L. The three skills missing a `## Gates` section (`conductor`, `harness-operator`,
   `ai-discovery-workshop`) are exactly the three with no skill-builder file read.
   `conductor/EVOLUTION.md:93` says it out loud: *"The dogfood gate has not been run.
   `skill-builder` calls it non-negotiable."*
3. **`references/publishing.md` has zero reads, zero mentions, and its central rule was
   violated at the next publish event** — Impact: H, Effort: L. 10 repos went public
   2026-08-10; only 2 were scrubbed; the scrubs used per-skill denylists rather than the
   shared `all-skills.scrub-denylist` that §7 mandates and that exists; and two public repos
   carry an unscanned branch. **No leak shipped** — the harvest cloned that branch and scanned
   every tracked file in all 11 repos and they are clean. The gate didn't run; the outcome
   held anyway, which is the least useful kind of pass.
4. **Two public repos have no LICENSE** — Impact: M, Effort: L. `ai-discovery-workshop` and
   `drawio-skill`: no `license:` in frontmatter, `contents/LICENSE` → 404 on both, against
   `SKILL.md:60` which calls a public repo with no licence all-rights-reserved and unreusable.
   All nine others have both.
5. **The dogfood gate has no fallback rung, so it gets dropped whole rather than deferred as
   debt** — Impact: M, Effort: L. `gsheets/EVOLUTION.md:68` (*"subagent use was disallowed in
   the authoring session"*) and `conductor/EVOLUTION.md:93`. Both shipped with the
   non-negotiable open, recorded only in their own ledgers, where skill-builder never looks.
   Carried forward from the 2026-08-09 critic's H1, still unapplied.
6. **A completed harvest of this skill was never recorded here** — Impact: M, Effort: L. See
   the recovered block below.
7. **Falsified claim on disk** — Impact: L, Effort: L. `authoring-checklist.md:32` said `dev`
   duplicates two spine files. `ls dev/references/` → four files, neither of them a spine copy.
8. **A snapshot copy of the constellation poisons every prescribed constellation-wide grep** —
   Impact: L, Effort: L. `claude-skills-used-2026-07-31/` is an untracked duplicate tree;
   the reference-don't-duplicate test returns ~2× hits, every second one a snapshot path.

### Hypotheses applied

- **H4** — description rewritten to claim the moment a skill is actually born (*before writing
  a SKILL.md by hand*), plus reusability and publish triggers (`SKILL.md` frontmatter).
  Closes 1, and is the upstream cause of 2 and 3.
- **Folded correction** — `authoring-checklist.md`'s `dev` exception removed (falsified), and
  the snapshot-tree trap named at the point where the grep is prescribed. Closes 7 and 8.

**Not applied, named so they are not lost:** 3, 4, 5, 6. Items 3 and 4 are partly *actions on
repos* rather than skill edits and were surfaced to the operator directly. Item 5 is the
second run in a row this has been proposed and not applied — it should lead next time.

### Recovered: the five hypotheses from the 2026-08-09 dogfood

`evolution/EVOLUTION.md:52` carried the open box *"the five `skill-builder` hypotheses the
dogfood produced are presented and dispositioned"*. They were at the approval gate and were
never written down here. Recovered from the transcript and recorded now, unapplied:

| # | Hypothesis |
|---|---|
| H1 | A fallback rung for the dogfood gate, so it defers as debt instead of vanishing |
| H2 | Delete `SKILL.md.skeleton` — its content is duplicated inline in SKILL.md's "the shape that works" |
| H3 | The publishing gate is unreachable from where a builder actually is |
| H4 | Add `scripts/refcheck.py` to mechanize the cross-reference check |
| H5 | The stale `dev` duplication exception (**applied this run** — see above) |

A harvest whose only output lands in a sibling's ledger did not close. That is now fixed for
this one; the lesson is the general case.

### Validation results (settling Evolution 1)

- **A skill authored from `SKILL.md.skeleton` carries canonical, greppable headers** →
  **REVISED**. The outcome holds wherever the file was opened: 4 sessions ever
  (`media-gen`, `omlx`, `gsheets`, `evolution`), and all four carry the seven headers
  verbatim. Of the four post-skeleton skills born *without* opening it, three lack a Gates
  section entirely. Counter-evidence in the other direction: `zalo-platform` conforms without
  ever touching skill-builder, so the convention also spreads by sibling imitation. The
  machinery works; its *reach* was over-claimed. New selector should name how a builder
  arrives at the shape, not assume the file does it. Inherits `PENDING`.
- **A dogfood run driven by `dogfood-brief.md` produces a strong critique** → **KEEP**.
  Three independent brief-named runs, each of which changed its skill: `omlx/EVOLUTION.md:75`,
  `omlx/EVOLUTION.md:149` (falsified three shipped claims), and `evolution/EVOLUTION.md:13`
  (12 findings, including a false statistic in `loop.md`'s central argument and two real bugs
  in `triage.py`). Comfortably ≥2 independent uses. **The constellation's first `KEEP` settled
  by the `evolution` loop.**
- **The reference-don't-duplicate grep test catches a real copy, or confirms none** →
  **PENDING** (never exercised in any authoring trace — `authoring-checklist.md` has been
  opened in 4 sessions total and in none of the eight in-window births). Run manually during
  this harvest: one live hit outside `core/` — `dev/SKILL.md` restates core §2 in expanded
  prose. Unsettled because nobody ran the gate, not because it failed.
- **Entry-level verdict** → **PENDING**. Two invocations by count, but one of them
  (`gsheets`) records its own central gate being skipped: *"the fresh-context dogfood required
  by `skill-builder` has not been run"*. An entry cannot reach `KEEP` on a pair where one use
  documents the non-negotiable being waived.

New, for a later run:

- [ ] A skill is born *through* this skill rather than beside it — the direct test of H4.
- [ ] The dogfood fallback rung, third time of asking.
- [ ] Whether the two unlicensed public repos got licences.

**Verdict: PENDING.** One `KEEP` settled, one `REVISED`, and a description change whose whole
purpose is to fix the reason everything else here went unmeasured. The honest summary: this
skill's content is in good shape and its *retrieval* is not, and no amount of content work
fixes a skill that isn't invoked when a skill is being built.
