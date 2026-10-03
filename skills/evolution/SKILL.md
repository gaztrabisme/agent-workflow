---
name: evolution
description: "A real-use learning loop that produces EVOLUTION entries, testable hypotheses and settled verdicts for a skill owner. USE WHEN repeated real-use evidence, a recurring correction, or an open verdict needs review. Not `skill-builder`, which creates or reshapes the skill; not `core`, which defines shared gates. Keywords: evolve, evolution, retrospective, harvest, EVOLUTION.md, PENDING, KEEP, REVISED, REVERT, improve a skill, lessons learned."
license: MIT
---

# Evolution

Evolution turns a skill’s real-use evidence into an auditable change proposal and a later, evidence-based verdict. Its artifacts are a dated `EVOLUTION.md` entry, a whole-set approval block, small attributable edits, and settled verdicts for the skill owner.

> Inherits the shared `core` kernel. Follow its integrity constraints and reference its gates; do not copy their operating text here. See [`../core/SKILL.md`](../core/SKILL.md).

## When it fires — and when a sibling owns it

- Use this for repeated real-use evidence, a recurring correction, or an open verdict on a skill that has been used. Explicit requests to evolve skills and repeated skipped gates also trigger review. A stale `PENDING` matters when the skill has seen use since the last entry. [book:site-reliability-engineering], Google’s Postmortem Philosophy
- `skill-builder` owns a skill’s initial structure, source distillation and authoring-time ledger entry. Evolution owns later entries grounded in use.
- `core` owns the shared operating contract and canonical gates; Evolution owns the loop that applies that contract to a skill’s evidence.

> **Disambiguation:** artifact and audience. `skill-builder` produces or reshapes a skill package for its author. Evolution produces an evidence-backed change record and settled verdict for the owner of a skill already used in real work.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| 1. Triage | Test eligibility, weigh signals, set scope and name exclusions | Evidence table with one reason per pick and skip |
| 2. Settle | Resolve eligible open verdicts before new pattern work | Updated prior entry or reasoned `PENDING` |
| 3. Harvest | Read bounded, real-use traces and assess their quality | Trace register and harvest brief |
| 4. Patterns | Find causes and recurring effects; prioritize by impact and effort | Ranked pattern list, including rejected candidates |
| 5. Hypotheses | Turn kept patterns into separate, falsifiable edits | One whole-set approval block |
| 6. Apply | Make approved, small, reversible changes | Attributable changes in the skill repository |
| 7. Record | Preserve the result and leave new claims unproven | Dated `EVOLUTION.md` entry with future checks |

A requested one-skill trim may skip broad triage and full harvest, but must settle prior open verdicts and register its supplied trace before approval; use the trim’s record rules in [`references/loop.md`](references/loop.md). (derived: dogfood 2026-10-01) A full evolution request uses the full loop. Scope effort to impact and review capacity; do not impose a fixed skill-count cap. Detailed rules live in [`references/loop.md`](references/loop.md) and [`references/triage.md`](references/triage.md).

## Gates

- **Grounding gate** — record the traces and period examined, their provenance, and what they changed. See [`../core/references/grounding-gate.md`](../core/references/grounding-gate.md).
- **Output Contract** — the durable result is the skill’s dated ledger entry and its reviewable evidence. See [`../core/references/output-contract.md`](../core/references/output-contract.md) and [`../core/references/wiki-protocol.md`](../core/references/wiki-protocol.md).
- **Pushback and Teach** — explain the mechanism when a requested edit would weaken a shared constraint. See [`../core/references/pushback-and-teach.md`](../core/references/pushback-and-teach.md).
- **Evolution gate (owned here)** — applied or document-derived changes remain `PENDING` until a later run settles them using qualifying real-use evidence. See [`references/loop.md`](references/loop.md).
- **Core reference rule** — link to shared gates instead of restating or duplicating them. [book:clean-code], Don’t Repeat Yourself

## Anti-patterns

- Treating a no-trace skill as stale, or inventing real-use evidence.
- Settling yesterday’s change on application day, or leaving a `PENDING` verdict without a reason and owner.
- Treating counts as conclusions, collapsing unlike measures, or letting an instrument choose a verdict.
- Bundling hypotheses, hiding rejected patterns, or applying edits before the approval stop.
- Treating non-adoption as proof of invalidity before checking scope, discoverability and weight.

## Composition

- **Consumes:** the target skill’s ledger, version history, relevant task traces, and any project records that contain evidence of how the skill was used.
- **Hands off:** initial structure and source-distillation work to `skill-builder`; shared gate definitions remain in `core`.
- **Re-entry:** a skill excluded by the no-trace gate can return only on traces the evolution run itself creates. Suspicion alone is not evidence.

## References

- [`references/loop.md`](references/loop.md) — phase order, verdicts, validation and role-specific evidence.
- [`references/triage.md`](references/triage.md) — signals, limits, selection and scope.
- [`references/hypothesis-protocol.md`](references/hypothesis-protocol.md) — hypothesis fields, approval authority and application.
- [`references/templates/harvest-brief.md`](references/templates/harvest-brief.md) — evidence-gathering brief and pattern questions.
- [`references/templates/approval-block.md`](references/templates/approval-block.md) — the single whole-set decision record.
- [`references/templates/EVOLUTION.md.skeleton`](references/templates/EVOLUTION.md.skeleton) — append-only ledger entry shape.
- [`scripts/triage.py`](scripts/triage.py) — summarizes an explicitly supplied, harness-neutral trace manifest.
