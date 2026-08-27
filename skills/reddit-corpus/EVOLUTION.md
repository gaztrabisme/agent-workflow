# Evolution Log — reddit-corpus

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: real crawl passes and their delta documents — the coverage ledger, the verifier's downgrade/reject counts, and what each pass's gap audit recovered are the skill's own telemetry.

---

## Evolution 1 — 2026-08-27 — birth, distilled from three measured crawl passes

### Harvest scope

Three passes over r/StableDiffusion + r/comfyui for a video-generation model (2026-08-08, 08-11, 08-22), and the method notes in that project's `docs/h3-research/README.md`. Representative because the three passes differ on exactly the axes the skill claims matter: pass 1 and 2 used a single-keyword query set and pass 3 widened it; pass 3 added the unprimed streams and the adversarial verifier; only pass 3 ran a gap audit. The failures are documented with counts rather than recalled.

Classify: **authored** — this is the practitioner's own fire-tested practice with measured numbers, not a distillation of someone else's writeup. It still ships `PENDING` per core gate 8, because one project is not two independent uses and every measured number comes from a single topic domain.

### Patterns found

Ranked (Impact ÷ Effort), with the proof each bit:

1. **Single-keyword query sets are structurally blind** — Impact: H, Effort: L. Passes 1–2 searched one keyword and could not return threads that displace the topic, because such threads never carry its name. Adding a raw `/new` sweep in pass 3 contributed **833 threads keyword search never returned**, including the release changelog and a licence PSA — two of the pass's highest-value items.
2. **The synthesis re-imposes the bias the fan-out removed** — Impact: H, Effort: L. Pass 3's delta was written from the verifier's priorities, which were the lead's existing question list. A gap audit over the same five digests recovered **22 items**, two outranking most of the original write-up. Collection was fine; a recrawl would have fixed nothing.
3. **A verdict is not a digest** — Impact: H, Effort: L. A 346-comment thread was reduced to an answer to the question asked; a second implementation, a memory-optimisation node, and two datapoints on the project's own GPU went unreported.
4. **Blind rate-limit spacing is worse than reading the headers** — Impact: M, Effort: L. `~1.2 s between requests` folklore both wasted the window and still collected 429s, losing **38 threads** before it was caught. The real contract is in `x-ratelimit-*`.
5. **Coverage claims are meaningless without a published number** — Impact: M, Effort: L. "No signal found" meant *not in the top 60 threads* at 57% coverage and *not in either corpus* at 98%. Same phrase, different strength, and nothing in the document distinguished them.
6. **The adversarial pass catches fabrication, not just weakness** — Impact: M, Effort: M. It downgraded ten claims and rejected six; two of the six were invented by digest agents rather than present in the corpus.
7. **Corpus-right is not reality-right** — Impact: M, Effort: L. A verifier correctly reported that the corpus attributed a licence clause elsewhere, and was wrong about the world — the clause did exist. Checkable-at-source claims must be checked at the source.

### Hypotheses applied

1. **`references/collection.md` §2 — query-set table with the `/new` sweep as a mandatory row, plus the 833-thread measurement** — closes pattern 1.
2. **`references/reading.md` §"The two failures this shape did NOT prevent" + `templates/agent-brief.md` §C standing mandate + §D gap-audit brief** — closes patterns 2 and 3. The standing mandate is the one-line fix; the gap audit is the backstop.
3. **`references/collection.md` §"The rate-limit contract" — read-the-headers protocol, with the folklore named as wrong** — closes pattern 4.
4. **`references/collection.md` §"Coverage ledger" + `templates/delta.md` §0** — closes pattern 5. Coverage is the first section of the output, not an appendix.
5. **SKILL.md anti-patterns — "skipping the adversarial verifier" and "reporting a community claim as a finding"** — closes patterns 6 and 7.
6. **SKILL.md principle 1 + `collection.md` §1 — the lead crawls, agents digest** — records the access asymmetry that shapes the whole design, so nobody rediscovers it by building a subagent crawler that fails quietly.

Not modified (validated as already-sound): the confidence-tag ladder (`[official]` → `[speculation]`) carried across all three passes without friction and is reproduced as-is.

### Validation results (settled by a later run's step 0)

- [ ] The widened query set + `/new` sweep is run on a **different subreddit and topic**, and the sweep again returns material keyword search did not.
- [ ] The gap audit runs on a pass whose delta was written *with* the standing mandate already in the verifier brief — does it still recover material, or did the mandate absorb its job? (If the audit comes back empty, the mandate works and the audit can be downgraded to optional.)
- [ ] The rate-limit protocol is exercised against Reddit's current headers — the contract may have changed since 2026-08.
- [ ] Every measured number in the references comes from one topic domain. Confirm or correct against a second.
- **Verdict: PENDING** — one project, one topic domain, one practitioner. Numbers are real but not yet shown to generalise, which is precisely what this skill claims to do.

### Dogfood — 2026-08-27

Fresh-context agent, briefed per `../skill-builder/references/templates/dogfood-brief.md`. Task: run phase 5 (gap audit) using `templates/agent-brief.md` §D as its operating instructions, cold, against five real digests and the 53 KB delta of the H3 week-3 pass — then compare its output against `digest_G_gapaudit.md`, a hand-run of the same audit it was forbidden to open first.

**Pass condition** (stated before the run): fires on the right task without sibling collision · every gate actionable as written · all cross-refs resolve · no `high`-severity finding survives.

**Result: passed after fixes.** It produced a 343-line audit with 16 ranked items against a document that had *already* been gap-audited once, so the yield was residue — and the residue landed almost entirely on classes the skill's brief could not see. Six defects found, all fixed:

| # | Defect | Fix |
|---|---|---|
| 1 | Confidence ladder promised "independent users" over a corpus with **no usernames** — unfalsifiable while looking rigorous; used ~20× on load-bearing claims | `reading.md` — tag is now *separate comments*; added the check-authorship-at-chunking-time warning |
| 2 | Coverage ledger never reconciled: `1,670 − 556 − 401 = 713` threads with no stated rule; 78% of *comments* silently read as 78% of *threads* (really 33%) | `collection.md` — reconcile-by-subtraction rule, both denominators quoted, absence claims scoped to mined |
| 3 | The verifier's three most consequential findings sat in its **preamble**; synthesis mined the verdict lists and skipped the framing | `agent-brief.md` §C — corpus-level findings must be numbered verdict items at the top of the list |
| 4 | Gap audit asks only "what was dropped?" and is structurally blind to contradictions **created by** a recovery pass | `agent-brief.md` §D — added the consistency second pass |
| 5 | Measured negatives that *close* a risk had nowhere to go and evaporated | `delta.md` — added "Closed risks" section |
| 6 | Findings about the method itself fit no section, so the pass could not report anything unflattering about itself | `delta.md` — added "About this pass, not the topic" |

Finding 1 also revealed a claim the skill was making that its own evidence did not support: the streams share a `BRIEF.md`, and all four digests carried an **identical wrong corpus size (536 vs 556)** — the same error in four separately-written files means it was copied from the brief, not counted. So the fan-out is less independent than the shape implies. Recorded as a caveat in `reading.md` rather than quietly dropped.

No sibling collision reported. Cross-refs resolved. Separately, the authoring-time collision check surfaced `conductor/references/task-force-protocol.md` as a near-neighbour; boundary drawn in both files and a **Mine** row added to conductor's routing table.
