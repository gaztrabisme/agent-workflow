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
- [x] A tabular artifact carries provenance structurally (`*_reported` or a tier column) with at least one asserted invariant. **(Evolution 6, 6 Aug.)** The deck's claim map keys every claim by `sha256` of its normalised paragraph text, and the gate asserts the map and the artifact agree. Partial credit only — it is a *content-address*, not a provenance tier, so it detects drift rather than recording who said it.
- [ ] An artifact set stays inside what was asked for, or the excess was proposed and accepted first.
- [x] A cold review runs on a primary artifact and is scored against pre-registered weaknesses. **(Evolution 6, 6 Aug — the strongest result so far.)** Three cold reviewers over a client-bound deck that had already passed five automated gates found four real defects. Pre-registered plan existed (`wiki/deck-final-check-plan.md`). **Still `PENDING`: same engagement, so not an independent use.**
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

## Evolution 5 — 2026-08-04 — The gate that audited last week's file, and the second opinion

### Harvest scope
One engagement across three days, carrying five project gates plus a sixth built mid-session for a
client-facing deck. Heavy bulk editing, two artifacts changing hands between two people with no version
control, and two cold adversarial reviews commissioned on different models against the same contested
judgement. Representative for this skill because it stresses the *grounding* and *output-contract* gates
rather than any one role's method.

### Patterns found

**P1 — A stale default makes a gate lie fluently. `Impact: H, Effort: L`.**
The deck gate defaulted to the previous deck version and a superseded plan. Run without flags it reported
eight hard defects, all true of last week's artifacts. It had done so for a day; the "green" state quoted in a
checkpoint came from an explicit flag nobody else passed. **The failure is silent by construction — the tool
succeeds, and its verdict is well-formed.** Nothing about a passing or failing result reveals that the
subject is wrong.

**P2 — Content-addressed IDs survive re-sequencing but move on any text edit. `Impact: M, Effort: L`.**
Hashing a claim's normalised text rather than its position was the right call and proved itself twice: a slide
was deleted upstream and all 32 mapped claims still resolved. But the corollary was not written down — **an
approved wording change re-keys the ID**, and the map must be updated in the same step or the gate reports
drift on a change that was intended. Twice in one session.

**P3 — Two cold reviews on different models converged, and the convergence was the signal.
`Impact: M, Effort: L`.**
Both independently identified an unmeasurable denominator, both independently demanded the same one-day
measurement on data already held, and they diverged on exactly the point that was genuinely undecided. The
convergence justified acting; the divergence located the soft judgement. Neither was told the other existed.

**P4 — Concurrent edits to one file with no version control, twice. `Impact: H, Effort: L`.**
A working copy was created specifically to avoid clobbering a colleague's file — and then that working copy
was edited by two parties in the same hour. Nothing was lost, but only because the second writer happened to
load the current file rather than hold an older one in memory. **"Who has the pen" was asked three times and
answered once, at the end.** The near-miss is the finding; the outcome is luck.

### Hypotheses applied

| # | Pattern | Edit |
|---|---|---|
| H1 | P1 | `references/grounding-gate.md` → **"A tool's default target is part of its claim"** — point defaults at the current artifact or make the argument required, and **echo resolved inputs above the verdict** so a stale target is visible in every pasted transcript |
| H2 | P3 | Same file → **"Two adversarial reviews on different models beat one review twice"** — converge/diverge reading, and the cold-brief rule |
| H3 | P2, P4 | *No edit yet.* P2 belongs with the claim-map pattern, which does not exist in a skill — it lives in the project. P4 is a working-agreement problem, not a grounding one, and the honest fix is procedural rather than another paragraph nobody reads. Both recorded here so a second occurrence has somewhere to land |

### Validation results
**`PENDING`.** H1 is the strongest candidate to generalise — it is a property of any self-resolving tool, and
the echo-your-inputs rule is nearly free. H2 is the one most at risk of being **over-scoped**: two reviews cost
real tokens and the value was high *because the judgement was going to a client and was contested*. On a
routine call it would be ceremony. If a later harvest shows it being skipped, the likely correct verdict is
`REVISED` with a selector naming when it is worth it — not `REVERT`.

**Updated 6 Aug (Evolution 6).** H3's two parked patterns have split. **P2 recurred and has now landed** — a
client-facing vocabulary change re-keyed ten content-addressed claim IDs in one pass, which is the second
sighting, and it is written up in `pptx` Evolution 2 H2 as *a vocabulary change is a code change*. **P4 did
not recur**: "who holds the pen" was named once and held for the rest of the engagement, which is weak
evidence that the procedural fix was the right call rather than another paragraph. Leave P4 parked.

---

## Evolution 6 — 2026-08-06 — The rule was already written, and it failed anyway

### Harvest scope

Two days at the end of the same presale engagement — the densest stretch of it. A client-bound deck taken
from `v1.5` to `v1.6` under five parallel agents, a 112-second explainer video built from nothing, three cold
reviewers, and a client session held against the result. Six live gates.

**Representative for the kernel in a way earlier harvests were not, because this one is mostly *negative*
evidence.** Three of the four patterns below are rules `core` already states, correctly, in files that were
open and being followed. Their failure is the finding. A harvest that only collects new rules will never
detect the class of defect where the rule exists and does not fire — and that is now the dominant class here.

### Patterns found

