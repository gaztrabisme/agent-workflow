# Estimation & costing — from WBS to a price the deal owner can defend

> **Applies to: both deal shapes, but the chain differs.** The blended-rate chain below is
> **enterprise-bid** machinery. A fixed-price delivery deal prices as a lump sum per phase plus CapEx/BOM —
> see "CapEx and bill of materials" below and `deal-shapes.md`.

SA owns the technical cost drivers (see `sa-lifecycle.md` Phase 4); this is the machinery that produces them. The chain below was validated on a completed enterprise AI-chatbot engagement (high-hundreds of engineering MD → one-time implementation price + per-environment cloud OpEx + AMS tiers).

**Scale to the engagement:** this is RFP / priced-proposal machinery. On an RFI, stop at ranged MD with uncertainty drivers — the blended-rate → price step belongs to the deal's commercial/bid owner (SA feeds it), and the per-environment cloud workbook + AMS tiers are over-ceremony unless the client asked for pricing structure.

## The estimation chain

```
WBS (engineering MD per work package, each with an uncertainty driver)
  → effort-distribution multiplier (engineering MD → total MD)
  → blended rate (total MD → man-months → price)
  → plus out-of-pocket % · cloud OpEx per environment · AMS retainer
```

### 1. WBS with an uncertainty-driver column

One row per work package: `WBS ref · package · description · deliverables · MD · uncertainty driver`. The **uncertainty driver** column states *what has to be true / become known for this number to hold to ±20%* — "API inventory to be determined in RFP", "BM SME availability", "environment count TBC". This turns the WBS into a negotiation instrument: every soft number points at the client input that would harden it, and the drivers double as clarification questions and assumptions-register rows.

Structure the WBS by phase (POC / Phase 1 → Phase 2 → Phase 3), plus **separate tracks for reclassified capabilities** (a readiness-assessment track like voice) and **AMS/hypercare transition setup** — these price separately and the client may drop them without disturbing the base.

### 2. Effort-distribution multiplier — declare the envelope

Bottom-up WBS MD is *build* effort only. Convert to total delivery effort with an explicit distribution.

**There is no universal multiplier.** Two real engagements, both defensible, landed nearly 2× apart — because they were pricing different envelopes:

| Category | Full-lifecycle envelope | Lean-delivery envelope |
|----------|------------------------|------------------------|
| Coding & DevOps (= the WBS MD) | 36% | 76% |
| Testing | 25% | 11% |
| Requirements & analysis | 16% | — *(excluded)* |
| Project management | 13% | 11% |
| Buffer / contingency | 10% | — *(excluded)* |
| **Effective multiplier** | **≈ ×2.8** (÷0.36) | **≈ ×1.3** |

The lean envelope isn't wrong — a small team on a tightly-scoped fixed-price build, where requirements were settled during presale and the client absorbs discovery, genuinely spends less on those lines. It becomes wrong the moment it's presented as if it covered them.

**The rule: a multiplier must name what it includes and what it excludes.** State the exclusions on the sheet, next to the number. Then:

- **Exclusions are risks to state, not savings to book.** "This price excludes requirements analysis and carries no buffer" is a sentence that belongs in the assumptions register *and* in the commercial conversation. Un-named, the first scope surprise eats the margin and the team works it for free.
- **Show the distribution, never a naked multiplier.** A reviewer or client will challenge "×2.8" and accept a five-line table they can argue per-line.
- **Scope the multiplier explicitly.** It applies to the **base build phases**; separately-priced tracks (a readiness assessment, AMS transition) are usually already scoped as total effort — state per track whether its MD is build-only or all-in, so the multiplier isn't double-applied.

Then: total MD → man-months (÷ ~20) → × blended rate → one-time price; add out-of-pocket as a % line (a low single-digit percentage is typical).

### 2b. Scenario multipliers — pricing options without re-scoping

A separate device, and a good answer to *"give me a cheaper number."* Hold the **engineering scope fixed** and vary the *provisioning* around it — typically three columns at ×0.7 / ×1.0 / ×1.3 applied to hardware, cloud, and licence lines:

