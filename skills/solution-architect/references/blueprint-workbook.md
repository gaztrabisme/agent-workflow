# The Solution Blueprint workbook — the carrier artifact of a live presale

> **Applies to: the enterprise-bid deal shape** (scored RFI/RFP, multi-round, bid team). On a fixed-price
> delivery engagement the carrier is the acceptance annex + client-obligation register instead — see
> `deal-shapes.md` and `acceptance-and-contract.md`. Don't impose a 15-sheet workbook on a deal that
> doesn't have review rounds to feed it.

On a real multi-week engagement, the markdown artifacts in this skill (traceability, assumptions, questions, risks) don't live as separate files — they converge into **one spreadsheet workbook** that the whole bid team iterates on across client review rounds. The workbook *is* the engagement's working memory; the response deck/document is generated from it. (Validated on a completed enterprise AI-chatbot engagement: the blueprint went v0.1→v0.5 across three client Q&A rounds and was the source of truth for the final proposal deck.)

**Column vocabulary:** in workbook mode the sheet columns below supersede the markdown templates — "working assumption" is the templates' "fallback assumption if unanswered"; the Assumptions sheet's `type` column absorbs the register's basis/confidence nuance. Same contract, one carrier.

## Sheet inventory (the shape that worked)

| Sheet | Carries | Skill reference it implements |
|-------|---------|-------------------------------|
| Executive Summary | Problem, recommended approach, phase focus, guardrails, KPIs — plus **prepared-for/by, date, blueprint status line** | `rfi-rfp-response.md` Response anatomy #1 |
| Requirements Traceability | Req ID · Area · Source requirement · Blueprint response · Mapped use cases · **Scope Treatment** · **Open Item** | traceability matrix |
| Use Cases & Phasing | ID · actor · channels · phase · KPIs · happy-path flow · integrations · data dependency · complexity drivers | `sa-lifecycle.md` Phase 2–4 |
| Solution Architecture | One row per layer: components · design description · indicative technology · dependency/TBC | Phase 3 |
| Scope Split | Scope type · item · description · **treatment** · key assumption | scope-treatment vocabulary below |
| WBS & Estimates | Work packages with MD + **uncertainty driver** column | `estimation-and-costing.md` |
| Roadmap | Stage · theme · **gate** · outcome · dependencies | Phase 4 |
| RACI | Activities × parties | Phase 4 |
| Risks & Mitigations | ID · risk · probability · impact · mitigation · owner | risk register |
| Assumptions & Dependencies | ID · category · statement · **type** (Assumption / Constraint / Dependency / Design invariant / Sizing input / Commercial assumption) · action/owner | assumptions register |
| Open Questions | Priority · category · RFI ref · question · **working assumption** · **status** | clarification questions |
| Commercial & AMS Model | Pricing model options + AMS tiers | Phase 4 commercial inputs |
| Delivery Team | Role · responsibilities · owner (us/client/shared) · mode (on-site/remote) | Phase 4 |
| Source Notes | Every input document + **how it was used** | provenance |
| Change Log | Cell-level: sheet · cell · previous value · new value · reason · **source answer reference** · change type | the answer-folding loop |

## The answer-folding loop (what makes the workbook alive)

Client answers arrive in rounds (Q&A compilations, review-meeting notes). Each round:

1. **Fold every answer into every sheet it touches** — an answer about channels updates Traceability, Use Cases, Scope Split, WBS descriptions, Roadmap, Assumptions, and the matching Open Question. Partial propagation is how workbooks rot.
2. **Move the Open Question's status**: `TBC / Open → Partially Resolved → Resolved`, and rewrite its **working assumption** to reflect what's now known vs still deferred.
3. **Record each cell change in the Change Log** with previous value, new value, reason, and the source-answer reference. (A completed engagement's final workbook carried several hundred logged changes.) This is what lets you defend "why does v0.5 say X when v0.3 said Y" in the evaluation room. It *complements* `wiki/decisions.md` — the change log records what changed and why; decisions.md still owns alternatives considered and rejected.
4. **Add the round to Source Notes** — every input document, dated, with one line on how it was used.

An unanswered load-bearing question never blocks: its working assumption is the position you proceed on, phrased so the client can correct it ("remains TBC for RFP" is a legitimate, *deliberate* deferral on an RFI-feeds-RFP deal — see `rfi-rfp-response.md`).

## Scope-treatment vocabulary (richer than in/out)

The binary in-scope/out-of-scope loses deals on requirements you can neither commit to nor drop. The treatments that survived client review:

- **Base** — committed, priced.
- **Phased** — committed to a later named phase, with the gate that unlocks it.
- **Optional** — priced separately, client elects (AMS tiers, add-on channels).
- **Excluded** — with the *reason* (regulatory boundary, client-owned), never silent.
- **In scope for design; implementation approach TBC** — the requirement is acknowledged and architected for, but the implementation decision is explicitly deferred to the RFP with the decision framed for the client (e.g. media upload — direct in-channel vs a secure-upload workflow).
- **Capability demonstration / separate readiness track** — de-risk a demanded-but-risky capability by committing to *demonstrate* it and run a scoped readiness assessment instead of committing to production (e.g. voice/speech became a separately-sized assessed track with its own decision gate, while the architecture stays "voice-ready").
- **Deferred with a named tradeoff** — the row-level form, useful on a delivery-shape WBS: each work package carries a *"deferred scope / tradeoff"* column naming what is explicitly **not** being committed ("no reranker in this phase"; "throughput target not committed"). Recording a non-commitment where the work is planned is far harder to forget than recording it in a separate scope document.

The last two are the high-skill moves: they answer an RFI requirement *without* either over-committing or conceding a gap.

## Naming phases in the client's outcome language

When the client corrects your positioning, the correction is a gift — propagate the term through **every** sheet and the deck. On one engagement the client reframed Phase 1 from a technology label ("knowledge assistant") to an outcome label ("customer self-service assistant") in a review round; the winning move was renaming the phase everywhere (traceability, scope split, WBS package descriptions, roadmap, deck) so the proposal reads as *their* initiative. A phase named after your tech ("RAG platform rollout") reads vendor-first; a phase named after their outcome reads client-first.
