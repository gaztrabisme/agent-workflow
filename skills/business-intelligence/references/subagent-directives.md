# Subagent Directives

Imperative instructions for spawning research subagents. Each section tells you WHEN to spawn, WHAT to provide, and HOW to use the result.

---

## Company Strategy Researcher

**When**: Starting research on any enterprise client.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Research current strategy for [COMPANY].
  Cover: strategic priorities, investment focus, CEO messaging, public commitments,
  recent shifts. Check annual reports, earnings calls, investor presentations.
  Output: compressed findings with priorities, investments, commitments, leadership
  messaging, gaps. Cite sources with dates. Flag anything > 12 months old.
  Distinguish facts from analyst speculation.
```

**After completion**: If strategy doesn't align with user's offering, loop back to user before continuing.

---

## Pain Points Researcher

**When**: Understanding challenges the user's offering might address.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Research pain points and challenges for [COMPANY] relevant to [OFFERING].
  Cover: leadership-stated challenges, analyst concerns, industry pressures,
  capability gaps, underperformance areas.
  Check earnings call Q&A, CEO interviews, analyst reports.
  Output: explicit pain points (they said it) vs implied (analysts say it),
  prioritized by relevance to [OFFERING], with evidence and sources.
  Don't invent pain points — evidence required.
```

**After completion**: If pain points don't align with offering, surface to user immediately.

---

## Technology Landscape Researcher

**When**: Understanding their current stack and technical context.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Map technology landscape for [COMPANY].
  Cover: major platforms, recent implementations, digital transformation initiatives,
  technology partnerships, hiring signals.
  Check press releases, job postings, conference talks, vendor case studies.
  Output: core platforms, recent changes, active initiatives, partnerships,
  hiring signals (what skills suggest about priorities), gaps.
  Note: job postings = medium reliability (may be aspirational).
  Flag anything > 18 months old.
```

**After completion**: Use findings to inform positioning of user's offering against existing stack.

---

## Competitive Position Researcher

**When**: Understanding market context and competitive pressures.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Research competitive position for [COMPANY].
  Cover: direct competitors, claimed advantages, competitive weaknesses,
  recent competitive moves, market share data.
  Check analyst reports, investor presentations, earnings call competitor mentions.
  Output: main competitors, positioning, advantages, weaknesses, recent moves,
  relevance to our engagement. Distinguish their claims from analyst observations.
```

**After completion**: If competitor just won relevant deal, flag for defensive positioning.

---

## Executive Profile Researcher

**When**: Building profiles of specific meeting attendees.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Build actionable profile of [NAME], [TITLE] at [COMPANY].
  Cover: current role and authority, career history, education, public statements,
  LinkedIn activity, conference appearances, cultural background.
  Check LinkedIn, company website, press releases, conference archives, interviews.
  Output: role and tenure, background, public positions, likely questions based
  on role and expertise, attack vectors, risk level (High/Medium/Low with rationale),
  cultural notes, engagement strategy.
  Flag if NEW to role (< 1 year) or external hire. Only public information.
```

**After completion**: If executive is NEW or external hire, flag to user — existing relationship may not carry weight.

---

## Partnership History Researcher

**When**: Existing relationship context is important.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Research partnership history between [COMPANY] and [USER'S COMPANY].
  Cover: past engagements, key contacts, joint announcements, relationship tenure.
  Check joint press releases, news archives, LinkedIn connections.
  Output: relationship overview, engagement history, key contacts (both sides),
  relationship health assessment, opportunities, risks.
  Separate public information from internal knowledge.
  Flag if key contacts have changed roles.
```

**After completion**: If relationship is at-risk or key contacts changed, surface to user.

---

## Claims Verification Researcher

**When**: You have materials (proposals, slides, feature lists) that will be presented. Run BEFORE synthesis — this prevents overclaiming.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Cross-reference claims in [MATERIALS] against product reality.
  For each claim: classify as Verified (evidence exists), Overclaim (exaggerated
  or unsupported), or Unknown (can't determine from available info).
  Check: proposals, feature documentation, demo capabilities, case studies,
  technical specs. Look for contradictions between materials.
  Output: claim-by-claim table with status and evidence.
  Flag: claims that contradict each other across documents,
  capabilities mentioned in marketing but absent from technical docs,
  metrics without methodology, integration claims without evidence.
  Be adversarial — assume a technical expert will probe every claim.
```

**After completion**: Any claim marked Overclaim or Unknown must be resolved before presenting. Options: verify with dev team, soften the language, or remove.

---

## Product-Environment Fit Researcher

**When**: You know the client's technology stack and need to understand how your offering fits (or doesn't).

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Analyze how [OFFERING] fits into [COMPANY]'s technology environment.
  Their stack includes: [KEY PLATFORMS/TOOLS].
  For each capability in [OFFERING]:
  1. Does their stack already cover this? (overlap = don't present)
  2. Does it fill a gap their stack can't? (gap = lead with this)
  3. Does it compete with something they've invested in? (competition = danger)
  4. Is it complementary? (complement = position as accelerator)
  Output: capability map with Overlap/Gap/Competition/Complement classification.
  Also identify: partner ecosystem threats (who else fills these gaps on their platform),
  integration requirements (what would connecting actually require),
  and positioning recommendation (accelerator vs platform vs point solution).
  Check their platform's partner directory, marketplace, and recent announcements.
```

**After completion**: Capabilities classified as Overlap or Competition go into the Negative Space (what NOT to present). Capabilities classified as Gap are the core pitch. Complement capabilities are supporting evidence.

---

## Research Synthesis

**When**: Multiple researchers have completed. Findings need integration.

**Spawn**:
```
Use the Task tool with subagent_type="general-purpose":
- Prompt: Synthesize research findings for [COMPANY] engagement.
  Input: [LIST RESEARCH OUTPUTS].
  Tasks: identify themes across research, resolve contradictions,
  prioritize pain points by relevance to [OFFERING], surface non-obvious insights,
  flag decisions needing user input.
  Output: executive summary, key themes, prioritized pain points, technology context,
  competitive context, executive dynamics, conflicts identified, gaps, recommendations.
  Do NOT hide contradictions. Compress to essentials. Cite sources.
```

**After completion**: Present synthesis to user. Do NOT proceed if loop-back alerts are triggered.

---

## Coordination Rules

1. **YOU are the coordinator** — spawn subagents, don't do research yourself
2. **Parallel when independent** — launch Company, Technology, Competitive simultaneously
3. **Sequential when dependent** — pain points may redirect competitive research
4. **Loop back on pivots** — any finding that changes direction goes to user first
5. **Compress before integrating** — subagent output should be key facts, not narratives
6. **3-attempt rule** — if a subagent fails, retry once with adjusted prompt, then escalate
