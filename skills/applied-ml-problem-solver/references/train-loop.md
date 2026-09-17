# The Experiment Loop

Iterative ML training loops — finetuning, architecture experiments, hyperparameter search. Unlike `dev`'s Build mode (test -> implement -> verify), the experiment loop measures success by metrics, not binary tests.

Read `ml-heuristics.md` (beside this file) for problem reframing and architecture decision heuristics. Read `../../core/references/pushback-and-teach.md` — the teach directive applies to ML math too: when you introduce a loss function, activation, optimizer, or architecture choice, narrate the *mechanism* (what it computes, what it penalizes, why the shape is what it is), not just the API call.

**Apply the Knowledge Base Grounding Gate (`../SKILL.md` -> Gates) before Phase 1.** ML is a KB-covered domain — search the corpus for the technique/architecture/metric you're about to use and record `KB: searched "<q>" → <finding|nothing relevant>` in the experiment log or Key Decisions. Ground the approach before spending compute.

---

## Phase 1: Define Convergence Criteria

Before any training, define what "done" looks like:

```markdown
## Convergence Criteria
- Primary: [metric] [operator] [threshold] (e.g., mAP@50 > 0.85)
- Secondary: [metric] [operator] [threshold] (e.g., inference latency < 50ms)
- Stop condition: [when to stop iterating] (e.g., 3 consecutive experiments with <1% improvement)
```

If you can't define convergence criteria, you're not ready to train — go back to Frame (`SKILL.md`, the flow table) first.

### Proxy vs. Decisive Metric (pre-register the gate)

**The rule and the traces that earned it live in `ml-heuristics.md` → Metrics** (Proxy vs.
Decisive Metric, and The Instrument Must Resolve the Delta). Not restated here.

What Phase 1 owes on top of the rule — the procedure:

1. Name the **proxy** you will iterate on and the **decisive gate** you will ship on.
2. **Write the ship threshold down before you run the decisive gate.** "Ships only if
   [decisive metric] beats [recorded baseline by ≥ X]" — recorded in `experiment-log.md`
   ahead of the run, not after the number arrives.
3. Record the gate's **minimum detectable effect** and confirm X exceeds it. The sizing
   arithmetic — and what to do when the statistic is binary or is an AP — is in
   `../SKILL.md` → Fit-Check Gate → *Sizing the gate*. If X is below the MDE, the
   experiment cannot answer the question; fix the instrument before spending the run.

## Phase 2: Validate Data

Before spending compute, verify the data is sound:

- [ ] Class distribution — are classes balanced? If not, is that intentional?
- [ ] Label quality — sample 20-50 items and manually verify labels
- [ ] Train/val/test splits — no data leakage between splits
- [ ] Data pipeline — does loading, augmentation, preprocessing produce expected output?
- [ ] Edge cases — what does the model see for ambiguous/hard examples?
- [ ] **Eval-set validity** — does the benchmark actually measure the lever you're pulling? Red flags: a near-ceiling baseline (no headroom to detect improvement), positives generated *from* the answer (queries inherit the answer's vocabulary → trivial match), distractor pools without hard negatives. Verify objectively (e.g., query↔positive lexical overlap) before trusting any score. See `ml-heuristics.md` → Eval-Set Validity.

If data pipeline engineering is needed (ingestion, cleaning, transformation), hand that work to `dev` Build mode (`../../dev/modes/build.md`), then return here.

---

## Phase 3: Baseline

Establish baseline with minimal configuration:
- Pretrained model, default hyperparameters, no augmentation
- Record all metrics in experiment log
- This is experiment #1 — every future experiment is measured against it

---

## Phase 4: Experiment Loop

```
Read experiment-log.md → Change ONE variable → Train → Evaluate → Record → Decide
```

