# Evolution Log — infrastructure

The loop turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: sessions where an environment plan, a deployment pipeline, a cloud cost estimate or a colleague's pricing workbook is produced or checked.

---

## Evolution 1 — 2026-10-14 — birth

### Harvest scope

- **Grounded:** read `core/SKILL.md`; `skill-builder/SKILL.md`, `references/authoring-checklist.md`, `references/rebuild-from-sources.md`; `solution-architect/references/estimation-and-costing.md` ("Cloud cost by environment" is linked, not copied); `dev/SKILL.md`, `dev/modes/build.md` (container and CI checks are linked); `xlsx/SKILL.md` (workbook mechanics are linked); `project/references/estimating.md` (provisioning rows go to its WBS); `project/proposals/project-skill-2026-10-14.md`, gap 1.
- **Engagement material (read only):** `C:\Users\HuyTL10\Documents\pwc\` — `source/fpt-internal/Fabric_Foundry_Pricing_Explainer_with_three_years-TCO_v1.7-thang-2026-10-13.xlsx` (the infrastructure lead's pricing workbook, v1.7); `deliverables/FSaaS-infra-PoC-v3b-2026-10-13.xlsx` (our PoC derivation, total USD 3,157.15); `deliverables/FSaaS-azure-resource-inventory-2026-08-17.xlsx`, sheet `Gaps and defects` (16 findings against the 17 Aug version); `CLAUDE.md` 17 Aug block on the funding refusal; `wiki/decisions.md` D-045, D-134, D-135, D-136.
- **Books** (knowledge base, read in context): Infrastructure as Code (Morris); Continuous Delivery (Humble & Farley); Cloud Native DevOps with Kubernetes; Python for DevOps; Release It! (Nygard); Site Reliability Engineering; Practical Cloud Security; Building Multi-Tenant SaaS; Fundamentals of Microsoft Fabric; LLMs in Production. The MCP server refused connections; the direct-import fallback was used. The data-platform book (slug `fundamentals-<vendor>-fabric`, sections "The Fabric Pricing Model" and "Storage") states that reserved capacity bills continually, pausing helps only pay-as-you-go, and storage bills while compute is paused; it is not cited in the modules because its slug contains a vendor name that the package's name check forbids. The modules cite LLMs in Production and Designing Distributed Systems for the billing rule and mark the storage rule derived.
- **Classify:** distilled from books plus authored from one engagement's defects. Starts `PENDING`.
- **Evidence class:** authoring-time, plus one exercise on real files (the two tests below).

### Cases

1. **Funding refusal on a mixed-period figure (17 Aug).** USD 8K sent to a funder was `DEV!B25` (whole phase, 4 weeks, $1,978.26) + `QA!B25` (whole phase, 9 weeks, $4,523.37) + `Azure_AI_Foundry!B23` (per month, $2,113.50); `PROD!B25` ($7,762.61, the largest sheet) was omitted. The file's own 16-week build total was $22,046.55, 2.76 times the figure sent. The same version billed week 13 in both QA and PROD, and one cell used 740 hours a month against 730 elsewhere. Source: D-134; inventory `Gaps and defects` rows 1, 2, 5. Rules: principle 1 and 3; cost-estimate "Periods"; review passes 1 and 2.
2. **The infrastructure lead's workbook is his (D-045, D-136).** Findings went back as a list; no cell was edited. The August review recorded: US rates for a Malaysian deployment (row 7, region rate $0.19 vs $0.18), region and agreement unstated (row 9), a note saying ~80/20 against cells at 40/60 (row 4), storage and licence inputs tagged ASSUMPTION with no owner (row 6), an unsourced 41% discount applied across 36 months (row 11), a worked example that bypasses the lookup (row 10), eleven meters missing (row 14). Rules: principle 6; review passes 3 to 5; cost-estimate "Pricing basis".
3. **Environment count and the production driver (D-135, D-136).** The workbook priced three environments where the plan funded one; correcting it lowers the total and weakens the funding ratio, so the decision was recorded as one to take on need, not on the ratio. The funder named the input: a three-year consumption projection by production document volume. The modelled 250,000 pages a month implied ~42 pages a statement; the 24 measured documents average 164.7 pages, so the figure was about four times low, and nobody had asked the client whether they submit whole reports or extracted statements. Rules: environment plan; cost-estimate "Drivers" and "Run projection"; correction on merits in both modules.
4. **Rescoping v1.7 to one PoC environment (13 Oct).** Our PoC workbook zeroed QA, Staging and PROD through their start and end weeks rather than deleting them. The shared container registry's allocation factor then recomputed from 0.529 to 1, moving the DEV registry line from $22.25 to $42.02. Rules: cost-estimate "Rescoping", steps 5 and 7.
5. **Two environments by design (D-019 in the engagement's `CLAUDE.md`).** A demo environment in the team's own subscription on public data runs before client provisioning; anything in the client's tenant carries extra weeks of approvals. Rules: environments-and-iac, demo environment and client-tenant dependency.

### Test 1 — rebuild the PoC total from v1.7

Method: `references/cost-estimate.md`, "Rescoping an existing workbook". Scratch copy at `C:\Users\HuyTL10\AppData\Local\Temp\claude\C--Users-HuyTL10-Documents-pwc\bf8c79ec-a726-4c49-a7be-437beeae9aea\scratchpad\infra-test\` (`rebuild.py`, `rebuilt.xlsx`, `recalc\rebuilt.xlsx`). Scope inputs taken from the PoC workbook's `Changes` sheet: one environment weeks 1–9, F32 paused to 50 hours a week, pay-as-you-go, no reporting licences, Document Intelligence 1,000 pages a month, no embedding; QA, Staging and PROD at zero duration. Eleven input cells changed; no computing formula touched; recalculated with LibreOffice and read back with `data_only=True`.

| | Value |
|---|---|
| Rebuilt `DEV!B91` | **3,157.15228767123** |
| PoC workbook `DEV!B91` | 3,157.15228767123 |
| Difference | 0.00 |
| Roll-ups (`ACA_Hosting!E66`, `TCO_3Y_All_Services!E27`) | 3,157.15, check cells 0, 0, 0 |
| Three-year run (`TCO_3Y!E44`) | 392,401.881, unchanged by the rescoping |
| Counterfactual: edit DEV only, leave the other sheets running, read `DEV!B91` | 3,137.38 (registry allocated at 0.529); 19.77 low |

**Finding during the test, folded into the skill:** the first draft of step 4 said "input cells only". `DEV!B19` (the reservation discount) is a link to the shared run-sheet discount, and the script stopped on it. Overwriting the shared cell would have changed the three-year run. Step 4 now allows overriding a pure link for one environment and forbids overwriting a computing formula.

**Evidence limit:** the scope inputs came from the PoC workbook, so the test checks the method's arithmetic path (zero by inputs, shared allocations, read-back), not the scope choices.

### Test 2 — review v1.7 with `references/reviewing-a-pricing-workbook.md`

Flags (sheet!cell; effect on total):

1. **Pass 1, environment count.** Build priced as DEV W1–9, QA W5–9, Staging W7–9 (three sheets); the PoC derivation provisions one environment. Confirm which plan rows fund QA and Staging. Lowers the build total if two are dropped.
2. **Pass 3, commitment coverage.** Every build sheet takes the 41% reserved discount (`DEV!B19` etc. link `TCO_3Y!B17`); `TCO_3Y!A55` argues one 96-CU reservation covers build and run. Committed units against units in use: 32 CU in W1–4, 64 in W5–6, 96 in W7–9. Modelled build compute 9,705.83; a 96-CU reservation bought at W1 bills 15,415.14; pay-as-you-go to W6 then reserved bills 12,879.82. Build compute understated by 3,174 to 5,709. Raises the total.
3. **Pass 3, one rate in one cell.** 0.18 and 0.41 typed inside 10 formulas each on `Fabric` (C14:D22, B30); eight rate cells typed as values on each of DEV, QA, Staging, PROD (B16:B18, B34:B38), noted "Same rate as …" but not linked; `TCO_3Y!B25` reads Foundry rates from `DEV!B34:B38`; the quick example types F32 and 32 CU (`Fabric!B26:B27`). A rate-card change does not reach every sheet. No effect today; a defect on the next change.
4. **Pass 3, region.** All rates are US list ("US region", `Fabric!C4`); deployment region and agreement are not stated. August measured the deployment region's capacity rate at 0.19. Raises the total about 5.6% on the capacity lines.
5. **Pass 3, discount source.** "~41%" from a public pricing page (`TCO_3Y!F17`), not a rate card for region and term. Effect unknown until sourced.
6. **Pass 4, production volume.** `PROD!B29:B30` 100,000 + 150,000 pages a month, tagged ASSUMPTION with no owner. Implied ~42 pages a statement against a measured mean of 164.7. Raises the run projection roughly fourfold if the client submits whole reports; the client has not been asked.
7. **Pass 4, note against cells.** `Azure_AI_Foundry!D4` "primary engine (~80% of documents)" against 100,000 / 150,000 pages (40/60) in B13:B14 and every environment sheet. Lowers extraction cost if the note is right.
8. **Pass 4, driver ratio.** Output tokens exceed input tokens in PROD, Staging and the rate-sheet example (10M against 5M); DEV and QA have input above output. A question for the owner.
9. **Pass 4, unsourced inputs.** OneLake GB (200 / 500 / 500 / 1,000; 2,000 in the run) and reporting-licence users tagged ASSUMPTION with no owner. Small money, credibility line.
10. **Pass 5, named but not priced.** Each environment's hosting note (`DEV!D70` and peers) gives every Container Apps environment a Log Analytics workspace; `TCO_3Y!A56`, `ACA_Hosting!A84` and `TCO_3Y_All_Services!A40` list Log Analytics as not included. It will be billed. Raises the total.
11. **Pass 5, flat figures.** Network $200 per non-production environment and $350 for production (`TCO_3Y!B26:B27`) are "supplied by the project team" with no breakdown. Effect unknown.

Passed: no monthly figure added to a whole-phase total (every total labelled with its period; build roll-ups read only whole-phase cells); PROD excluded from the build with the reason on the sheet; one 730 and one 168 constant (the August 740 is gone); check cells read zero; registry allocations add to one registry; the grand total shows build and run parts. Against the August review, rows 4, 6, 7, 9, 10 and 11 persist; rows 1, 2 and 5 are fixed. Flags 2, 8 and 10 are new.

**Side finding on our own PoC workbook (not edited; this task is read-only there):** `TCO_3Y_All_Services!A23` in `FSaaS-infra-PoC-v3b-2026-10-13.xlsx` reads "Microsoft Fabric (1-yr reserved)" over a DEV sheet priced pay-as-you-go. Review pass 2, label check.

### Hypotheses applied

1. **The four modules and SKILL.md** — close gap 1 in the project-skill proposal, which recommends writing gap 1 first. Built on the coordinator's request of 14 Oct; the proposal itself is marked "proposed, not applied", and no owner approval of it was seen.

### Validation plan

| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Review module | The workbook owner confirms or rejects flags 1–11; at least 8 confirmed | Owner's written answer | natural | Huy Tran Le | 2026-10-28 | PENDING |
| Rescoping method | A fresh-context agent, given only this skill and a different workbook or scope, reproduces a stated total to the cent | One run on new material | exercise | Huy Tran Le | next infrastructure task | PENDING |
| Environment and pipeline modules | Used on a real project's environment plan or pipeline without a sibling skill being needed for the same question | One real use | natural | Huy Tran Le | next project | PENDING |

**Verdict: PENDING** — the cost and review modules have one exercise on real files; the environment and pipeline modules have none. Settle after two independent real uses.

### Not grounded in a book

Every rule marked `(derived: EVOLUTION case N)`: the period rules, the environment-counted-or-excluded rule, the one-rate-one-cell rule, the commitment-coverage check, the driver source classes, and the rescoping steps. No book read covers reviewing a cloud pricing spreadsheet; the cost-per-tenant passage in Building Multi-Tenant SaaS and the reservation passages are the nearest.
---

## Blind test — 2026-10-14

A fresh agent that had read this skill (not its `EVOLUTION.md`) invented a cloud pricing workbook and cover note (event platform on another cloud, priced in another currency) for a fictional project unlike any case above and planted 8 defects: 6 the skill's rules cover, one per review pass, and 2 the seeder judged outside its text. A second fresh agent, given only the skill and the material, reviewed it; the answer key stayed apart (scratch folder `blindskill/infrastructure/`).

Result: 8 of 8 found and located. Both outside defects (a currency converted twice; a provider's minimum billable size per message ignored) were found from general knowledge, so they are candidate rules for the next revision. The reviewer also showed that `project/scripts/check_quoted_figures.py` matched a typed total no formula computes; the script now marks such matches.

Verdict stays PENDING: this is one blind run on invented material. Next evidence: use on a real project by someone who did not write the skill.
