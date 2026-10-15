# Evolution Log — data-engineering

The loop turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: data designs, layer models, pipeline diagrams and data-work estimates reviewed or built with this skill.

---

## Evolution 1 — 2026-10-14 — birth

### Harvest scope

- **Grounded:** read `../core/SKILL.md`, `../skill-builder/SKILL.md` with its authoring checklist and rebuild method, `../dev/SKILL.md`, `../applied-ml-problem-solver/SKILL.md`, `../solution-architect/SKILL.md`, `../infrastructure/SKILL.md` (frontmatter, built the same day), and `../project/references/estimating.md`. Reused: the canonical skeleton headings, core gate links, the estimate method (linked, not copied). Requested by the `project` proposal of 14 Oct 2026 (`../project/proposals/project-skill-2026-10-14.md`), gap 2.
- **Classification:** distilled from books plus one engagement's practice. Starts PENDING.
- **Evidence class:** authoring-time.
- **Knowledge base access:** the MCP search tool refused connection; the local Qdrant server was not running. Started it with the knowledge base's own boot routine (`knowledge_base/qdrant_boot.py`, binary `bin/qdrant.exe`, storage `qdrant-storage`) and queried through `knowledge_base.server` directly. Four search rounds, each followed by `read_chunk` on the strongest hits with their neighbours.

### Sources read (passages cited in the skill)

| Book | Sections read |
|---|---|
| `building-medallion-architectures` (Strengholt) | What Is a Medallion Architecture?; The Three-Layered Design; Idempotency as a Key Design Principle; Data Contracts; Tailored Medallions Architectures; Bronze Layer (unstructured data) |
| `practical-lakehouse-architecture` (Thalpati) | Core Components of a Data Platform (part 2); Data Storage (part 1); Data Processing; Data Consumption and Delivery; Data and ML Model Quality; Estimation and Planning Phase |
| `fundamentals-data-engineering` (Reis and Housley) | Orchestration; Batch Transformations (part 3); Whom You'll Work With; Software Engineering (read, not cited) |
| `financial-data-engineering` (Khraisha) | Principle 8: Data Contracts; Principle 5: Data Lineage; Entity Resolution Described; Dimension 1: Data Errors |
| `data-quality-fundamentals` (Moses, Gavish, Vorwerck) | Understanding Data Quality Downstream; dbt Unit Testing; Managing Data Quality with Apache Airflow; Measuring and Maintaining High Data Reliability at Ingestion (part 1); Data Observability; How to Set SLAs, SLOs, and SLIs for Your Data; Basic Lineage Requirements; Building End-to-End Field-Level Lineage for Modern Data Systems |
| `automating-data-quality-monitoring` (Stanley and Schwartz) | The Limits of Automation |
| `building-machine-learning-pipelines` | 4. Data Validation (part 3) |
| `building-event-driven-microservices` | Chapter 4. Schemas and Data Contracts; Reprocessing Historical Data for Breaking Schema Changes |
| Others, one passage each | `designing-distributed-systems-2e` Idempotency; `machinelearningengineeringwithpython_secondedition` Airflow idempotency; `continuous-delivery` The Results of the Commit Stage; `architecting-data-ml-platforms` Store; `machine-learning-production-systems` ML Metadata; `data-governance-definitive-guide` Data Lineage Monitoring |

Second-book confirmations: layer roles (Strengholt, Thalpati; the Fabric fundamentals book also says layer names are only a suggestion); idempotency (Strengholt, Burns, ML engineering with Python); contracts (Strengholt, Khraisha, Thalpati, Bellemare); raw files kept for reprocessing (Thalpati, Tranquillin); quality dimensions (Moses et al., Thalpati, Khraisha, who adds that no fixed list exists); lineage (Moses et al., Crowe et al., Eryurek et al., Khraisha).

**Not grounded in a book, so marked derived:** detect versus resolve, transform evidence, separate rows for values never compared, model maps and code computes, rule-gated review queues, signed versus unsigned provenance, rate denominators by layer, error injection, the estimate drivers other than ingestion and orchestration. No book searched gave effort figures for data work; the skill gives none.

### Cases (the engagement behind the derived rules)

Source: the PwC FSaaS presale workspace (`C:\Users\HuyTL10\Documents\pwc`, read only). Financial-statement extraction from PDF annual reports into bronze, silver and gold layers, with a rules engine and a review workbench.

