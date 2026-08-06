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

---

## Evolution 4 — 2026-07-29 — The recipient axis; rigour aimed at the wrong reader

### Harvest scope

**A competitive, vendor-brokered presale for a document-extraction and verification platform** — a Big-4
professional-services client in South-East Asia. Fixed-price delivery shape. Genuinely independent of Evolutions 1–3: different client, sector,
country, team, language, and broker. The skill ran **end to end** — Phase 0 intake through a priced
3-week estimate, plus a research fan-out and a cold adversarial review.

Two hard signals, both from practitioners rather than self-assessment:

1. **The delivery PM rejected the primary artifact and rebuilt it himself** — *"đọc mấy cái hiện tại anh
   thấy kiểu ko liên quan đến implementation mà liên quan đến governance và process hơn"* ("this is
   governance and process, not implementation"), *"máy móc quá"* (too mechanical), *"AI suggest a thấy nó
   ko hợp lý"* (the AI suggestion doesn't look sensible).
2. **The engagement owner lost the thread.** Asked for a scope list and a man-day estimate, received 11
   markdown files totalling 22,400 words: *"I'm lost in the middle… I thought we just need to make a WBS?
   Did Tri just push more tasks to us?"* — and diagnosed the style as *"too many proses, narratives, and
   showing someone insecure trying too hard to justify and prove themselves."*

### Patterns found

1. **Recipient-blindness — H/L.** The skill selects machinery by *deal shape* and has no axis for **who
   picks the artifact up next and what they must decide**. `composition.md` hardcoded one downstream
   consumer (`dev`). The rejected workbook was Summary · Scope-In · Scope-Out · WBS · Capacity ·
   Assumptions · Obligations · Risks — **three sheets about the work, five about defending the number.**
   Correct for a client evaluator; noise to a PM distributing tasks to discipline leads.
   *Not a wrongness result — a selector result (`evolution-loop.md` §non-adoption).*
2. **The instrument/argument distinction — H/M.** The adopted artifact's effort column is **empty: 0
   numeric cells across 234 task rows**, yellow-highlighted, with a fill legend and a calibration anchor.
   Ours pre-filled it, pre-derived capacity, collapsed releases to one and pre-decided the cut order. An
   architect who fills the effort column has answered a question the PM owns.
3. **The teaching mandate has no channel boundary — H/L.** `core/references/pushback-and-teach.md` is
   written for one developer in a chat window and is inherited unchanged. Justification migrated into
   cells and into a parallel prose corpus. Measured density, cells ≥12 words: **PM 0.49% · peer
   practitioner 2.2% · our rebuild 10.3% · our rejected version 21%.** Adoption tracks that column
   monotonically. Literal instance in a client-bound scope document: *"This is a disclosure, not a hedge."*
4. **An input assumption reverse-engineered to fit capacity — H/L, and it recurred.** The client said on
   the record *"about 200 data fields… needs to be verified"*; the estimate assumed 40–60, which made the
   work fit and broke the headline claim. Caught by cold review. Re-priced at 200 → 72 MD against 58
   available → closed to 59 by a 0.7 productivity factor on a selected subset. **Same reflex, second
   costume.**
5. **Integrity checks present, correct, and never executed — H/L.** Three live values for total effort
   (106/120/121) across four artifacts; an orphaned `AC-11`; two live assumption registers; a `D-` prefix
   collision created by accommodating the PM's vocabulary; and a reconciliation section asserting
   `58 = 58 ✓` three sections below a total row reading **59** — while the project instructions stated
   *"numeric reconciliation has been run."* **A false clean report.**
6. **Artifact proliferation defeats the integrity machinery — M/L.** Reconciliation cost grows with the
   square of the artifact count. 11 documents + 2 workbooks + a 75-row manifest against a two-item ask.
7. **Coverage-matrix polarity — M/L.** Our *"4 covered, 4 partial, 5 minimal, 3 out"* and his *"GAP items
   are where we differentiate"* are the same arithmetic. One is a confession.
8. **Formula regression — M/L.** Our rebuild shipped **0 formulas** (a deliberate fix for blank cached
   values); the PM's has 226, the peer practitioner's 27. Literal-only workbooks lose the self-checking
   property, which was the reason the numbers were trustworthy.

