# Evolution Log

Retrospectives that turn real engagement experience into skill improvements.

A change distilled from documents carries borrowed confidence; a change distilled from one engagement
carries that engagement's assumptions. Both are fixed the same way: apply the change, then **validate it on
a later, independent engagement**. Until two independent uses confirm it, a change is a hypothesis and its
verdict stays `PENDING`.

Engagement details are summarised by *shape*, not identity — the pattern is the portable part.

---

## Evolution 1 — 2026-06-30 — Birth + same-day dogfood

### Scope

The skill was authored in response to a live enterprise engagement: a response to an **RFI for an
enterprise AI chatbot in regulated financial services**. The framing question — "where does SA work live:
fold it into discovery/client-research/dev, or unify it?" — resolved to a standalone skill composing with
all three (`business-intelligence → ms-ai-discovery → solution-architect → dev`).

Same-day dogfood: a fresh-context critic agent used the v1 skill end-to-end on that RFI and reported as a
harsh critic (~103k tokens, 19 tool uses). It ran Frame + Clarify for real, honored the KB gate with a live
search, built an LLM-hosting options analysis the existing draft never had, and test-filled the response
template. Testing the skill on the very deal that motivated it made the friction real first-use friction.

### Patterns found (severity → impact)

1. **No carrier for the "pair each question with a fallback assumption" rule** — H/L. The register was
   *named* a primary artifact but had no template, and the clarification workflow had no column to hold the
   pairing. Proof it bit: the real workbook had **zero** assumptions against 16 open questions, on an RFI
   that wouldn't be answered before submission.
2. **`nfr-checklist.md` had no Integration & API section** — H/L. The deal's core requirement *was* a secure
   integration layer; the agent had to invent the checklist.
3. **RFI-feeds-RFP strategy absent + win-theme/criteria contradiction** — H/L. Phase 1 said map win themes
   to "how they'll score," but an RFI publishes no criteria → mapped to nothing. The high-leverage move
   (shape the future RFP) was unstated.
4. **"Challenge the brief" ignored source-document provenance** — M/L. The source RFI was partly copy-pasted
   from a different solicitation, leaving leaked out-of-scope sections, duplicate clause refs, and two
   contradictory figures for the same quantity. Nothing told you to audit the source for self-consistency.
5. **Pricing punted to `business-intelligence`** — M/L. A misroute: that skill is client *research*, not a
   costing function.
6. **Traceability self-contradiction + no coverage-status column** — M/L.
7. **No diagram-view guidance; the `drawio` skill uncited** — M/L.
8. **`business-intelligence` skill vs "BI/Power-BI" capability name collision** — M/L.
9. **Approach-declaration ceremony on a small RFI; KB domain list omitted RAG-eval/multilingual** — L/M.
10. **Template shipped fixed numbering while instructing "mirror the client exactly"; no demo block** — L/L.

### Hypotheses applied (all 10, same session)

New `references/templates/assumptions-register.md` + `references/templates/clarification-questions.md` with the paired-fallback
column · Integration & API section in `nfr-checklist.md` · RFI-feeds-RFP sub-mode · source-integrity scan in
Phase 1 · pricing rerouted to the commercial/bid owner · coverage column + RFI-vs-RFP granularity rule ·
diagram views + `drawio` cross-link · BI naming disambiguation · approach gate marked skippable for
single-actor engagements · template renumbering callout + optional demo block.

