# applied-ml-problem-solver

A [Claude Code](https://claude.com/claude-code) skill for **ML/AI judgment** — deciding whether
an approach is the right one, and whether you could tell if it worked.

It owns the decision questions: what problem is this really, what baseline must I beat, does
this architecture/loss/metric fit, can my instrument see the difference I'm gating on, will
this survive contention in production. It does not write the code — `dev` does that.

## What's in it

| File | Covers |
|---|---|
| `SKILL.md` | Identity, the flow, the gates, anti-patterns |
| `references/ml-heuristics.md` | Problem reframing, label schema, multi-task architecture, metrics (proxy-vs-decisive, discrimination floor, eval-set validity), experiment design, augmentation, deployment export |
| `references/train-loop.md` | Convergence criteria → validate data → baseline → one-variable loop → evaluate, plus the `experiment-log.md` spec and negative-result discipline |
| `references/rag-heuristics.md` | Do you even need RAG, chunking, hybrid retrieval, reranking, contextual enrichment, retrieval eval |
| `references/production-thinking.md` | The layer below, graph-level thinking, systems interaction, scale projection, hardware constraints, operational failure modes |
| `references/templates/eval-harness.md` | Fill-in eval-harness spec |

Two gates are specific to this skill:

- **Fit-Check** — write the problem's shape (signal volume, latency, breadth, budget, failure
  mode, instrument stability) *before* naming a technique. The failure it prevents is silent:
  the library works, the code runs, and the method was never capable of answering the question.
- **Baseline-Named** — name the published thing you'd have to beat, its benchmark number *and
  the protocol that produced it*, and the trivial-to-best span, before building a component
  that decides something a published system already decides.

Both are marked **PENDING** in `EVOLUTION.md`. That is deliberate — see below.

## Install

Clone into your Claude Code skills directory:

```bash
git clone https://github.com/gaztrabisme/applied-ml-problem-solver.git ~/.claude/skills/applied-ml-problem-solver
```

### Dependencies on sibling skills

This skill **references `../core/` and will not resolve without it.** It also points at `../dev/`
and `../conductor/`, which are optional but referenced:

| Sibling | Required? | Where |
|---|---|---|
| [`core`](https://github.com/gaztrabisme/core) | **Yes** — the shared spine (integrity constraints, gate-by-artifact, wiki protocol, grounding gate, pushback-and-teach) | `~/.claude/skills/core` |
| [`dev`](https://github.com/gaztrabisme/dev) | Optional — receives the framed problem and builds it | `~/.claude/skills/dev` |
| [`conductor`](https://github.com/gaztrabisme/conductor) | Optional — routes unrouted intent here | `~/.claude/skills/conductor` |

The grounding gate assumes a knowledge-base MCP server over technical books. Without one,
declare the domain uncovered rather than skipping the gate silently.

## How it evolves

`EVOLUTION.md` is the ledger. It records what changed, why, and **what is not yet trusted**.

Verdicts are honest rather than flattering: a change stays `PENDING` until at least two
independent real uses confirm it, and the ledger names the ones that are still unproven. It
also records the two adversarial dogfoods this skill failed before it passed — including an
arithmetic error in its own sizing rule that would have inflated a required sample size by
~445×, caught by a critic and fixed. A log that shows its own failures is more useful than one
that doesn't.

## Licence

MIT — see `LICENSE`.
