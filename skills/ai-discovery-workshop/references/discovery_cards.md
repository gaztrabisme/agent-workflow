# Discovery Cards and Agentic Workflow

## Four AI Transformation Pillars

Place every use case in one of the four transformation pillars:

1. Enrich employee experiences.
2. Reinvent customer engagement.
3. Reshape business processes.
4. Bend the curve on innovation.

Use the pillar to frame the opportunity. It does not replace the client's problem statement or determine whether AI fits.

## Journey map and card use

Map the client's current journey before adding AI. Show the User and AI Discovery lanes. Add the Agentic Workflow lane when a task needs multiple steps or decisions; otherwise mark it `none found`. (derived: dogfood 2026-10-01) Order user tasks in the sequence they happen; a task is an action toward a goal. [book:user-story-mapping], 2. Organize Your Story [book:user-story-mapping], Tasks Are What We Do

For each stage, estimate where AI might augment or automate work; delimit the substeps that AI could address instead of treating the whole process as one task. [book:art-of-ai-product-development], 10.1 Discovery and user research [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation

### Compact capability prompt cards

Use this short, self-contained set when a full authorized card deck is unavailable. These generic prompts are derived from dogfood 2026-10-01; they are starters, not a comprehensive capability catalogue.

| Discovery capability card | Prompt |
|---|---|
| Find and summarize | Could AI find trusted information and summarize it for this step? |
| Extract and classify | Could AI extract fields or sort incoming items, with uncertain cases flagged? |
| Predict and prioritize | Could AI estimate what may happen next or help order work, using relevant evidence? |
| Draft and adapt | Could AI prepare a draft or alternative for a person to review? |

In the 15-minute Develop block:

1. Pick one journey step.
2. Spread relevant cards from this compact set or an authorized current AI Discovery deck, filtered to the capability category.
3. Ask the client to choose one or two cards that fit the step.
4. Record the capability and the evidence or question it creates on the map.

If the journey contains a multi-step or decision-heavy task, select a fitting pattern below or from an authorized current Agentic Card deck. Choose for contextual fit rather than maximum capability. [book:agentic-mesh], Finding the Right Agent (derived: dogfood 2026-10-01)

| Agentic workflow card | Starter sequence |
|---|---|
| Prepare a response | Intake → retrieve trusted information → draft → human review |
| Investigate an exception | Detect → gather evidence → recommend → escalate |
| Carry out approved steps | Plan approved steps → execute one step → verify → stop or escalate |

Use the selected card as the workflow lane template and populate it with tasks specific to the client's context. If no pattern fits or no agentic task is found, record `none found`; do not invent a workflow to fill the lane. (derived: dogfood 2026-10-01) User tasks express actions toward goals; the swim lane is this workshop's way to make the workflow concrete. [book:user-story-mapping], Tasks Are What We Do

## Automation levels

Describe the proposed degree of automation as assisted, augmented, or autonomous. These labels make the human and system roles explicit while the client compares alternatives. [book:art-of-ai-product-development], 3.3.2 Assisted, augmented, and autonomous intelligence

For each proposed output, ask whether the user can independently check it before acting. Outputs containing objective information that drive action need a secondary human verification layer. [book:designing-ai-interfaces], Designing for Verifiability

## Agent purpose and handoff

Write each proposed agent's purpose in plain language: what it should do, for whom, and within which workflow. A natural-language purpose gives the team a reference point for outcomes and governance. [book:agentic-mesh], Identity, Description, and Purpose

Treat the workflow as a client-validated sketch. Capture unresolved decisions, required data, human checks, and candidate tasks for the architecture handoff; do not present the card as a finished design.