Kept unchanged as validated-helpful: NFR forcing questions (they surfaced the deal's #1 risk), the
neutral-then-position decision record, the KB grounding gate, and the two-bucket clarification split.

### Validation

- [x] Assumptions register produced and non-empty on a real run. *(Ev.2, and again at 100% coverage in Ev.3.)*
- [x] Integration & API checklist used on an integration-heavy deal. *(Ev.2.)*
- [x] On an RFI-feeds-RFP deal, the response visibly shapes the future RFP's criteria. *(Ev.2.)*
- [ ] Source-integrity scan catches a real document inconsistency. *(Still not observed in either later engagement.)*
- [x] Traceability matrix ships with coverage status and no silent gaps. *(Ev.2, in a richer form than proposed.)*
- [x] No new friction introduced by the added structure. *(Ev.2.)*
- **Verdict:** **KEEP** for the assumptions pairing, Integration & API section, RFI-feeds-RFP sub-mode, and
  coverage column. The source-integrity scan remains **PENDING** after two further engagements — if a third
  passes without exercising it, it should be cut rather than carried indefinitely.

---

## Evolution 2 — 2026-07-14 — Harvest of the completed engagement

### Scope

The *final* deliverables of the Evolution-1 engagement, run to completion by a full bid team across three
client Q&A rounds: a ~50-slide proposal deck, a 15-sheet solution blueprint workbook with a cell-level
change log, a per-environment cloud cost workbook, and three ratified architecture diagrams. This was the
fire-test Evolution 1 was waiting for — the same deal, finished.

### Patterns found

1. **The carrier artifact is a workbook, not markdown files** — H. Traceability, assumptions, questions,
   risks, WBS, RACI and roadmap all converged into one spreadsheet with two sheets the skill never
   mentioned: a **cell-level Change Log** (previous value / new value / reason / source-answer ref) and
   **Source Notes**. The answer-folding loop was the engagement's core discipline and was undocumented.
2. **Scope-treatment vocabulary richer than in/out** — H. Two high-skill treatments recurred: *"in scope for
   design; implementation approach TBC"* and *"capability demonstration / separate readiness track"*. The
   skill had no vocabulary for de-risking by reclassification.
3. **Estimation chain undocumented** — H. Finals priced via WBS MD with a per-package *uncertainty driver*
   column → an explicit effort distribution → blended rate → one-time price, plus per-environment cloud
   sheets and tiered AMS with a retainer floor. Phase 4 had said "size honestly" with no machinery.
4. **Split-region residency posture** — H. The Evolution-1 client finding (a required managed service not
   generally available in the mandated region) resolved into a nameable, reusable pattern.
5. **Defects that shipped = a missing final QA pass** — M. Label/content rows offset by one; internal
   reviewer notes left in cells; a numeric range coerced to a date; a stale currency conversion beside a
   fresh total; deck agenda numbering contradicting the section dividers. All mechanically catchable.
6. **Phase naming in the client's outcome language** — M. A client review renamed Phase 1 from a technology
   label to an outcome label; propagating that term everywhere was the winning move.

### Hypotheses applied

New `blueprint-workbook.md` (sheet inventory, answer-folding loop, change-log discipline, scope-treatment
vocabulary, outcome-language phase naming) · new `estimation-and-costing.md` (the WBS→price chain,
per-environment cloud workbook, AMS tiers, pre-ship sanity checks) · split-region posture added to
`nfr-checklist.md` · Final QA pass section added to `rfi-rfp-response.md` and the close-out.

### Dogfood (same session)

A fresh-context critic walked the updated skill as a first-time user on a hypothetical regulated-market RFP.
12 findings, all applied — notably competing traceability schemas (coverage enum vs scope-treatment columns)
resolved with an explicit mapping rule, and a mis-stated multiplier corrected.

### Validation — resolved at Evolution 3

- [ ] **Blueprint workbook adopted as the carrier on a new engagement** → **NOT ADOPTED.** See Ev.3; the
      cause was over-generalization, not rejection.
- [x] **A risky capability reclassified rather than committed or excluded** → independently reinvented as a
      per-row *deferred scope / tradeoff* column on a delivery WBS.
- [ ] **Estimation chain reproduced** → **NOT REPRODUCED.** See Ev.3.
- [–] **Split-region posture reused or consciously rejected** → **N/A**: the second engagement resolved
      residency by client-owned on-premise hardware instead. The sibling posture is now documented.
- [x] **Final QA pass catches ≥1 defect before shipping** → an independent engagement produced the same
      defect class at volume.
- **Verdict:** **KEEP** for scope-treatment vocabulary and the Final QA pass. **REVISED** for the blueprint
  workbook and the estimation chain — both were correct machinery described as universal; superseded by
  `deal-shapes.md` rather than re-asserted. See Evolution 3.

---

## Evolution 3 — 2026-07-27 — First independent engagement

### Scope

A **fixed-price AI platform engagement with an SME manufacturer** — a different client, team, sector,
country, contract model, and working language from Evolutions 1–2, and the first genuinely independent
validation of anything in this skill. Mid-flight at harvest: proposal delivered, contract and acceptance
annex in drafting, clarification sheet authored but not yet returned by the client.

Two structural differences from the prior trace drove everything: the engagement **began from a factory
visit and a conversation**, not a document; and it ends at a **signed fixed-price contract**, not a
submitted response.

### Patterns found

1. **The skill encoded one deal shape as universal** — H. The workbook and the blended-rate chain were not
   adopted, and the first read was that both Evolution-2 hypotheses had failed. They hadn't. A fixed-price,
   acceptance-gated, hardware-inclusive engagement has its own spine (acceptance criteria, not requirement
   refs), its own carrier (acceptance annex + obligation register, not a 15-sheet workbook), and its own
   pricing chain (lump sum + CapEx, not blended rate). The fix is a selector, not louder insistence.
2. **No front gate** — H. The lifecycle began at Frame, which presumes a formal input. Real engagements
   begin with an informal dump. The evidence is that the project team hand-built exactly the artifact a
   front gate should produce — fact vs inference labelled, buyer motivations, opportunity table, open
   threads — because nothing told them to. **This gap was invisible for two evolutions because both prior
   traces started from a client document.**
3. **Every observed defect was a referential-integrity failure** — H. Not one was a writing failure. The
   same population of acceptance criteria was counted four different ways across four live artifacts; two
   clarification questions cited criteria deleted a revision earlier; ten criteria had no question behind
   them; a translated annex still committed to a whole function the governing-language annex had dropped,
   with six criteria attached; and the cost model still priced that dropped function.
4. **A client-obligation register is a distinct artifact** — H. What the client must physically deliver,
   serving which criterion, by a schedule-relative deadline, with a named focal point. Distinct from the
   assumptions register: an assumption you proceed on, an unmet obligation stops you. Its first rows were
   not logistics but **commercial risk-transfer terms** — defect-severity definitions, T0, change-request
   day rate, standby rate for client-caused delay.
5. **Acceptance criteria carry preconditions and a preparing party** — H. "Which party must provide what,
   before this test is even executable" converts a promise into a dated dependency, and is where
   fixed-price schedule risk actually lives.
6. **There is no universal effort multiplier** — H. A second real distribution came in near **×1.3** against
   the documented **×2.8** — because it excluded requirements analysis and buffer entirely. Neither is
   wrong; presenting either as universal is.
7. **Question columns beyond the pairing rule** — M. 66 of 66 clarification questions carried a paired
   fallback assumption (Evolution 1's flagship change, independently reproduced at 100%), *plus* two columns
   the skill never specified: **impact if the assumption differs**, and the **acceptance criterion served**.
8. **Residency by ownership** — M. Client-owned on-premise compute as a sovereignty posture, with its own
   tradeoffs (CapEx, lead time, lifecycle risk, fixed capacity).
9. **Hardware pricing is a missing chain** — M. Bill of materials with per-line source citation, tax
   treatment, installation labour, contingency, and an explicit answer to who fronts the capital.
10. **Multi-author fragmentation** — M. Four parallel WBS lineages across three authors, and two same-named
    files in different folders whose contents had silently diverged.

### Hypotheses applied (this session)

1. New `references/deal-shapes.md` — the selector; applicability headers added to `blueprint-workbook.md`
   and `estimation-and-costing.md`. (Pattern 1)
2. New `references/engagement-intake.md` + `references/templates/engagement-frame.md`; **Phase 0** added to the
   lifecycle. Includes statement tiering, the negative-space questions, the opportunity→candidate-project
   promotion test, and a **sensitive-inference handling rule** for inferences that damage the relationship
   if surfaced. (Pattern 2)
3. New `references/artifact-integrity.md` — the cross-artifact checks, wired into Phase 5 and the close-out
   alongside (not instead of) the Final QA pass. (Pattern 3)
4. New `references/acceptance-and-contract.md` + `references/templates/client-obligations-register.md`; **Phase 6
   Contract & Acceptance** inserted, Handoff renumbered to Phase 7. (Patterns 4, 5)
5. `estimation-and-costing.md` — the **declare-the-envelope** rule with both distributions shown side by
   side, scenario multipliers as a pricing-options device, a **CapEx/BOM** section, and six new numeric
   sanity checks drawn from observed defects. (Patterns 6, 9)
6. `references/templates/clarification-questions.md` — **impact-if-wrong** and **serves-criterion** columns, binary
   P1/P2 priority. (Pattern 7)
7. `nfr-checklist.md` — **owned-infrastructure residency posture** as the sibling of split-region. (Pattern 8)
8. `artifact-integrity.md` C7 — one carrier per artifact class with a named owner; the same-name-fork
   hazard. (Pattern 10)

### Validation (fill on the next independent engagement)

- [ ] Deal shape is declared before machinery is chosen, and the selector prevents at least one mismatch.
- [ ] Phase 0 runs on an informal-start engagement and produces a frame plus ≤5 asks — and the human reports
      it moved them from fog to a concrete next step.
- [ ] The opportunity→candidate-project promotion test demotes at least one item that would otherwise have
      been scoped.
- [ ] Artifact-integrity checks catch ≥1 cross-artifact defect before it ships (or honestly report clean).
- [ ] A client-obligation register is produced with named focal points, and at least one commercial
      risk-transfer term lands in a contract.
- [ ] The estimation envelope is declared with its exclusions stated, rather than a naked multiplier.
- [ ] The sensitive-inference handling rule is exercised — or consciously found unnecessary.
- **Verdict:** **PENDING.** Distilled from one independent engagement, and mid-flight at that. The
  `deal-shapes` correction is the highest-confidence item (it explains two prior validation failures);
  the front gate is the least tested (its evidence is one hand-built artifact, not a run of the phase).

### Method note

This evolution also corrected the loop itself. Evolution 2's verdicts were written as though non-adoption
would mean the hypothesis was wrong. It didn't — it meant the hypothesis was *scoped wrong*. When a later
engagement declines to use something, the first question is whether it was described too broadly, not
whether it works.