**Rules:**
1. **One variable per experiment** — changing lr AND augmentation AND architecture means you can't attribute the result
2. **Read the log first** — always, every time. This survives context compression.
3. **Record before deciding** — write the result before choosing the next experiment. Prevents confirmation bias.
4. **Stop when criteria met OR diminishing returns** — don't chase the last 0.1% unless the business requires it
5. **Iterate on the proxy, ship on the decisive gate** — use the cheap metric to rank candidates fast, but a candidate only graduates when it clears the pre-registered decisive gate (Phase 1). Never promote a proxy win straight to ship.

**Typical experiment order** (high-to-low impact):
1. Architecture / model selection
2. Data augmentation strategy
3. Learning rate and schedule
4. Batch size
5. Regularization (dropout, weight decay)
6. Fine-grained hyperparameters

---

## Phase 5: Evaluate & Handoff

When convergence criteria are met:
- Run final evaluation on held-out test set (not val set)
- Profile inference performance (latency, throughput, memory)
- Export model (see `ml-heuristics.md` Deployment section)
- Record final results in experiment log

**Handoff to `dev` Build mode** (`../../dev/modes/build.md`) for: inference engine, API wrapper, deployment pipeline, monitoring.
**Handoff to Analyze mode** for: "why do certain classes underperform?", error analysis, failure mode investigation.

**Output contract:** the experiment isn't done until the `experiment-log.md` entry exists (config, metric vs. pre-registered baseline, verdict) and any direction-changing result is in `wiki/decisions.md`. A negative result is a required write, not an optional one. See `../../core/references/wiki-protocol.md` → Output Contract.

### When the experiment says DON'T ship

A pre-registered gate (Phase 1) exists precisely so it can come back negative. **"This change does not ship" is a first-class, successful outcome — not a failure to paper over.** When a candidate loses its gate:

1. **Honor the gate.** You pre-registered the threshold before seeing the result (Phase 1) specifically so you couldn't rationalize a regression into a ship now. Don't move the bar.
2. **Revert cleanly to the baseline** and confirm the baseline number is restored. Keep the rejected artifacts (e.g. `*_rejected/`, gitignored) so a future revisit doesn't start from scratch.
3. **Write the post-mortem as the deliverable.** Record *why* it lost and the mechanism — the negative result is reusable knowledge that stops you (and the next session) re-running a dead end. Put it in `wiki/decisions.md` with a "why it failed — the lesson" note, and add a `wiki/` Rejected Approaches entry if it's a whole direction.
4. **Keep reusable infra.** The harness/optimizer/pipeline you built to run the experiment is still valuable even when the experiment loses — note that it's re-runnable if the corpus/objective changes.

This realizes Integrity Constraint 6 ("Honest failure beats fabricated success") at the experiment level. A sprint that concludes "ship nothing" with a clear post-mortem is a clean win.

---

## Experiment Log

Maintain an append-only `experiment-log.md` in project root. This survives context compression and prevents retrying dead ends.

### Format

```markdown
# Experiment Log

## Goal
[One sentence: what we're optimizing for]

## Current Best
| Metric | Value | Config | Checkpoint |
|--------|-------|--------|------------|
| [e.g. mAP@50] | [value] | [key hyperparams] | [path/epoch] |

## Log

### Exp [N] — [timestamp]
- **Changed:** [what was different from previous]
- **Result:** [metrics]
- **Verdict:** [better/worse/inconclusive — why]
- **Next:** [what to try based on this result]
```

### Rules

1. **Always read the log before starting a new experiment** — this is your memory across context compressions
2. **Update "Current Best" immediately** when a new best is found
3. **Record failures** — "tried X, got worse because Y" prevents retrying dead ends
4. **Keep entries terse** — this file will be read many times

---

## Key differences from `dev` Build mode

| Build Mode | Train Mode |
|-----------|------------|
| Success = tests pass (binary) | Success = metrics meet criteria (continuous) |
| Test → implement → verify (linear) | Experiment → evaluate → adjust (loop) |
| Subagents for separation | Coordinator runs directly (training is sequential) |
| Contract changelog for changes | Experiment log for iterations |
| Adversarial review at end | Analyze mode for result investigation |

Train mode chains into: **Build** (inference engine, deployment pipeline), **Analyze** (why are results bad?), or more **Train** (next experiment).
