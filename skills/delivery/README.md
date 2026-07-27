# delivery

An [Agent Skill](https://agentskills.io) for **project management of a signed client engagement** — the
phase between "the proposal was accepted" and "the work is accepted and paid."

Presale produces a forecast. The build produces software. This skill keeps the two attached to each other:
a frozen baseline, progress measured by the client's own signature rather than self-report, change that is
priced instead of absorbed, and client-side delay that is dated and visible rather than silently carried.

It is aimed at **fixed-price, acceptance-gated consulting delivery** — a lump sum, defined acceptance
criteria, payment gated on sign-off. That shape is where the machinery here earns its keep. Internal product
teams running continuous delivery will find most of it unnecessary.

## What it gives you

| | |
|---|---|
| `delivery-baseline.md` | Scope, schedule, cost frozen as the plan of record, with a mobilisation reconciliation checklist |
| `acceptance-tracker.md` | The spine — criterion → status → evidence → signatory, plus defect log, client obligations, and the contract mechanics that must be settled before acceptance starts |
| `change-request-log.md` | Every change with its impact, including the zero-cost ones you absorbed |
| `status-report.md` | Client-facing report with RAG derived from the trackers rather than chosen |

Plus four references: the five-phase lifecycle, honest progress measurement, acceptance execution, and
change control.

## The core idea

On an acceptance-gated engagement, three instruments collapse into one:

```
progress metric   =  acceptance criteria signed / total
acceptance event  =  the same row flipping to signed
invoice trigger   =  the same row flipping to signed
```

A criterion is binary and the client signs it, so there is nothing to inflate — no "90% done for six weeks."
This is the **0/100 rule** applied to a spine that already exists in the contract. The skill's main job is
to stop you building a second measurement system beside it.

## Install

Skills live in `~/.claude/skills/` (or your agent's equivalent):

```bash
git clone https://github.com/<you>/delivery.git ~/.claude/skills/delivery
```

**Dependencies.** This skill references sibling skills by relative path and expects them installed alongside:

- **[`core`](https://github.com/gaztrabisme/core)** — *required.* The shared spine (integrity constraints,
  gate-by-artifact, wiki protocol, evolution loop). Links to `../core/…` break without it.
- **[`solution-architect`](https://github.com/gaztrabisme/solution-architect-skill)** — *recommended.*
  Produces the estimate, acceptance annex, obligations register, and the ID spine this skill baselines.
  Delivery works without it, but you'll be creating those inputs by hand.

## Where it sits

```
business-intelligence → solution-architect ──signed──┐
   (know the client)      (sell the work)            │
                                                     ├──→ [ DELIVERY ]  ── runs continuously
                                                     └──→   dev (build) ── cycles inside it
```

Delivery is **not** the next box after `dev`. It runs concurrently with the build for the whole engagement.

## Maturity

Every hypothesis in this skill currently sits at verdict **`PENDING`**. It was distilled from prior-art
research and practitioner sources, and has **not yet been fire-tested on a real delivery** — and the
fresh-context dogfood gate has not been run either. Both facts are recorded in `EVOLUTION.md` rather than
quietly omitted, because a log that shows its own gaps is worth more than one that doesn't.

Treat it as a well-researched starting structure, not as validated practice. It will be corrected by its
first real engagement, and the corrections will be logged.

## Licence

MIT — see `LICENSE`.
