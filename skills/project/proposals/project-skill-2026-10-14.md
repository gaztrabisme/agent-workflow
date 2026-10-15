# Proposal: one skill, `project`, for a project run end to end by one person with agents (2026-10-14)

Status: **proposed, not applied.** Nothing below is changed until the owner says go.

## Owner direction (14 Oct 2026)

- Plan for one person running a software project from presale to close, doing every job with agents. Inside today's company structure, work is still delegated to the people who own it; that is a setting per project, not a limit of the skill.
- `project-management` and `conductor` become one skill, named `project`.
- Go over the whole skill inventory: link every skill a solo project needs, and list what is missing.
- Carried from the plan approved earlier the same day: a stress test for each checklist line, the audience declared before writing, the speaker-script pass for decks, folding conductor in, and the review rules with a routing table.

## Design

### Roles: who holds each one, set per project

The skill lists the roles a project needs and who holds each. By default the one person and their agents hold every production role. A project's organisation can assign a role to someone else (on PwC: price and concessions to the PM, cloud cost to the infrastructure lead); then our work in that role goes to them as a draft for their decision, as the skill already says for other disciplines' rows.

Two rules do not depend on headcount:
- **Someone outside the work accepts it.** A one-person company still has a client who accepts and pays, and a business that carries the loss if it fails. PRINCE2 keeps the executive (who owns the business case) and the project manager as two roles, and the executive's accountability cannot be delegated. [book:prince2-managing-successful-projects], 7.2. PRINCE2's requirements for organization
- **The producer never approves their own work.** Assurance must be independent of the project manager. [book:prince2-managing-successful-projects], C. Roles and responsibilities. With one person, the independent reviewer is an agent with no prior context, briefed with the product's quality criteria, plus the client's acceptance.

### Shape of `project`

| Part | Holds | Comes from |
|---|---|---|
| `SKILL.md` | The backbone: PRINCE2 stages from presale to close, the roles table, the routing table, the anti-patterns | project-management `SKILL.md` and conductor's routing |
| `references/run-the-work.md` | Running agents in PRINCE2 terms: work package = an agent's brief (product, quality criteria, tolerances, how to report back); checkpoint report = the agent's report; quality review = a reviewer agent that did not produce the work; exception = stop when a tolerance will be broken; highlight report = the report to the owner; the success-criteria file and its checks | conductor (Plan Block, goal file, lane plan, convergence, run ledger), rewritten; PRINCE2 Agile 20.3.1 (work packages defined together with the team) |
| `references/review-and-audience.md` | Declare each artifact's reader before writing; check every artifact rendered (deck, sheet, diagram, page), never on "export succeeded"; the client-in-the-room read; the speaker-script pass for decks | core "Client-facing pages", drawio quality conventions, the approved plan |
| `references/checklist-uat.md` | For each issue-checklist line: how to check it, what a failure looks like, a deliberately broken example; a reviewer agent with no context must catch the example, then tries to build something that passes the line and is still wrong | PRINCE2 A.17 (quality criteria and quality method per product), 8.4 (quality review technique) |
| Existing references | planning-method, wbs-workbook, estimating, business-case-and-tolerances, issue-checklist, templates/wbs | unchanged |

The entry skill stays small: backbone, roles, routing and the agent method. Detail for each stage is loaded only when that stage starts, so the skill does not load everything for every request.

### Changes outside `project`

- `presentation`: the speaker-script pass (one agent walks the deck in order, each slide scripted with the script so far; a fresh agent marks each sentence new or repeated; the one planned repeated message is kept). [book:storytelling-with-data], chapter one; [book:articulating-design-decisions], Chapter 3
- `conductor`: retired, or kept as a two-line pointer to `project` for multi-step work that is not a project. Recommendation: pointer.
- 18 files outside `project-management` and 25 outside `conductor` name them; each link is updated in the same change.

### Cost to flag

The skills folder is a merge of an upstream set (`gaztrabisme/agent-workflow`, per `README.md`) with local rules. Renaming one skill and retiring another moves this copy further from upstream; each later sync has to carry the rename by hand.

## Inventory, by stage

"Link" means `project` routes to the skill at that stage. "When needed" means only for some projects.

