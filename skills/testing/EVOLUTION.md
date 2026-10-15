# Evolution Log — testing

The loop turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: test strategies, case sets, measurement designs, acceptance packs and test estimates built or reviewed with this skill.

---

## Evolution 1 — 2026-10-14 — birth

### Harvest scope

- **Grounded:** read `../core/SKILL.md` and `../core/references/output-contract.md` (independent review), `../skill-builder/SKILL.md` with `references/authoring-checklist.md` and `references/rebuild-from-sources.md`, `../dev/SKILL.md` and `../dev/modes/build.md`, `../delivery/references/acceptance-execution.md`, `../applied-ml-problem-solver/SKILL.md` and its `references/templates/eval-harness.md`, `../project/references/estimating.md`, `../data-engineering/SKILL.md` (built the same day). Reused by link, not copied: core's independent-review rules, dev's per-change test rules (test-first, red for the right reason, reproduction before a fix, test sizes, mocks), delivery's acceptance recording, the eval harness's sample-size formulas, project's estimate method. Requested by the `project` proposal of 14 Oct 2026 (`../project/proposals/project-skill-2026-10-14.md`), gap 3.
- **Classification:** distilled from books plus one engagement's practice. Starts PENDING.
- **Evidence class:** authoring-time.
- **Knowledge base access:** the MCP search tool refused connection (WinError 10061). Queried through `knowledge_base.server` directly with `uv run` from `~/knowledge-base`. Six search rounds, each followed by `read_chunk` on the strongest hits; later rounds used terms from earlier passages (fault seeding, oracle, slice-based evaluation, holdout).

### Sources read (passages cited in the skill)

| Book | Sections read |
|---|---|
| `swebok` (Software Testing chapter, plus Requirements) | 1. Software Testing Fundamentals (oracle problem; limits of testing); 2. Test Levels (target, objective; regression); 3.3. Code-Based Techniques (equivalence partitioning, boundary-value analysis); 3.5. Usage-Based Techniques (error guessing, mutation testing); 5. Test Process (fault seeding and its limits; mutation score); 5.1. Practical Considerations (risk-based testing, test documentation, independent test team); 5.2. Test Activities (test measures, cost commensurate with criticality, termination); 6. Software Testing Tools (problem reporting, defect tracking); 8. Software Requirements Tools (requirements tracing to test cases) |
| `continuous-delivery` (Humble and Farley) | Types of Tests (part 1) (strategy as risk identification; suite as regression; non-functional tests); Creating Acceptance Tests (part 2); The Automated Acceptance Test Gate (part 2) (whole team owns acceptance tests); Managing Test Data (part 2); Common Delivery Problems—Their Symptoms and Causes; Managing Your Environments (part 1) |
| `software-testing-with-genai` (Winteringham) | 3.3 Knowing when to use LLMs in testing; 5.1 Defining test planning in modern testing; 5.2 Focused prompts with the use of models (area of effect); 8.1 Organizing exploratory testing with LLMs |
| `tdd-by-example` (Beck) | (part 19) test list and Isolated Test; (part 22) read, not cited |
| `growing-oo-software-by-tests` | Levels of Testing |
| `software-engineering-at-google` | TL;DRs (Larger Testing: a strategy that identifies risks); Real Implementations (part 1) (nondeterminism and flakiness) |
| `testing-javascript-applications` | 11.3.3 Retrying tests (flaky tests catch only consistent bugs) |
| `designing-ml-systems-huyen` | Slice-based evaluation (part 1); Perturbation tests |
| `building-machine-learning-pipelines` | 7. Model Analysis and Validation (part 1) (one metric hides detail) |
| `ai-powered-search` | 14.2.4 Formatting the golden set for training, testing, and validation (holdout set) |
| `statistics-by-simulation` | 6.5. Time Series Should Not be Detrended by Default (part 1) (independence assumption) |
| `building-secure-reliable-systems` | Dynamic Program Analysis (no mirrored production data in tests); Define Operating Parameters for Engaging the IR Team (severity fixed, priority changes) |
| `owasp-wstg-v4.2` | 0 - The Web Security Testing Framework (part 1) |
| Others, one passage each | `real-world-software-development` Code Coverage; `hands-on-selenium-webdriver` Types of Testing (verification vs validation); `clean-code` Conclusion (T5 test boundary conditions) |

