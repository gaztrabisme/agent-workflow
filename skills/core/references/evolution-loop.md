# Evolution Loop

The mechanism that turns a skill from "current instinct / borrowed confidence" into earned, refined judgment. A skill that never ingests its own real traces is frozen at its authoring assumptions; a skill *distilled from documents* is a confident hypothesis until fire-tested. The loop fixes both.

## The loop

1. **Harvest** — gather real traces of the skill in use: build commits + wiki (dev), win/loss debriefs (BI), engagement outcomes vs the distilled claims (SA / ms-ai-discovery), skills authored (skill-builder). Real traces only — not imagined use.
2. **Patterns** — extract what recurred: friction, gaps, contradictions, silent-skip near-misses, things you *needed* that the skill didn't give you. Tag each `Impact: H/M/L, Effort: H/M/L`. Prioritize `Impact ÷ Effort`.
3. **Hypotheses** — turn each kept pattern into a *specific* edit (file + change), not a vibe. "Add an integration-patterns section to nfr-checklist and point Phase 3 at it," not "improve integration guidance."
4. **Apply** — make the edits. Record which pattern each closes.
5. **Validate** — in a *later* harvest, check whether the change is actually exercised in real traces and didn't introduce friction. Only then does its verdict move `PENDING → KEEP` (or `REVERT` with a post-mortem).

## The artifact

Each skill repo carries an **`EVOLUTION.md`** (projects use `wiki/decisions.md` + `log.md`). Same section convention across all skills so they're greppable and comparable:

```
## Evolution N — <date> — <one-line theme>
### Harvest scope        (what traces, why representative)
### Patterns found       (ranked, Impact/Effort, with the proof each bit)
### Hypotheses applied   (each mapped to file(s) changed + pattern closed)
### Validation results   (measured in a later harvest; verdict per change)
```

## The PENDING discipline (the anti-overconfidence rule)

- A change from a **single trace**, or **distilled from documents** and never run, ships with verdict **`PENDING`**.
- It earns **`KEEP`** only after **≥2 independent real uses** exercise it without new friction.
- A change that fails in the field gets **`REVERT` + a post-mortem** recording the *mechanism* of failure, so nobody re-runs the dead end. A documented negative result is reusable knowledge; an undocumented one gets repeated.

This is why `solution-architect` and `ms-ai-discovery` (both document-distilled) must sit at `PENDING` until real engagements validate them — borrowed confidence is not evidence.

## Role variants of "harvest"

| Skill | Harvest source | Turns into |
|-------|----------------|------------|
| `dev` | build commits, wiki decisions/gotchas | mode + heuristic edits |
| `business-intelligence` | win/loss debriefs, deal outcomes | framework/positioning/gate edits — learning about *the skill*, not just the deal |
| `solution-architect` | response outcomes, RFP conversion, dogfood runs | lifecycle/reference/template edits |
| `ms-ai-discovery` | workshop outcomes vs distilled method | method/script edits; validate the PDF's claims |
| `skill-builder` | skills authored + their later EVOLUTION verdicts | convention/checklist edits |

The discipline is identical; only the substrate changes. Keep the loop cheap (one retro per real engagement) — its value is compounding, not ceremony.
