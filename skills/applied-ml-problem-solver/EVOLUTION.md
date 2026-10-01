# Evolution Log — applied-ml-problem-solver

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`.
Harvest source: real ML/CV/NLP/retrieval work — framing decisions, experiment logs, eval designs,
inference budgets — plus the traces of `dev` handing ML framing here.

---

## Evolution 1 — 2026-09-17 — birth by split from `dev`

### Harvest scope

Two sources, one structural and one evidential.

**Structural (the split itself).** Measured against `dev` on 2026-09-17:
- ML judgment was **~1,000 of dev's ~2,190 lines** — `ml-heuristics.md` (349),
  `production-thinking.md` (385), `rag-heuristics.md` (108), `modes/train.md` (158).
- **Zero external dependents.** A constellation-wide grep found nothing outside `dev`
  referencing those four files; the only outside mention was `skill-builder`'s authoring
  checklist naming them in a parenthetical.
- **Undiscoverable through its own trigger.** `dev`'s `description` contains no ML keyword —
  "idea, concept, design, architect, spec, build, fix bug, refactor, assess, audit, review,
  analyze, root cause". Roughly half the skill's body could not be retrieved by the skill's
  own retrieval surface.
- `production-thinking.md` was measured before deciding whether to split or copy it:
  **259 ML-serving terms against 110 generic, with zero sections coming out generic** by
  section-level term counts. There was no generic half to leave behind, so it moved whole
  rather than being partially copied — copying ~80% of a file is the drift trap, not a trim.

Precedent followed: `core` moved `evolution-loop.md` out to the `evolution` skill by the same
rule, repointing ~22 references. Classified **authored** (from fire-tested `dev` practice),
not distilled — the four files carry five evolution cycles of real use inside `dev`.

**Evidential (the two new gates).** One project: a personal adaptive language-tutor design
whose agent-instructions file was grounded by a 14-agent task force
— 8 research streams, 6 adversarial verifiers, ~250 citations machine-checked, 0 fabrications.
Aggregate verifier verdicts: 38 CONFIRMED, 26 ADJUSTED, 14 REFUTED.

### Patterns found

Ranked (Impact ÷ Effort), with the proof each bit:

1. **A technique was named before its shape was checked against the problem's** — Impact: H,
   Effort: L. The design specified GRPO over a reward whose two most important terms arrive
   *days* later, on a problem with exactly one learner where the algorithm scores a group of
   samples per gradient step. Both mismatches are visible from the algorithm's signature.
   Verified against `trl/trainer/grpo_trainer.py` at source: set up that way it does not
   error — it NaNs, is `nan_to_num`'d to advantage 0, and trains on nothing silently.
   **Nothing in `ml-heuristics.md` asked the fit question.**
2. **A baseline was invented rather than found** — Impact: H, Effort: L. The design proposed a
   hand-rolled heuristic scheduler as the thing later work must beat. FSRS exists, is
   `pip install fsrs`, and beats SM-2 for 99.6% of users on a public benchmark. Worse, the
   benchmark caps the prize: 0-parameter defaults score 0.3620 log loss against 0.3328 for a
   503-parameter model — a span of 0.029. Headroom was measurable *before* building anything.
   **Nothing in the existing files said "name the published baseline first."**
3. **Negative existence claims were trusted** — Impact: H, Effort: L. Three of the five biggest
   corrections in the run were a stream reporting "no such study/benchmark/dataset exists" and
   a verifier finding it. The clearest: a claim that no study manipulates item duration at
   constant time-on-task, refuted by two papers found under the field's own term of art
   (*presentation rate*) rather than the domain's vocabulary.
4. **The proxy-vs-decisive and discrimination-floor rules held** — Impact: —, Effort: —.
   Already in `ml-heuristics.md` Metrics from Evolutions 4 and 8; the run exercised them and
   found nothing to change. Left untouched.

### Hypotheses applied

1. **New `SKILL.md` § Fit-Check Gate** — five constraint rows (signal volume, latency, breadth,
   budget, failure mode) written *before* a technique is named. Closes pattern 1.
2. **New `SKILL.md` § Baseline-Named Gate** — name the published thing, its benchmark number
   and protocol, and the trivial-to-best span, before building a component that decides
   something a published system already decides. Closes pattern 2.
3. **Negative-existence clause inside the Baseline-Named Gate** — *"not found with the search
   terms used," never "does not exist"*, plus the search-the-term-of-art instruction. Closes
   pattern 3.
4. **New principle #6, "Simulated is not real"** — a simulator/synthetic/replay result is
   evidence about the simulator until a real-population result agrees; label it at every
   citation. Drawn from the same run, where mislabelling simulation as real-learner evidence
   was the most common error found in the surrounding literature.
5. **Structural:** four files relocated, internal cross-references repointed, `modes/train.md`
   renamed `references/train-loop.md` (it is no longer a mode of anything), `dev` given a
   hand-off section and a reference back for `production-thinking.md`, defers-to lines wired
   both ways against `dev`'s proactive activation.

Not modified (validated as already-sound): `ml-heuristics.md` Metrics, `rag-heuristics.md`
in full, `production-thinking.md` in full — moved verbatim apart from path repointing.

### Dogfood — 2026-09-17 — FAILED first pass, fixed, re-run

Fresh-context critic, real task: **design the retrieval evaluation for the `knowledge-base`
MCP** (~115 books, live, never measured) — deliberately not the project the gates were mined
from. Plus a transfer test against that project. It ran 8 real KB queries before designing.

**Verdict: FAIL on first pass — 3 high findings.** All fixed:

| # | Finding | Fix |
|---|---|---|
| 1 | `SKILL.md` claimed *"Called by `conductor`"* but `conductor` had zero references to this skill — and `conductor` is the default entry point in the user's global CLAUDE.md, so the documented path in was the one that did not exist | Wired `conductor/SKILL.md` (a **Model** shape row) and `conductor/references/routing-table.md` (§ ML / model work, with the precedence rule) |
| 2 | `train-loop.md` used `../core/references/…` which resolves to `<skill>/core/` — broken | Fixed. **The sweep found it was wider than reported:** the same bug pre-existed in all four `dev/modes/*.md` and in `dev/references/subagent-briefs.md`, and I had introduced two more in my own `dev` edits. 9 files fixed; a constellation-wide check now passes **111 relative refs, 0 broken** |
| 3 | The Fit-Check trigger ("about to name an algorithm, framework or architecture") did **not** fire on metric or eval-set design — the skill's own headline use case. The critic ran it anyway and rows 3/4/5 each forced a design change | Trigger broadened: *"or fixing a metric, an eval set, or a scoring protocol. A metric is a mechanism."* |

**Medium findings, also fixed:**
- **No sizing arithmetic anywhere** (the critic's "most important missing thing") — `ml-heuristics.md` mandates knowing the MDE up front and supplied no formula. Added `MDE ≈ 2.8 × σ_diff/√n`, an n→MDE table, the noncentral-t and multiplicity caveats, and the rule that **σ_diff is measured on run 1, never assumed**.
- **Baseline-Named contradicted the grounding gate** — it demanded a published benchmark number from a substrate that carries method, not leaderboards (`grep_books("nDCG@10")` → zero hits). Added the `UNVERIFIED-PENDING-LOOKUP` clause, which obliges you to build the trivial baseline yourself rather than skip the gate.
- **Both worked examples came from the single derivation project** — the rows transferred, the *shape of a filled answer* did not. Added a second worked example to each gate from the critic's own retrieval run.
- **No eval-harness template** despite `rag-heuristics.md` calling the harness the real deliverable — the critic invented the structure. Added `references/templates/eval-harness.md`, shaped from what it actually produced.
- **The `dev` boundary was asserted, not enforceable.** Added an explicit precedence rule in three places (this skill, `dev`, `conductor`'s routing table): tie-break on **the deliverable of this turn**.
- `rag-heuristics.md` "Frontier" got an as-of dateline; a serving pointer to `production-thinking.md` was added to the retrieval flow.

**A sixth Fit-Check row, earned by the transfer test.** The critic's hardest blocker was one
the five rows did not ask about: the KB's `top_k` is honoured in neither direction (`top_k=3`
→ 2 results), so any metric named `@10` has no referent. Added as row 6, **instrument
stability** — *does the system actually expose the knob my measurement assumes, and does it
honour it?*

**Transfer verdict, in the critic's words: the gates transfer, the examples and triggers did
not.** Four of five rows earned their keep on a task with no RL, reward or learner anywhere;
row 3 (breadth) bit hardest in an entirely different guise — exhaustive relevance annotation
over 115 books is impossible — and forced the same class of redesign. Baseline-Named changed
its answer, catching it reaching for a hand-rolled internal comparator structurally identical
to the one this skill was born criticising. **Circularity is real but narrow, and was located
in the worked examples and the triggers, not in the rows.** Both have been fixed.

It also found two real defects in the KB substrate itself, which are a finding about the
grounding gate both skills depend on and are recorded here because nothing else owns them:
the `search` index and the `grep_books` corpus are **different documents** for at least one
book (search returns OCR-mojibake where grep returns clean text, so capitalised identifiers in
that book are invisible to BM25), and `top_k` is not honoured.

### Dogfood 2 — 2026-09-17 — routing test + re-run after the structural fixes

Second fresh-context critic. Two structural fixes from dogfood 1 were untested, so this pass
**did not name the skill**: it was given an unrouted user-voice request — an object-detection model confusing one class
for a visually similar one, but only under a minority sensor condition — and told to route it
from `conductor` alone.

**Routing result: correct, by a stated rule, but not cleanly.** It landed here via the
routing-table's ML section and the precedence rule. But three *main-table* rows matched first
and none of them pointed at the ML section, and the section listing "the three collisions that
actually happen" ended *"it does not invent a fourth"* while the dev↔ML collision **is** a
fourth, filed in an unlinked block below "What conductor never routes". Reading top-down and
stopping at the first match lands on `dev`. What saved it was `conductor/SKILL.md`'s Classify
table. Its verdict: *"Yes, I could have got this wrong."*

**The previous falsified checkbox is now half-closed.** The critic confirmed the boundary is
genuinely enforced **on `dev`'s side** — `dev/SKILL.md:111,122`, `modes/build.md:15-16`,
`modes/design.md:27,57` hand ML framing out by name. Conductor's table was the stale half.

**Verdict: FAIL again — 2 high findings. Both fixed.**

| # | Finding | Fix |
|---|---|---|
| H-1 | **The multiplicity rule added by the last fix was arithmetically wrong.** "Multiply the critical value by the number of tests" — Bonferroni divides α by m. At m=30 the constant is **3.99, not 84**; taken literally it inflates required `n` by ~445×. The base formula and the whole n→MDE table checked out row by row; the one wrong line was in the one thing the previous fix added | Replaced with the correct rule and a constants table (m=1 → 2.80, m=5 → 3.42, m=30 → 3.99), naming the 445× error explicitly so it is not re-derived |
| H-2 | **`conductor/references/routing-table.md:12` routed "train / finetune / evaluate the model" to `dev → Train` — a mode that no longer exists**, while `dev/SKILL.md:111` sent the same keywords here. Two files, opposite answers, one pointing at a dead target, on the row the request actually hits | Row repointed here; the "three collisions" count corrected to four and the ML section titled as the fourth |

**Medium findings, fixed:**
- **M-1** "check against those **five** lines" against a six-row table, and a scope note still claiming five. Both corrected; the note now says row 6 came from the transfer test and treats the growth as evidence the list is incomplete.
- **M-2** the sizing arithmetic silently assumed a paired *continuous* statistic. Added the transfer table: paired binary → McNemar (σ_diff ≈ √p_discordant), **AP/mAP has no per-item σ_diff at all** and needs a bootstrap over images, and anything non-decomposable → bootstrap or admit you cannot size it.
- **M-3** `UNVERIFIED-PENDING-LOOKUP` was self-attested with its guard in a separate clause it never pointed at — and the critic found a published mAP figure for the whole task in 20 seconds, so it did *not* need the hatch at task level but did one level down. Now points at its guard and requires recording **which level** was searched.
- **M-4** `eval-harness.md` transferred structurally (every section filled for a CV problem) but three rows were retrieval-worded, and contamination control *actively misdirected* — the CV leak is camera/shift/identity adjacency across splits, not query-from-its-own-chunk. Rewritten per-domain; substrate defects now carries a cross-domain table.
- **M-5 — the one that mattered most, and the one I was most likely to under-act on.** The skill **grew on two consecutive dogfoods and retired nothing.** Proxy-vs-decisive was stated in full in *both* `ml-heuristics.md` and `train-loop.md`, retelling the same trace; the MDE formula existed verbatim in `SKILL.md` **and** `eval-harness.md`. That second copy **never received the H-1 correction** — the drift happened inside one session, exactly as predicted. Cut: `train-loop.md`'s restatement replaced by the procedure plus a pointer, `eval-harness.md`'s formula replaced by a pointer, and `ml-heuristics.md`'s closing note corrected where it claimed `train-loop` owned rules this file actually owns.
- **LOW** `eval-harness.md` cited `rag-heuristics.md` from `references/templates/`, one level short. The previous ledger's "0 broken" had swept only `../` forms and missed the templates directory. Sweep widened: **12 refs in this skill, 0 broken**, and 111 constellation-wide.

**LOW findings from dogfood 2's remainder, also fixed:**
- **L-3** the flow table filed the eval harness under *"(any phase)"* while the template's first
  line says *"fill this in **before** running the thing you are evaluating"* — and "any phase" is
  the weaker claim, which undercuts the gate. Now a named **Instrument** phase, "before running
  any of it".
- **L-4** the two Fit-Check worked examples printed **3 of 6 rows each, and the two halves did
  not overlap** — so nothing anywhere in the skill showed a complete filled gate. A reader
  copying an example wrote half a table. Replaced with one fully-filled six-row example, plus
  the instruction to fill all six even when most return OK: *the cheap rows are what make the
  expensive one survivable.*
- **L-1** `eval-harness.md` cited `rag-heuristics.md` as a bare filename from inside
  `references/templates/`. My first attempt to fix this **silently failed** — the replacement
  targeted a string that a line break had split — and I recorded it as fixed. The widened sweep
  caught it. That is gate-by-artifact failing on my own edit: I checked that the command ran,
  not that the file changed.
- The `UNVERIFIED-PENDING-LOOKUP` block gained the field it was missing — **what terms were
  searched** — and now states that it applies at a stratum or sub-question far more often than
  to a whole task, which is the common case and was the critic's actual experience: a published mAP figure for the
  overall task was one search away, while no published number exists for the specific
  confusable-class-under-one-sensor-condition failure the project actually cared about.

**A sweep defect this exposed, which matters beyond this skill.** The previous ledger's
"111 relative refs, 0 broken" was **true but misleading** — it matched only `../`-prefixed
paths. Widening it to bare filenames found a class of bug across the constellation: a path
written as `references/x.md` from *inside* `references/` resolves to `references/references/x.md`.
Fixed in the four repos this task touched (**85 refs, 0 broken**). **Thirty-five remain in twelve
other skills** — `solution-architect`, `business-intelligence`, `delivery`, `screencast`,
`media-gen`, `evolution`, `core` and others. Out of scope here, reported rather than silently
fixed or silently ignored, and worth a dedicated sweep.

**What this pass establishes about the two gates:** rows 1–6 held on a computer-vision
detection problem with no retrieval and no RL — a third domain. The *arithmetic* the gates
lean on did not, and needed a domain-specific transfer table. That is the pattern across both
dogfoods: **the questions transfer, the worked machinery does not.**

### Validation results (settled by a later run's step 0)

- [ ] **Fit-Check Gate fires on a real ML task and catches a mismatch** — or is correctly silent. *(First dogfood: fired, caught 3 mismatches on a non-derived task. Needs a second independent use.)*
- [ ] **Baseline-Named Gate produces a named published baseline** on a real component build. *(First dogfood: produced BM25-via-BEIR and changed the critic's design. Needs a second.)*
- [x] **Cross-references resolve** — 111 checked constellation-wide, 0 broken.
- [~] **The `dev` ↔ `applied-ml-problem-solver` hand-off works from both entry points without a trigger collision.** Falsified on pass 1; **half-closed on pass 2** — an unnamed, unrouted request reached this skill by a stated rule, and `dev`'s side of the boundary was confirmed enforced. But the critic could have got it wrong reading `routing-table.md` top-down, and said so. Conductor's table was fixed after that run and is **again untested**. Still the first thing the next real use must exercise.
- [~] **The six Fit-Check rows are the right six.** Row 6 was added by transfer test 1 (retrieval). Transfer test 2 (CV detection) added **no seventh row** — all six applied — but forced a domain-specific sizing table, which suggests the rows are stabilising while the arithmetic beneath them is not.

**What counts as a "use" for the PENDING → KEEP ladder:** a real task, not a toy, where the
skill was *invoked to make a decision* and produced an artifact on disk — a filled Fit-Check
table, a named baseline, an eval-harness spec, or an `experiment-log.md` entry. A fresh-context
dogfood counts as one. Reading the skill does not. Two more independent uses are required, and
they must be on domains the gates were not mined from — the transfer test is the point.

- **Verdict: PENDING** — the structural split is measured and verified, and the first dogfood
  failed and was fixed rather than passed on inspection. Both gates still rest on **one
  derivation project plus one transfer test**. The hand-off precedence rule is **untested**.
  `KEEP` requires two more independent real uses.

## Evolution 2 — stage B rebuild (2026-10-01)

### Harvest scope
- Read the approved proposal, the applied-ML and core rule ledgers and crosswalks, the practitioner review, the current skill and references, the shared kernel, and the skill-builder instructions and templates.
- Read the cited chapters for routed rules and adopted candidates from: ai-engineering-huyen, ai-powered-search, art-of-ai-product-development, building-machine-learning-pipelines, building-reliable-ai-systems, critical-thinking-about-research, d2l-en, data-science-for-business, designing-ai-interfaces, designing-ml-systems-huyen, effective-conversational-ai, essential-graphrag, hands-on-site-reliability-engineering, how-to-read-a-paper, human-in-the-loop-ml, kagglebook_secondedition, machine-learning-production-systems, real-world-software-development, research-methods-psychology, site-reliability-engineering, software-engineering-at-google, statistics-by-simulation.
- This is a source-based rebuild; the change needs two real uses before its practice can be settled.

### Patterns found
1. **The skill was organized as accumulated rules rather than a decision flow.** The practitioner review also identified defaults that overreached their evidence, including pipeline-first optimization, assumed GPU synchronization, and a fixed fusion target.
2. **Several useful practices were absent.** The book candidates added evaluation reliability and scoring guidance, multiple baselines, data diagnostics, monitoring, and staged rollout and recovery practices.

### Hypotheses applied
1. **Rebuilt `SKILL.md` around the ML decision record and its workflow** — frame, ground, fit-check, resolve the gate, name headroom, run experiments, and decide.
2. **Separated durable reference material by job** — ML formulation, experiment loop, retrieval, evaluation harness, and inference production thinking. Kept the linked `production-thinking.md` and `rag-heuristics.md` paths.
3. **Applied crosswalk corrections and review findings** — profile the largest measured bottleneck, qualify CPU/GPU synchronization by runtime evidence, avoid fusion targets as defaults, and use class counts as evidence rather than a universal 5% trigger.
4. **Coverage:** 209 routed rules: 46 agrees, 81 refines, 82 field rules, 0 disputed. Adopted 27 candidates; left 6 skill candidates and 27 core candidates out of this skill.

### Validation results
- 2026-10-01 dogfood: visual-inspection presale, 7 findings (2 high, 4 med, 1 low); fixed 7, rejected 0.
- [ ] Two real uses confirm the workflow is usable and the added practices help decisions.
- **Verdict: PENDING** — this rebuild is distilled from formal sources and a practitioner review; it has not yet been exercised in two independent real uses.