Second-book confirmations: risk-based strategy (Humble and Farley; Winteringham; Software Engineering at Google; SWEBOK); per-class reporting (Huyen; Building ML Pipelines); flakiness (Google; da Costa); boundary values (SWEBOK; Clean Code); acceptance ownership is shared (Humble and Farley) while SWEBOK allows an external team for an unbiased view — the skill reconciles them by splitting ownership from judging.

Not grounded in a book, carried as derived rules from the cases below: the three tiers of figure; paired figures; injected errors as a constructed denominator (fault seeding in SWEBOK supports the method and its limits, not the commit tier); the drop rate; the evidence-to-producer check; separating fixing from fix verification. Searched without a usable hit: a testing-specific source on clustered observations (the independence passage used is from a time-series section); a book ratio for test effort as a share of development (none used; the skill points to `project` estimating instead).

### Cases (sources of the derived rules)

All from one engagement: a nine-week PoC for a financial statement extraction and verification platform, workspace `C:\Users\HuyTL10\Documents\pwc`, read only.

1. **Measurement tiers and the remedy buckets** — `docs/poc-acceptance-criteria.md` (retired criteria AC-12…AC-19, 4 Aug 2026): commit, report and method tiers; targets locked at mobilisation exit after a first run; injected errors (≥100 per class, published to the client, add or veto) so the detection denominator is constructed; per-class tables never pooled; false alarms counted per fired-rule instance; a rule × document × column coverage matrix with no unexplained empty cell; every number from a scored run with versions and config hashes; three remedy buckets (ours / client set missing → "not measurable" / scope change → re-based).
2. **What consistency checks cannot see, and the outside service** — `docs/verification-pipeline.md` §8: "a missing field breaks no equation", so a coverage line of expected vs populated fields; §9 R-13: whether the extraction service returns positions is a boundary test that survives the "do not test the extractor" decision.
3. **The published blind spot** — workspace `CLAUDE.md` decision D-026 and PoC assumption A-10: a wrong figure that is also internally consistent breaks no rule and is not detected.
4. **Golden set mechanics** — PoC workbook assumptions A-14, A-20, A-23, A-26 and dependency O-12: two client labellers, adjudication by a named authority, match rule (scale, sign, empty vs zero), one labelled field = one test case, rates follow the ten-document count; decision D-102: drop rate published beside every result; deck: corpus stratified by class before labelling.
5. **Acceptance shape** — decision D-102 (12 Aug 2026): acceptance is test-case pass/fail against a pre-agreed list plus a severity defect gate; accuracy figures are reported, not gated; PoC deck v3.1 acceptance pages: entry conditions, W8 dry run, W9 binding run, deferral of steps whose client input is missing.
6. **Paired figures and a cut injection suite** — AC-12 (≤30 fields to a reviewer) is gameable alone and was bonded to AC-13; deck v3.1 pairs precision on auto-cleared fields with the share cleared. PoC workbook: planted-error test (3.3.1) removed; deck says "Injected faults: next phase".
7. **Evidence with no producer** — decision D-144 (17 Aug 2026): under a trim, four of five evidence items had no producing row; the coupling sat in task text, not in the dependency graph. Recurs in the PoC internal workbook: row 12.1.1 still names "run log" and "witnessed rerun" whose rows 3.2.2 and 3.2.3 are removed.
8. **Scoring before labels** — `docs/60k-v3-pm-review-fable-2026-10-13.md`: accuracy scoring scheduled W3–W4 while labelling ran to W4; fixed by decision D-197 (scoring from W5).
9. **Regression before the demo** — PoC workbook row 8.1.3 "Regression pass before the demo".
10. **Independence** — PoC workbook PM note: defect fixing (8.1.2) sits on the tester's seat (raised there as a cost question, about USD 1,069 to move). Workspace practice since August: cold reviewers with no prior context repeatedly found defects the author's own gates passed (`CLAUDE.md`, "Two kinds of prose", and decision D-143).
11. **Inherited size driver** — `docs/estimate-model.md` §5.2: golden-set labels 1,020 = 3 × 200 + 7 × 60, derived from an unconfirmed ~200-field count (O-01).
12. **Tuning on the scoring set** — found by the test below: deck v3.1 and decision D-197 tune configuration on the first measurement (W5–W7) and score the binding run on the same corpus; no workspace record raises the overlap.
13. **Defect budget basis** — PoC workbook row 8.1.2: "budgeted at an industry default rate, not measured from our own history".

