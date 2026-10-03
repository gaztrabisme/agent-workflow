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

Before a requirements or proposal document crosses to someone who can reject it, review it while it is still a document and before resources commit to delivery. The persona-crossing trigger is conductor’s own: use this for stakeholder judgment, incentives, and reception. [book:swebok], 6. Requirements Validation.

**Do not use a persona where a fact or real user evidence would settle it.** "Would the regulator allow this" needs a source; an affected user’s task needs testimony or observation. Personas are for judgment, incentive, and reception — never a substitute for evidence. [book:swebok], 3.2. Elicitation Techniques.

## Casting

Cast from the **actual stakeholder map**, not a generic list. If upstream work has mapped buyers, sponsors, blockers, and their needs, use those people. Otherwise derive the map from the situation, disclose that it was derived, and make a point of seeking advice from uncomfortable sources as well as familiar ones. [book:facilitating-software-architecture], Step 2a: Making your set of decision options; [book:facilitating-software-architecture], Seek advice from those with conflicting views.

For an internal artifact, cast the people who will use or maintain it, even when there is no buying committee. Use the user reactions in `design-cell.md` Step 6 to ground that cast when available. Keep the persona pass on interpretation, workflow, incentives, and reception; verify domain conventions with a source or an actual expert rather than treating role-play as evidence. (derived: dogfood 2026-10-01)

The archetypes worth covering — pick the 3–5 that exist in *this* situation:

- **Economic buyer** — signs and pays. Objects on price, downside, and what happens when it fails.
- **Blocker** — can say no for their own reasons: legal, IT, procurement, a rival sponsor, someone whose prior decision this contradicts.
- **End user** — has to actually use it and was not in the room. Objects on effort, trust, and whether it is worth changing habits for.
- **Operator** — inherits it after handover and lives with every shortcut. Objects on what breaks at 3am.
- **Rival / incumbent** — what they say in the room *after you leave*. Objects by reframing.
- **Regulator / auditor** — only where there is a legal surface. Objects on evidence and traceability.

Two casting rules:

1. **Never cast only the friendly personas.** Seek advice from people with conflicting views; include someone who can block or kill the proposal. The blocker requirement is this skill’s operational safeguard. [book:facilitating-software-architecture], Seek advice from those with conflicting views.
2. **Cast the specific person, not the role.** *"You are a CFO"* returns generic CFO noise. *"You are an investor who has compressed every budget he has touched this year, who is being asked for a check at a valuation with no comparable, and whose real return is a round-2 markup"* returns the objection that actually lands. Specificity is the entire yield. [book:getting-to-yes], 2 Separate the People from the Problem.

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
behind it and you are not obliged to be fair. [book:research-methods-psychology], Threats to Internal Validity: Did the Independent Variable Really Cause the Difference?

Return:

1. DECISION — sign / stall / counter / refuse. One of those four words, then
   the real reason in one sentence. "Stall" is a decision and is the most
   common one; do not round it to yes or no. [book:getting-to-yes], 7 What If They Won't Play?

2. OBJECTIONS — ranked by their effect on your decision. For each, say what
   you object to, what you care about and want, and whether the artifact
   already answers it or does not address it. [book:articulating-design-decisions], Anticipate Reactions.

3. THE UNSPOKEN ONE — what you would NOT say in the meeting but would say
   to your colleague afterwards. This is the highest-value line you produce.

4. MISREADING — what you understood and what context or wording led you
   there. Treat a misreading as a possible communication gap to clarify,
   not as a demand for a line-by-line quotation. [book:articulating-design-decisions], What's Really Going On?

5. WHAT WOULD CHANGE YOUR MIND — the specific thing that moves you from
   your decision to a better one. If nothing would, say so. [book:bargaining-for-advantage], Purpose 3: Signaling Expectations and Leverage.

Stay in your interests throughout. Do not be constructive, do not balance
your view, and do not write in character — no dialogue, no scene-setting.
Return the five sections and nothing else.
```

## Convergence — an objection register, not a synthesis

Persona threads converge **differently from research threads.** Research converges on a fact; personas converge on a *ranked list of things that can stop you*. Never average them or erase the kind of objection; disagreement between personas is signal, and a consensus view is the one artifact that helps nobody. [book:learning-systems-thinking], Middle ground.

Build one register:

| Objection | Raised by | Already answered? | Planned response |
|---|---|---|---|

- Rank objections by their consequence for the decision, including whether the person can block it; do not count repeated mentions as votes. Keep blocking power, gap type, and owner in the planned response when needed, not as extra register columns. [book:learning-systems-thinking], Bandwagon.
- Resolve the kind of gap in the planned response:
  - **Presentation gap** — the artifact answers this, but the persona missed or misunderstood it. Clarify the context and fix the document where that will prevent the same misunderstanding. [book:articulating-design-decisions], What’s Really Going On?
  - **Substance gap** — there is no answer. The fix is a decision, a concession, or more work — and it goes into `DECIDE NOW` for the next run, not silently onto a backlog.
  - **Fact gap** — settling it needs sourced evidence. Spawn a research stream (`task-force-protocol.md`); do not resolve it by opinion.
- **Unspoken objections get their own section** and are quoted verbatim. They are the reason to run this at all.

Land the register beside the artifact and retain advice in its raw form with the decision record. Record in wiki/decisions.md which objections were accepted, priced in, or consciously ignored, and why. An objection you decided to accept is a decision; an objection you forgot is a defect. [book:facilitating-software-architecture], Gathering Advice.

## Anti-patterns

- **Persona theatre** — in-character prose, dialogue, invented meeting scenes. Return decisions and objections.
- **The rationale leak** — giving the persona the reasoning; it then argues *for* the artifact.
- **Friendly cast** — no one in the room who can say no.
- **Averaging** — merging personas into a balanced consensus view, destroying the disagreement that was the yield.
- **Persona instead of research** — role-playing a question that a source would answer.
