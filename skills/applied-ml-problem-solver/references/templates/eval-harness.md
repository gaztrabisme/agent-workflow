# Eval Harness — template

Fill this in *before* running the thing you are evaluating. `../rag-heuristics.md` calls the
harness the real deliverable; this is its shape. Works for retrieval, classification, ranking
and generation-with-a-rubric — the sections are the same, the metrics change.

Delete any section you deliberately skip **and say why** — a silently missing section reads as
"we covered that."

---

## Decision this eval serves

One sentence: *what choice does a number from this harness change?* If no decision moves, you
are building decoration. Name the decision, not the metric.

- **Absolute score or paired comparison?** An absolute number for a system with no competitor
  is decoration; a paired A/B regression instrument is a tool. Say which you are building.

## Frame — and the reframings you rejected

- **The problem as reduced:** …
- **Rejected:** *<reframing>* — why it fails (one line each). At least one; if nothing was
  rejected you did not reframe, you accepted.
- **Who consumes the output** — a human reader, an agent, a downstream model? This decides the
  match unit below more than any other fact.

## Grounding

One line per search against the substrate (`../../SKILL.md` → Gates):
`KB: searched "<query>" → applied <finding> (book/chapter)` or `→ nothing relevant`.

## Fit-Check

The six-row table from `../../SKILL.md` § Fit-Check Gate, filled. A metric **is** a mechanism,
so this gate fires here. Row 3 (breadth) and row 6 (instrument stability) are the two that most
often force a redesign rather than a tuning change.

| # | Constraint | Answer for this problem | Verdict |
|---|---|---|---|
| 1 | Signal volume | | |
| 2 | Signal latency | | |
| 3 | Signal breadth | | |
| 4 | Budget | | |
| 5 | Failure mode | | |
| 6 | Instrument stability | | |

**Any MISMATCH is a redesign.** Name what it forces.

## Baseline

The three lines from `../../SKILL.md` § Baseline-Named Gate:

1. **Published thing to beat:** name + citation + whether a runnable implementation exists.
2. **Its number and the protocol that produced it** — or `UNVERIFIED-PENDING-LOOKUP` with where
   and when you searched. Log-replay, pooled human qrels and a live trial are different claims;
   say which.
3. **Trivial → best span.** Run the trivial baseline first. A small span caps the whole
   project's headroom, and you want that number before the spend, not after.

## The eval set

| Field | Value |
|---|---|
| Size (n) | |
| How built | |
| **Contamination control** | how items were moved away from the source they were built from, and the **measured** overlap threshold — never "we paraphrased". The leak is domain-specific: for retrieval it is a query generated from the chunk that should answer it; **for vision it is near-duplicate frames, the same camera, shift, scene or identity spanning the train/eval split**; for tabular it is time. Name the leak *your* domain has, then state how the split prevents it |
| Strata | |
| Refresh policy | when it is rebuilt, and what invalidates it |

**Strata table** — one row per archetype, reported per stratum and *never only in aggregate*;
an aggregate hides the stratum that regressed. Include at least one stratum the system is
expected to **fail** (out-of-corpus / unanswerable), or you cannot measure false confidence.

| Stratum | n | How built | Why it exists |
|---|---|---|---|

## Match unit

What counts as a hit — and it must be **what the consumer is actually handed**, not the
internal unit the system indexes. State the adjacency/partial-credit rule explicitly.

## Metrics

| Role | Metric | Why this one |
|---|---|---|
| **Decisive** (the gate) | | the number that decides ship / don't ship |
| **Proxy** (cheap, per-iteration) | | and how you verified it tracks the decisive one |
| **Diagnostic** | | reported, never gated on |

- **Proxy–decisive correlation must be measured, not assumed** — record it, and re-check it
  whenever the system changes shape.
- **Decompose composite metrics.** Report each axis; a composite can hold still while two axes
  move in opposite directions.

## Discrimination floor

The gate is not real until the instrument can see the delta.

**The formula, the n→MDE table, the multiplicity rule, and what to do when your statistic is
binary or is an AP/mAP: `../../SKILL.md` → Fit-Check Gate → *Sizing the gate*.** Not restated
here — a copy of an arithmetic rule is a copy that will go stale, and this one already did
once.

| Field | Value |
|---|---|
| n (paired units) | |
| σ_diff | **measured on run 1** — an assumed σ scales every number here |
| MDE | |
| Number of tests / multiplicity correction | |
| Smallest delta worth shipping | |

If MDE > the smallest delta worth shipping, the harness cannot answer the question. Fix that
before running it, not after.

## Known substrate defects

Anything you found by probing that invalidates a naive design. **Probe before designing; these
are invisible from the abstract.** Examples across domains, so the shape is recognisable:

| Domain | Defect shape |
|---|---|
| Retrieval | a `top_k` not honoured; an index built from different text than is served; a response cap that truncates |
| Vision | labels whose class definition drifted mid-collection; a camera whose exposure or IR cut-in differs by shift; annotations at a different resolution than inference |
| Any | a preprocessing step present in training and absent at eval; a timestamp that is ingest time, not event time |

## Run protocol

- One variable per run.
- Pre-registered gate, written down *before* the run.
- Where the result lands: `experiment-log.md` entry (config, metric vs. baseline, verdict).
- **A negative result is a required write.**
