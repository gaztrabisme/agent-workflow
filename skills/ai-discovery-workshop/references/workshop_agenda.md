# Workshop Agenda and Structure

## Contract and prework

Before preparation, identify the business units and client roles involved. Agree in writing on the workshop's boundaries, objectives, participant roles, client support needed, and schedule. [book:flawless-consulting], Elements of a Contract

### Readiness check and brief state

Before booking the full two-session programme, record the decision owner, whether the client is actively considering AI or has deferred it, and what current workflow, data, or baseline is available or obtainable. If AI is explicitly deferred, pause that candidate and record the prerequisite and revisit trigger. If there is no decision owner or no path to the needed evidence, produce a `prework draft` and name the missing input and owner instead of presenting a workshop decision. When data or a baseline is unavailable but the client wants to explore the problem, decide together whether a short readiness session is useful now or whether discovery should wait; keep scores provisional. (derived: dogfood 2026-10-01)

For a single-owner client, use one focused decision session around the problem, current workflow, AI suitability, evidence gaps, and next step. Record the owner as the decision participant; leave broader user and workforce validation open until those people have been consulted. Do not imply group consensus. (derived: dogfood 2026-10-01)

Use this short brief header (derived: dogfood 2026-10-01):

```text
Brief state: prework draft | client-validated
As of / session date: [date or not held]
Participants: [names and roles, or to confirm]
Golden Questions: not yet asked | wording used: [client-language variants]
Changes from draft: [client changes, or none]
Score status: provisional | updated from client discussion
```

Mark a brief `client-validated` only after a dated client session; record attendees, the questions and wording used, and what changed or that nothing changed. A question not asked or a score still based on assumption stays open or provisional.

Use business-intelligence research as prework; bring relevant, validated context into the session without turning the workshop into an account-research presentation. Confirm which business unit or single-owner context is in scope. For each participating unit, or the single owner's scope, align on which of the four AI Transformation Pillars matters. For a multi-stakeholder Day 8 decision, confirm the business and technical decision-makers can attend.

Prepare a lightweight persona draft for each in-scope business unit, with fuller drafts for the top two or three. Start with a collaborative proto-persona sketch based on what the team currently assumes, and mark it as an assumption to validate rather than a researched fact. [book:lean-ux], Proto-Personas The book describes narrowing a team brainstorm to a small initial persona set. [book:lean-ux], The Persona Creation Process

If access permits, recruit people who fit the persona drafts and check whether the team's assumptions match their experience. [book:lean-ux], The Persona Creation Process

Map how people work today before adding AI. Ask for successful as well as difficult parts of the workflow, then source candidates from both pain points and places where the work already goes well. [book:user-story-mapping], 2. Understand Customers and Users [book:flawless-consulting], The Power of Positive Deviance

Source candidate use cases from client goals and AI benefit types using an AI opportunity tree. [book:art-of-ai-product-development], 2.1.1 The AI opportunity tree Use a short AI-suitability screen to ask whether the task has learnable patterns in data; a red flag is a question for investigation, not an automatic rejection. [book:art-of-ai-product-development], A.2.2 Identifying AI-friendly problems

Shortlist at most six to ten candidates before Day 1 and narrow to three to five for the workshop discussion. These are use-case candidates, not a target number of agentic journey steps. Be willing to remove weak opportunities. [book:user-story-mapping], Be Picky

Prefill known information in each BXT assessment for candidates with a plausible AI role, the journey map, and an industry AI Pattern Scorecard when an authorized, current one is available. Otherwise use the compact client-evidence pattern notes in references/bxt_template.md. Keep observations separate from assumptions, and leave unknown scores open rather than inventing data. [book:art-of-ai-product-development], 2.2.1 Defining your prioritization criteria

Review the Golden Questions for each BXT dimension and prepare client-specific variants. If the session will use another language, agree the translated variants with a bilingual client contact during prework and record the wording used. Confirm business and technical decision-maker attendance for a multi-stakeholder Day 8 decision. Arrange a business, technical, and user-experience trio to work together during story mapping where those roles are available. (derived: dogfood 2026-10-01) [book:user-story-mapping], The Three Amigos

## Full engagement structure

For an enterprise, multi-stakeholder engagement, Day 1 Discovery and Day 8 Prioritization are each planned as a two-to-six-hour session. Adjust the activities and breaks to the client group and evidence available. Use the single-owner variant above when a two-session programme would exceed the decision need. (derived: dogfood 2026-10-01)

### Day 1: Discover and shortlist

