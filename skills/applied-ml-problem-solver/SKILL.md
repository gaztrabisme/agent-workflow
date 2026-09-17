---
name: applied-ml-problem-solver
description: "Decide whether an ML/AI approach is the right one, and whether you could tell if it worked — problem reframing, label and architecture decisions, metric and eval-set validity, retrieval/RAG design, the experiment loop, and the inference-serving realities that decide whether a working model survives production. USE WHEN framing an ML/CV/NLP problem, choosing a loss/architecture/metric, designing a training or eval experiment, picking a baseline to beat, debugging a model that scores well but behaves badly, building RAG or semantic search, sizing a model to an inference budget, or judging whether a technique fits your data and latency constraints. Not `dev`, which writes the code once these decisions are made; not `omlx`, which operates a local endpoint. Keywords: ML, CV, NLP, training, finetune, experiment, baseline, metric, eval set, proxy metric, class imbalance, augmentation, RAG, retrieval, chunking, reranking, embeddings, inference latency, VRAM, quantization, throughput, reward design, model selection."
license: MIT
---

# Applied ML Problem Solver

Judgment for machine-learning work: is this the right problem, will this mechanism fit the constraints you actually have, and would you be able to tell if it worked. It produces decisions and their evidence — a problem reframed, a label schema that survives contact, a pre-registered convergence gate, an experiment log with a negative result written down, a retrieval design with an eval harness, an inference budget that accounts for the layer below. It does not produce the code; `dev` does that.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## When it fires — and when a sibling owns it

- **This skill:** the *decision* questions. What problem is this really? What baseline must I beat? Does this architecture/loss/metric fit? Can my instrument see the difference I'm gating on? Will this survive ten cameras on one GPU?
- **`dev` instead:** the *construction* questions. Write the `Dataset` subclass, the training script, the inference API, the tests. `dev`'s Build mode (test → implement → verify) works fine on ML code; it just shouldn't be the thing deciding whether the model is the right idea.
- **`omlx` instead:** operating a local MLX endpoint — request contract, schema enforcement, serving ops.

> **Disambiguation:** decide on **question type, not technology**. A question about *what to
> build and how you'd know it worked* is here. A question about *making the code work* is
> `dev`. Both skills fire on an ML project; they fire at different moments, and `dev`
> explicitly hands the framing questions here.
>
> **Precedence when both match** (they usually do, and `dev` activates proactively on intent):
> this skill runs **first** and hands `dev` a framed problem with a pre-registered gate; `dev`
> does not reframe. The tie-break is **the deliverable of this turn** — a decision, a metric,
> an eval design or an experiment verdict lands here; a file of code lands in `dev`. If the
> turn would produce both, split it and run this one first. Same rule in
> `../conductor/references/routing-table.md` § ML / model work.

## Principles / anchoring rules

1. **Reframe before solving.** The right question is rarely "which model?" — it is "what simpler problem does this reduce to?" A reframe that removes a class, collapses two heads, or turns detection into classification is worth more than any architecture choice downstream.
2. **The instrument must resolve the delta.** A number that moved is not a win until you know why it moved, and a measurement that cannot discriminate the difference you are gating on is still a proxy. This is `core` spine #2 aimed at metrics.
3. **Negative results are deliverables.** The experiment that failed, with the mechanism named, is reusable knowledge that stops the next session re-running a dead end. Writing it down is the Output Contract, not optional bookkeeping.
4. **One variable per experiment.** Two changes and a moved metric tell you nothing you can act on.
5. **Standard library over wrappers, primitives over frameworks.** A 40-line metric beats a dependency. See `dev`'s Engineering Style — it applies here and is not duplicated.
6. **Simulated is not real.** A result from a learner simulator, a synthetic corpus, or a benchmark replay is evidence about the simulator until a real-population result agrees. Label it as such every time it is cited.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| **Frame** | Reduce to the simplest problem that still solves the need | Problem statement + rejected reframings |
| **Fit-check** | Confirm the technique's shape matches the constraints | One line per constraint (see gate below) |
| **Baseline** | Name and run the thing you must beat | Baseline number in the experiment log |
| **Experiment** | One variable at a time against a pre-registered gate | `experiment-log.md` entry per run |
| **Evaluate** | Decide ship / don't ship, and write why | Verdict + post-mortem in `wiki/decisions.md` |
| **Instrument** | Design what will judge all of the above — **before running any of it** | `references/templates/eval-harness.md`, filled |
| **Serve** | Survive the layer below and the tenth concurrent client | Inference budget + pre-deployment checklist |

