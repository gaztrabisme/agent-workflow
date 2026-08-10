# ai-discovery-workshop

A [Claude Agent Skill](https://agentskills.io/specification) for running an **AI Discovery & Envisioning workshop** with an enterprise client — the structured two-session engagement that takes a client from vague AI ambition to one use case scored, agreed, and ready for a funded proof of value.

## What it covers

| | |
|---|---|
| **The flow** | Discover → Define → Develop → Deliver, with the named method at each stage |
| **Scoring** | BXT (Business / Experience / Technology) and the five golden screening questions per pillar |
| **The cards** | 79 AI Discovery Cards + 12 Agentic Cards, organised by transformation pillar |
| **Facilitation** | Verbatim questions to ask the client, by phase |
| **Commercial** | Where the funding conversation belongs in the arc, and how to build an ROI claim that survives the CFO |

Targets 3–5 agentic use cases per engagement, narrowed to one approved for PoV by the close of the second session.

## The two rules that matter most

**Scope to two domains: human experience and business process.** These are the only two areas the framework targets. If a candidate use case isn't clearly enriching an experience or reshaping a process, stop and rescope.

**Don't overconfident-consult.** If you can't defend a claim under pushback, don't make it. Not timidity — it's not getting caught by a follow-up question you can't answer. Flag uncertainty, know the negative space, back every number into the client's own baseline.

## Why the workshop exists at all

Roughly 80% of AI projects fail, and the common cause is solving the wrong problem well. Everything here is built to spend a client's first two sessions on *which* problem, not on which model — because the cost of picking wrong compounds through every subsequent phase, and no amount of engineering rescues a use case nobody needed.

That is also why BXT scoring is non-negotiable rather than decorative. A use case that scores well on Business and Experience but honestly badly on Technology is a *later* use case, not a dead one — and saying so in the room is what buys the credibility to be believed on the one you do recommend.

## Install

```bash
git clone https://github.com/gaztrabisme/ai-discovery-workshop.git ~/.claude/skills/ai-discovery-workshop
```

**Dependency:** references the `core` kernel at `../core/` for the shared spine (integrity constraints, grounding gate, output contract). Without it those links dangle:

```bash
git clone https://github.com/gaztrabisme/core.git ~/.claude/skills/core
```

Composes with [`business-intelligence`](https://github.com/gaztrabisme/business-intelligence) (client research before Day 1) and [`solution-architect`](https://github.com/gaztrabisme/solution-architect-skill) (turning the workshop output into an architecture and a proposal). Its ledger follows the [`evolution`](https://github.com/gaztrabisme/evolution) loop.

## Vendor neutrality

The method is deliberately platform-agnostic. Where a specific product would normally be named, the skill names the *category* — an off-the-shelf assistant, a low-code agent builder, a managed LLM service, a unified data platform — so the scoring works whichever cloud the client already runs on. Map to their stack, not to yours; a workshop that quietly assumes one vendor has stopped being discovery and started being a pitch.

## Honesty about its own status

Its verdict is `PENDING` and should stay there: **no real workshop has yet been run through this skill and written up.** `EVOLUTION.md` records that plainly, along with exactly what a later harvest has to check — whether the golden questions produced usable answers, whether BXT scores changed a scoping decision or merely decorated one, and whether the discovery cards got used at all.

A log that shows its own gaps is worth more than one that doesn't.

## License

MIT
