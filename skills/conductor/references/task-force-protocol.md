# Task-Force Protocol

Fan out research over a question that a decision rests on, verify it adversarially, converge it into one artifact that says **what moved**.

Codified from two runs that worked — an 8-agent market validation and a 10-agent cost validation (6 research streams + 4 adversarial verifiers, 228 tool calls, bilingual sources) that line-audited a budget inside a live funding document and moved it under 2% with **every line sourced**. Both were invented in the moment. This is the shape, so the third one isn't.

## When it fires

A **load-bearing** claim is unverified: a cost, a quota, a regulation, a price, a competitor's behaviour, a market size — something a decision or a client-facing number rests on. Not for curiosity. The test: *if this is wrong, what breaks?* No answer → don't run a task force.

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

Each stream agent gets: its question, the current assumption it is testing against, the output path, and this contract.

```
Research: <the specific question — not "everything about X">

Do NOT write implementation code. Do NOT revise the assumption yourself —
report the delta and let the synthesis propose the change.

Write to <path>/<Letter>-<slug>.md with exactly these sections:

## Summary
  The headline in prose: what you found, and what it means for the assumption.

## Findings
  A table, one row per item:
  | Item | Value found (native units + converted) | Confidence | Current assumption | Verdict vs assumption |
  - Confidence is HIGH / MED / LOW and must name WHY:
      HIGH = official/primary source, read live, date it.
      MED  = secondary corroboration, or a model built on HIGH inputs.
      LOW  = single uncorroborated source, or inference.
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
Search in every language the answer might live in.
```

## Verifier brief

The verifier's independence is the whole mechanism. Give it the stream file and this instruction — **not** the stream agent's reasoning.

```
You are checking a finding written by someone else. Your job is to REFUTE it.

1. Read the stream file's claim on <the load-bearing item>.
2. Independently search for sources it did NOT cite. Citing the same source
   back is not verification — it is an echo.
3. Return a verdict:
     CONFIRMED — survives attack; list the independent sources that back it.
     ADJUSTED  — partly wrong; give the corrected value and the source.
     REFUTED   — the claim does not hold; show what does.
   State explicitly whether an adjustment is against the ORIGINAL ASSUMPTION
   or against the STREAM's finding — they are different failures.
4. Name any trap a reader could fall into: a price quoted for a different
   deal shape, a rule that changed, a benchmark that doesn't apply.

Default to REFUTED if you cannot independently source it. Do not rubber-stamp.
```

Verdicts land in one `VERIFY.md` with the verdict counts up top.

## Engine

| Streams + verifiers | Engine |
|---|---|
| ≤ 8 total | Agent fan-out, single message, parallel calls. Visible and interruptible. |
| > 8, or you want verify-as-each-stream-lands | Workflow `pipeline()` — each stream flows into its own verifier without a barrier. Resumable; a stream that dies drops to `null` instead of killing the run. |

Barrier only where synthesis genuinely needs every stream at once — which it does, so the *synthesis* is the barrier and nothing before it needs to be.

## Synthesis

One file — `README.md` beside the streams. Contract:

1. **Inventory table** — file, what it covers, verifier verdict.
2. **Headlines: what moved**, grouped by direction — *cheaper than assumed / more expensive than assumed / green lights / newly discovered lines*. This is the section the human actually reads; it is not a summary of the streams, it is a diff against the assumption.
3. **Contradictions, surfaced.** Where two streams disagree, say so and say which is better sourced. Never silently pick one.
4. **Open quote-required questions**, consolidated — who to call, what to ask.
5. **Proposed revision — NOT applied.**

That last rule is load-bearing. When the task force feeds a document that is client-, investor-, or contract-facing, the synthesis **proposes** the revised numbers in a was → proposed → why table and stops. A human applies them. The cost-validation run did exactly this and it is why the resulting numbers were defensible: someone chose each one.

For internal, reversible artifacts, apply and say you applied.

## Cost discipline

Roughly 20–25k output tokens per stream agent, more for a bilingual sweep. A 10-agent run is a real spend — declare the agent count in the Plan Block. **Never silently cap coverage:** if you drop a stream, drop a verifier, or sample instead of sweeping, say so in the synthesis. Silent truncation reads as "we covered everything."