Open by stating the workshop objective and the decision the group is working toward. Allocate about five percent of the actual meeting time to the opening and agenda; distribute the remaining steps by proportion to the session length. [book:flawless-consulting], The Meeting for Action, Step by Step

1. **Discover:** explore personas, current workflow, pain, and what already works. Use Five Whys, Rose/Thorn/Bud, and solution-redirection prompts where useful.
2. **Define:** affinity-cluster observations into themes. Screen whether each candidate needs AI before scoring; fill the BXT assessment for candidates with a plausible AI role using the Golden Questions for each dimension. Route a clear `no` to conventional scope and keep it out of the AI matrix. (derived: dogfood 2026-10-01)
3. **Develop:** build a journey map with User and AI Discovery lanes. Add an Agentic Workflow lane only when the workflow contains a multi-step or decision-heavy task; otherwise mark `none found` and do not invent one. (derived: dogfood 2026-10-01)
4. Score AI-suitable candidates from one to five on each criterion, then plot them on the matrix to surface two or three for further discussion. The plotted scores remain provisional and evidence-linked.

During pain discovery, use open questions to go beyond the first problem named and understand its impact. Follow up on how often it occurs, who it affects, and what it costs, without pressuring the client toward a predetermined answer. [book:meddicc], DISCOVERY

Hold a halfway check-in: ask whether the meeting is giving the client what they need while there is still time to adjust. [book:flawless-consulting], The Meeting for Action, Step by Step

### Day 8: Refine and hand off

Before the session, refine scores for the shortlisted cases and prepare an authorized current industry scorecard or the compact client-evidence pattern notes in references/bxt_template.md. Review the shortlist and evidence gaps with the group.

1. Select the GenAI approach by discussing data, customization, development complexity, and end users.
2. Compare potential value and complexity, and describe the integration scenario: AI as an add-on to an existing product, AI as the core value driver, or AI as an internal enabler. [book:art-of-ai-product-development], 2.1.4 Navigating different scenarios for AI integration
3. Estimate ROI from client workflow baselines. Include the cost of the current pain and use ranges when outcomes or probabilities are uncertain.
4. Co-design a preliminary system and workflow view with the client: user roles, data, boundaries, human checks, and open architecture questions. Jointly diagnose the opportunity with the client instead of prescribing an off-the-shelf answer. Hand the formal architecture and proposal to solution-architect. [book:value-based-fees], CHAPTER 7 Seventy Ways to Raise Fees and/or Increase Profits Immediately
5. Cover secondary personas and their decisions, workflow RACI, human oversight, and the workflow goals that should ground an agent. Human review is a useful component when an agent's actions need checking. [book:art-of-ai-product-development], 9.1.2 Turning the human into a tool
6. If the evidence and decision-makers support it, nominate one use case for a small rapid prototype using an AI coding assistant, or for a PoV. The implementation owner builds it after handoff. Before a commitment, validate the concept with users where possible and keep a tight feedback loop. [book:user-story-mapping], Discover a Minimum Viable Solution; [book:art-of-ai-product-development], 10.1.3 Validating AI design concepts.

The client may choose a use case for PoV when the evidence supports that decision. Do not treat an approved PoV, ROI baseline, architecture draft, or prototype as automatic outputs of every Day 8 session.

## Schedule and facilitation

For the enterprise reference agenda, short activity blocks are 15 minutes for BXT, 15 for Develop with Discovery Cards, 20 for Business Envisioning, and 30 for Solution Envisioning. Fit them into the session with discussion and breaks; they do not define a complete 90-minute agenda. Resize or omit blocks in a shorter single-owner session to fit its decision need. Reserve about ten minutes in the enterprise session for recording decisions and commitments, and scale that time for shorter sessions; raise the next-step decision early enough that the client can make it with you present. [book:flawless-consulting], The Meeting for Action, Step by Step (derived: dogfood 2026-10-01)

Use one journey step for the card exercise and ask the client to choose one or two relevant capability cards from the compact set in references/discovery_cards.md or another authorized current deck. For story work, the business, technical, and user-experience collaborators can check the same task together.

## Materials

For an in-person room, provide the compact capability prompts or another authorized card set, a flipchart or whiteboard, sticky notes, pens, and a long, continuous wall workspace for mapping. The continuous workspace is the room setup principle; the specific supplies are this workshop's checklist. [book:flow-architectures], The 10,000-Foot View of EventStorming

For remote participants, use a shared virtual whiteboard with the compact digital capability prompts, BXT assessment, journey map, and prioritization matrix available on the board. [book:flow-architectures], The 10,000-Foot View of EventStorming
