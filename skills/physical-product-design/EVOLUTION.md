# Evolution Log — physical-product-design

## Evolution 1 — 2026-10-05 — Printer feedback becomes measurable acceptance

### Harvest scope
- **Grounded:** UltraDex printing-team slicer feedback supplied in this conversation; preserved at `/Users/GaryT/Documents/Work/lab/ultra-dex/design/v2/printer-feedback/`. The user approved acceptance criteria, print rework and skill updates.
- **Coverage:** One physical-product task and one maker review. This is a bounded correction, not a survey of all uses. No prior evolution ledger existed here.
- **Evidence limits:** The screenshot does not establish a physical failed print, exact STL revision or operator profile. Written part numbers and the tall pictured part are ambiguous. Current geometric regression is same-task exercise evidence, not an independent natural use.
- **Evidence class:** Natural maker feedback; exercise measurements and regression checks.

### Settled verdicts
No prior tracked hypotheses to settle.

### Patterns found
1. **Successful slicing concealed specific manufacturing defects** — Impact H; effort M. Preserved baseline measurement finds the intended broad base face 7 mm behind protrusions and two cartridge webs only 0.6 mm thick. Feature-start inspection then found the housing rear plane floating 0.2 mm above the lock receiver contact, with broad bridge/overhang extrusion beginning on the second layer; this prompted a rear-plane correction rather than an unsupported pass. Proof: `design/v2/printability/report-baseline.json` and its annotated plots in the UltraDex workspace. Mesh validity and collision checks had not answered these questions.
2. **A rework creates new engineering obligations** — Impact H; effort M. Splitting the protrusions requires keyed seats, fastener ligaments, underside access and installation order. A short wall coupon would not reproduce a long web or two-anchor seating problem. The first revised insert attempt also failed actual cable and underside fastener/tool checks; a broad bearing-contact exemption concealed screw-head/rib overlap. Failed reports are preserved under `design/v2/experiments/v24-validation/first-insert-attempt/`. This same-task exercise supports adding explicit approach and contact-exemption review, not a field-effectiveness verdict.

### Hypotheses applied
1. **SKILL.md:** Route maker feedback through explicit measurable acceptance and a baseline negative control. Authorized by the user's implementation request.
2. **references/engineering-validation.md:** Add defect mapping, finished-geometry thickness/bed seating, tiny first-layer features, split-joint verification and representative test artifacts. Keep operator qualification separate from digital checks. Authorized by the same request.

### Validation plan
| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Entry-point acceptance gate | Agent defines a discriminating criterion before redesign | Two independent later physical-design tasks reproduce a reported defect and compare the corrected revision without false physical claims | natural | Skill owner / next executing agent | 2026-11-05 or next two uses | PENDING |
| Detailed manufacturing workflow | Finished geometry and representative prototypes expose print risks missed by generic mesh checks | Two independent later tasks document first-layer/feature evidence and operator cleanup/fit outcomes, with scope limits | natural | Skill owner / next executing agent | 2026-11-05 or next two uses | PENDING |

**Verdict: PENDING.** Same-day regression and skill validation support implementation correctness; they do not establish repeatable field effectiveness. Physical UltraDex tests remain not run. Codex and Claude Code resolve to the same canonical skill directory.


## Evolution 2 — 2026-10-05 — Primary use and independent evidence

### Scope, authorization and prior verdict
User approved the focused update and next Nano candidate after two retrospective analyses (conversation “Go”, 2026-10-05). Direct traces: Nano P05 review at `yeti-nano-dock/reviews/p05-2026-10-05/REVIEW.md`, P06 concept decision at `yeti-nano-dock/p06-concepts/docs/decision.md`, and this conversation. One product, bounded digital evidence; no physical prints or acoustic tests. Evolution 1 remains PENDING: this provides another digital application, but does not meet its two-task physical-outcome evidence floor.

### Approved hypotheses and changes
- H1: Add primary-use validation before architecture selection and state-aware compactness. Prediction: a later task tests intended placement/use before investing in final joints, or explicitly keeps selection conditional. Alternative: more end-stage checks; rejected because they discover wrong-use assumptions late.
- H2: Add consequential lifecycle scenarios and coupled-requirement review. Prediction: a later mechanism task evaluates an entire adjustment/unlocked/service action, exposing issues omitted by seated CAD. Alternative: mandatory exhaustive scenario checklist; rejected as disproportionate for simple parts.
- H3: Distinguish shared-source consistency from independent evidence; prioritize decision-changing experiments. Prediction: a later task identifies a critical common assumption and closes it with independent observation before claiming qualification. Alternative: duplicate existing provenance/manufacturing rules; rejected because they already exist.
All three target only `SKILL.md`; existing detailed references remain unchanged. Technical impact: earlier experiment selection and more explicit conditional claims, no new tools or universal thresholds. Risk: unnecessary process for simple products; wording limits scope to consequential decisions. Approval owner: user; implementation: current agent. Rollback: exact pre-edit files preserved at `yeti-nano-dock/p06-revision/skill-update/before/`; revert only these attributable additions if subsequent edits exist.

### Future validation
Status for H1/H2/H3: **PENDING**, not established by this same-session application. Owner: skill owner / next executing agent. Revisit by 2026-11-05 or next two independent uses. Evidence floor: two later natural design tasks record a use experiment (or explicit conditional gate), a consequential lifecycle review and an independently checked critical input; at least one physical observation must affect or confirm a decision. Record time/effort and reject or narrow a hypothesis if it repeatedly adds ceremony without changing decisions. This Nano revision is exercise evidence only.
