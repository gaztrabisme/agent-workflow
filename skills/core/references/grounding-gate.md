# Grounding Gate

Ground domain decisions in a substrate rather than improvising from memory. This is a **gate**, not a suggestion: on a covered domain, consult the substrate *before* deciding and record one line.

## The gate

1. **Before** designing/implementing/claiming in a covered domain, consult the substrate for prior art / exact terms / theory.
2. **Record one line** where decisions live (Key Decisions / decisions.md / the response):
   - `Grounded: <query/source> → applied <finding>`, or
   - `Grounded: <query/source> → nothing relevant`.
3. **Skippable only** by stating the domain isn't covered (e.g. glue code, pure logistics). A silent skip on a covered domain is a gate violation.

The point is cheap, honest grounding — one consult, one line — not ceremony.

## Substrate by role

| Role-skill | Substrate | Covered domains |
|------------|-----------|-----------------|
| `dev` | Knowledge Base MCP (46 books) | ML, RAG, databases, security, distributed systems, cryptography |
| `business-intelligence` | External sources, graded by the Admiralty Code | any factual claim about a client, market, competitor, or person |
| `solution-architect` | Internal/client docs + KB for the tech layer | the RFI/RFP itself, architecture patterns, NFRs, the client's stated constraints |
| `ms-ai-discovery` | The Microsoft partner-training source + internal docs | BXT, discovery methods, Azure Accelerate, the stack |
| `skill-builder` | Existing skills + this `core` kernel | conventions, the spine, prior skills' patterns |

## The honesty corollary (why this is also an integrity gate)

Grounding is the mechanism behind three integrity rules at once:

- **A claim you cannot ground, you do not make** — or you flag it explicitly as an assumption/unknown. (This is the enforceable form of "demand evidence, yours and theirs" and "don't overconfident-consult.")
- **Grade what you ground.** In research/presale, attach a source grade (Admiralty A–F / 1–6) so the reader knows how load-bearing a claim is. Two grounded-but-weak sources ≠ one strong one.
- **Record the negative space.** Note what you *couldn't* ground — the unknowns — as first-class output. Getting caught by a follow-up you can't answer is the failure this prevents.

An ungrounded confident claim is the single highest-severity defect in client-facing work, exactly as a faked test result is in code. Same gate, different substrate.
