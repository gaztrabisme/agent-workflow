# Facilitator Prompts

## Use prompts literally

Use these questions as literal workshop prompts; do not rephrase them. Ask clarifying follow-ups as needed while preserving the provided wording.

Keep questions open-ended. Invite the client to tell what happens, explain why it happens, or describe a decision or handoff. [book:meddicc], DISCOVERY

## Define: questions for BXT scoring

Use the Golden Questions in references/five_golden_questions.md. Ask about outcomes, affected users, data, risk, and unknowns before assigning a score. Do not score a pillar without asking its questions.

## Define: problem statement

Invite the client to describe the problem in their own words: “We see [person or role] trying to [goal] in [context]. What gets in the way, and what result would matter?” Keep the framing open so it does not dictate a solution. Adapt the starter to the team and its context. [book:lean-ux], Problem Statement

## Develop: journey map prompts

- **User lane:** What does the user do now, in order, to reach the goal? Where do they wait, decide, hand off, or recover from an error? Mapping today's work helps reveal the problem the user is solving. [book:user-story-mapping], 2. Understand Customers and Users
- **AI Discovery lane:** Which substeps could AI augment or automate, and where should the boundary sit? Delimit the process substeps rather than labeling the whole process as an AI task. [book:art-of-ai-product-development], 10.1 Discovery and user research
- **Agentic Workflow lane:** Which tasks require multiple steps or decisions, and what goal, constraint, or policy shapes each one? Agent planning addresses multi-step and decision-heavy tasks. [book:art-of-ai-product-development], 9.2.2 Planning the task execution

## Deliver: choose an approach

Ask the group to work through four dimensions:

### Data

What data is needed, in what modality, and where is it available? What data or modality limits the model or engineering choices? [book:art-of-ai-product-development], 3.1 Data

### Customization

Can a prompt or retrieval from trusted sources meet the need, or would fine-tuning be worth assessing? [book:art-of-ai-product-development], 8.1.2 Evaluating fine-tuning as a solution

### Development complexity

What skills, time, compute, integration, and operating effort would each approach require? Fine-tuning can add computational, expertise, and time demands. [book:art-of-ai-product-development], 8.1.2 Evaluating fine-tuning as a solution

### End user

Who uses the system, what skills do they have, and where do trust, control, or human approval matter? [book:art-of-ai-product-development], 10.1.2 Understanding the skills and psychology of your users

Use these as hypotheses to compare, not automatic prescriptions:

- An off-the-shelf assistant may fit low-data, low/no-code use with nontechnical users; pretrained models and existing frameworks can be faster and more cost-effective than custom training. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation
- A custom assistant may fit multiple data sources, moderate customization, and a team prepared for pro-code work. Consider fine-tuning only when the team's background or motivation supports it. [book:art-of-ai-product-development], 8.1.2 Evaluating fine-tuning as a solution
- A unified data platform may fit complex infrastructure, full customization, and technical users when the learning problem's nature and complexity call for it. [book:art-of-ai-product-development], 3.2 Different types of intelligence

## Deliver: estimate value

Replace placeholders with the client's workflow, baseline metric, and target improvement. Start with the time currently spent on the task, then quantify possible savings in the client's terms. [book:art-of-ai-product-development], 12.3.1 Communicating the value of your AI

If no baseline exists, record that gap and include measurement in the PoV plan rather than assuming an improvement.

## Deliver: solution notes for handoff

After a use case is selected for PoV, ask:

- Which secondary personas act in the workflow, and what are their actions and decision points? [book:user-story-mapping], Describe Your Customers and Users
- Where does a person need to review, approve, or be able to stop an action? [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation
- Who is Responsible, Accountable, Consulted, and Informed for each important step? Represent roles and relationships clearly. [book:pmbok-guide-7e], 4.6.6. Visual Data and Information
- Which workflow goals, tasks, and constraints should ground the proposed agent? Give each agent a plain-language purpose describing what it should do. [book:agentic-mesh], Identity, Description, and Purpose

Capture the answers as client-validated design inputs for the architecture and implementation handoff. They are not a final architecture.