**Not a pattern, and worth recording:** the PM's replacement was itself machine-written (`creator:
openpyxl`, never opened in Excel). He did not object to a machine-made artifact — he objected to *that
specification*. Every failure here is reachable by editing the skill.

### Hypotheses applied

| # | Change | File(s) | Pattern |
|---|---|---|---|
| 1 | **Axis 2 — declare the recipient**, with the four-recipient table and the declaration line | `deal-shapes.md`, `SKILL.md`, `sa-lifecycle.md` Phase 0 | 1 |
| 2 | **Downstream is four consumers, not one** — incl. the pre-signature PM and `delivery` (which upstream had wired into `SKILL.md` but not into this file) | `composition.md` | 1 |
| 3 | **New: the WBS as a collection instrument** — effort column ships empty, formula summary, capacity sheet, two-direction traceability | `templates/delivery-wbs-workbook.md` | 2, 8 |
| 4 | **Two channels** — the WHY belongs in conversation and `decisions.md`, never in a deliverable; ≤1 prose cell per 100 | `../core/references/pushback-and-teach.md` | 3 |
| 5 | **The capacity-fit gate** — no input assumption selected because it makes the total fit; a calibrated factor is the same defect | `estimation-and-costing.md` | 4 |
| 6 | **The check must execute, not narrate** + **C8 one namespace per concept** | `artifact-integrity.md` | 5 |
| 7 | **Ask ledger** — anything beyond the ask is *proposed*, not produced | `SKILL.md`, `sa-lifecycle.md` | 6 |
| 8 | **Traceability polarity** — Origin column, gaps lead, run both directions | `rfi-rfp-response.md` | 7 |
| 9 | **Tier in the schema, not the prose** — `*_reported` fields and an asserted invariant | `../core/references/grounding-gate.md` | 5 |
| 10 | **Cold review before a primary artifact ships**; Wu Wei extended to engagement artifacts | `../core/SKILL.md` | 6 |

### Validation — Evolution 3's checklist, resolved

| Ev.3 item | Result |
|---|---|
| Deal shape declared before machinery; selector prevents ≥1 mismatch | **PASS.** D-001 declared fixed-price delivery and *explicitly rejected* the blueprint workbook and blended-rate chain as *"ceremony instead of leverage on a 3-week window."* Second independent use → **`KEEP` candidate.** |
| Estimation envelope declared with exclusions, not a naked multiplier | **PASS.** Five-line distribution, ×1.55 effective, exclusions stated as risk not booked as saving. Second independent use → **`KEEP` candidate.** |
| Phase 0 runs on an informal start; fog → concrete next step | **MIXED.** The frame was produced and both parties worked from it; *"I'm lost in the middle"* is counter-evidence on the second half. → `PENDING`; hypothesis 7 addresses it. |
| Artifact-integrity catches ≥1 defect, or honestly reports clean | **FAILED — worse than not run.** Not executed; a false clean report shipped. → **`REVISED`**: the checks are correct, the execution mode is wrong (hypothesis 6). |
| Sensitive-inference rule exercised | **PASS, with a gap.** Exercised with a named holder — but left sitting in `docs/`, the folder the client deck gets built from. → `PENDING`; it needs a location rule, not just a label. |
| Client-obligation register with named focal points; ≥1 risk-transfer term in a contract | **PARTIAL.** Register produced with deadlines and blocking effects; no contract reached. → `PENDING`. |
| Opportunity→candidate-project promotion demotes ≥1 item | **Not observed.** Carry forward. |
| Source-integrity scan catches a real document inconsistency *(open since Ev.1)* | **REVISED, not cut.** Third engagement without firing *as specified* — but it fired against **our own** inherited artifacts: a proposal deck shipped carrying another client's RACI (including a "Shariah review" row) and a chatbot engagement's phasing, and a Q&A workbook carrying a third engagement's requirements. → broaden from "audit the client's source document" to "audit any inherited document, ours included." |

### Validation (fill on the next independent engagement)

- [ ] Recipient declared in Phase 0, and the primary artifact is **accepted by that recipient rather than rebuilt**. *This is the real test.*
- [ ] Where the recipient is a delivery planner, the effort column ships **empty** and comes back filled.
- [ ] Primary artifact scores **≤2% of cells ≥12 words**, and any summary sheet carries formulas.
- [ ] Integrity checks run **as a script**; the result is the artifact's, not a typed ✓.
- [ ] An estimate that does not fit is reported as *"doesn't fit, by N MD"* rather than closed by moving an input.
- [ ] Artifact count matches the ask ledger; anything beyond it was proposed and accepted first.
- [ ] A cold review runs before a client-bound artifact ships, scored against pre-registered weaknesses.
- **Verdict: `PENDING`.** One trace. Two Ev.3 items reach `KEEP` candidate on a genuine second independent
  use; the integrity execution mode is `REVISED`; everything authored here is unvalidated.

### What was deliberately not changed

The rejected artifact was not over-rigorous — it was **rigorous at the wrong reader**. Strip the argument,
not the analysis. Held intact: `artifact-integrity.md` in full (every check fired as a live defect; the
failure was non-execution); the capacity chain, which the adopted benchmark lacks entirely — 165 tasks
tagged for one release against a 15-day window with no denominator anywhere; the uncertainty-driver column;
`decisions.md` with rejected options — **hypothesis 4 moves justification *into* that file, and if it is
ever implemented as "write less" it has failed**; the declared cut order and committed-vs-upside criteria;
and Phase 0 intake, which no failure implicated.

Also held: **D-002, "MVP, never POC."** The adopted benchmark labels 56 tasks `POC` and is wrong against
the buyer's twice-recorded words. Recorded here so that *"adopt his shape"* is never later misread as
*"adopt his content."*

### Cross-skill note

`delivery`'s principle 7 — *"the engagement is one graph… never invent a second numbering system"* — was
violated **in presale, by SA**, before delivery existed. The fix lands in `artifact-integrity.md` C8, not
in `delivery`. **First pass concluded `delivery` had no harvestable evidence here because the trace never
reached signature; that was corrected** — see `delivery`'s Evolution 1. No *execution* trace is not no trace:
the delivery planner's pre-signature behaviour tests the SA↔delivery seam, which both skills had drawn by
inference and both had drawn wrong.

---

## Evolution 5 — 2026-07-30 — Same engagement, next day: the recipient accepted the artifact

### Harvest scope

**The same engagement as Evolution 4, one day later** — the day the rebuilt artifacts actually met their
recipients. Not an independent trace, and its value is not confirmation: Evolution 4 closed with a
seven-item checklist marked *"fill on the next independent engagement,"* and six of those items got real
evidence within 24 hours. **This is the validation window Evolution 4 asked for, arriving early.**

Traces: two architecture diagrams through **three practitioner review rounds** (solution architect, then
delivery PM); a WBS through **three rebuilds** driven by recipient feedback; a client-facing deck a colleague
built from our output; a Teams thread in which the team made two scope decisions and reversed two recorded
ones; and a transcript re-read that found a second instance of a defect class purged the day before.

### Validation — Evolution 4's checklist, answered

| Ev.4 item | Result |
|---|---|
| **Recipient declared; the primary artifact is accepted by that recipient rather than rebuilt.** *"This is the real test."* | **PASS.** The PM reviewed it, asked three clarifying questions, flagged one defect, made two scope decisions, then **took ownership** — *"khi anh xong cái file slide, thì em work trên cái slide luôn đi, đừng work trên file WBS nữa."* He did not rebuild it. ⚠ It took **three in-session iterations** to get there, so the hypothesis is validated at the artifact level, not first-pass. → **`KEEP` candidate** (second use, and the decisive one) |
| Effort column ships **empty** and comes back filled | **REVISED.** It shipped *absent*. The PM asked for *"not MD est but grouped by week."* Filled/empty was a false binary; **schedule position** is a third form and the right one when duration is the unknown. Machinery survives, applicability named → new selector at `PENDING` |
| ≤2% of cells ≥12 words; summary carries formulas | **MIXED → REVISED.** First cut failed loudly, with the reviewer quoting my own banner rows back. Passed only after an `assert` was put in the generator. The metric is right; **the mechanism was missing.** Formulas: still zero — pattern 8 of Ev.4 **unresolved and now twice-observed** |
| Integrity checks run **as a script** | **PASS.** Three gate scripts run after every edit; the index gate *failed twice* on real omissions and that failure was the gate working. Generator asserts caught a dangling dependency. → **`KEEP` candidate** |
| An estimate that does not fit is **reported**, not closed by moving an input | **PASS, in a new form.** Work landed in W5 against a publicly-stated four weeks, left visible in the grid. Separately, a broken numbers chain was left broken behind a *stale-at-the-premise* banner rather than force-reconciled |
| Artifact count matches the ask ledger | **FAILED, then fixed in-session.** The workbook accreted all five jobs `delivery-wbs-workbook.md` §8 warns about. **The author had read that warning.** |
| **Cold review before a client-bound artifact ships** | **FAILED, with a cost.** A colleague's client deck shipped embedding a stale diagram export whose rule count was wrong — and wrong again in the body text beside it. No cold review ran on it |

**The last two are one finding: a prose warning fails silently.** This is precisely the mechanism
`grounding-gate.md` already documents for provenance tiering — *"prose rules fail silently at scale"* — now
observed a third time, in a third place. The correction is always the same shape: make it countable, or make
it execute.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **Effort has three representations, not two.** The empty column assumes the window is fixed and effort unknown. When *duration* is the unknown, the instrument is a week grid, and bars spilling past the committed number are the planner's verdict — derived, not argued | H/L | *"not MD est but grouped by week"*; work landed in W5 against a deck stating four |
| 2 | **A time marker inside a structurally-ordered list is a false claim.** Horizontal milestone banners read *"everything above is complete"*; rows grouped by feature run three weeks past them | H/L | PM: *"chỗ title End W1 nhưng task a thấy qua mấy W2 và 3,4."* **The reference schedule he had himself supplied already showed the correct pattern** — a vertical band in one week column. Right example in hand, wrong shape used |
| 3 | **The accretion warning is prose and failed on its own author.** §8 names the five jobs and calls the outcome *"exactly how an eight-sheet workbook gets built and rejected"* | H/L | Shipped obligations-with-consequences, a risk register, a cut order, commercial assumptions and a status banner into an engineering task inventory. Recipient: *"we just went out of our lanes"* |
| 4 | **Out-of-lane is a distinct failure from too-long, and trimming does not fix it.** Every offending row was short, accurate and well-written — and aimed at a different reader | H/L | The prose budget had *already* been applied to those rows; the lane problem survived it untouched |
| 5 | **A `Confirmed` tier with no named speaker is not confirmed** — and the same defect class recurred one day after being purged | H/L | *"~80%"* purged 29 Jul; *"~10 Sep"* found 30 Jul, tiered **Confirmed** as the engagement trigger. Transcript: the **broker** says *"within September"*; **our own account lead** says *"the 10th September"*; the client's *"Correct"* answers a remark about decision timing. No client voice states the date |
| 6 | **A defect description propagates like any other ungrounded claim.** *"106 / 120 / 121"* was copied into four files; `106` existed **nowhere** | M/L | Grep. The real defect was two totals and was **definitional, not arithmetic** — one counted capacity, the other requirement. Unresolvable from a description that was fiction |
| 7 | **Two registers for two audiences is correct; C8 as written would merge them** | M/L | Engineering assumptions (build-changing) vs proposal assumptions (client-correctable) share almost no rows and serve different readers |
| 8 | **Fixing a namespace collision unblocks the register that owns it** | M/L | Moving dependencies off `D-` is what made the next decision ID mintable; the project had frozen `D-` while ambiguous |
| 9 | **Numbers inside images are ungreppable, so the completeness search is blind** | H/L | A corrected count could not be found in a `.pptx`; recovery required parsing the archive and reading the image |
| 10 | **A colleague's client-facing artifact stating a position *is* the decision once sent** | M/L | A deck stated three assumptions that reversed two recorded decisions (tenant, ground-truth ownership). Captured as a decision record rather than treated as input |
| 11 | **Every column must be readable by the recipient without a glossary** | M/L | *"What does T0-1 here mean?"* (an internal package ref) and *"how to read Priority and do we even need it?"* — both dropped |
| 12 | **Handover inverts "regenerate, don't hand-edit" into a destructive instruction** | M/L | The PM took the file; the index still said regenerate; the next run would have destroyed his edits |

### Hypotheses applied

| # | Change | File(s) | Pattern |
|---|---|---|---|
| 1 | **Effort has three representations** — filled / empty / **schedule position**, with a selector and the `N+2` column rule | `templates/delivery-wbs-workbook.md` §0; `../delivery/references/delivery-lifecycle.md` Phase −1 | 1 |
| 2 | **Milestones live on the time axis**, never as horizontal bands | same, both files | 2 |
| 3 | **Countable pre-ship check** replacing the accretion warning: sheets describing the work must outnumber sheets defending the number | `templates/delivery-wbs-workbook.md` §7 | 3 |
| 4 | **The prose budget is asserted, not aspired to** — if the artifact is generated, one `assert` makes it a gate | same §7 | 3 |
| 5 | **The lane test** — name recipient + decision, ask if the row serves them; distinct from the prose budget, run both | `../core/references/pushback-and-teach.md`; `templates/delivery-wbs-workbook.md` §7 | 4 |
| 6 | **A section heading is a label, not an argument** — the diagram rule, promoted to structure | `../core/references/pushback-and-teach.md` | 3 |
| 7 | **Record the speaker, not the source** — *whose sentence is this?*; plus the re-read-on-refresh corollary | `engagement-intake.md` §2; `../core/references/grounding-gate.md` | 5 |
| 8 | **Ground the defect statement too** | `artifact-integrity.md` §The check must execute | 6 |
| 9 | **C8a — two registers for two audiences**, with the requirement to record the split so integrity passes do not merge it; plus *preserve the numbers when a register shrinks* | `artifact-integrity.md` C8 | 7, 8 |
| 10 | **Final QA items 7–8** — every embedded diagram matches its source export; figures inside images re-verified by eye; ask where the previous export went | `rfi-rfp-response.md` | 9 |
| 11 | **Every column readable without a glossary**; dependencies declared by key and resolved at build time; a constant column carries nothing | `templates/delivery-wbs-workbook.md` §1 | 11 |
| 12 | **Handover retires the generator** | `templates/delivery-wbs-workbook.md` §6b; `../delivery/references/delivery-lifecycle.md` | 12 |
| 13 | **Phase vocabulary survives a phase collapse** — name the survivor in the buyer's word (*"MVP (next phase)"*) so workbook and deck do not diverge | `templates/delivery-wbs-workbook.md` §7 | — |

### Validation (fill on the next independent engagement)

- [ ] Effort form is **chosen with the planner before the sheet is built**, and the chosen form is the one returned.
- [ ] Primary artifact accepted **first-pass**, not after three iterations. *This is the unmet half of Ev.4's real test.*
- [ ] The sheet-count check catches ≥1 accreting sheet, or the artifact is clean by construction.
- [ ] Prose budget **asserted in code** where the artifact is generated.
- [ ] The lane test rejects ≥1 correct-but-misaimed row before a recipient does.
- [ ] Every client constraint in the frame carries a **named speaker**; ≥1 turns out to be ours.
- [ ] Final QA opens every artifact that embeds a diagram; no stale export reaches a third party.
- [ ] Formulas present on any summary sheet — **twice-failed, still open** (Ev.4 pattern 8).

**Verdict: `PENDING` for everything authored here.** The trace is the same engagement as Evolution 4, so it
validates but cannot independently confirm. Two Ev.4 items reach **`KEEP` candidate** — *recipient-accepted
artifact* and *integrity checks execute as a script*. One is **`REVISED`** — the effort binary gains a third
form. Two remain **`FAILED`** with named mechanisms: the cold-review gate did not run on a colleague's
client-bound artifact, and the accretion warning did not survive contact with its own author.

### What was deliberately not changed

**The prose budget was not loosened.** It fired correctly and the artifact that passed it was better. What
failed was that it was measured by hand, and that it does not look at headings or at whether the content was
ours to write — hence hypotheses 4, 5 and 6 rather than a revision.

**The empty-effort-column rule was not weakened into "ask the PM what they want."** The prohibition on an
architect pre-filling it is intact and was never contested; what changed is that "empty" is one of two valid
collection modes, not the only one.

**`artifact-integrity.md` stands, again.** Every finding this session was a defect the file already names —
a phantom number, a namespace collision, a stale derived artifact. The additions are about *what the checks
look at* (defect descriptions, embedded images, deliberate splits), never about relaxing them.

---

## Evolution 6 — 2026-07-31 — The re-review: what a rebuild breaks, and the artifact you didn't check

**Trigger.** Final check on the revised client deck (32 → 35 slides) against a **pre-registered** plan written
before the revision was opened. 12 of 14 items closed; the interest is in the two that didn't and the five
defects the rebuild introduced.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **A fix applied to *an* instance is not a fix applied to *the* string.** A correction landed on one slide and was missed on two others; the tracker said done | H/L | *"24 false-positive suppressors"* fixed on slide 23, live on 21 and 22 |
| 2 | **Splitting a dense slide is the highest-yield density fix and it reliably leaves stale continuation headers.** Two splits produced two pairs of consecutive slides sharing a section counter *and* a title | H/L | Slides 28/29 and 32/33 each read `1 / 2` under identical headings; advancing looks like the deck failed to change. Meanwhile the split itself worked: slides over 1,600 chars went **7 → 1** |
| 3 | **The working file and its export are two deliverables and can carry different defects.** The deck was clean; the PDF made from it had opaque grey slabs on 28 of 35 pages, from an exporter flattening a 30%-opacity layout image | H/L | Checking only the source ships a disfigured client PDF; checking only the export reports a defect that isn't in the deck. It had also been present in the *previous* version, unreported, because no renderer had been tried |
| 4 | **Pre-registering the weaknesses of a check makes the check auditable, and it pays.** Of six pre-registered failure modes, two fired and were caught by their own entries; one was refuted outright | H/L | *"'already fixed' is an assumption"* → caught pattern 1. *"word-vs-digit will miss something"* → caught the third invented quantity. *"no visual QA is possible"* → **false**, and refuting it produced every structural finding |
| 5 | **A reviewer's own artifacts are outside their review frame.** The diagram handed to the deck author carried the exact defect the review was telling him to fix in the text | M/L | Body text corrected to 38; the supplied diagram said 42 |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **Final QA pass extended by four items** — word-and-digit number sweeps with clause-mate verification (9); re-verify "already fixed" rather than trusting the tracker (10); walk section counters and continuation slides after any split (11); treat the source file and its export as two deliverables (12) | `references/rfi-rfp-response.md` §Final QA pass | 1, 2, 3 |

### Validation (fill on the next response cycle)

- [ ] Every correction is re-swept across the whole deliverable, not just the reported instance.
- [ ] Any slide split is followed by a counter-and-title pass.
- [ ] Where both a source file and an export will circulate, both are checked and both are named as deliverables.
- [ ] The review's own supplied artifacts are checked against the same criteria as the client's.
- [ ] A re-review pre-registers its failure modes before opening the revision, and scores itself against them.

**Verdict: `PENDING`.** Pattern 4 is the one to promote if it holds — pre-registration cost about ten minutes
and was the only reason three of these findings exist. Pattern 5 has no cure yet beyond awareness; the
candidate is *"list what you supplied, and review it as if someone else had."*

## Evolution 7 — 2026-08-04 — Acceptance criteria that could not be measured, and the one that was deleted

### Harvest scope
Same engagement as Evolutions 4–6, now at the point where an internal review demanded *measurable success
criteria the client agrees in advance, so the outcome cannot be argued afterwards*. Four thresholds were
authored, put through **two independent adversarial reviews on different models**, redesigned, and rebuilt.
Representative because it is the seam this skill owns — turning a solution into something a client can sign —
and because the first attempt failed in a way the skill's own prior evolution had already warned about.

### Patterns found

**P1 — Two of four thresholds were unmeasurable by the instrument proposed. `Impact: H, Effort: M`.**
*Detection ≥90%* counted the share of the client's extraction errors caught — against a denominator produced
by a component we had contractually agreed not to test or tune. At the component's likely accuracy the golden
set contains ~10 errors; demonstrating 90% needs ~29 with zero misses. **Perverse structure: the better the
client's component performs, the less provable our number becomes.** *False positives ≤15%* contradicted our
own design document — *"a failed rule identifies a set of fields, one of which is wrong; it does not identify
which"* — so one honest break implicating twelve fields is eleven false positives at field level.

**P2 — The metric scored our best outputs against us. `Impact: H, Effort: L`.**
Under *"of the fields flagged, the share that were correct all along"*, a document whose **own published
totals fail arithmetic** counts as a false positive. So does a correctly-detected restatement. Those are the
two findings the pitch most wants to show. A metric definition can invert the product's value proposition
without anyone noticing, because the definition reads as neutral.

**P3 — Effective n is clusters, not observations. `Impact: H, Effort: L`.**
~1,020 labels sounded like a sample. They came from 10 documents, sharing one extraction, one layout, one
column-detection pass — behaving like 15–29 independent observations. The confidence interval around a 95%
claim was ±8–11 points, which cannot distinguish 95% from 87%. Nobody involved had asked.

**P4 — A restatement deleted the value proposition and no gate noticed. `Impact: H, Effort: L`.**
The old criteria bounded reviewer workload at *"≤30 of ~200 fields flagged"*. A same-day restatement dropped
it. Nothing then constrained queue size, so a system routing 120 of 200 fields would pass every remaining
threshold while delivering **no efficiency gain at all** — against a client whose stated goal was exactly that
reduction. Consistency gates check that claims agree; they do not check that the load-bearing one survives.

**P5 — Criteria authored for the wrong deal shape cannot be patched. `Impact: H, Effort: M`.**
The set was already recorded as mis-aimed — written as fixed-price acceptance gates for what is a PoC stage.
The first fix retired three and restated one with new numbers, **repeating the original error at smaller
scale three days later.** The shape, not the numbers, was the defect.

**P6 — Two adversarial reviews on different models is a materially stronger instrument than one.
`Impact: M, Effort: L`.** Run cold with the same facts and none of the prior conclusions, they converged on
the unmeasurable denominator and independently demanded the same one-day corpus check — which was then run
and changed a design decision. Where they diverged marked exactly where the judgement was soft.

### Hypotheses applied

| # | Pattern | Edit |
|---|---|---|
| H1 | P1, P3 | `references/acceptance-and-contract.md` → **"Tier criteria by what the instrument can carry"** (commit / report / method, with the membership test), plus **"Effective sample size is clusters, not observations"** and **"A denominator you do not control is not measurable"** — the latter carrying the constructed-denominator fix and its three credibility guardrails |
| H2 | P2, P4 | Same file → **"Check the set for gameability before you sign it"** — read every criterion as an adversary, bond criteria that are only meaningful together *on the artifact*, and watch what a restatement drops |
| H3 | P5 | Same file → **"When the deal shape changes, replace the criteria — do not renumber them"**, including the observed repeat-at-smaller-scale failure |
| H4 | — | *No edit made for P6.* Cross-model adversarial review is a `core` practice, not an SA one; folded into `core` Evolution 5 instead so it is not duplicated |

### Validation results
All **`PENDING`**. P1–P3 are the most likely to generalise — they are properties of measurement, not of this
domain — but every one came from a single engagement and none has yet survived a client conversation, which
is the actual test. **The specific thing to check at the next harvest: did the tiering survive contact with a
buyer who wanted a single headline number?** The design's answer is a bonded pair plus a lock date; if that
gets negotiated away in the room, the tiering is right in theory and unusable in practice, and the honest
verdict is `REVISED` with a lighter floor rather than `KEEP`.

**Update, 6 Aug — the room happened and the question is still open.** The deck carrying the tiered criteria
was presented. The only record of the session is a short set of team notes, and **they say nothing about the
criteria either way** — so this is *no evidence*, not *weak evidence*. Do not read the silence as acceptance:
the notes discuss scope, not measurement, and a tiering that was never tested is indistinguishable in a
summary from one that passed. Verdict unchanged at `PENDING`; ask again when the scope settles.

---

## Evolution 8 — 2026-08-06 — A gate that ran, passed, and checked the wrong property

### Harvest scope

The end of the same engagement: a client-facing deck rebuilt under five parallel agents, taken through six
automated gates and **three cold reviewers**, and presented. Small harvest by design — most of what this pass
produced is kernel material and went to `core` Evolution 6. What is left is the part this skill owns: the
integrity machinery over a client-bound artifact set.

**Representative because the defect below is the first one in this engagement that every existing instrument
was pointed at and still missed.** Earlier misses were gaps in coverage. This one was covered.

### Patterns found

**P1 — A note that records a gap is not a control. `Impact: H, Effort: M`.**
A slide claimed four reviewer actions and badged them in scope. The traceability map behind it carried an
explicit note that two of the four were *"not separately scoped"*, and the mockup on the same slide drew a
button for one of them. **Five automated gates and three cold reviewers passed it**, because the gate asserts
*a claim must name a real WBS task* — and the task it named exists. The client-facing artifact promised
capability the plan did not fund, and **the record that knew it was inside the file the gate was reading.**

Two distinct failures, and separating them is the whole finding:

- **Traceability proves a link exists, not that the target satisfies the source.** No ID-set operation can
  compare a sentence's promise against a task's content, so a gate built from set differences will never see
  this class however well it is written.
- **A caveat field nothing consumes is worse than no field.** The note was correct and deliberate. Its
  presence made the map *look* governed, which suppressed exactly the suspicion that would have caught it.

**P2 — An attributed quotation is a cross-artifact fact, and this skill had no check for it. `Impact: M-H,
Effort: L`.** `artifact-integrity.md` checks counts, dangling refs, orphans, versions, language parity,
priced-vs-committed, namespaces — and had nothing on quoted material. A quotation attributed to a named
client partner and tagged `(Confirmed)`, in the engagement's own orientation document, was a colleague's
internal summary. The general rule is `core`'s; the **cross-artifact** obligation is this skill's, because a
quotation drifting between a proposal, a deck and a wiki page is structurally the same defect as one
population counted four ways.

### Hypotheses applied

| # | Pattern | Edit |
|---|---|---|
| H1 | P1 | `references/artifact-integrity.md` → new **C3a — The inverse orphan: a link is not a warrant**, placed beside C3 so the pair reads together. Carries the capability-comparison requirement and the general rule: **if a traceability map has caveat or exception fields, the gate consumes them or they get deleted.** Closes with the transferable question — *when a gate has never failed on a class of defect, ask what property it actually asserts* |
| H2 | P2 | Same file → new **C9 — Attributed quotations are cross-artifact facts**: verbatim in a source of record, byte-identical across artifacts, with the cheap scripted form and a pointer to `core`'s scoping rule rather than a restatement of it |

### Validation results

**Both `PENDING`.** One engagement, and both defects were found and fixed inside the pass that produced them.

**H1 is the stronger claim and the harder one to test**, because its own logic says a *passing* gate is not
evidence. The test is not "did C3a fire" — it is whether a later engagement, applying it, finds a claim whose
cited task does not cover it. If a harvest reports C3a running clean across a large artifact set, that is
**ambiguous**, not confirmatory: it may mean the claims are sound, or that the check was applied as another
ID-set operation. Ask *how* it was run.

**H1's second half is the more portable half, and it is where I would expect friction.** "Delete a caveat
field the gate does not read" is a strong instruction, and the natural objection — *the note was true and
useful* — is correct. The reason it still holds is that a true note in a governance file reads as governance.
If a later engagement pushes back on deleting rather than wiring, the right verdict is `REVISED` with a third
option: keep the field and make its presence itself a gate failure until something consumes it.

**H2 should be cheap to validate and is the one most likely to reach `KEEP` first** — it is mechanical, and
the engagement that produced it already has the script.

**Next harvest should ask:** did any client-facing claim ship whose cited task did not deliver it, and was
C3a run as a content comparison or quietly reduced to another set difference?
