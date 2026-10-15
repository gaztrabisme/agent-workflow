# Task-Force Protocol

Fan out research over a question that a decision rests on, verify it adversarially, converge it into one artifact that says **what moved**.

Codified from two runs that worked — an 8-agent market validation and a 10-agent cost validation (6 research streams + 4 adversarial verifiers, 228 tool calls, bilingual sources) that line-audited a budget inside a live funding document and moved it under 2% with **every line sourced**. Both were invented in the moment. This is the shape, so the third one isn't.

## When it fires

A **load-bearing** claim is unverified: a cost, a quota, a regulation, a price, a competitor's behaviour, a market size — something a decision or a client-facing number rests on. Not for curiosity. The test: *if this is wrong, what breaks?* No answer → don't run a task force.

> **If you cannot name the claim, this is the wrong protocol.** Every stream here is briefed with its question *and the assumption it tests against*, which is what makes it accurate and also what makes it blind: it can only return answers to questions you already had. When the ask is "what's the latest on X" or "what are we missing", use `../../../reddit-corpus/SKILL.md` — same adversarial verifier, plus unprimed streams that are denied the question list and a gap audit over the synthesis.

## Shape

```
      ┌── Stream A ──┐
      ├── Stream B ──┤                ┌── Verifier 1 ──┐
ask ──┼── Stream C ──┼── stream files ┼── Verifier 2 ──┼── VERIFY.md ──┐
      ├── Stream D ──┤                └── Verifier N ──┘               ├── synthesis ── wiki
      └── Stream N ──┘                                                 │
                                                     contradictions ───┘
```

**Streams are cut by domain, not by source type.** "Entity & legals", "payments", "hardware & colo" — each one a coherent question a single agent can own end to end. Cutting by source ("one agent does web, one does the KB") produces overlap and gaps.

**Verifiers are fewer than streams, and aimed at the load-bearing numbers only.** Four verifiers over six streams is the right ratio — you verify what the decision rests on, not everything found.

## Stream brief

Each stream agent gets its specific question, the current assumption it tests, the output path, and this contract. [book:research-methods-psychology], How Scientists Work.

```
Research: <the specific question — not "everything about X">

Do NOT write implementation code. Do NOT revise the assumption yourself —
report the delta and let the synthesis propose the change. [book:research-methods-psychology], Research Transparency and Credibility.

Write to <path>/<Letter>-<slug>.md with exactly these sections:

## Summary
  The headline in prose: what you found, and what it means for the assumption.

## Findings
  A table, one row per item:
  | Item | Value found (native units + converted) | Evidence and uncertainty | Current assumption | Verdict vs assumption |
  - In the Evidence and uncertainty cell, grade the evidence basis: HIGH only for a dated live primary source; MED for secondary corroboration or a model based on HIGH inputs; LOW for a single uncorroborated source or an inference. State why. Do not compress the finding's uncertainty into a tier: state what remains uncertain, why, and how it will be monitored or resolved. [book:learning-systems-thinking], Be Honest About Potential Pitfalls.
  - Verdict is against the ASSUMPTION, not in the abstract:
      Confirms / Cheaper than assumed / Higher than assumed / Assumption is stale / No evidence either way.
    A finding with no verdict column is trivia.

## Details & citations
  Full URLs with the date you fetched them. Verbatim quotes for anything
  load-bearing — in the original language, translated beside it.
  Flag traps with ⚠: stale third-party tables, a price that is a different
  deal shape, a rule that changed on a date.

## Quote-required
  What research CANNOT settle — the questions only a named firm, official,
  or counterparty can answer. Name who to ask and write the question script.
  An empty section is a claim that everything is knowable from sources; be sure.

Prefer PRIMARY sources read live over aggregators. Third-party summaries go
stale silently and are the single largest error source in this protocol.
Search in every language the answer might live in. Prefer primary sources read live. [book:research-methods-psychology], How Scientists Work. Make source URLs explicit and link them. [book:facilitating-software-architecture], Step 3: Make Options and Gather Their Consequences. Record each retrieval date, and quote load-bearing material verbatim in its original language with a translation beside it.
```

