# Harvest Brief — one skill, bounded evidence

Use one evidence-gathering worker per selected skill when parallel work is appropriate. The workers examine independent skill scopes concurrently; the accountable lead merges their findings once into a single synthesis. If multiple workers inspect the same traces, compare their extraction and resolve disagreements before using the evidence. [R022] [R129] [evolution-C29] [book:agentic-design-patterns], Create the ParallelAgent (Runs researchers concurrently); [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis

---

**You are examining real-use evidence for one selected skill. Do not edit files.**

## Read first

- The selected skill’s `SKILL.md`, linked references and `EVOLUTION.md`.
- The source records named by the triage decision.
- The loop’s verdict and non-adoption guidance in `../loop.md`.

## Settle open items

For each unchecked item and `PENDING` verdict in the last unresolved entry, state whether post-entry traces exercised it. Name the evidence, or state that no qualifying trace exists. Recommend `KEEP`, `REVISED`, `REVERT`, or reasoned `PENDING` using the non-adoption sequence. [R131]

## Harvest

Bound the evidence window by the last entry’s date. Record what sources and periods were actually read. Stream large records and filter to the question; do not load an entire large transcript when a bounded excerpt answers it. [R035] [book:python-for-devops], Dealing with Large Files

For each source, record its origin, observed date, task identity, directness, completeness and any known instrumentation limits. A source-quality judgment must be available before its contents support a strong pattern. [evolution-C25]

Work through the fixed pattern questions in [`../triage.md`](../triage.md) to identify recurring causes and relationships. Report patterns with their evidence and uncertainty; do not require each finding to fit a fixed taxonomy of categories. [R134]

Report findings as advice a separate decision taker may act on; the decision taker retains the choice, and the finding does not itself authorize implementation. [R137] [book:facilitating-software-architecture], Direct Versus Representative Democracy

## Pattern questions

Use the seven questions in `../triage.md` to find repeated causes and relationships. Mark patterns first noticed after examining evidence as exploratory and state what further evidence would strengthen or overturn them. [evolution-C27] [book:critical-thinking-about-research], 9 Inferences, Conclusions, and the Research Report

## Output

```markdown
## <skill>
### Settled verdicts
- <item> → KEEP | REVISED | REVERT | PENDING(<reason>) — evidence: <trace>

### Patterns found
1. <pattern> — Impact: H/M/L, Effort: H/M/L — proof: <trace>

### Traces examined
<source, period, task identities, quality and limits>

### Nothing-found
<what was checked and not found>
```

Each test states its expected result. Document the work clearly enough that another owner can repeat the evidence check. [R127] [book:swebok], Test Activities
