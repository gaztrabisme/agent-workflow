# Deep Research Patterns

Reference guide for conducting deep research with iterative refinement.

---

## Core Loop: Plan-Act-Observe-Reflect

```
PLAN → what needs to be done
  ↓
ACT → invoke tool (search, read, query)
  ↓
OBSERVE → examine result
  ↓
REFLECT → identify gaps, decide next action
  ↓
REPEAT until sufficient knowledge (max 5 iterations)
```

---

## Query Decomposition Strategies

| Strategy | When | Example |
|----------|------|---------|
| **Parallel** | Independent sub-topics | "Research strategy, technology, and executives simultaneously" |
| **Sequential** | Each step informs next | "First understand their pain points, then research how competitors address them" |
| **Tree** | Branching exploration | "If they use Azure, research Azure-specific integrations; if AWS, research AWS patterns" |

---

## Gap Analysis Pattern

After each research iteration:

```
Review findings so far:
[SUMMARY OF CURRENT KNOWLEDGE]

Identify gaps:
1. What questions remain unanswered?
2. What contradictions need resolution?
3. What assumptions need validation?
4. What depth is missing?

Generate follow-up queries targeting each gap.
```

### Gap Categories

| Gap Type | Example | Resolution |
|----------|---------|------------|
| **Missing** | No info on their AI initiatives | Targeted search on "[Company] AI strategy" |
| **Stale** | Last update was 2 years ago | Search for recent news, earnings calls |
| **Conflicting** | Two sources disagree on investment amount | Find primary source (investor relations) |
| **Shallow** | Know they have initiative, not details | Deep dive on specific program |
| **Unverified** | Single source claim | Triangulate with additional sources |

---

## Search Strategy: Broad to Narrow

1. **Broad sweep**: Short, general queries to map the landscape
2. **Evaluate**: What's available? What approaches exist?
3. **Narrow focus**: Specific queries targeting identified areas
4. **Deep dive**: Detailed queries on chosen aspects

### Query Formulation Tips

| Goal | Query Pattern |
|------|---------------|
| Current strategy | "[Company] strategy [year]" |
| Pain points | "[Company] challenges" OR "[Company] CEO concerns" |
| Technology | "[Company] technology stack" OR "[Company] digital transformation" |
| Investments | "[Company] investment" OR "[Company] budget" |
| Initiatives | "[Company] [domain] initiative" |
| Executive views | "[Executive name] speech" OR "[Executive name] interview" |

### Anchoring Queries with Named Frameworks

When a research track stalls (pain-point research returns platitudes, competitive research returns marketing copy, executive research returns LinkedIn blurbs), anchor the query to a named framework. The framework gives you vocabulary the source material was likely written in.

| When stuck on... | Try anchoring to... |
|------------------|---------------------|
| Pain points returning "wants to be more efficient" | **Sandler pain funnel** — layered questioning: surface problem → business impact → personal impact. Search for language at each layer. |
| Decision-making process unclear | **MEDDIC** — Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion. Each is a separate query. |
| Competitive position vague | **Forrester Wave / Gartner Magic Quadrant** for the relevant category. Analyst language is explicit about strengths and weaknesses. |
| Market dynamics generic | **Porter 5 forces** — rivalry, new entrants, substitutes, supplier power, buyer power. Gives you five distinct query angles. |
| Sales objection patterns | **Challenger Sale** — Commercial Teaching, Tailoring, Taking Control. Useful for understanding how the client's own sales org frames value. |

See `references/frameworks_vocabulary.md` for 1-line descriptions of each. Purpose is vocabulary, not education — these are named anchors to get you unstuck, not methodologies to adopt wholesale.

For enterprise AI engagements specifically, the **BXT framework** (Business viability / Experience desirability / Technology feasibility) is the scoring lens. See the `ms-ai-discovery` skill for the full framework and its Five Golden Questions.

---

## Source Prioritization

| Source Type | Reliability | Use For |
|-------------|-------------|---------|
| **Investor Relations** | Highest | Strategy, financials, targets |
| **Earnings Calls** | High | Pain points, priorities, CEO messaging |
| **Press Releases** | High | Announcements, partnerships, initiatives |
| **Annual Reports** | High | Comprehensive strategy, metrics |
| **Analyst Reports** | Medium-High | Market position, forecasts |
| **Industry Publications** | Medium | Context, competitive analysis |
| **News Articles** | Medium | Recent events, quotes |
| **Job Postings** | Medium | Technology stack, hiring priorities |
| **LinkedIn** | Medium | Executive backgrounds, recent activity |
| **Conference Talks** | Medium | Technical details, executive views |
| **Forums/Social** | Low | Sentiment, unverified claims |

### Date Sensitivity

| Information Type | Freshness Requirement |
|------------------|----------------------|
| Executive roles | Verify current (check LinkedIn) |
| Strategy | < 12 months |
| Technology stack | < 18 months |
| Financial metrics | Latest reported |
| Pain points | < 6 months preferred |
| Competitive position | < 12 months |

---

## Context Compression

Before returning findings to coordinator:

1. **Extract key facts** — Remove narrative fluff
2. **Cite sources** — Note which source said what
3. **Flag conflicts** — Note when sources disagree
4. **Prioritize** — Most relevant first

### Compression Format

```markdown
## Key Findings
- [Finding 1] (source: [X], date: [Y])
- [Finding 2] (source: [X], date: [Y])

## Conflicts
- Source X says A, but Source Y says B

## Gaps
- Still unknown: [topic]

## Confidence Assessment
- High confidence: [topics with multiple sources]
- Low confidence: [topics with limited/old sources]
```

---

## Iteration Limits

| Research Depth | Max Iterations | When |
|---------------|----------------|------|
| Quick scan | 1-2 | Simple factoid lookup |
| Standard | 3 | Most research tasks |
| Deep dive | 5 | Complex, high-stakes decisions |

**Hard stop at 5 iterations** — if not resolved, escalate to user with what was found, what remains unknown, and recommended next steps.

---

## Error Recovery

```
On search failure:
  → Try alternate query formulation
  → Try different source types
  → Try broader/narrower scope
  → After 3 failures: note gap, move on

On conflicting information:
  → Note both perspectives with sources
  → Identify which is more recent/authoritative
  → Flag for user decision if critical

On stale information:
  → Note the date clearly
  → Search for updates
  → Flag uncertainty in synthesis
```
