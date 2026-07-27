# Clarification Questions — template

*Two buckets. Bucket 1 goes to the client; Bucket 2 you route internally or decide yourself. Business/domain-first ordering; logistics last or omitted. Guidance: `../rfi-rfp-response.md`.*

**Pairing rule:** every Bucket-1 question carries a **fallback assumption** — what you proceed on if it goes unanswered. Copy each fallback into the assumptions register (`assumptions-register.md`) so the pairing is structural. On an RFI, assume some questions go unanswered.

**Impact rule:** every Bucket-1 question also states **what changes if the assumption turns out wrong**. This is the column that actually gets a client to answer — a question with a visible consequence gets prioritised; a bare question gets deferred. It is also what tells *you* which unanswered questions are safe to proceed on.

**Spine rule:** on a delivery engagement, each question cites the **acceptance criterion** it serves (`../artifact-integrity.md`). A question serving no criterion is either scope you haven't captured or a question you don't need. On an enterprise bid, cite the requirement ref instead.

## Bucket 1 — Questions for the client

| # | Priority | Serves criterion / req ref | Category | Question | Our working assumption | Impact if the assumption is wrong | Client answer | Answered by |
|---|----------|----------------------------|----------|----------|------------------------|-----------------------------------|---------------|-------------|
| 1 | `P1` | `[TC-1.1.1]` | `[Business value & scope]` | `[business/domain-first, outcome-framed]` | `[what we proceed on → goes to register]` | `[what changes in scope, cost, schedule, or architecture]` | | |
| 2 | `P2` | | | | | | | |

*Priority is binary and honest: **P1** blocks a criterion, a price, or a design decision — **P2** improves the answer but you can ship without it. If everything is P1, nothing is; the client will answer the short list first and you want to choose which one that is.*

*Group the rows by function or requirement area with section headers — clients answer a sheet organised the way they think about their business, not the way you numbered it.*

## Bucket 2 — Resolve internally / decide ourselves

| # | Original ask | Why not ask the client | Action / owner |
|---|--------------|------------------------|----------------|
| 1 | `[logistics: dates, contacts, presentation format]` | `[partner already knows; spending goodwill]` | `[route to account partner]` |
| 2 | `[document convention: template mismatch, numbering]` | `[self-answerable; asking reads as junior]` | `[state our convention in the response]` |
| 3 | `[anything researchable: public company facts, product ranges, market context]` | `[research, not a client question]` | `[look it up]` |

*Reframe "tell us your config" → "what outcome / what baseline." Prune to the high-signal set; a tight list beats an exhaustive one that buries the good questions.*