| Stage | Skill | What it supplies | Link |
|---|---|---|---|
| Qualify the opportunity | business-intelligence | Client and account research, stakeholders, competitors | Link |
| | reddit-corpus; deep-research (plugin) | What a community or the web knows about a tool or approach | When needed |
| | ceric | Audit of a source's claims and evidence | Link |
| Discover the need | ai-discovery-workshop | Client workshop to choose AI use cases | When needed |
| | product-management | What to build and why; measures; roadmap | Link |
| | ux | User research, flows, wireframes, interface words | Link |
| Shape the solution and offer | solution-architect | Architecture, options, NFRs, traceability, response pack, commercial terms | Link |
| | applied-ml-problem-solver | ML framing, data, evaluation design | When needed |
| | zalo-platform | Zalo platform facts | When needed |
| Plan and price | `project` itself | WBS, estimate, schedule, business case, tolerances | Own |
| | xlsx | Workbooks built and checked by script | Link |
| Make the artifacts | presentation; pptx, docx, pdf (plugins) | Decks, documents, handouts, recorded demos | Link |
| | drawio | Architecture and flow diagrams, with the new checker | Link |
| | information-design; dataviz (plugin) | Charts and data graphics | Link |
| | visual-design; color-theory | Composition, type, colour decisions | Link |
| | fpt-infographics | FPT-branded one-pagers | When needed |
| | motion | Animated explainers | When needed |
| | communication | Client messages and updates | Link |
| Build | dev | Design, build, review, root-cause analysis | Link |
| | frontend | Web interfaces | Link |
| | code-review, security-review, simplify (plugins) | Review of a change | Link |
| | claude-api (plugin) | Building on Claude | When needed |
| Deliver under contract | delivery | Baseline, acceptance, change, client obligations, close | Link |
| Learn | evolution | Lessons into the skills | Link |
| | skill-builder | Building or reshaping a skill | When needed |
| Shared rules | core | Evidence, output contract, wiki, pushback | Inherited |

Not needed for a software project: photo, physical-product-design, domestika-course-archive.

## Missing, for a solo software project

Ordered by how often a project like PwC needs them. "Sources we hold" are books already in the knowledge base.

| Gap | What it would cover | Partly covered today by | Sources we hold |
|---|---|---|---|
| 1. Cloud infrastructure and deployment | Environments, infrastructure as code, CI/CD, provisioning, release; the infrastructure lead's estimate | solution-architect "Cloud cost by environment" (cost only); dev build mode (one line on deployment) | Infrastructure as Code (Morris); Continuous Delivery; Cloud Native DevOps with Kubernetes; Python for DevOps; Release It! |
| 2. Data engineering | Ingestion, lakehouse layers, pipelines, data quality checks | dev (general code only) | Fundamentals of Data Engineering; Practical Lakehouse Architecture; Financial Data Engineering; Data Quality Fundamentals; Automating Data Quality Monitoring |
| 3. Testing and quality | Test strategy, test cases, test data, regression, acceptance test scripts; the tester's role | dev build mode (tests per change); delivery acceptance execution; applied-ml evaluation | Software Testing with Generative AI; Test-Driven Development by Example; Growing OO Software, Guided by Tests; Testing JavaScript Applications |
| 4. Security and data protection | Threat model, cloud security design, client security questionnaires, handling client data | dev invariant gate; security-review plugin (code only) | Building Secure and Reliable Systems; Practical Cloud Security; OWASP Web Security Testing Guide; LLM Security Playbook; Software Supply Chain Security |
| 5. Operations and support | Monitoring, alerts, incidents, runbooks, support and maintenance after go-live | dev design (SLOs); delivery close (runbooks handed over) | Site Reliability Engineering; Hands-On SRE; Intelligence-Driven Incident Response |
| 6. Requirements analysis | Requirement lists, user stories, acceptance criteria per story; the BA's role | ux; product-management; solution-architect traceability | SWEBOK chapter 1; User Story Mapping |
| 7. User documentation and training | User and admin guides, training material, handover documents | presentation; docx plugin | none found |
| 8. Legal review | NDA, contract and data-processing terms | solution-architect commercial terms; Getting to Yes and Bargaining for Advantage (negotiation, not law) | none; stays with a lawyer, named as a delegated role |

Recommendation: write gaps 1 to 3 first, as specialist skills `project` links to, each built from the books listed and tested on PwC's own material (gap 1 on the infrastructure lead's workbook, whose total we can already reproduce; gap 2 on the bronze-silver-gold pipeline; gap 3 on the accuracy evaluation). Gaps 4 to 6 next. Gap 7 when a project reaches handover. Gap 8 is a role, not a skill.

## Decisions for the owner

1. **Roles table** with "held by" set per project and the two rules above. Recommended.
2. **Build `project`** from project-management and conductor in the shape above; conductor kept as a pointer. Recommended.
3. **Routing table** from the inventory above. Recommended.
4. **Gaps:** write 1 to 3 next, in that order, each as a linked specialist skill. Recommended.
5. **Upstream:** accept that the rename diverges from the upstream skill set. Your call.

Order of work once approved: the `project` skill and its links; then the checklist stress test and the speaker-script pass (both use agents, and the deck pass runs first on the PwC PoC deck as an internal script); then the gap skills. Each change gets an `EVOLUTION.md` entry with its cases and test.
