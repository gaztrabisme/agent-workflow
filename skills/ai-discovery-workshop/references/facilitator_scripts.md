# Facilitator Scripts — Verbatim Questions by Phase

All questions are verbatim from the source PDF. Use these as literal prompts in the workshop.

## Define Phase — BXT Scoring (PDF pp 25–27)

### Business Viability questions
- "Is there a clear and quantifiable revenue?"
- "What changes are expected in efficiency?"
- "Will implementation result in cost reductions?"
- "Does it create a durable competitive advantage?"
- "What is the predicted time to value?"

**Closing prompt:** "What other viability questions come to mind?"

### Experience / Desirability questions
- "Does it align with users' needs and preferences?"
- "How will solution impact user experiences?"
- "Is the user clear? Who is the 'pilot' of the assistant?"
- "Will users be motivated to use it over other experiences?"
- "Are there any potential pain points for users in adopting the solution?"

**Closing prompt:** "What other experience questions come to mind?"

### Technology / Feasibility questions
- "Is there a skill gap within your organization?"
- "Is implementing technology a 'catch up,' or a differentiator?"
- "Are there any potential integration challenges with existing systems?"
- "How ready are you to consume this vendor's technology?"
- "What value is a generative approach going to add?"
- "How can we ensure the accuracy of the models?"

**Closing prompt:** "What other feasibility questions come to mind?"

## Define Phase — Problem Statement Prompt

**Template to elicit user voice:**
> "Ideally, I'd tell the system what I need, and it would..."

Fill in the blank with the client's own words. This keeps the problem statement user-anchored, not tech-anchored.

## Develop Phase — Journey Map Prompts

Three swim lanes on the Agentic User Journey Map. One prompt per lane:

- **User lane:** "Create steps for the main persona to complete the user tasks and their KPIs."
- **AI Discovery lane:** "Ideate and enhance tasks with AI capabilities."
- **Agentic Workflow lane:** "Ideate and identify agentic tasks that can be automated."

## Deliver Phase — GenAI Approach Selection (PDF pp 52–54)

Four decision dimensions; ask each set of questions:

### Data
- "Where is my data?"
- "What infrastructure do I need to connect it?"
- "How does my data need to interface with the platform's data and other sources?"

### Customization
- "How will customers interact with my app?"
- "Do I need to control its tone and behavior?"
- "Am I prepared to manage security and compliance?"

### Development Complexity
- "How much time can I dedicate to app dev?"
- "What resources can I dedicate to this app?"
- "Who do I have available to staff to this project?"

### End User
- "Who is the end user?"
- "How much technical know-how will my end user have?"
- "Where would the end-user interface with the app?"

**Maps to:**
- Low data + no/low-code + non-technical users → **Adopt / extend an off-the-shelf assistant**
- Multiple data sources (API) + moderate customization + pro-code → **Build a custom assistant**
- Complex infrastructure + full customization + technical users → **Build on a unified data platform**

## Deliver Phase — ROI Framing Question

Example phrasing to walk a client through ROI:

> "What are my cost savings per year in [Contoso / client name], to optimize each [candidate recruitment duration] by 30%, and reduce [manhours effort] by 50%?"

Replace bracketed items with the client's specific workflow, baseline metric, and target improvement.

## Deliver Phase — Solutioning Considerations Prompts

Ask these once a use case is chosen for PoV:

- "Are there secondary personas in this workflow (submitter, reviewer, approver, finance)? What's different about their actions and decision points?"
- "Where does a human need to stay in the loop (HITL)? Which tool calls require approval vs. autonomous execution?"
- "What's the RACI for this workflow once deployed?"
- "As agents scale, do we have a catalog of user workflows and goals to ground new agents against?"

## Discover Phase — Five Golden Questions

⚠️ **See `five_golden_questions.md`.** The source methodology names this technique but does not define it in one place — the reconstruction there is inferred from the BXT screening questions and should be treated as `PENDING` until confirmed against a trainer or a real workshop.