Depth lives in the references. `references/train-loop.md` owns the experiment loop and the log format.

## Gates (declared, inherited from core)

- **Grounding gate** — substrate for this skill is the **Knowledge Base MCP** (ML, databases, security, distributed systems, RAG). Before designing or implementing on a KB-covered domain: `search("concept")` for theory, `grep_books("exact term")` for API/algorithm names, `get_chapter(book, ch)` to read deeper. Record one line — `KB: searched "<query>" → applied <finding> (book/chapter)` or `→ nothing relevant` — in the experiment log or Key Decisions. Skippable only by stating the domain isn't covered; a silent skip on a covered domain is a violation. See `../core/references/grounding-gate.md`.
- **Output Contract** — primary artifacts: an `experiment-log.md` entry for every run (config, metric vs. pre-registered baseline, verdict), and any direction-changing result in `wiki/decisions.md`. **A negative result is a required write.** See `../core/references/wiki-protocol.md`.
- **Pushback & teach** — ML math is in scope for teaching: when you introduce a loss, activation, optimizer or architecture, narrate the *mechanism* — what it computes, what it penalizes, why the shape is what it is — not just the API call. See `../core/references/pushback-and-teach.md`.
- **Approach declaration** — declare how you'll run it before substantive work. `sim / probe-first` is the characteristic choice here: when the fork is expensive or irreversible (a long training run, hardware spend, a schema lock-in), build the cheapest experiment that resolves the biggest uncertainty first. (core SKILL.md §7.)

### Fit-Check Gate

*Verdict: **PENDING** (birth — one project). Earns KEEP only after two more real uses.*

**The disease it treats:** naming a technique before checking its shape against the problem's. The failure is silent — the technique is real, the library works, the code runs, and the method was never capable of answering the question. Observed once, concretely: a design that specified GRPO over a reward whose two most important terms arrive *days* after the action, on a problem with exactly **one** learner where the algorithm scores a group of samples per step. Both mismatches are visible from the algorithm's signature; neither was checked. Set up that way, training does not error — it produces NaN, gets `nan_to_num`'d to zero advantage, and trains on nothing.

**FIRES WHEN** you are about to commit to a mechanism — naming a specific algorithm, framework or architecture in a spec, plan or `AGENTS.md`, **or fixing a metric, an eval set, or a scoring protocol.** A metric is a mechanism: it has signal requirements exactly like an optimizer does, and an eval design that assumes data you cannot collect fails the same way a training algorithm does.

**Then, BEFORE naming it — write the problem's shape first, one line each:**

| # | Constraint | The question to ask out loud |
|---|---|---|
| 1 | **Signal volume** | How many labelled/scored examples exist per decision the method must make? |
| 2 | **Signal latency** | How long after the action does the outcome arrive — milliseconds, or days? |
| 3 | **Signal breadth** | Can I score *every* sample the method wants scored, or only the one that happened? |
| 4 | **Budget** | What fits in the memory, time and money I actually have? |
| 5 | **Failure mode** | If this is mis-specified, does it crash — or does it silently produce nothing? |
| 6 | **Instrument stability** | Does the system actually expose the knob my measurement assumes, and does it honour it? |

**Then check the technique's stated requirements against those six lines.** A mismatch on any row is a redesign, not a tuning problem.

```
Fit/volume:   ~40 scored items/week; GRPO group size 8 → 1 real score per step. MISMATCH
Fit/latency:  retention observable at day 7; on-policy advantage needs it now. MISMATCH
Fit/failure:  silent (NaN → advantage 0). Gate required, crash not available.
```

Second worked example — a retrieval-eval design, no RL anywhere, **all six rows filled** so
there is one complete gate in this file to copy:

```
Technique about to be named: NDCG@10 + Recall@10 over a 200-query LLM-generated golden set.

Fit/volume:    ~11k chapters; I can label 200-500 queries by hand or judge.          OK
Fit/latency:   retrieval is synchronous; the score exists in milliseconds.           MATCH
Fit/breadth:   true Recall needs every relevant chunk known per query across 115
               books. I can only annotate what was retrieved.                        MISMATCH -> known-item design
Fit/budget:    200 queries x ~8 parents x ~3.5k tokens = ~5.6M judge-tokens per
               arm per run; a paired A/B is two arms.                                MISMATCH -> proxy/decisive split must be structural
Fit/failure:   silent - a golden set generated FROM the chunks scores ~0.93, has
               no headroom, and never moves. No crash.                               Gate required
Fit/stability: top_k is honoured in neither direction (top_k=3 -> 2 results), so
               any metric named "@10" has no referent.                               MISMATCH -> fix substrate first
```