1. **Raw layer holding derived values cannot replay.** `docs/data-layer-model.md` §1, "Why bronze cannot hold it all": once a value is scaled from `RM'000` or periods aligned, it is no longer what the document said; replay corrects every affected figure without re-extracting a PDF.
2. **Detect versus resolve, and transform evidence.** Same file §2: bronze records the printed scale and where it was printed; silver records the resolved value, the rule, and the evidence ("scale applied x1000, declared at page 42 statement header, span 118–126").
3. **Separate rows for values that must not be compared.** Same file §3: silver grain `(entity, period, column basis, concept)`; Group and Company figures in separate rows because IAS 34 ¶14 says they are not comparable.
4. **Structure detected per document.** `CLAUDE.md` load-bearing decisions and `docs/reconciliation-rules-grounded.md` §5: no standard mandates the Group/Company column layout; column count is 2 or 4 and detected per filing.
5. **Operational store is not gold.** Data layer model §1: review queue, drafts and assignments are mutable workbench state; gold is the promoted output.
6. **Consumers bypassing the signed layer.** Data layer model §5, "Today's plan has no path by which a signed figure reaches a query": WBS rows `6.1.4 → 6.1.5 → 6.1.1` fed the index from normalised values, not gold; `6.1.3` loaded the client's manual extracts straight into the index, mixing signed and unsigned provenance with no field to tell them apart.
7. **Measurement is a component; denominators move.** Data layer model §5: the evaluation harness spans layers; silver removes scale, rounding and column artifacts before a rule sees them, so the false-positive rate improves without the rules improving. Error injection as the way to own a detection denominator: `CLAUDE.md` decision D-027.
8. **Field-level versus document-level approval.** Data layer model §4: figures promote field by field with provenance; narrative promotes with the document and is "signed by association". `docs/verification-pipeline.md` step 10: nothing promotes on the agent's authority alone; §7: a human correction re-runs the rules.
9. **Model maps, code computes; rules gate, confidence ranks.** `CLAUDE.md` decisions D-014 and D-015; `docs/verification-pipeline.md` §2 and §4. The residual: a wrong but internally consistent figure breaks no rule (D-026).
10. **Extraction as a client dependency.** `CLAUDE.md` decision D-016: the client declared the extraction service solved; its boundary goes in the assumptions, not into fallbacks.
11. **Duplicate key with uncaptured fields.** `docs/INDEX.md` entry for `plan-audit-findings-2026-08-27.md`: the duplicate check assumed an industry code and a registration number loaded at upload; neither was captured, so the check had no key.
12. **Legitimate differences, absent inputs, mixed units, re-run cost.** `docs/reconciliation-rules-grounded.md` §3 lists 24 false-positive sources from the standards; §2.7 items 3 and 4 settle skip-not-fail for absent line items and normalising mixed units. `docs/estimate-model.md` line 121: "re-running is free" was superseded; a re-run is a silver rebuild plus rule re-execution.
13. **Three documents, three positions.** Data layer model, opening note: the scope list, the pipeline doc and the WBS disagreed on promotion; the layer spec was made normative. `CLAUDE.md` D-025: two diagram numbering schemes never mapped.
14. **Work filed under the wrong group.** Data layer model opening note and §5: about 29 MD of normalisation and indexing filed under Consumption; column-band detection moved from the engine to silver with its effort, "neither a saving nor an addition".
15. **Unenumerated driver and an assumed volume.** `CLAUDE.md` numbers chain: "~200 fields" never enumerated, moves 46 MD; 250,000 pages a month assumed, measured mean of 164.7 pages over 24 documents put it near one million.

### Test: design-review module applied to the layer model and the PoC v3 diagram

Inputs: `docs/data-layer-model.md` (normative, 17 Aug) and `docs/design/fsaas-architecture-poc-v3-2026-10-13.drawio` with its PNG; cross-checked against `docs/verification-pipeline.md`, `docs/reconciliation-rules-grounded.md`, `docs/estimate-model.md`, `docs/corpus-spec.md` and `docs/poc-v3.1-speaker-script-2026-10-14.md`. Nothing in the workspace was edited. Run by the author, not a fresh-context reviewer.

**Confirmed (14):** layer jobs, writers and mutability (spec §1 table); raw holds observation only, with the replay argument (§1); detect versus resolve (§2); transform evidence (§2); operational store kept apart (§1, purple box on the diagram); grain stated as a key (§3); separate rows for Group and Company (§3); structure detected per document (§3); no hand-editing, fix and replay (§6); field- versus document-level approval (§4); measurement as a component and rates tied to their layer (§5); consumption disposable (§1, §6); arithmetic in code and rules gating the queue (pipeline §2, §4); legitimate differences and absent-input behaviour catalogued (rules §3, §2.7).

