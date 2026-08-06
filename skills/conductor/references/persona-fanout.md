# Persona Fan-Out

Run an artifact past the people who will actually receive it — each agent inhabiting **one stakeholder's incentives**, reacting as that person would.

This exists because stakeholders reject things for reasons that have nothing to do with correctness. A verification agent checks whether the work is right. An adversarial reviewer tries to prove it wrong. **Neither can tell you that the person signing will stall for three weeks because approving it makes their last decision look bad.** That objection is invisible to every gate in the constellation, and it is the one that kills deals.

## Persona vs the briefs it is not

| | Asks | Is | Output |
|---|---|---|---|
| **Research agent** | what is true? | neutral | sourced findings |
| **Adversarial reviewer** | is this claim wrong? | hostile, but disinterested | verdicts on the artifact |
| **Persona agent** | what would *I* do about this? | **deliberately partial** | a decision + the objections behind it |

A persona is *supposed* to be biased. That is the instrument. Do not correct for it.

## When it fires

Before anything crosses a boundary to a person who can say no: a proposal, a deal document, a spec being handed to a team, a product decision, a price, a plan someone must live inside. Cheap on prose, expensive on shipped code — **contest the frame while it is still a document.**

**Do not use a persona where a fact would settle it.** "Would the regulator allow this" is a research stream with a citation, not a role-play. Personas are for judgment, incentive and reception — never a substitute for grounding.

## Casting

Cast from the **actual stakeholder map**, not a generic list. If `business-intelligence` has done stakeholder mapping or `solution-architect` has an engagement frame with buyer / sponsor / blocker slots filled, those are the cast. Otherwise derive them, and say you derived them.

The archetypes worth covering — pick the 3–5 that exist in *this* situation:

- **Economic buyer** — signs and pays. Objects on price, downside, and what happens when it fails.
- **Blocker** — can say no for their own reasons: legal, IT, procurement, a rival sponsor, someone whose prior decision this contradicts.
- **End user** — has to actually use it and was not in the room. Objects on effort, trust, and whether it is worth changing habits for.
- **Operator** — inherits it after handover and lives with every shortcut. Objects on what breaks at 3am.
- **Rival / incumbent** — what they say in the room *after you leave*. Objects by reframing.
- **Regulator / auditor** — only where there is a legal surface. Objects on evidence and traceability.

Two casting rules:

1. **Never cast only the friendly personas.** A cast without someone who can kill it is theatre.
2. **Cast the specific person, not the role.** *"You are a CFO"* returns generic CFO noise. *"You are an investor who has compressed every budget he has touched this year, who is being asked for a check at a valuation with no comparable, and whose real return is a round-2 markup"* returns the objection that actually lands. Specificity is the entire yield.

## The brief

Give each persona the **artifact cold**. Withhold the reasoning behind it — a persona handed the rationale defends it instead of attacking it.

```
You are <name/role>. Your situation:
  - What you are measured on: <...>
  - What you are afraid of: <...>
  - What a win looks like FOR YOU: <...>
  - Your constraints: <budget, authority, timeline, politics>
  - What you already believe about this: <priors>

Read the attached artifact as this person. You have NOT seen the reasoning
behind it and you are not obliged to be fair.

Return:

1. DECISION — sign / stall / counter / refuse. One of those four words, then
   the real reason in one sentence. "Stall" is a decision and is the most
   common one; do not round it to yes or no.

2. OBJECTIONS — ranked. For each: what you object to, how hard it would be
   to satisfy you, and whether the artifact ALREADY answers it (badly) or
   does not address it at all.

3. THE UNSPOKEN ONE — what you would NOT say in the meeting but would say
   to your colleague afterwards. This is the highest-value line you produce.

4. MISREADING — where the artifact is ambiguous in a way that hurts its
   author. Quote the exact line and say what you took it to mean.

5. WHAT WOULD CHANGE YOUR MIND — the specific thing that moves you from
   your decision to a better one. If nothing would, say so.

Stay in your interests throughout. Do not be constructive, do not balance
your view, and do not write in character — no dialogue, no scene-setting.
Return the five sections and nothing else.
```

## Convergence — an objection register, not a synthesis

Persona threads converge **differently from research threads.** Research converges on a fact; personas converge on a *ranked list of things that can stop you*. Never average them — disagreement between personas is signal, and a consensus view is the one artifact that helps nobody.

Build one register:

| Objection | Raised by | Blocking power | Already answered? | Type | Owner / fix |
|---|---|---|---|---|---|

- **Blocking power** — can this person alone stop it? High / medium / low. Rank by this, not by how many personas raised it. One blocker beats three end users.
- **Type** is the split that decides the work:
  - **Presentation gap** — the artifact answers this, but the persona missed it or misread it. The fix is in the document, and it is cheap.
  - **Substance gap** — there is no answer. The fix is a decision, a concession, or more work — and it goes into `DECIDE NOW` for the next run, not silently onto a backlog.
  - **Fact gap** — settling it needs sourced evidence. Spawn a research stream (`task-force-protocol.md`); do not resolve it by opinion.
- **Unspoken objections get their own section** and are quoted verbatim. They are the reason to run this at all.

Land the register beside the artifact and record in `wiki/decisions.md` which objections were accepted, which were priced in, and which were consciously ignored — with the reason. An objection you decided to accept is a decision; an objection you forgot is a defect.

## Anti-patterns

- **Persona theatre** — in-character prose, dialogue, invented meeting scenes. Return decisions and objections.
- **The rationale leak** — giving the persona the reasoning; it then argues *for* the artifact.
- **Friendly cast** — no one in the room who can say no.
- **Averaging** — merging personas into a balanced consensus view, destroying the disagreement that was the yield.
- **Persona instead of research** — role-playing a question that a source would answer.
- **Register without types** — a flat objection list, so a cheap wording fix and a missing business model look identical.
