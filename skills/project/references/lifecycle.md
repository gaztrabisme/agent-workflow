# Lifecycle

The stages of a project from presale to close, named after the PRINCE2 processes they correspond to. For each stage: what it produces, which module of this skill and which linked skill it uses, and the check that ends it. Plan in detail only to the next stage boundary and re-estimate there ([estimating.md](estimating.md)). Every stage that runs agents follows [run/flow.md](run/flow.md); routes are in [routing.md](routing.md).

## Stages

| Stage (PRINCE2 process) | Produces | Modules of this skill | Linked skills | Exit check |
|---|---|---|---|---|
| Qualify and discover (starting up a project) | Client and account research, use-case brief, product decision, the project brief | [roles.md](roles.md) (fill the roles table); [run/flow.md](run/flow.md) Ground and intent interview; [planning-method.md](planning-method.md#frame-the-plan-from-a-brief) | `business-intelligence`, `ceric`, `reddit-corpus`, `ai-discovery-workshop`, `product-management`, `ux` | Every input read as a CERIC hunt in `grounded.md`; each missing item is an owned question ([run/ceric-gates.md](run/ceric-gates.md)) |
| Shape, plan and price (initiating a project) | Solution and response pack; WBS, estimate, schedule, capacity and dependency view; both business cases and tolerances | [Planning flow](#planning-flow) below; [planning-method.md](planning-method.md), [wbs-workbook.md](wbs-workbook.md), [estimating.md](estimating.md), [business-case-and-tolerances.md](business-case-and-tolerances.md) | `solution-architect`, `applied-ml-problem-solver`, `zalo-platform`, `xlsx` | [issue-checklist.md](issue-checklist.md) run before the plan goes out; the [reviews before issue](#reviews-before-issue) that apply have run; the client's business case and ours both hold |
| Make the artifacts (initiating a project) | Decks, documents, diagrams, charts, client messages | [review-and-audience.md](review-and-audience.md) | `presentation`, `drawio`, `information-design`, `visual-design`, `color-theory`, `communication` | Per [review-and-audience.md](review-and-audience.md), and the [reviews before issue](#reviews-before-issue) that apply |
| Build (controlling a stage; managing product delivery) | The products, each from a work package | [run/flow.md](run/flow.md), [run/goal-file.md](run/goal-file.md), [run/lane-plan.md](run/lane-plan.md) | `dev`, `frontend`, review plugins; `infrastructure`, `data-engineering`, `testing` | Goal-file UAT run per row by the coordinator, with an output sample read; the [reviews before issue](#reviews-before-issue) that apply have run |
| Stage boundary (managing a stage boundary) | Re-estimate to the next boundary; updated business case; exception report when a tolerance is forecast to break | [estimating.md](estimating.md), [business-case-and-tolerances.md](business-case-and-tolerances.md#tolerances) | `delivery` for the signed baseline and change requests | Business case still holds; a forecast tolerance breach has gone to the person above the PM |
| Close (closing a project) | Close report; estimates against actuals; lessons | [run/flow.md](run/flow.md#8-close-the-uat-audit); [estimating.md](estimating.md#keep-estimates-against-actuals) | `delivery` (close record), `evolution` | Goal file audited pass or fail per row; decisions, log and active work updated |

## Reviews before issue

A specialist skill's review only works if something sends the work to it. Before any of these leaves the project, run the review named, by an agent that did not produce the artifact ([review-and-audience.md](review-and-audience.md#independent-reviewer)), and record the result in the goal file.

| Before this goes out | Run | From |
|---|---|---|
| An acceptance design, measurement plan or test strategy | Accuracy measurement and acceptance testing review | [`testing`](../../testing/SKILL.md) |
| A cloud pricing workbook: ours, or a colleague's we forward or quote | Pricing workbook review, on our own copy as well as theirs | [`infrastructure`](../../infrastructure/SKILL.md) |
| A data layer model, pipeline design, or a diagram showing data flow | Design review; `check_diagram.py` for the diagram's layout | [`data-engineering`](../../data-engineering/SKILL.md), [`drawio`](../../drawio/SKILL.md) |
| A deck | Rendered check, client-in-the-room read, speaker-script pass | [`presentation`](../../presentation/SKILL.md), [review-and-audience.md](review-and-audience.md) |
| An email, cover note or slide that quotes figures from an attached or referenced file | Every quoted figure matched against the file it cites ([issue checklist](issue-checklist.md), line 21; [check_quoted_figures.py](../scripts/check_quoted_figures.py)) | this skill |
| A plan or WBS workbook | [Issue checklist](issue-checklist.md), with the evidence its opening names | this skill |

A review that does not apply is recorded as not applicable with its reason, as for the checklist.

On a signed client project, `delivery` runs alongside every stage from signature to close; this skill's plan feeds it and does not replace its records.

## Planning flow

Used in the shape, plan and price stage.

| Phase | Goal | Primary artifact |
|---|---|---|
| Frame | Clarify the plan's purpose, audience, outcome, and scope | Project brief or plan outline |
| Route | Name each kind of work and the skill that owns it ([routing](routing.md)); look up the engineering practice for each area in the knowledge base and have a second agent verify the citations; record one entry per WBS row once the rows exist | Skill-and-book map |
| Decompose | Turn deliverables into right-sized work and a suitable hierarchy | WBS |
| Sequence | Show timing, dependencies, milestones, and available capacity | Schedule and dependency register |
| Commit | Select a feasible release or sprint slice with the team | Sprint or period commitment |
| Hand over | Keep the plan editable, readable, and current; run the [issue checklist](issue-checklist.md) before it goes out | Shared plan and handover note |

## Build the plan

Route before decomposing. The skill-and-book map lists, for each WBS row, the routed skill's reference files and the verified book chapters a builder reads first, or "none found" with the searches run, or "not applicable" with a reason. Every brief's Load section is copied from it ([lane plan](run/lane-plan.md)). A row added later gets its entry before its first brief. Practice found this way can change the WBS itself (for example a security or re-run row), which is why it comes before the first estimate. (derived: adapt-os 2026-10-15 — the WBS was drafted and built from without routing or a practice lookup; the defects the lookup found later each needed new rows.)

Start with [the planning method](planning-method.md) to clarify the brief, choose a useful view, and shape release or sprint work. Use [the workbook guidance](wbs-workbook.md) when the plan needs a WBS, effort collection, capacity check, or dependency register. Use [the estimating reference](estimating.md) for every effort figure, and [the business case reference](business-case-and-tolerances.md) when price, margin, tolerances or a cut to reach a price are in play. Adapt the detail to the project; do not build every view for every job. When an agent builds the workbook, [templates/wbs](../templates/wbs/README.md) holds optional scripts that build and check it from data files.

For a client project, use the brief and any agreed scope document as planning inputs. Keep the external commitment and the internal task plan distinguishable. The signed-engagement baseline and acceptance/change/obligation records belong with `delivery`.

On a supplier's bid, the client's business case and ours are separate, and both must hold. [book:prince2-managing-successful-projects], 6.3. Guidance for effective business case management

## Gates applied to planning

- **Grounding gate** — use the brief, agreed scope, team input, and relevant plan history as the substrate; mark unknowns rather than guessing. See [core grounding gate](../../core/references/grounding-gate.md).
- **Output Contract** — the plan, schedule, and any needed dependency or capacity view must exist and be usable by their recipient before work is committed. See [core output contract](../../core/references/output-contract.md) and [core wiki protocol](../../core/references/wiki-protocol.md).
- **Pushback and teach** — when a requested scope, date, or workload does not fit the plan, explain the constraint and offer a workable fork. See [core pushback and teach](../../core/references/pushback-and-teach.md).

Gates applied to running agents are in [run/flow.md](run/flow.md#gates-as-applied).