**Fill all six rows even when most come back OK.** A row that costs one line and returns MATCH
is the cheap half of what makes the expensive half survivable; skipping the easy rows is how
you miss the one that bites. In both worked examples above, two or three rows forced a
redesign and the rest cost a line each.

#### Sizing the gate (how big does n have to be?)

A Fit-Check on signal volume is not done until you can say what effect size your `n`
can actually see. For a paired comparison at 80% power and α = .05 two-sided:

```
MDE ≈ 2.8 × σ_diff / √n          (2.8 ≈ z_{.975} + z_{.80} = 1.96 + 0.84)
```

Use the exact noncentral-t when `n` is small (under ~30 the normal approximation is
optimistic by roughly 5%).

**Multiplicity divides α; it does not multiply the constant.** Gating on several metrics at
once means recomputing the critical value at α/m — five metrics over six contrasts is thirty
tests, not one, and the constant grows far more slowly than the test count:

| tests (m) | α/m | constant (z<sub>1−α/2m</sub> + z<sub>.80</sub>) |
|---|---|---|
| 1 | .05 | **2.80** |
| 5 | .01 | 3.42 |
| 30 | .0017 | **3.99** |

Thirty tests costs about 2× the sample size, not 30×. (Multiplying the constant by `m`
instead would give 84 and inflate required `n` by roughly 445× — an error worth naming,
because it makes a feasible experiment look impossible.)

| n (paired units) | MDE, in units of σ_diff |
|---|---|
| 25 | 0.56 σ |
| 50 | 0.40 σ |
| 100 | 0.28 σ |
| 240 | 0.18 σ |
| 1,000 | 0.089 σ |

**This formula assumes a paired, continuous, per-item statistic.** It does not transfer
unchanged:

| Statistic | What to use instead |
|---|---|
| Paired **binary** outcomes (correct/incorrect) | McNemar on the discordant pairs; σ_diff ≈ √p_discordant, so the rate of *disagreements* sizes the study, not the accuracy |
| **AP / mAP** (detection, ranking) | There is no per-item σ_diff — AP is computed over the whole set. Bootstrap over images/queries and read the CI directly |
| Metrics with **no per-unit decomposition** | Bootstrap. If you cannot resample it, you cannot size it, and you should say so rather than quote a number |

**`σ_diff` is not a thing you may assume.** It is measured on run 1 and then fixes every
number downstream, so an assumed σ silently scales the whole design. If you have not
measured it, say so and treat the sizing as provisional — the single most common way an
experiment plan is wrong by an order of magnitude is an invented σ.

> ⚠ **Scope honesty.** Rows 1–5 were mined from ONE project (a personal language tutor, an
> RL-for-teaching design). **Row 6 was added by the first transfer test** — a retrieval task
> whose hardest blocker none of the first five asked about. That the list grew on its first
> contact with a second domain is evidence it is still incomplete. Add rows when a real
> mismatch fits none of them; retire rows that stop appearing.

### Baseline-Named Gate

*Verdict: **PENDING** (birth — one project). Earns KEEP only after two more real uses.*

**The disease it treats:** inventing a baseline instead of finding the published one, then measuring an "improvement" against a straw man. A hand-rolled heuristic you wrote is not a baseline; it is the thing your method should embarrass, and if it can't, you have learned nothing.

**FIRES WHEN** you are about to write a scheduler, ranker, scorer, retriever, or any component whose job is a decision a published system already makes.

**Before building it, name in one line:**
1. **The published thing you would have to beat** — by name, with a version or citation, and whether an implementation exists you could run.
2. **Its number on a public benchmark**, and the evaluation protocol that produced it (log-replay and live trial are not the same claim).
3. **The gap between the trivial baseline and the best-in-class number.** If that span is small, the whole project's headroom is small, and you should know that before you spend the compute, not after.

```
Baseline: FSRS-6, `pip install fsrs`, beats SM-2 for 99.6% of users (log-replay, not a live trial).
Headroom: 0-param default 0.3620 → best-in-table 0.3328 log loss. Span 0.029. Measure the gap first.
```

Second worked example — a retrieval system, different field, same three lines:

```
Baseline: BM25 via BEIR — the standard published floor for retrieval; implementation exists (`rank_bm25`, Pyserini).
Number:   BEIR reports per-dataset nDCG@10; no entry for a private 115-book corpus → measure BM25 on my own eval set.
Headroom: unknown until BM25 is run here. Build it first; a dense retriever that cannot beat BM25 on your own corpus is not a result.
```

**When the number genuinely isn't published.** Some fields publish methods and no
leaderboard — the grounding substrate carries the technique and not a benchmark table.
That is a legitimate outcome, and it is not a licence to skip the gate. Record it as:

```
Baseline: <named published system/method>, implementation: <exists / none found>
Number:   UNVERIFIED-PENDING-LOOKUP
          searched: <where> | <when> | terms: "<the exact terms, including the field's own term of art>"
          level:    <whole task | a stratum | a specific failure mode>
Headroom: unknown → run the trivial baseline yourself and publish your own span first
```

An `UNVERIFIED-PENDING-LOOKUP` obliges you to build the trivial baseline **before** the
real thing, so the span exists even if nobody else measured it. What it never becomes is
a silent omission.

**It is not valid until the search below has actually been run**, including under the field's
own term of art — this clause is self-attested, and the paragraph that follows is its guard,
not a separate suggestion. **This clause applies at a stratum or a sub-question far more often than to a whole task**,
and that is the common case, not the exception: a published number usually exists for the task
(a common detection task will have public mAP figures on a standard benchmark) while the
failure mode you actually care about — one confusable class, under one sensor condition that
is a minority of your data — has none.
Recording `UNVERIFIED` for the whole task when one search would have found it is the abuse this
field exists to make visible.

**"I couldn't find one" is only valid after a real search** — and it is the least reliable sentence in any research report. Treat a negative existence claim as *"not found with the search terms used,"* never as *"does not exist."* Search the field's own term of art, not the one your domain uses: a search for *micro-lesson item duration* returns nothing; the same question asked under the cognitive-psychology term of art, *presentation rate*, returns a controlled second-language study with a measured optimum.

## Anti-patterns (hard no-list)

- **Naming the technique before writing the problem's shape.** The Fit-Check Gate exists because this is the default.
- **Benchmarking a component in isolation** and projecting the number into a system with contention. See `references/production-thinking.md`, "The Benchmark Lie."
- **Optimizing a proxy you never checked against the decisive metric.**
- **Reporting a simulated result as if it came from a real population.**
- **Two variables in one experiment.**
- **A constant that claims to be measured without naming its instrument.**
- **Reaching for RL because RL is available**, before a fitted non-RL baseline exists and has been beaten.
- **Duplicating `dev`'s engineering style or `core`'s spine here.** Reference them.

## Composition

- **Inherits:** `core` — integrity constraints, gate-by-artifact, wiki protocol, grounding gate, pushback-and-teach, the evolution loop.
- **Hands construction to:** `dev` — once the problem is framed and the experiment designed, Build mode writes and tests the code; `dev`'s Engineering Style and Pattern Gate govern *how* it is written.
- **Hands local serving to:** `omlx` — when the thing being served is a local MLX endpoint.
- **Consumes:** the Knowledge Base MCP as its grounding substrate.
- **Called by:** `conductor` when a request is ML-shaped and nobody named a skill.

## References

- `references/ml-heuristics.md` — problem reframing, label schema design, multi-task architecture, training schedule, metrics (proxy-vs-decisive, discrimination floor, eval-set validity), experiment design, augmentation, architecture decisions, deployment export.
- `references/train-loop.md` — the experiment loop: convergence criteria → validate data → baseline → one-variable loop → evaluate/handoff, plus the append-only `experiment-log.md` spec and negative-result discipline.
- `references/rag-heuristics.md` — retrieval decisions: do you even need RAG, match-unit vs context-unit chunking, hybrid dense+BM25, reranker tiers, contextual enrichment, retrieval eval harness.
- `references/templates/eval-harness.md` — fill-in eval-harness spec: decision served, frame + rejected reframings, the filled Fit-Check table, baseline, eval set with contamination control and strata, match unit, proxy/decisive/diagnostic metrics, the discrimination floor with its sizing arithmetic, known substrate defects, run protocol.
- `references/production-thinking.md` — everything after "my model works": the layer below, graph-level thinking, systems interaction, scale projection, hardware constraints, operational failure modes, pre-deployment checklist.
