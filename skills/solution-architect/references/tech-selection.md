# Tech-stack selection & options analysis

The deliverable of a technology choice is not the choice — it's the **defensible comparison** behind it. Architect neutral, then position.

## The method

1. **Derive the axes from the requirement, not the vendors.** What does *this* client actually weigh? Common axes: data residency, customisation/control, time-to-value, scale & cost-at-volume, security/compliance fit, lock-in/portability, team skill fit, ecosystem alignment. Pick the 5–8 that matter here; drop the rest.
2. **Shortlist 2–3 genuinely viable options.** Not one (that's a guess) and not ten (that's noise). Include the "obvious incumbent/aligned" option even if you'll argue against it — it shows you considered it.
3. **Score against the axes, honestly.** Use words or a small scale; cite the *reason*, not just a rating. A cell that says "Limited: no in-country region" beats "Low."
4. **Recommend — and graft.** State the winner and *why the others lost*. Often the right answer is a **hybrid**: primary option for the hard constraint, secondary where it's strongest (e.g. low-code for fast FAQ, pro-code for secure transactions).
5. **Name the design-time checks.** What must be confirmed before commit (regional availability, license terms, a benchmark on the client's own data). These become assumptions or clarification questions.

## Tradeoff-table template

```markdown
| Consideration (axis) | Option A | Option B | Option C |
|----------------------|----------|----------|----------|
| <the hard constraint, e.g. residency> | <reason-bearing cell> | … | … |
| Customisation / control | | | |
| Time-to-value | | | |
| Scale & cost at <client volume> | | | |
| Security / compliance fit | | | |
| Lock-in / portability | | | |

**Recommendation:** <option or hybrid> — <why, anchored to the top axis>.
Use <secondary> for <where it's strongest>.
**Design-time checks:** <what to confirm before commit>.
```

## Decision record (write to `wiki/decisions.md`)

```markdown
## D<n> — <decision title>
**Context:** <the constraint/requirement forcing the choice>
**Decision:** <what was chosen>
**Tradeoff:** <what we give up; what gates it>
**Rejected:** <option> — <why it lost (cost / residency / lock-in / maturity)>
```

The **Rejected** line is the highest-value part — it stops a future session (or a teammate, or the client's challenge) from re-litigating a settled call.

## Neutral-then-position

- Phase 3 (Architect) is **vendor-neutral**: capabilities and patterns, no product names in the reference architecture's logic.
- Positioning is a **separate, explicit** step: map capabilities → a named stack, with the tradeoff table as justification.
- When the deal positions **Microsoft**, pull the stack and commercial framing from `ms-ai-discovery` (its `references/commercial_framing.md`) rather than re-deriving — and keep the neutral comparison visible so the choice stays defensible.

## Anti-patterns

- **Vendor-led design** — the stack you want to sell picks the architecture. Reverse it.
- **Strawman alternatives** — listing options you never seriously considered fools no evaluator.
- **Ratings without reasons** — "Low/Med/High" with no cause is unscoreable and undefendable.
- **Hiding the hybrid** — forcing a single winner when "A for X, B for Y" is the honest answer.
