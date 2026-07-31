# Deal shapes — pick the machinery before you use it

Most of this skill's machinery was derived from one kind of deal: a scored, multi-round **enterprise bid**.
That machinery is real and it works — but it is not universal, and applying it to a different deal shape is
how a skill starts generating ceremony instead of leverage.

**Declare the shape in Phase 0.** Everything downstream — what the spine is, what carries the engagement,
how it's priced, and what "done" means — follows from it.

## The two shapes

| | **Enterprise bid** | **Fixed-price delivery** |
|---|---|---|
| **Trigger** | RFI / RFP / tender. Scored, multi-round, often multi-vendor. | Direct brief or negotiated engagement. Single vendor, relationship-led. |
| **Buyer behaviour** | Procurement-mediated; formal Q&A rounds; published or inferable criteria. | Owner/executive-mediated; conversational; criteria are personal and often unstated. |
| **Spine** (the ID everything keys to) | **Requirement refs** from the client's document. | **Acceptance-criteria IDs** you author. |
| **Carrier artifact** | Blueprint workbook (`blueprint-workbook.md`). | Acceptance annex + client-obligation register (`acceptance-and-contract.md`). |
| **Pricing chain** | WBS → effort distribution → blended rate → total (`estimation-and-costing.md`). | Lump sum per phase, plus CapEx/BOM where hardware is in scope. |
| **What you're defending** | Coverage and score. | Scope boundary and payment gates. |
| **Terminal artifact** | The response, submitted. | The contract, signed. |
| **Biggest risk** | A scored gap you didn't trace. | An acceptance criterion you can't run because the client didn't deliver something. |

## Axis 2 — declare the recipient

Shape tells you what the *deal* is. It does not tell you who picks the artifact up next, or what they have
to decide with it. Both axes are needed, and the second one is easier to forget because the skill has
historically only had a name for the first.

Declare it beside the shape, in one line:

`Recipient: <role> — decides <what> — therefore the primary artifact is <shape>`

| Recipient | What they decide | Primary artifact | What is noise to them |
|---|---|---|---|
| **Client evaluator** | whether to buy, and from whom | the response — narrative, win themes, traceability as proof | internal capacity maths, cut order, your risk register |
| **Delivery planner (PM / TL)** | release split, staffing, sequence | a WBS **instrument** — task rows, disciplines, **effort column empty** | scope defence, assumptions prose, commercial framing |
| **Engineering team** | how to build it | spec, contracts, data models, success criteria | pricing, positioning, commercial risk |
| **Signing counterparty** | what they are bound to | acceptance annex + obligation register | architecture detail, options analysis |

**Why this page needed a second axis.** On a real engagement the shape was declared correctly — fixed-price
delivery, workbook explicitly rejected as ceremony — and the primary artifact was still rejected by its
recipient. It was eight sheets: Summary · Scope-In · Scope-Out · WBS · Capacity · Assumptions · Obligations
· Risks. **Three about the work; five about defending the number.** Correct for a client evaluator, noise
to a PM distributing tasks to discipline leads. His verdict: *"this is governance and process, not
implementation."* He then rebuilt it himself, with five times the rows and a third of the words per cell.

The machinery was not wrong. It was aimed at the wrong reader — which is a selector problem, not a
retraction (`../../core/references/evolution-loop.md`).

## What both shapes share

These are shape-independent — never skip them on the grounds that "this is only a small deal":

- **Phase 0 intake** — the frame, the fact/inference separation, the negative space (`engagement-intake.md`).
- **Question ↔ assumption pairing** — every load-bearing question paired with the position you proceed on
  if it goes unanswered (`templates/clarification-questions.md`).
- **Options analysis** — 2–3 viable options, recommend one, say why the others lost (`tech-selection.md`).
- **NFRs** — security, scale, residency, integration, operations (`nfr-checklist.md`).
- **Artifact integrity** — one ID spine, every artifact a view over it (`artifact-integrity.md`).
- **Final QA pass** — the mechanical last read by a non-author (`rfi-rfp-response.md`).

## Choosing, and the honest middle

Ask three questions:

1. **Is there a scored document to answer?** Yes → enterprise bid. No → fixed-price delivery.
2. **Who authors the acceptance criteria?** The client's requirements list → enterprise bid.
   You, as part of the contract → fixed-price delivery.
3. **What signature ends the presale?** A submission receipt → enterprise bid. A contract → fixed-price.

**Hybrids are common and legitimate.** An enterprise bid that you win becomes a fixed-price delivery
contract; the shape *changes mid-engagement* and the machinery should change with it. When it does, say so
explicitly and migrate the spine: requirement refs become acceptance criteria, and the traceability matrix
becomes the acceptance annex. That migration is the single most defect-prone moment in an engagement — run
`artifact-integrity.md` across the boundary.

## Sizing within a shape

Shape tells you *which* machinery; deal size tells you *how much* of it.

- **A one-pager clarification** on an enterprise bid needs Phase 0–2 and nothing else. No workbook, no
  blended rate.
- **A small fixed-price engagement** still needs acceptance criteria and an obligations register — those
  *are* the deal — but may not need a phased roadmap or a risk register with owners.
- The rule from `SKILL.md` holds: start light, add depth only where the deal's risk demands it. A skipped
  step is fine; a **silently** skipped step is not.

## Why this page exists

The skill's workbook and blended-rate chain were distilled from a single enterprise engagement and written
as though every deal worked that way. A later, independent engagement — fixed-price, acceptance-gated,
hardware-inclusive — adopted **neither**, and the initial read was that both hypotheses had failed
validation. They hadn't. They were correct machinery, over-generalized from one shape. This page is that
correction, and it is the reason later machinery pages carry an applicability header naming the shape they
serve.