- **Optimized** — reuse what the client already owns (existing cameras, existing servers, minimum viable tiers).
- **Recommended** — the configuration you'd actually deploy.
- **Full-spec** — headroom for growth, redundancy, larger buffers.

Give each column a one-line description per row saying *what physically differs* ("reuse existing CCTV + 2 pilot units" vs "new units at every station"). Two disciplines keep it honest: **labour stays identical across columns** — if engineering effort changes, that's re-scoping, not a scenario, and it belongs in the WBS; and the cheap column must state **what the client gives up**, not just what they save. A scenario table where only the total moves teaches the client that your prices are soft.

### 3. Cloud cost workbook — one sheet per environment

Estimate cloud OpEx as a workbook with **one sheet per environment** (Dev / QA / Staging / Prod) so the client sees non-prod isn't priced like prod. One row per service:

`Layer · Component · Purpose · Region · Suggested SKU/tier · Sizing driver · Billing note · Estimated monthly (min–max)`

Discipline that made it defensible:

- **Min–max ranges, not point estimates**, for every usage-based line; totals as min/max per month and per year.
- **Flag the dominant meter** — mark the line that will actually drive the bill ("Billed — dominant" on the LLM tokens line; "watch this one" on log ingestion). One or two lines usually dwarf the rest; the client should see you know which.
- **`Verify` flags** on lines that depend on client licences or unconfirmed plans (existing ExpressRoute circuit, Defender plans, DevOps licences).
- **BYOL / client-provided exclusions stated per line** ("identity platform — existing client licences — Included/BYOL") and echoed as a commercial assumption — this is where double-charging accusations die.
- **Environment zeroing with a reason** — non-prod lines set to 0 with "no need in Dev", not silently deleted, so sheets stay row-aligned and diffable across environments.
- **Sizing driver per row** (tokens/min, RU/s, GB/day, MAU) — ties every number to the volume assumption (sessions/month, peak uplift) in the assumptions register.

### 4. AMS pricing shape

Tiered catalog + retainer floor, aligned to the support NFRs (`nfr-checklist.md` Observability/operations):

- **Tiers:** Bronze (business-hours L2/L3, incident mgmt, monthly report) → Silver (+ content/eval operations: KB refresh, golden-set regression, prompt tuning) → Gold (+ release mgmt, enhancement backlog, quarterly roadmap). For AI solutions the Silver content-ops tier is the quality-sustainability recommendation — the model degrades without it.
- **Retainer floor:** a minimum monthly charge (e.g. 3 man-months/month standby inside an annual package); effort above the floor billed on actuals with per-ticket effort norms (L2 ≈ 0.5 MD, L3 ≈ 1–5 MD).
- **Escalation commercial edge:** name the on-site trigger ("if unresolved after 24h of restoration effort") and mark its commercial treatment TBC rather than absorbing it silently.
- L1 in/out of scope stated explicitly; severity/SLA matrix (P1–P4 response/resolution + SLA %) attached.

### 5. CapEx and bill of materials (when hardware is in scope)

Cloud-only deals price consumption. On-premise, edge, and manufacturing deals put **hardware on your invoice** — often the largest single line — and it prices nothing like software. One row per item:

`Group · Item · Specification · Qty · Unit price (ex-tax) · Tax % · Total ex-tax · Total inc-tax · Source/URL · Notes`

- **Cite a source per line.** A URL or quote reference per item is what survives the client's own procurement team pricing it independently. Unsourced hardware numbers get challenged and you lose the room.
- **Show ex-tax and inc-tax separately.** Local sales tax/VAT is often reclaimable for the client and not for you, and mixing the two is the fastest route to an argument about a number nobody disputes.
- **Add an explicit contingency line** with its own percentage, and say whether sub-groups carry their own. Hardware prices move between quotation and purchase.
- **Installation and mechanical work is a line item**, not an afterthought — cable routing, drilling, mounting, wiring, calibration. On a factory floor this is routinely a fifth of the hardware cost.
- **Decide and state who fronts the capital.** Client purchases directly (you spec it) · you procure and hand over at cost · you procure with a stated markup. Each has different cash-flow, warranty, and ownership consequences, and the warranty path must be named: who replaces a failed unit in month 9, and against whose warranty?
- **Name the ownership and residency consequence.** Client-owned on-premise hardware is a *residency posture* (see `nfr-checklist.md`) as well as a cost line — often the whole reason the deal is winnable.

