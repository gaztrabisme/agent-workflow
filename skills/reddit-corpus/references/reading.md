# Reading — getting findings that aren't your own assumptions

Phases 3–5. The corpus is on disk; nothing here touches the network. This half of the skill exists because **the measured run's collection was fine and both of its failures were at the reading stage** — a recrawl would have fixed neither.

## 3 · The fan-out shape

Five agents, three distinct mandates:

| Stream | Count | Given | Withheld |
|---|---|---|---|
| **Discovery (unprimed)** | 2 | the corpus slice, the topic | **repo context, question list, prior deltas, hypothesis names, hardware, model names** |
| **Verification** | 2 | the corpus slice + the known open questions | — |
| **Adversarial verifier** | 1 | every load-bearing claim + the source threads | — |

> ⚠ **Scope of the evidence: the measured run achieved ONE unprimed stream, not two.** Dogfood checked the actual briefs. One was properly blindfolded and said so in its own text. The second, nominally a discovery stream, was handed the full use case — clip length, camera setup, GPU size, downstream purpose — and a named model list. It was a verification stream wearing a discovery label. So "2 unprimed" is the *recommendation*; `n=1` is the *evidence*. It is a real n=1: the genuinely unprimed stream produced exactly the items the synthesis dropped hardest, which is the thesis holding once, not twice.
>
> **Priming leaks through the brief you write, not the label you give it.** Before dispatch, read the composed discovery brief back and confirm it names no use case, no hardware, no hypothesis, no candidate models. A list of models to look for is a question list in disguise — the stream will find those and stop.

**Why two of them are blindfolded.** An agent handed your question list returns answers to your questions. That is a confirmation engine, and it will feel productive — well-sourced, well-organised, and containing nothing you didn't already suspect. The unprimed streams are the only part of the shape that can report something you weren't looking for. Withholding context from them is the point, not an oversight.

**Why the adversarial pass is not optional.** On the measured run it downgraded **ten** claims and rejected **six** — two of which were the digest agents' own fabrications rather than anything in the corpus. Three of the crawl's biggest headline numbers did not survive it.

> ⚠ **The streams are less independent than the shape implies, and you should say so.** They share a `BRIEF.md`, so anything unchecked in it propagates into every digest as if four readers had confirmed it. Caught in dogfood: all four digests stated the corpus size as 536 threads when it was 556 — the *identical* wrong number in four separately-written files, which is only possible if it was copied from the brief rather than counted. Keep the shared brief to what is genuinely shared (safety rules, output format, attribution) and put **no facts about the corpus in it** that the agents could instead derive. Then treat convergence between digests as weaker evidence than it looks.

Briefs: `templates/agent-brief.md`.

## The two failures this shape did NOT prevent

Read these before running a pass. Both are reading failures; both are cheap to avoid once named.

### Failure 1 — a verdict is not a digest

An agent was pointed at a 346-comment thread and asked a question. It answered the question, well, and reported nothing else. The thread also contained a second independent implementation of the technique, a memory-optimisation node nobody had mentioned, and two performance datapoints **on the exact GPU the project runs**. None of it surfaced, because none of it answered the question asked.

**Fix, in the brief:** for any thread above a size threshold, the agent must report what the thread *contains* — techniques, tools, numbers, disagreements, retractions — and only then how it bears on the question. Make "what else is in here?" an explicit deliverable, not a courtesy.

### Failure 2 — the synthesis re-imposes the bias

The unprimed streams did their job. Then the delta was written from the adversarial verifier's priorities — and those priorities were the lead's pre-existing question list. Every discovery-stream finding that answered *no question anyone had asked* was documented correctly in its digest and never elevated to the delta. A later audit over the same five digests recovered **22 items**, two of which outranked most of the original write-up.

**Fix, and it is one line:** the verifier must not inherit its priorities solely from the lead's question list. Give it the known questions **plus a standing mandate to elevate anything the discovery streams surfaced that answers no question anyone asked.** Then run the gap audit below regardless.

## 4 · Synthesis

