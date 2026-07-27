# solution-architect

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for **presale solution architecture** —
turning a client's stated need (an RFI, an RFP, a workshop output, or a conversation after a site visit)
into a solution the client can buy and a team can build.

Vendor-neutral by default. The output is an architecture and a response you can defend in the evaluation
room: every requirement traced, every major choice justified against alternatives, every assumption stated,
every non-functional risk named before the client finds it.

## What's in it

An eight-phase lifecycle, scaled to the deal rather than run wholesale:

| Phase | Produces |
|-------|----------|
| **0. Intake** | An engagement frame from an informal dump, plus ≤5 asks only the human can answer |
| **1. Frame** | The problem, sponsor, evaluation criteria, constraints |
| **2. Clarify** | Clarification questions paired 1:1 with fallback assumptions |
| **3. Architect** | Options analysis → reference architecture, integration, security, residency, NFRs |
| **4. Plan** | Phasing, sizing, risk register, commercial drivers |
| **5. Respond** | The response document + requirements-traceability matrix |
| **6. Contract & Acceptance** | Acceptance criteria that gate payment + a client-obligation register |
| **7. Handoff** | Decision records + a build-ready brief |

Supporting references cover deal shapes, engagement intake, tech selection, an NFR catalog with forcing
questions, RFI/RFP response anatomy, the blueprint workbook, estimation and costing, acceptance and
contract, and cross-artifact integrity checks — plus fill-in templates for the frame, clarification
questions, assumptions register, obligations register, and the response itself.

## Two ideas it's built around

**Pick the deal shape before reaching for machinery.** A scored enterprise bid and a fixed-price delivery
contract need different instruments — different ID spines, different carrier artifacts, different pricing
chains. Applying one shape's machinery to the other produces ceremony instead of leverage. See
`references/deal-shapes.md`.

**An engagement is a graph, not a folder.** By mid-engagement the proposal, cost model, acceptance annex,
clarification sheet, WBS and translations all restate the same facts. When they disagree, nobody wrote a bad
sentence — the same fact has four values in four files. `references/artifact-integrity.md` is the
mechanical check for that, and it catches a different defect class than a proofread does.

## Install

Clone into your skills directory:

```bash
git clone https://github.com/gaztrabisme/solution-architect-skill.git \
  ~/.claude/skills/solution-architect
```

### Dependency: the `core` kernel

This skill inherits its shared operating spine — integrity constraints, gate-by-artifact, the wiki
protocol, the grounding gate, pushback-and-teach, and the evolution loop — from a sibling skill rather than
restating them. Install it alongside:

```bash
git clone https://github.com/gaztrabisme/core.git ~/.claude/skills/core
```

The `../core/references/…` links resolve when both live in the same skills directory. Without `core` the
skill still works, but those cross-references won't open.

## Composes with

```
business-intelligence → ms-ai-discovery → [ solution-architect ] → dev
  (know the client)     (scope use cases)   (architect + respond)   (build it)
```

`solution-architect` handles the client-facing presale artifact. When the audience is the engineering team
rather than the client — implementation specs, data models, feature work — that's a build skill's job, not
this one. The disambiguation rule: artifact goes *to the client to win the deal* → here; artifact goes *to
engineers to build it* → your build skill.

## How it evolves

`EVOLUTION.md` records what changed, why, and whether it survived contact with a later engagement. A change
distilled from a single engagement carries that engagement's assumptions, so its verdict stays `PENDING`
until an independent use confirms it — and the log keeps the failures visible, including two hypotheses
that a later engagement declined to adopt and what that turned out to mean.

## License

MIT — see `LICENSE`.
