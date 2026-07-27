# RFI / RFP / Proposal Response — fill-in template

*Vendor-neutral skeleton, generalised from a real enterprise AI RFI response. **Map sections to the client's required structure and numbering exactly** — the §1–7 numbering below is illustrative; if the client publishes e.g. a §4.1–4.7 layout, renumber to match theirs. Replace every `[bracketed placeholder]`. Delete guidance notes (in italics) before submission. If the client mandates a solution presentation/demo (common), add a short commitment block (see §8). Companion guidance: `../rfi-rfp-response.md`.*

---

**RESPONSE TO [RFI / RFP] — [Engagement / solution name]**
Prepared for: `[Client legal entity]` `[+ parent/group if relevant]`
Respondent: `[Your registered legal entity]`
Date: `[dd/mm/yyyy]` · Version: `[1.0]` · **PRIVATE & CONFIDENTIAL**

---

## 1. Executive Summary
*The most-read section. State the outcome, the approach in ~3 sentences, and the win themes — not a feature dump.*

`[One paragraph: the business outcome we deliver and the headline approach.]`

`[One paragraph: the shape of the solution — neutral capability language, the one or two differentiators that matter to this client.]`

**Phased delivery** *(de-risk + show value early; adjust count/names to the deal):*

| Phase | Scope focus |
| --- | --- |
| Phase 1 | `[lowest-risk, fastest-value slice]` |
| Phase 2 | `[…]` |
| … | … |

**Why us:** `[2–3 proof points mapped to the client's evaluation criteria — relevant domain experience, residency/compliance fit, time-to-value, references, total cost. Each backed by evidence.]`

## 2. Company Information
*Complete every field the client asks for; don't boilerplate the description — tailor to the domain.*

| | |
| --- | --- |
| Company name | `[…]` |
| Registration number | `[…]` |
| Business / correspondence address | `[…]` |
| Description of business | `[tailored to this engagement's domain]` |
| Representatives (name, title, phone, email) | `[…]` |
| Nature of company / incorporation | `[…]` |

## 3. Skills & Services Offering
*Map your capabilities onto the categories the client named (consulting / integration / infrastructure / analytics / support). A ticked summary often goes in an appendix.*

- **Consulting:** `[…]`
- **Implementation / integration:** `[…]`
- **Infrastructure & platform:** `[…]`
- **Analytics, monitoring & optimisation / support:** `[…]`

## 4. Solution
*The core. Lead with a narrative, then the reference architecture, then options/recommendation, then how it meets each requirement. Written explanation is authoritative; diagrams illustrate.*

### 4.1 Solution overview
`[One paragraph tying the client's stated vision to your solution end-to-end.]`

### 4.2 Reference architecture
*Describe in layers; the prose is the authoritative description, diagrams are renderings.*
- **Entry / channels:** `[…]`
- **Application / orchestration:** `[…]`
- **Core capability:** `[…]`
- **Integration:** `[…]`
- **Data:** `[…]`
- **Security & governance:** `[…]`

*Insert diagrams (use the `drawio` skill): **context** → **component** → **data** → **deployment** (regions/network/residency) → a **key-flow sequence** for the sensitive journeys. Render only the views the deal needs; they're load-bearing if the client mandates an architecture demo.*

### 4.3 Options analysis & recommendation
*Vendor-neutral comparison on the axes that matter to THIS client, then recommend. See `../tech-selection.md`.*

| Consideration (axis) | Option A | Option B | Option C |
| --- | --- | --- | --- |
| `[the hard constraint]` | `[reason-bearing cell]` | | |
| `[…]` | | | |

**Recommendation:** `[option or hybrid]` — `[why, anchored to the top axis; why the others lost]`.
**Design-time checks:** `[what must be confirmed before commit]`.

### 4.4 Technology stack
*Only after the neutral comparison. Map capability → named technology.*

| Capability | Technology |
| --- | --- |
| `[…]` | `[…]` |

### 4.5 Key flows
*2–4 representative end-to-end journeys showing the architecture in action (esp. the sensitive/secure ones).*
- **`[flow name]`:** `[step-by-step, calling out where security/identity/data boundaries sit]`

### 4.6 Cross-cutting design
*One short subsection each — these are where credibility is won (run against `../nfr-checklist.md`).*
- **Integration:** `[patterns: sync / async / event; gateway; resilience]`
- **Security, identity & data residency:** `[authn/authz, encryption, masking, residency, audit]`
- **Scale, performance & reliability:** `[volumes, latency targets, availability, DR]`
- **Governance & quality:** `[lineage, approval, monitoring; for AI: eval/groundedness gates]`

### 4.7 Requirements response
*Answer each client requirement. For long lists, a table; for a few, prose.*

| Ref | Client requirement | Our approach & technology |
| --- | --- | --- |
| `[x.y]` | `[verbatim / tight paraphrase]` | `[how we meet it]` |

## 5. Operational Support
| No | Question | Response |
| --- | --- | --- |
| 1 | `[warranty / support tiers / maintenance as asked]` | `[…]` |

## 6. Pricing
*Follow the client's pricing format; complex pricing usually goes as separate labelled attachments. Match precision to RFI (light) vs RFP (precise). **Answer every pricing question the client asks or explicitly defer it to a labelled attachment — never leave it blank.** Common asks: itemised cost (hardware/software/licences/services/cloud rate card/testing/training/Y1 support); lease / base+option terms & cancellation; COTS vs bespoke; Year 1–5 maintenance schedule; multi-year TCO. SA supplies the cost drivers/framing; final numbers come from the bid/commercial owner.*

| No | Question | Response |
| --- | --- | --- |
| 1 | `[itemised price / TCO / lease / COTS / Y1–5 maintenance as asked]` | `[… or "see attachment Pricing-Qn"]` |

## 7. Implementation Schedule
*WBS, roles (on-site vs remote), risk approach, dated timeline/Gantt.*

| No | Question | Response |
| --- | --- | --- |
| 1 | `[schedule / roles / risk / Gantt as asked]` | `[…]` |

## 8. Solution Presentation & Demonstration
*Include only if the client mandates or invites a session (many RFIs do). Confirm format and commit the right people.*

`[Confirm attendance at the [duration] session covering (1) business-user capabilities/use cases and (2) technical architecture/integration/security; name the business and technical specialists who will attend and handle Q&A. State demo vs walkthrough if the client specified.]`

---

## Appendix A — Compliance & Requirements Traceability Matrix
*Proof of coverage. Every requirement → solution element → technology → phase. No silent gaps.*

| Requirement area | Ref | Coverage | Component | Technology | Phase |
| --- | --- | --- | --- | --- | --- |
| `[…]` | `[x.y]` | `[Met/Partial/Clarify/Excluded]` | `[…]` | `[…]` | `[P1…]` |

*Every requirement ref must appear here. RFP → one row each; RFI → may group, but no ref is dropped. `Clarify` = mapped to an open clarification question, not a silent gap.*

## Appendix B — Service Offering
*Tick/confirm the services per the client's table. If their table is mis-templated, state your mapping convention rather than asking permission.*

## Annex — Assumptions, Data Handling & Residency
**Assumptions register** *(everything unconfirmed — state it correctably):*

| # | Assumption | Basis | Impact if wrong | To confirm with |
| --- | --- | --- | --- | --- |
| 1 | `[…]` | `[…]` | `[…]` | `[…]` |

**Data handling / residency / confidentiality:** `[commitments per the client's NDA/special terms — residency, no-training-without-consent, conflict of interest, applicable data-protection law].`