**P1 — The speaker rule failed a fourth time, wearing the opposite costume. `Impact: H, Effort: L`.**
`references/grounding-gate.md` has carried *"For anything attributed to another party: record the speaker"*
since Evolution 3, with three worked instances **from this same engagement**. The fourth landed anyway: the
orientation document every fresh session is instructed to read first presented a sentence **in quotation
marks, attributed to the client partner by name, tagged `(Confirmed)`** — sourced in fact from a colleague's
Teams summary. The three earlier instances were unquoted assertions absorbed into our prose. **This one
survived precisely because it looked more sourced than its neighbours.** Nobody re-checks a direct quote.

A second instance the same week generalises it past client attribution: a sentence recorded in three files as
the **guard** protecting a vocabulary change was a composite appearing on **no page** of the artifact — so the
guard failed by the exact method it invited, and a searcher could not distinguish "the artifact broke" from
"the guard was fiction".

**P2 — A check whose output is mostly noise is worse than no check. `Impact: H, Effort: L`.**
The response to P1 was a script — correct, and what `Tier in the schema, not the prose` prescribes. Run
unscoped it returned **217 candidates**: chat, mail, standards text, our own prose, every one a correct match
for "a quoted string of 8+ words". Filtered to quotations **attributed to a named external speaker** it
returned a workable set and found **two real defects**. The unscoped version was not merely useless — shipping
it would have taught the team that gate output is noise, discrediting the five gates beside it. `core` said
*put the check in a script* and said nothing about the check's signal-to-noise being the property that decides
whether it is a gate at all.

**P3 — The tool that produced the deliverable lived in session temp. `Impact: H, Effort: L`. Second
independent trace.**
An entire video pipeline — driver, encoder settings, and the harness that decoded the output back to verify
it — existed only under a **session-scoped UUID scratch path**. The MP4 had already shipped and was embedded
in a client deck, so nothing about the finished state revealed the problem. **This is the second occurrence
five weeks after the first**, when two workbook generators were recovered from session temp during a
reorganisation; that project's own index records that without them the workbook would have been rebuilt by
hand. Both survived by someone happening to look.

**P4 — VALIDATION: cold review found what six gates could not, and the *where* is the transferable part.
`Impact: H, Effort: L`.**
Evolution 2's spine item #10 ran for real against a pre-registered plan. Three reviewers found four defects in
an artifact already passing every automated check — and **every one was inside a screenshot**. Not a
coincidence: an image is the artifact class no gate can read, so it is where undetected defects accumulate.
The gate as written says *scale to stakes*; it did not say *aim it at what your automation structurally
cannot inspect*.

### Hypotheses applied

| # | Pattern | Edit |
|---|---|---|
| H1 | P1 | `references/grounding-gate.md` → new sub-section **"Quotation marks are themselves a claim"** under the speaker rule. Quotation marks assert the enclosed characters exist in that order in a source of record; if you cannot produce them, **remove the marks, not the sentence**. Extended to guards, sentinels and defect descriptions — each is a claim about a source and each is one search away from verification, so **run that search when you write it, not when you rely on it** |
| H2 | P2 | Same file → new section **"Scope the check until its output is all signal"**, placed directly after *Tier in the schema*. Records the predicate as engagement config while the shape is portable; adds the two consequences — *a tuned but unwired check is a tool, not a gate*, and **a narrow predicate can go stale into a silent pass**, so it needs a non-empty-corpus assertion |
| H3 | P3 | `references/wiki-protocol.md` → Output Contract gains a checklist line and **"A deliverable whose toolchain is in temp is not complete"**. The generator is part of the deliverable; record the inputs it expects and the verification that proved its output correct; repoint hardcoded absolute paths during the move |
| H4 | P4 | `SKILL.md` spine item #10 extended with the targeting selector — rank the artifact by what a script can inspect and spend the reviewer on the bottom of that list |

### Validation results

**H3 ships `KEEP`, not `PENDING`** — two independent traces five weeks apart, different artifact classes
(workbook generators, a video pipeline), same mechanism, and the second occurred *after* the first had been
written up in the project's own index. That is the bar `evolution-loop.md` sets, and this is the first kernel
change to clear it on evidence rather than by inheritance.

**H1, H2, H4 `PENDING`.** All from one engagement.

- **H1 is the one to watch, and its own history is the reason.** This is the fourth failure of a rule that has
  been rewritten after each of the previous three. If a fifth instance appears, the correct response is **not**
  a fifth paragraph — it is to conclude that the prose form cannot carry this rule and that only H2's
  scripted-and-scoped form can. **H1 and H2 should therefore be validated together**, and a harvest that finds
  H1 holding *because* H2's check was running should record that as H2's win, not H1's.
- **H4's risk is over-scoping.** "Aim cold review at what automation cannot read" was derived from a deck, an
  artifact unusually rich in images. On a text-only deliverable the ranking is flat and the selector says
  nothing useful. If a later harvest shows it ignored there, that is `REVISED` with a substrate selector, not
  `REVERT`.
- **H2 carries a self-referential trap worth naming.** Its own advice — a narrow predicate can go stale into a
  silent pass — applies to itself. The check it was harvested from is scoped by a hardcoded list of client
  names, and the day that engagement's cast changes it will report clean.

**Next harvest should ask:** did anything reach a client-bound artifact through the *image* channel again
after H4 existed, and did anyone write a quotation without running the search H1 demands? The second question
is the real test, because it has now been asked and answered wrongly four times.
