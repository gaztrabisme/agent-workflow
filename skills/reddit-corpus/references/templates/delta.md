# `NN-<window>-delta.md` — the output shape

One file per pass, numbered so the series reads in order. The reader is someone who has to *decide* something, not someone catching up on Reddit.

```markdown
# <Topic> — delta, <date-from> → <date-to>

> What changed since <prior pass>. Claims carry confidence tags; nothing here is
> a finding until our own kit confirms it. Coverage and blind spots in §0.

## 0 · Corpus and method
  queries      <n> (<list the angles, including the /new sweep>)
  indexed      <n> threads
  mined        <n> threads / <n> comments  (<pct>% of indexed)
  cut          <n> threads — rule: <the cut rule, stated>
  blind spot   <what could not be reached, and the date window>

Fan-out: <n> unprimed discovery · <n> verification · 1 adversarial verifier ·
1 gap audit. Verifier downgraded <n>, rejected <n>.

## 1 · Headline
<Three to six lines. What a decision-maker does differently because of this pass.>

## 2 · <Theme>            ← one section per theme, most consequential first
### <Finding>  `[widely reported]`
<What it is. What it would change. The constraint that decides whether we can
use it — licence, hardware, version.>
Source: <url> · <url>

## N · Corrections to prior passes
<Anything an earlier delta got wrong, stated plainly. This section is why the
series is trustworthy; a delta that never corrects itself is not being checked.>

## N+1 · Closed risks
<Measured negatives: things we were worried about that the corpus or our own kit
cleared. A risk that turns out not to exist is a result. Without a section for
it, it evaporates — the synthesis has nowhere to file "we checked, it's fine",
and the next pass re-opens it from scratch.>

## N+2 · About this pass, not the topic
<Findings about the METHOD. The corpus could not establish X. The digests shared
a wrong figure, so they were not independent readers. A region was cited but
never verified. The ledger did not reconcile.

This section exists because these findings fit nowhere else and are therefore
dropped — and they are the ones the NEXT crawl inherits. A pass that never
reports anything unflattering about itself was not audited.>

## N+3 · Recovered by gap audit
<Items the synthesis dropped and the audit put back. Kept separate on purpose —
that they were dropped says something about the brief, and the next pass should
see it.

If a PRIOR audit's items were dropped again here, say so explicitly — an item
recovered once and dropped twice is the strongest signal in the pass.>

## N+4 · Test queue
| # | Hypothesis | How we'd settle it | Cost |
|---|---|---|---|
| 1 | <claim> | <the measurement that discriminates> | <time/compute> |

<Everything above leaves this document as a hypothesis. This table is where it
becomes work. A "measurement" that cannot distinguish the two outcomes is not
one — see core gate 2.>
```

## Rules

- **Confidence tag on every claim.** Untagged reads as fact.
- **Constraint travels with the technique.** A method you cannot license, or cannot run on your hardware, is not a finding — it's trivia. Say which it is.
- **Corrections are not optional.** If the pass overturned nothing, say so; that is itself information about whether the last pass was any good.
- **The test queue is the point.** A delta with no queue is reading material.
- **Coverage first, not buried.** §0 is what lets a later reader calibrate every "not found in the corpus" in the document.