Hardware is CapEx and behaves differently from the labour chain above: it doesn't take the effort multiplier, it doesn't scale with scope changes the way effort does, and it usually has a longer lead time than any software task. Track its lead time as a schedule dependency in the obligation register (`acceptance-and-contract.md`), not just as a cost.

## Presentation split

The response shows **CapEx** (one-time implementation + hardware + out-of-pocket) and **OpEx** (cloud consumption per environment + AMS) as separate tables. When the client prefers a subscription-model comparison, present subscription as the primary comparison basis and usage-based as supplementary sensitivity — mirror *their* preferred commercial lens, don't impose yours.

## The capacity-fit gate — the one that hides best

**No input assumption may be selected because it makes the total fit the capacity.**

When an estimate closes only *after* an assumption moves, name the assumption, put the client's own stated
figure beside it, and re-derive. If it still doesn't fit, the output is **"it doesn't fit, by N MD"** —
that is a finding, not a failure, and it is the most useful thing you can hand a deal owner.

This applies identically to an efficiency or productivity factor. **A factor calibrated until the gap
closes is the same defect wearing a different hat**, and it is harder to spot because it looks like
craft rather than arithmetic.

> *Observed, twice in one engagement.* The client said on the record: *"there's about 200 data fields the
> user is going to use and it needs to be verified."* The estimate assumed a 40–60 field set — which made
> the work fit the window, and broke the headline claim the scope existed to make, since "200 → 25 flagged"
> only holds if the denominator really is 200. Caught by a cold review. Re-priced at 200, the requirement
> came to 72 MD against 58 available — and closed to 59 via a 0.7 productivity factor applied to a
> selected subset of packages. Same reflex, second costume.

The tell: you changed an input and the total landed within a rounding error of capacity. Write down what
the number was *before* you touched the assumption, in the same table. If a reader can't see the
pre-adjustment figure, the adjustment isn't an estimate — it's a target.

## Sanity checks before the numbers ship

This is the canonical home for the numeric checks. All of these have shipped in real deliverables.

- Recompute every total and **every currency conversion** from the raw cells — a stale conversion shipped next to a freshly-updated total in the other currency.
- Spreadsheet range-entry hazard: `50-100` typed into a numeric cell can coerce to a **date** (`1950-05-01` once shipped as a cloud line-item cost). Scan cost columns for date-typed cells before export.
- The WBS total, the distribution table, and the priced man-month figure must reconcile to one chain — a reviewer who finds two different totals stops trusting all of them.
- **Effort units must agree across sheets.** One workbook labelled a line "Labor (299 mandays)" on the summary sheet while the detail sheet summed to **57**. Both numbers were live; only one was right.
- **Read every summary label against its own content.** A row labelled "Labor (incl. contingency + overhead)" sat above a breakdown whose contingency and overhead rows were both **zero**. The label promised what the arithmetic didn't contain.
- **One formula per concept.** The same workbook defined maintenance twice — "15% of development + hardware" on the summary, "10% of development" on the detail sheet — producing two different numbers for the same line.
- **Zero-priced rows carrying a non-zero effort note.** A feature priced at 0 across every column, with a note reading "37 mandays", is either free work you're about to do or a scope item that shouldn't be listed.
- **Reconcile the price list against the commitment artifact.** Every priced function must appear in the acceptance annex and vice versa — see `artifact-integrity.md` C6. Pricing a function that the current annex has dropped is a live commercial exposure, and it has happened.
- **Proofread client-facing feature names.** A misspelled capability name propagates from the cost model into the deck and the annex, and it is the one defect every reader notices.
