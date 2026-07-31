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
- [x] **Migrate `dev` to reference core** (retire the two duplicated files) — resolves Pattern 2. **Done 2026-07-01:** repointed 21 references across SKILL/CLAUDE/6 modes/subagent-briefs/EVOLUTION, deleted dev's copies. Single canonical home; drift risk closed.
- [ ] Confirm the Grounding Gate's per-role substrate is actually recorded in real traces (dev/BI/SA).
- [ ] Confirm no gate is too abstract to apply in a role skill without re-deriving it.
- **Verdict: PENDING** — core is a same-day extraction; it earns `KEEP` once ≥2 skills demonstrably run on the kernel without re-deriving or duplicating it.

---

## Evolution 2 — 2026-07-29 — Channel boundaries, structural tiering, and the cold-review gate

### Harvest scope

Harvested from a single `solution-architect` engagement (see that skill's Evolution 4), but every pattern below is a **kernel** defect: the failing rule lives in `core` and is
inherited unchanged by every role-skill. Nothing here is presale-specific.

### Patterns found

1. **`pushback-and-teach.md` has no channel boundary — H/L.** The file opens by describing a single
   developer learning through his own codebase, and mandates WHY-narration on every mode. Correct in a
   chat window. But four role-skills inherit it verbatim while producing artifacts for *external* readers,
   and nothing scopes the mandate — so justification migrates into the deliverable. Measured on the trace:
   cells of ≥12 words ran at **21%** in the rejected artifact and **0.49%** in the practitioner's adopted
   replacement, with adoption tracking that column monotonically. The engagement owner's own diagnosis was
   *"too many proses, narratives, and showing someone insecure trying too hard to justify and prove
   themselves"* — and a client-bound scope document literally contained the sentence *"This is a
   disclosure, not a hedge,"* an argument with a critic who had not spoken.
2. **The grounding gate's honesty corollary is a prose rule, and prose rules fail silently at scale —
   M-H/L.** Values reported by research subagents were written into artifacts using the word *"measured"*;
   the underlying files had never been downloaded. *"A claim you cannot ground, you do not make"* was
   present, correct, and did not fire. The project then authored a **schema-level** fix on its own —
   `*_reported` columns plus the asserted invariant *"no row carries a `page_count` without a `sha256`"* —
   which is stronger than the rule it repairs. Harvested upward.
3. **Wu Wei was scoped to skill structure, not to engagement output — M/L.** §9 governs pages, references
   and gates earning their place. Nothing extended it to the artifacts a skill *produces*, so an
   engagement asked for two deliverables and received 11 documents totalling 22,400 words. Volume is not
   merely noise: it defeated that engagement's cross-artifact integrity checks, whose reconciliation cost
   grows with the square of the artifact count.
4. **The highest-yield instrument in the trace was undocumented — H/L.** A cold review — weaknesses
   pre-registered, then a reviewer given **no prior context** verifying against the source of record —
   found all five pre-registered weaknesses plus roughly fifteen more, two of them deal-losing. It is
   already de-facto practice in `dev` and referenced loosely elsewhere, but was never stated as a gate.

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | New **"Two channels"** section: the WHY lives in the conversation and in `decisions.md`, never inside a deliverable; a handoff artifact carries the conclusion plus a reference token; ≤1 prose cell (≥12 words) per 100 non-empty cells; anti-pattern for pre-emptive self-defence in a deliverable. **Additive and scoping — removes no teaching obligation, and explicitly exempts internal design specs, so `dev` behaviour is unchanged.** | `references/pushback-and-teach.md` | 1 |
| 2 | New **"Tier in the schema, not the prose"**: `*_reported` fields, an invariant a script can assert, grading in a column rather than a footnote. | `references/grounding-gate.md` | 2 |
| 3 | §9 Wu Wei extended — *"this binds engagement artifacts as well as skill structure: a document nobody asked for, that no decision depends on, is cost wearing the costume of thoroughness."* | `SKILL.md` | 3 |
| 4 | New spine item **#10 — cold review before a primary artifact ships.** Pre-register expected weaknesses; reviewer gets no prior context and verifies against the source of record, not against sibling artifacts that agree because one author wrote them. Scale to stakes. | `SKILL.md` | 4 |

### Validation (fill on the next independent use, in any role)

- [ ] A deliverable ships with its justification in `decisions.md` and a reference token in the artifact, and the recipient does not ask for the reasoning back.
- [ ] A tabular artifact carries provenance structurally (`*_reported` or a tier column) with at least one asserted invariant.
- [ ] An artifact set stays inside what was asked for, or the excess was proposed and accepted first.
- [ ] A cold review runs on a primary artifact and is scored against pre-registered weaknesses.
- [ ] `dev`'s behaviour is measurably unchanged by hypothesis 1 — this is the blast-radius check, and if `dev` starts under-explaining in conversation, the scoping was written too broadly.
- **Verdict: `PENDING`.** One trace, one role. Hypothesis 1 is the highest-risk of the four: it narrows a
  rule that has been fire-tested in `dev` for far longer than this evolution has existed, and the failure
  mode to watch for is a skill that stops teaching rather than one that stops teaching *in the wrong place*.

---

## Evolution 3 — 2026-07-30 — Prose rules fail silently: the third sighting

### Harvest scope

**One presale engagement, the day after Evolution 2 was written on it.** Not an independent trace. Its value
is a specific one: Evolution 2 authored *"Tier in the schema, not the prose"* on the observation that a prose
integrity rule was *"present, correct, and did not fire."* Within 24 hours the **same mechanism fired twice
more, in two different kernel rules**, on the same engagement, with the same author. Three sightings of one
failure mode is no longer an anecdote.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **Attribution needs a speaker, not a source.** A transcript records the client, the broker and your own colleagues **in one voice**. "It's in the call transcript" therefore establishes nothing about who constrained you | H/L | *"~80% accuracy"* was purged as vendor-originated on 29 Jul. On 30 Jul the *engagement trigger itself* — a deadline tiered **Confirmed** — turned out to be our own account lead's guess: the broker said *"within September"*, our lead said *"the 10th September"*, the client's *"Correct"* answered a different sentence. Every plan had worked backwards from it |
| 2 | **The two-channels budget does not look at headings.** It counts prose *cells*; an arguing section banner is neither a cell nor exempt | H/L | Shipped banners reading *"RISKS CARRIED — tracked here because a risk is a dependency you cannot name an owner for yet"*. The rule that catches this already exists for diagrams (*specification, not explanation*) and was never generalised to structure |
| 3 | **Out-of-lane is a distinct failure from too-long.** Every offending row was short, true and well-written, and the prose budget had already passed them | H/L | Recipient: *"why are you including lots of commercial assumptions? We're building this WBS from engineering POV — we just went out of our lanes."* Trimming would not have found any of it |
| 4 | **Restating a prohibition can invert it.** Where a rule's value is a *negative*, a summary or translation can flip the polarity with no word obviously wrong | M/L | An assumption saying *these mismatches are our own bug, do not report them* was restated for the team as *"those wrong ones we escalate to the user"* — the exact action the rule existed to prevent |
| 5 | **A request to "refresh my memory" is a grounding trigger, not a recall prompt** | H/L | Both pattern-1 defects were found by re-opening the primary source when asked to explain what a number meant. The second had been re-summarised repeatedly without anyone re-reading the transcript |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **New section: "For anything attributed to another party: record the speaker"** — *whose sentence is this?*, a `stated_by` column where tabular, and the re-read-on-refresh corollary | `references/grounding-gate.md` | 1, 5 |
| 2 | **"A section heading is a label, not an argument"** — the diagram-derived *could a reader disagree with this line?* test, applied to structure | `references/pushback-and-teach.md` | 2 |
| 3 | **New: the lane test** — name recipient + decision, ask whether the row serves them; stated explicitly as *catching a different defect than the prose budget, run both* | `references/pushback-and-teach.md` | 3 |
| 4 | **New: "Restating an assumption can invert it — check the negatives"** — read the restatement back and ask what action it authorises | `references/pushback-and-teach.md` | 4 |

### Validation (fill on the next independent use, in any role)

- [ ] A client-attributed constraint is checked for its **speaker** and ≥1 turns out to be ours.
- [ ] The lane test rejects a row that the prose budget passed.
- [ ] No section heading in a shipped artifact contains a clause a reader could disagree with.
- [ ] A negative rule restated by someone else is read back for polarity before it circulates.
- **Verdict: `PENDING`.** Same engagement as Evolution 2, so these validate that evolution's *diagnosis*
  without independently confirming its *cures*. Hypothesis 1 is the load-bearing one: it adds work to every
  attributed claim, and the failure mode to watch is a role-skill that starts demanding speaker attribution
  for things nobody disputed. It is aimed at **constraints** — dates, volumes, bars, budgets — not at every
  sentence in a transcript.

### Cross-skill note

All three sightings share one shape: **a correct rule, written as prose, in a place where nothing counts it.**
Evolution 2's answer was to move the rule into the schema. Evolution 3's is the same move applied twice more —
into a countable check (`solution-architect` hypothesis 3: sheets describing the work must outnumber sheets
defending the number) and into an executable one (hypothesis 4: assert the prose budget in the generator).
Worth stating as a kernel-level heuristic: **when a kernel rule fails, prefer relocating it to a channel that
executes over rewording it more forcefully.** Rewording is what produced three sightings.

---

## Evolution 4 — 2026-07-31 — A limitation is a claim; and the third invented quantity

**Trigger.** A deck review that had recorded *"no rasteriser on this machine, so there is no visual QA"* and
carried it across three rounds — into a pre-registered check plan, as a stated method constraint. The tool was
installed the whole time, at the vendor's default path, absent only from `PATH`.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **The grounding gate is written for positive claims and silently exempts negative ones.** *"I can't do X"* is an assertion about the world, made without evidence, and nothing in the gate fired on it | H/L | Three rounds of review ran text-only checks in place of the visual pass. When the tool was finally probed it surfaced every structural defect in ten minutes — none visible to the checks that had substituted for it |
| 2 | **A limitation is self-fulfilling: nobody audits a capability you said you lacked.** It is the one claim class with no natural challenger | H/L | Two later passes inherited the constraint as established fact rather than re-testing it |
| 3 | **Limitations become load-bearing on scope faster than facts do.** *"Since we can't check X we'll rely on Y"* converts an unverified constraint into a plan premise, and the premise then justifies the omission | H/L | The check plan's §3 listed it beside genuine constraints, giving it equal standing |
| 4 | **`which` is not a probe.** Installers routinely skip `PATH`; the default install directory is the real check | M/L | `which soffice` → nothing; the binary was at `C:\Program Files\LibreOffice\program\soffice.exe` |
| 5 | **An invented quantity hides best beside a real one** — third sighting of the "whose sentence is this?" defect on one engagement, and it survived the purge of the second because the fix swept the *digit* and not the *card* | H/L | *"Three Lines of Service … in one quarter"* sat next to the client's genuine `~200`; the client names five LoS and his own example uses two |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **New: "A limitation is a claim, and it needs grounding too"** — probe-then-declare with a falsifiable probe line in the record; `which` is not a probe; re-probe on environment change; never let an asserted limitation become a planning premise | `references/grounding-gate.md` | 1–4 |
| 2 | **Speaker-attribution block extended to a third instance**, plus the rule that verifying one quantity in a clause obliges verifying the others, and that number sweeps run word-form as well as digit-form | same §record the speaker | 5 |

### Validation (fill on the next engagement)

- [ ] Every stated limitation carries a probe line naming what was checked.
- [ ] No limitation is inherited across sessions without re-probing.
- [ ] A limitation that starts shaping scope triggers a re-verification before the plan hardens.
- [ ] Number sweeps run both word and digit forms, and clause-mates of any verified quantity are checked.

**Verdict: `PENDING`.** Pattern 1 is the load-bearing one and it generalises well beyond documents — the same
shape covers *"the API doesn't support that"* and *"that can't be tested offline"*. Failure mode to watch: an
author who writes the probe line from memory instead of running the probe.