### The test and its result

**Task:** following only this skill, write a one-page test strategy for the engagement's PoC from its deck v3.1 and internal workbook, then compare with what the workspace already holds. Artifact: `C:\Users\HuyTL10\AppData\Local\Temp\claude\C--Users-HuyTL10-Documents-pwc\bf8c79ec-a726-4c49-a7be-437beeae9aea\scratchpad\testing-test\poc-test-strategy.md`. The author of the skill ran the test (not a fresh-context reviewer), so this is authoring-time evidence only.

**What the skill added that the workspace did not have:**
- Tuning on the scoring set (case 12): configuration is tuned on the W5 measurement and the W9 binding run scores the same corpus; the reported precision on auto-cleared fields is therefore measured on the set the confidence floor and auto-pass rule were fitted to. Not raised in any workspace record found (searched `docs/60k-v3*`, `wiki/decisions.md`, `wiki/active-work.md`).
- Fix verification on the same seat as fixing (case 10), raised as an independence issue rather than a cost one.
- A deferral register promised in the evidence pack with no producing task; run log and witnessed rerun still named in internal row 12.1.1 after their rows were removed (case 7).
- No security test row although real client documents sit behind a network restriction (row 9.1.2); no unit-test level stated explicitly in the plan.

**What the skill missed that the workspace had (folded back the same day):**
- False alarms counted per fired-rule instance, and the rule × document × column coverage matrix → added to `references/accuracy-measurement.md`.
- The three remedy buckets, including "not measurable" when the client's reference set is missing → added to `references/acceptance-testing.md`.
- Throughput, latency and cost per document reported with no threshold (speaker script, 14 Oct) — the skill had a non-functional bullet but the strategy omitted it → a non-functional row added to the template.
- Not folded: the static check that no numeric operation runs in a model call path (AC-17). It is an architecture fitness function and belongs to `dev`.

**Contradiction:** the skill requires tuning and scoring sets to be separate or the overlap stated; the workspace plan tunes and scores on one ten-document corpus. With ten documents a split leaves few per class; the skill offers "state the overlap on the result" as the alternative. Owner decision.

### Validation plan

| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Whole skill (birth) | A fresh-context agent using only this skill on a real delivery produces a strategy that a reviewer judges complete, without contradicting `dev`, `delivery` or `applied-ml-problem-solver` | Two independent real uses, at least one by a fresh-context agent, on different projects | natural | Skill owner | First test plan of the next delivery | PENDING |
| Tuning vs scoring separation | The rule changes a real measurement plan or is consciously waived with the overlap stated | One engagement decision | natural | Skill owner | Next accuracy measurement | PENDING |
| Evidence-producer check | The check finds or clears orphaned evidence on a real scope cut | One scope cut | natural | Skill owner | Next scope cut | PENDING |
| Agent role split | A build run with separate case-author, implementer and judge agents finds at least one defect the implementer's own tests passed, or shows the split was not worth its cost | Two runs | natural | Skill owner | Next agent-built feature | PENDING |

**Verdict: PENDING** — distilled skill, authoring-time evidence only. Do not mark `KEEP` until the floors above are met.
---

## Blind test — 2026-10-14

A fresh agent that had read this skill (not its `EVOLUTION.md`) invented a test strategy, acceptance design and test rows (claims classification and extraction) for a fictional project unlike any case above and planted 8 defects: 6 the skill's rules cover, one per module, and 2 the seeder judged outside its text. A second fresh agent, given only the skill and the material, reviewed it; the answer key stayed apart (scratch folder `blindskill/testing/`).

Result: 8 of 8 found and located. Both outside defects (masked identifiers scored as automatic passes; post-go-live accuracy measured only from officer corrections) were found; the first was traced to the existing match-rule and drop-rate rules. The reviewer also raised valid problems the seeder did not plant (a tester booked before joining; regression scored before labels exist).

Verdict stays PENDING: this is one blind run on invented material. Next evidence: use on a real project by someone who did not write the skill.
