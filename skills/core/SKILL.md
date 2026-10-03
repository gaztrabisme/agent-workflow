---
name: core
description: "The cross-skill operating contract and reusable gates for every skill author and operator. USE WHEN a rule must apply across roles or a shared integrity gate is needed. Keywords: core skill, shared kernel, evidence, grounding, output contract, wiki protocol, pushback, review gates."
license: MIT
---

# Core — the shared spine

Core defines the cross-skill contract and reusable gates for the people who author and operate role skills. It is a kernel, not a workflow: each role skill names its own artifact and audience, then points to the relevant gates here.

## The spine

1. **Result integrity** — [references/output-contract.md](references/output-contract.md).
2. **Grounding and evidence provenance** — [references/grounding-gate.md](references/grounding-gate.md).
3. **Durable completion records** — [references/wiki-protocol.md](references/wiki-protocol.md) and [references/output-contract.md](references/output-contract.md).
4. **Confidentiality and external claims** — [references/grounding-gate.md](references/grounding-gate.md#confidential-material-and-external-claims).
5. **Decision records and shared memory** — [references/wiki-protocol.md](references/wiki-protocol.md).
6. **Reader-focused writing** — [references/artifact-writing.md](references/artifact-writing.md).
7. **Pushback and teaching** — [references/pushback-and-teach.md](references/pushback-and-teach.md).
8. **Checks and independent review** — [references/grounding-gate.md](references/grounding-gate.md) and [references/output-contract.md](references/output-contract.md).

## How a role skill consumes core

- Name the primary artifact and its audience in the role skill.
- Point to the shared gate that applies; keep its operating detail in the canonical reference.
- Tailor the selected gates and artifacts to the work's context, then state any planned gate that was skipped and why.

## References

- [references/output-contract.md](references/output-contract.md) — result integrity, completion evidence, quality measures, and review.
- [references/grounding-gate.md](references/grounding-gate.md) — grounding, source provenance, check quality, limitations, and external claims.
- [references/wiki-protocol.md](references/wiki-protocol.md) — project memory, decisions, session records, freshness, and roll-ups.
- [references/artifact-writing.md](references/artifact-writing.md) — writing, editing, decision rationale, and audience fit.
- [references/pushback-and-teach.md](references/pushback-and-teach.md) — recommended forks, concise explanation, and task-specific preferences.
