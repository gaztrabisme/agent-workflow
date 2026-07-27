# RFI / RFP / proposal responses

*A ready-to-fill skeleton implementing this guidance is at `templates/rfi-rfp-response-template.md` — start there for the document, return here for the why. On a multi-week engagement, these artifacts converge into a single living spreadsheet — see `blueprint-workbook.md` for the sheet inventory, the answer-folding loop, and the change-log discipline.*

## RFI vs RFP — know which you're in
- **RFI (Request for Information):** a market scan. The buyer is gathering options, often won't rank or reply, and dates may be open. Clarification answers may not arrive before your deadline. → Respond to **inform and position**; lean on assumptions; demonstrate domain mastery; don't over-invest in precision pricing.
- **RFP (Request for Proposal):** a scored, binding-track solicitation. → Respond to **win on the published criteria**; precision matters; traceability and compliance are non-negotiable.
- **Direct brief / proposal:** no formal template — *you* impose the structure. Lead with outcome and value.

Misreading RFI for RFP wastes effort on precision the buyer didn't ask for; misreading RFP for RFI loses on scored gaps.

### RFI-feeds-RFP — the real game
When the RFI says it will *issue an RFP based on refined requirements* (very common), the response's highest-leverage job is **shaping that future RFP** so its requirements and criteria favour your differentiators — e.g. by demonstrating that data residency, sector-specific compliance, and evaluation rigour *should* be scored, and framing them as table-stakes. Because an RFI publishes no scoring and "won't rank," **win themes map to the *inferred* RFP criteria** (state the inference), not to nothing. Don't over-invest in precision pricing here, but do invest in setting the agenda the RFP will inherit.

## Response anatomy (map to the client's required structure exactly)
1. **Executive summary** — the outcome, the approach in three sentences, and the win themes. Not a feature dump. The only section some evaluators read in full.
2. **Company / capability** — relevant proof, mapped to *this* domain. Tailor, don't boilerplate.
3. **Solution** — the narrative + reference architecture + options/recommendation. Written explanation is authoritative; diagrams illustrate.
4. **Requirements coverage** — the traceability matrix (below).
5. **Delivery** — phasing/roadmap, roles, risk approach, timeline.
6. **Operational support & commercial** — SLAs, support model, pricing structure (often separate priced attachments).
7. **Assumptions, residency, compliance annex** — state what you assumed and what you commit to.

If the client's template is internally inconsistent or mis-templated, **state your convention and proceed** — don't ask permission for things you can decide.

## Requirements-traceability matrix (proof of coverage)

```markdown
| Requirement (ref) | Client requirement | Coverage | Solution approach & technology | Phase |
|-------------------|--------------------|----------|--------------------------------|-------|
| 4.4.x | <verbatim or tight paraphrase> | Met / Partial / Clarify / Excluded | <how we meet it + which component/tech> | P<n> |
```

The **Coverage** column is the most useful one for an evaluator — and the natural home for "maps to a clarification, not a silent gap" (`Clarify`). A requirement you *can't* cleanly map is `Partial` / `Clarify` / `Excluded` with a reason — never a silent omission. The matrix is the single most persuasive credibility artifact in an enterprise response.

**In workbook mode** (`blueprint-workbook.md`), the Coverage enum generalizes into two richer columns: **Scope Treatment** (Met → Base/Phased; Excluded → Excluded-with-reason; plus the reclassification treatments) and **Open Item** (the home of `Clarify`). Same contract — every ref accounted for, no silent gaps — different carrier; the sheet columns win when the workbook is the artifact.

**Granularity (resolves the 1:1 vs RFI-light tension):** in an **RFP**, one row per requirement — coverage is scored. In an **RFI**, you may *group* closely-related requirements into one row for readability, but every requirement ref must still appear *somewhere* in the Coverage column — grouping is not dropping. Never present a condensed matrix as "full coverage" without every ref accounted for.

## Clarification questions — a positioning instrument

Questions are read by the client as a signal of seniority. Discipline:

- **Dual-purpose:** every question should elicit an answer *and* demonstrate domain understanding. A sharp domain question (e.g. a sector/regulatory nuance most vendors miss) is worth more than five logistics questions.
- **Ask only what the client alone can answer** — priorities, data, success metrics, regulators, integration specifics. **Route or decide the rest** — dates, contacts, document conventions go to your internal partner or get stated as your convention.
- **Business/domain first, logistics last (or omitted).** Order signals what you think matters.
- **Reframe "tell us your config" → "what outcome / what baseline."** "What's today's cost-to-serve and what defines Phase-1 success?" beats "how many systems do you have?"
- **Prune.** A tight set of high-signal questions beats an exhaustive list that buries the good ones.
- **In an RFI, assume some go unanswered** — pair every load-bearing question with an assumption you can proceed on.

Maintain two buckets: **(1) Questions for the client** and **(2) Resolve internally / decide ourselves**. Use `templates/clarification-questions.md` — its Bucket-1 table carries a **"fallback assumption if unanswered"** column so every load-bearing question is paired with how you proceed without it; copy each fallback into the assumptions register.

## Assumptions register

```markdown
| # | Assumption | Why (basis) | Impact if wrong | To confirm with |
|---|-----------|-------------|-----------------|-----------------|
```

Full template: `templates/assumptions-register.md` (adds confidence, linked-question, and impact columns). The register is a **primary artifact** — close-out requires it to reflect every open item, and the high-impact / low-confidence rows surface in the response's assumptions annex. State assumptions confidently and correctably: they convert unknowns into a defensible position instead of a blocked one, and they protect you when an unanswered question turns out the other way.

## Win themes
Three to five, each mapped to a published or inferred **evaluation criterion**, each backed by proof. "Why us" must answer *how the client will score the bid* — domain experience, residency fit, time-to-value, references, total cost — not a generic capability list.

## Final QA pass — before anything leaves the building

Every defect below **shipped in a real final deliverable**. None require judgment to catch — only a deliberate last pass, done by someone (or a fresh-context agent) who didn't author the file:

1. **Label ↔ content alignment.** After rounds of editing, summary tables drift: an exec-summary table shipped one row off — the "Business problem" label held the solution text, and the "Phase 1 focus" label held Phase-2 scope. Read every label/value pair as a pair.
2. **Strip internal review notes.** Reviewer comments — including ones written in the team's own working language rather than the client's — survived in shipped cells. Grep the export for your team's working languages and comment markers.
3. **Recompute totals and currency conversions** from raw cells; a stale conversion shipped next to a fresh one.
4. **Date-coercion scan** on numeric columns: `50-100` range entries can silently become dates (`1950-05-01` shipped as a cost). *(Items 3–4 in full, with the reconciliation chain, in `estimation-and-costing.md` "Sanity checks" — that's the canonical home for the numeric checks.)*
5. **Agenda ↔ section numbering:** the deck's agenda order and its section-divider numbers diverged (agenda said 01 Company Introduction; dividers said "02. Company Introduction" then "01. Executive Summary"). Walk the deck once, only reading numbers.
6. **Version/date consistency** across cover, footer, filename, and status line.

## Anti-patterns
- Feature-matching every clause with no solution narrative or win theme.
- Boilerplate company section not tailored to the domain.
- Silent gaps in coverage (no matrix, or matrix with holes).
- Over-asking the client; asking permission for decidable conventions.
- Precision pricing on an RFI that won't be scored; vague pricing on an RFP that will.