## Empirical findings

For load-bearing empirical findings, look for independent replications; a single result or a repeated summary does not establish that a finding has been reproduced. If no independent replication is available, state that uncertainty. [book:research-methods-psychology], How Scientists Work.

## Verifier brief

The verifier must be independent of the stream producer. Give it the stream file, its brief, and enough relevant context to test the claim. Independence comes from assigning a separate reviewer, not from withholding useful reasoning. [book:swebok], Chapter 4: Software Testing.

```
You are checking a finding written by someone else. Your job is to REFUTE it.

1. Read the stream file's claim on <the load-bearing item>.
2. Independently search for sources it did NOT cite. Citing the same source
   back is not verification — it is an echo. Check critical data with an
   out-of-band source where one exists. [book:site-reliability-engineering], Trust but Verify.
3. Return a verdict:
     CONFIRMED — survives attack; list the independent sources that back it.
     ADJUSTED  — partly wrong; give the corrected value and the source.
     REFUTED   — the claim does not hold; show what does.
   State explicitly whether an adjustment is against the ORIGINAL ASSUMPTION
   or against the STREAM's finding — they are different failures.
4. Name any trap a reader could fall into: a price quoted for a different
   deal shape, a rule that changed, a benchmark that doesn't apply.

Default to REFUTED if you cannot independently source it. Do not rubber-stamp. [book:critical-thinking-about-research], 1 Seeking Trustworthy Knowledge.
```

Verdicts land in one `VERIFY.md` with the verdict counts up top. [book:pmbok-guide-7e], 2.7.3. Presenting Information.

## Engine

| Streams + verifiers | Engine |
|---|---|
Use ordinary parallel fan-out for at most eight total streams and verifiers. Above eight, or when verifying each stream as it arrives matters, use a documented dynamic-workflow capability or coordinator-pipelined stages from `workflow-patterns.md`. Respect the current harness cap and scale the fan-out to the value and risk of the work.

Run independent streams to completion in parallel and gather their results for the combined outcome. Keep synthesis as the barrier; stages that can stream do not wait for unrelated work. [book:agentic-mesh], Parallelization.

## Synthesis

One file — `README.md` beside the streams. Contract:

1. **Inventory table** — file, what it covers, verifier verdict.
2. **Headlines: what moved**, grouped by direction — *cheaper than assumed / more expensive than assumed / green lights / newly discovered lines*. This is the section the human actually reads; it is not a summary of the streams, it is a diff against the assumption.
3. **Contradictions, surfaced.** Where two streams disagree, say so and say which is better sourced. Name the accountable decision owner; record advice without iterating toward broad consensus. Never silently pick one. [book:facilitating-software-architecture], Make Who Is Accountable for Each Decision Explicit.
4. **Open quote-required questions**, consolidated — who to call, what to ask.
5. **Proposed revision — NOT applied.**

That last rule is load-bearing. When the task force feeds a document that is client-, investor-, or contract-facing, the synthesis proposes revised values in a was → proposed → why table and routes the proposal to the accountable change authority or project change control board for approval, delay, or rejection. The cost-validation run did this; each value had a named decision owner. [book:pmbok-guide-7e], 4.4.3. Meetings and Events; [book:flawless-consulting], Roles Consultants Choose.

For internal, reversible artifacts, apply and say you applied.

## Cost discipline

Roughly 20–25k output tokens per stream agent, more for a bilingual sweep. A 10-agent run is a real spend — declare the agent count in the Plan Block. [book:research-methods-psychology], Presenting Results: APA-Style Reports and Conference Posters. **Never silently cap coverage:** if you drop a stream, drop a verifier, or sample instead of sweeping, say so in the synthesis. Silent truncation reads as "we covered everything."
