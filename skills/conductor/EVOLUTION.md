# EVOLUTION — conductor

The ledger. Every change: the trace that motivated it, the edit, and the verdict.
Verdicts are `PENDING` until **≥2 independent real uses** confirm `KEEP`.
Protocol: `../core/references/evolution-loop.md`.

---

## Evolution 1 — 2026-08-06 — Birth: the missing entry point

### Why it exists

The constellation composes correctly on paper — `core` is a real kernel, `harness-operator`
draws the SA/delivery/dev composition explicitly, every sibling disambiguates against its
neighbours on a stated axis. What it had no answer for was the **first move**: a raw intent,
unrouted, with no human deciding which skill owns it. Everything downstream of that decision
worked; the decision itself was made by hand, every time.

The trigger was a request to **merge** the constellation into one skill. That was declined —
`skill-builder`'s own rule ("compose, don't merge; a mega-skill triggers on everything and
disambiguates nothing"), plus three mechanical failures: merging destroys the description-level
disambiguation the siblings were built around, loads ~10,500 lines of markdown on every turn
instead of progressively disclosing it, and collapses seven independent `EVOLUTION.md` verdict
streams into one where nothing can be attributed. The repo's own history is the strongest
argument: root `SKILL.md` *was* one skill, and was deliberately decomposed into `core` +
siblings. A merge is a completed migration run backwards.

The real gap was a **driver**, not a merge — and `harness-operator` already demonstrated the
shape (80 lines, deliberately thin, *"all judgment content lives in the siblings; mine them,
never duplicate them here"*). Conductor is that shape one level up: it covers the whole
intent → product arc rather than the build spine alone.

### Traces it was built from

**T1 — the pattern already worked twice, and was written down nowhere.** A live engagement ran
an 8-agent market validation (2026-08-03) and a 10-agent cost validation (2026-08-06: 6 research
streams + 4 adversarial verifiers, 228 tool calls, bilingual sources) that line-audited a budget
inside a funding document, moved it under 2%, and sourced every line. Both were invented in the
moment from scratch. → `references/task-force-protocol.md` codifies the shape: domain-cut
streams, confidence grades, verdict-vs-assumption columns, refute-instructed verifiers that must
find *uncited* sources, a quote-required section for what research cannot settle, and
propose-don't-apply on anything client-facing.

**T2 — persona fan-out did not exist anywhere.** Grepped the full constellation: zero hits.
`dev/references/subagent-briefs.md` carries research / test / impl / verify / adversarial /
spec-adversarial / mechanical — every one of them *disinterested*. Nothing in the constellation
could surface an objection driven by a stakeholder's incentives rather than by correctness, which
is the class of objection that actually stops deals. → `references/persona-fanout.md`, with the
persona-vs-adversarial distinction made explicit so the briefs don't collapse into each other.

**T3 — the checkpoint placement was set by the user, against the obvious design.** The intuitive
answer to "where should it stop?" is *between phases*. Rejected on a stated reason: *"if it stops
in the middle I don't have the context of what it had been doing so far to make a decision."* A
mid-run stop asks for a decision with hour-old context plus a paragraph — stripped of exactly what
would answer it. → the one-stop-at-T0 design, the `DECIDE NOW` row that front-loads every
foreseeable fork, and the *decide forward / escalate whole* rule.

### What shipped

| # | Trace | Edit |
|---|---|---|
| H1 | T3 | `SKILL.md` — single checkpoint at T0; the Plan Block with `DECIDE NOW` as its load-bearing row; the four legitimate mid-run stops enumerated as a closed list; escalation must be self-contained |
| H2 | T1 | `references/task-force-protocol.md` — stream/verifier briefs, confidence + verdict-vs-assumption contract, engine selection by agent count, propose-don't-apply |
| H3 | T2 | `references/persona-fanout.md` — casting rules, the cold-artifact brief, the five-section return, objection register with presentation/substance/fact typing |
| H4 | — | `references/convergence.md` — the three failure modes (staple / average / lose-the-tail), and the **interaction pass**: does finding A change what finding B means. Nothing in a single thread can see this by construction |
| H5 | — | `references/routing-table.md` — intent→skill map reusing the siblings' existing disambiguation axes (artifact+audience, tense, board) rather than inventing a fourth |

### Verdict: `PENDING` — nothing here has been fire-tested

Authored, not yet run. Two of the five edits (H2, H3) are distilled from real traces; the other
three are design. Per the evolution loop, **distilled ≠ validated**.

### What to watch on the first real runs

- **Does conductor actually fire?** It competes for triggers with `dev` on build-shaped prompts.
  If it loses consistently, the fix is a routing line in the user's global `CLAUDE.md`, not a
  broader description — a broader description is the mega-skill failure arriving by the back door.
- **Is `DECIDE NOW` ever empty on non-trivial work?** That is the single measurable proxy for
  whether H1 works. An empty row followed by a mid-run stop falsifies the whole design.
- **Does the interaction pass (H4) find anything?** If three runs produce no cross-thread
  interaction, it is ceremony and should be cut to a line in the synthesis contract.
- **Does conductor stay out of the domain?** The predicted failure mode is conductor reasoning
  about the work instead of routing it. Watch for it doing research inline rather than dispatching.
- **Does the persona register's presentation/substance/fact split hold?** If most objections land
  in one bucket, the typing is not earning its column.