Write the delta from the digests, not from memory. Every claim carries a confidence tag:

| Tag | Meaning |
|---|---|
| `[official]` | the vendor/maintainer, in an identified post or AMA. Outranks everything. |
| `[widely reported]` | three or more **separate comments**, consistent |
| `[single source]` | one comment, unconfirmed |
| `[speculation]` | reasoning, not observation |

> ⚠ **Check whether your corpus preserves authorship before you define these tags.** If your thread files strip usernames — many chunkers do — then "independent users" is **structurally unknowable**, and a legend promising independence is unfalsifiable while looking rigorous. Say *separate comments* and state the limit. Caught in dogfood: a delta defined its middle tag as "three or more independent users" and used it ~20 times on load-bearing claims, over a corpus with no usernames in it. The claims weren't wrong; the ladder just couldn't discriminate what it said it discriminated. Decide this at chunking time — keeping author hashes costs nothing and buys you the stronger tag.

Three rules that keep the delta honest:

1. **Everything is a hypothesis until your own kit confirms it.** A corpus about a newly-released tool is mostly first impressions. Where the community and your own measurement disagree, **the measurement wins**.
2. **Corpus-right is not reality-right.** A verifier can be exactly correct about what the corpus contains and still wrong about the world. Real case: a verifier rejected a licence clause as belonging to a different product — correct about the corpus, wrong about reality, because the clause did exist in the actual licence. When a claim is checkable at the source, check the source, not the corpus.
3. **Check load-bearing numbers for retractions.** A figure circulates long after its author withdraws it. Real case: a widely-repeated "VAE takes 30% of generation time" had been publicly retracted by its author; the real figure was ~20%. The retraction is usually in the same thread, below the fold.

Also flag anything that was **already known**. A "discovery" that your own decisions file recorded weeks ago is a synthesis error, not a finding, and presenting it as new corrodes trust in the rest of the document.

## 5 · The gap audit — the highest-yield step

Once the delta exists, re-read **every digest** asking one question: *what did the delta not carry over?*

- **No network cost** — no crawl, no rate-limit budget. But budget one full read of every digest plus the delta; on the measured run that was ~4,000 lines. If the digests exceed the auditor's context, split per-digest and merge, rather than skipping.
- It is the step most likely to be skipped, because the delta feels finished.
- On the measured run it recovered **22 items**, two of which outranked most of the original write-up. On the dogfood re-run against an already-audited delta it recovered 16 more. Yield falls with each pass but has not reached zero.

Brief a fresh agent for it (`templates/agent-brief.md` §D) rather than doing it yourself — the author of the delta is the worst-placed reader to notice what the delta omitted. Output shape: `templates/gap-audit.md`.

Record the recovered items in their own section of the delta. Do not silently merge them; the fact that the first pass dropped them is itself a signal about the brief.

### The audit's own output gets dropped too — close the loop

**Recovering an item does not mean it ships.** Measured in dogfood: of 22 items a gap audit recovered, the synthesis carried 19 and silently dropped three — including the one item where three independent streams had converged on the same bottleneck. The audit's output is filtered by the *same* synthesis bias the audit exists to correct, one level up.

So before the delta ships:

> Re-read the prior audit's item list against the final document and account for **every** item — carried, merged, or consciously rejected with a stated reason. An item an audit recovered and the synthesis dropped **twice** is the strongest signal in the pass.

This also applies when you are auditing a delta that already carries a recovered-items section, which — since `templates/delta.md` mandates one — is every pass after the first.

## Common reading errors

- **Dismissing a technique on a threshold without checking the threshold is tunable.** Real miss: a sparse-attention method was written off for "sequence length too short" when `min_seq_len` was a parameter — and the low-motion regime, which the project was entirely in, was the *favourable* case for it.
- **Treating an agent's confident summary as verified.** Two of the six rejected claims were invented by digest agents, not present in the corpus.
- **Letting one loud thread stand for the community.** Comment count is engagement, not consensus.
- **Reporting a technique without its licence or hardware constraint.** The constraint is usually what decides whether you can use it.