**Flagged (11), ranked:**

| # | Flag | Where | Already handled? |
|---|---|---|---|
| 1 | The PoC diagram has no gold layer; sign-off is next phase; the two PoC consumers (company keys, spreadsheet export) take their arrow from the silver box. The spec says nothing reaches consumption unsigned. | diagram; spec §1 | **Partly.** The speaker script lists "signed-off figures" and the gold layer as next phase, so the scope is honest. Not found: any marker in the export saying its figures are unreviewed; "export source trail" is MVP-only. |
| 2 | The diagram draws the silver box last, after conformance check, queue and crop; the spec says the rules run on silver. A reader concludes the checks run on bronze. | diagram; spec §1, §5 | **No** for this diagram. Spec §5 records the same defect for the older pipeline diagram only. |
| 3 | No extractor version per bronze record. The PoC tunes the extractor once in weeks 5–7 and freezes it; bronze before and after tuning comes from two configurations, which affects replay and accuracy comparison. | spec §1 "Carries" row | **No**, not found in any file read. |
| 4 | No stop rules: which failures halt a document (unreadable layout, duplicate) versus flag a field. | spec; pipeline doc | **Partly.** Speaker script: a missing input defers the dependent step "neither failed nor silently passed". |
| 5 | Original PDF retention and hash not in the layer spec. | spec §1 | **Partly.** `corpus-spec.md` uses sha256 as the corpus dedup key. |
| 6 | Duplicate-check key fields must be captured before the check. | diagram "Duplicate check" | **Yes.** Plan audit of 27 Aug found it and drove the plan revision. |
| 7 | Concept vocabulary, period convention and entity authority undecided. | spec §7 items 2–4 | **Yes**, listed as open. ⚠ The speaker script now states a period rule ("keyed on the financial year end, never the year label"); spec §7 item 3 still says undecided. |
| 8 | Idempotency not in the spec. | spec | **Yes**, funded as estimate row `2.6.1`. |
| 9 | No backfill plan for a new transform version (range, check, what consumers see meanwhile). | spec | **No**; low for a PoC on a prepared set. |
| 10 | The diagram connects the evaluation harness only to the operational store; spec §5 says it measures bronze and silver too. | diagram; spec §5 | **No**; low. |
| 11 | Monitoring named ("Run metrics and alerts: in the PoC") without freshness or volume checks. | diagram footer | **Partly.** |

**Result:** the checklist ran end to end on real material and every item resolved to confirmed, flagged or not applicable. Of 11 flags, 3 were already handled, 4 partly, 4 not found. Flags 1, 2 and 3 are the ones worth taking to the owner. Flag 3 produced a new rule (extractor version per raw record).

**Limits:** the author wrote both the cases and the checklist from the same material, so the 14 confirmations are expected by construction; the flags not taken from the cases (2, 3, 4, 9, 10, 11) are the real test. No fresh-context reviewer ran it.

### Validation plan

| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Skill birth: six modules and the design-review checklist | A reviewer using only this skill flags at least one defect in a data design that its authors had not recorded, and the skill's rules raise no false flag the reviewer must discard as wrong | Two independent real uses, at least one by a fresh-context reviewer, at least one on a project other than the case engagement | natural | skill owner | 2026-12-14 | PENDING |
| Derived rules (cases 1–15) | Hold on a second project's data design without rewording | One use on a different domain | natural | skill owner | 2026-12-14 | PENDING |

**Verdict: PENDING** — validation condition above. Do not mark KEEP on the strength of the birth test.
---

## Blind test — 2026-10-14

A fresh agent that had read this skill (not its `EVOLUTION.md`) invented a layer model, pipeline diagram and estimate with test plan (sensor readings and work orders for a utility) for a fictional project unlike any case above and planted 8 defects: 6 the skill's rules cover, one per module, and 2 the seeder judged outside its text. A second fresh agent, given only the skill and the material, reviewed it; the answer key stayed apart (scratch folder `blindskill/data-engineering/`).

Result: 8 of 8 found and located. Both outside defects (late-arriving readings overwriting a day's aggregate; asset topology kept as current state only) were traced by the reviewer to the existing re-run, key and grain rules, so the skill reaches them through its general rules; a rule naming each explicitly is a candidate for the next revision.

Verdict stays PENDING: this is one blind run on invented material. Next evidence: use on a real project by someone who did not write the skill.
