# Status Report — <engagement> — Cycle N (YYYY-MM-DD)

> Derived from the trackers, not from recall. Every number below should be pointable-at.
> `Grounded: acceptance tracker rows N–M → …`

## Summary

**Status: 🟢 / 🟡 / 🔴** — *one sentence on why, and if not green, what decision is needed.*

| | This cycle | Baseline | Variance |
|---|---|---|---|
| Criteria accepted | __ / __ | __ planned by now | ±__ |
| Progress | __% | __% | ±__ |
| Effort spent (person-days) | | | ±__ |
| Next milestone | | | |

**Variance cause:** *one line. A variance without a cause can't be acted on. Attribute honestly — including
when the cause is client-side.*

**In flight (not counted as progress):** __ criteria submitted, awaiting client response.

## Accepted this cycle

| Criterion | Signed by | Date | Invoice trigger |
|---|---|---|---|
| | | | |

## Awaiting client

The section that makes client-side delay visible. Never omit it, even when empty.

| # | What we need | Serves | Owner | Due | Days overdue | Impact if it stays open |
|---|---|---|---|---|---|---|
| | | | | | | |

*State impact concretely: "blocks acceptance of F3.1–F3.4; each further week moves final acceptance by a
week." Not "may cause delays."*

## Change

| CR | Request | Status | Impact |
|---|---|---|---|
| | | | |

*Absorbed (zero-cost) this cycle: __ · cumulative: __*

## Risks

| Risk | Likelihood | Impact | Mitigation | Owner | Trend |
|---|---|---|---|---|---|
| | H/M/L | H/M/L | | | ↑ / → / ↓ |

## Decisions needed from the client

The most important section. If it's empty, say so explicitly rather than deleting it.

| # | Decision | Needed by | Consequence if late |
|---|---|---|---|
| | | | |

## Next cycle

- …

---

### Reporting discipline

- **RAG is computed, then sanity-checked** — not chosen. Green = within tolerance, no unmitigated
  above-threshold risk, no overdue critical-path obligation. Amber = outside tolerance *with* a credible
  named-owner recovery plan. Red = needs a decision the delivery team can't take alone.
- **Amber has an expiry.** Amber for four cycles is red with better manners.
- **Red is a request, not a confession.** It should arrive with the specific decision needed.
- **Skipped a cycle?** Say so in the next report. Never backfill silently.
