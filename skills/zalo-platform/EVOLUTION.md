# Evolution Log — zalo-platform

The ledger. Every re-research round and every refinement lands here, with the
verdict kept honest. Shape defined in `../evolution/references/loop.md`.

**Classification: distilled + authored.** Distilled from Zalo's own documentation
(borrowed confidence — the digests are only as good as the corpus and the reading),
authored from empirical tests recorded during a real client build. Both halves
ship `PENDING` until ≥2 independent real uses.

**Verdict: `PENDING`.** Fire-tested once, on itself (see Round 1). Needs two
independent real consultations before it can reach `KEEP`.

---

## Birth — 2026-08-06

**Why it exists.** Zalo knowledge was scattered across two client projects and
drifting apart. A concrete, live example of the cost: one project's channel layer
hard-codes `_MAX_SENDS = 8` per 48 hours and documents it as *"real Zalo OA
policy"* — a rule Zalo **abolished on 01/01/2026**. Another project's wiki had the
correct rule but three wrong ZBS prices. Same platform, two codebases, three
different versions of the truth, and no mechanism to converge them.

**Seeded from** a 689-URL / 592-page documentation crawl dated 2026-07-21, plus
empirical group/DM reach tests from 2026-07-07 and 2026-07-15, plus desk research.

**Built:** 8 reference digests · 3 scripts (`kb_search`, `crawl_zalo`,
`staleness_check`) · the corpus.

**Grounded:** read `core` + `skill-builder` (SKILL.md, authoring-checklist,
SKILL.md.skeleton) → reused the canonical section headers, referenced
`../core/references/*` rather than copying, adopted the gate-declaration pattern
and the PENDING-until-fire-tested discipline.

---

## Round 1 — first re-research, 2026-08-06 (same day as birth)

Run as the skill's own dogfood: build against the archive, then immediately
execute the protocol the skill prescribes. It found more than expected.

### What the round did
Sitemap-driven re-crawl of all sources (**1,396 pages**, up from 592) + a
`chrome-devtools` navigation session over four browser-computed targets.

### Corrections to this skill's own prior beliefs — the valuable output

| Prior belief (from the inherited notes) | Reality | Where it would have hurt |
|---|---|---|
| ZBS OTP/xác thực = **300đ** | **400đ** — the top tier, tied with voucher | A client quote, understated |
| ZBS "các loại còn lại" = **200đ** | **300đ** | Every non-OTP template, understated by 50% |
| Image surcharge un-crawlable (`NaN`), must be read live | **300đ, printed in the table** — and present in the 2026-07-21 archive all along | Sent a whole research round chasing a non-problem |
| "Delete 55đ from any cost model" | 55đ/tin is **live** for outside-48h sends beyond allowance; only the *"8 free then 55đ"* framing died | Would have removed a real cost line |
| OA comparison table has **3** tiers | **4** — "Cơ bản" exists | Mis-stated entry-level entitlements |
| Bot's silent docs might mean unrestricted proactive send | **Prior interaction required** — Bot cannot cold-message | Would have promised reach Bot does not have, and mis-priced against ZBS |

### The structural finding
**Zalo rehosted its developer documentation and hollowed out the old host rather
than retiring it.** All 317 legacy `stc-developers.zdn.vn/docs/v2/*` URLs return
**HTTP 200** while serving a ~450-character placeholder; content moved to
`docs.zaloplatforms.com/docs/{MA,OA,ZBS,Social,BOT,TS}`.

This is the failure mode a status-code check cannot see. Absorbed by: re-pointing
every citation to the new hub (facts re-verified there, surviving verbatim),
keeping the dead host in the crawl as a **tripwire**, and confirming
`staleness_check.py` compares text rather than status.

### New facts the browser found that no crawl could
- OA **6-month pricing**: Tăng trưởng 1.400.000đ, Toàn diện 3.400.000đ; Tiêu
  chuẩn has no 6-month option. Annual is ~11–12% cheaper per month.
- **API rate limit 100 vs 2.000 req/min** across the two paid tiers — a 20× cliff,
  absent from the pricing cards, and often the real reason to buy Toàn diện.
- Bot creation requires a **verified personal Zalo account** — a governance
  problem for corporate clients that the API surface never reveals.
- The Bot landing page **contradicts itself** on the free quota: 3.000 messages
  per *month* (card) vs per *day* (FAQ).
- The ZBS estimator's headline figures are **UID prices**; the tables are **phone
  prices**. Exactly 0.70× — quoting both as alternatives double-counts.

### Bugs this round found in the skill's own tooling
1. **Link-following crawler reached 12 developer pages and reported success.**
   Docusaurus renders its sidebar client-side. Fixed: sitemap-driven frontier
   (12 → 318). *A crawler that silently under-collects is worse than one that
   errors — it produces a confident, incomplete corpus.*
2. **Diff was ~90% extractor noise** (blank lines, inline joins), which would have
   made the staleness report unreadable and therefore unused. Fixed: normalise,
   then diff at word level.
3. **Archived snapshots surfaced in search as if current.** Fixed: `archive-*`
   sources excluded by default, opt-in via `-s`.

### Open items carried forward
`references/open-questions.md`. The two 🔴 items (`can_join_groups`, Bot Pro
limits) are **not closable by research** — they need Zalo support or a live test.
Newly opened: whether legacy SDK/ZNS documentation survived the rehost or was
dropped.

**Verdict: `PENDING`.** The tooling is fire-tested (it found real bugs in itself
and real errors in its inherited beliefs). The *digests* are not yet validated by
independent use.

---

## Evolution 2 — 2026-08-12 — the corpus was right and the way in was broken

First harvest by the `evolution` loop. Window: since Round 1 (2026-08-06).

### Harvest scope

Every trace of this skill in existence: `grep -rl '"skill":"zalo-platform"'` across
`~/.claude/projects` returns exactly two transcripts, and they are **one consultation** —
a parent in massrec `1b6125a6` at `08:09:36Z` and its own workflow child at `08:16:34Z`.
Plus the downstream artifacts that consultation produced (`massrec/docs/market-research/
cost-validation-2026-08/{D-zalo-cogs.md, VERIFY.md}`, `docs/investment-proposal.md`,
`wiki/log.md`), the read-once log, the prompt history, and ten live `kb_search.py` runs
reproducing the queries the consultation actually ran.

**Correction to the triage table that commissioned this harvest:** there is no 2026-08-12
invocation and there are not two consultations. Both artefacts were `triage.py` bugs
(mtime dating, subagent counting), fixed in `evolution@7feda94` and `evolution@9f918f9`.

### Patterns found

1. **`kb_search.py` matched a literal phrase on a single line, and its no-hit message
   converted that into a statement of fact** — Impact: H, Effort: L. 4 of 5 content queries
   in the real consultation returned nothing. One of them became
   *"Template approval fees — None found"* at MED confidence in `D-zalo-cogs.md:36`, a
   document that fed an investor cost model. The page was in the corpus. Reproduced
   2026-08-12: `kb_search.py "phí duyệt"` → NO HITS; `-e "duyệt template"` → the ZBS
   billing page.
2. **Anchoring rules 3 and 4 pulled opposite ways and the cheaper one won** — Impact: H,
   Effort: L. Both agents ran `--stale`, saw `0 days old`, read rule 3 as permission to
   skip, never navigated. Round 1's `[NAV · 2026-08-06]` readings were then restated as
   *"official price page, read live 2026-08-06"* — verification that never happened.
3. **The corpus had three sizes on screen at once** — Impact: L, Effort: L. `SKILL.md`
   1,300 / `EVOLUTION.md` 1,396 / `--stale` 1,968 / manifest 2,091.
4. **317 hollowed-out placeholder pages sit in the default search set** — Impact: M,
   Effort: L. `developers-legacy` is not prefixed `archive-`, so the tripwire Round 1
   deliberately kept is indistinguishable from real content in a citation line.
5. **Digests carry our fetch date, not the platform's effective date** — Impact: M,
   Effort: L. The adversarial verifier had to supply *"ZBS prices effective 16/03/2026"*.
   For a price that changed twice in 2026, the client-facing question is when Zalo's number
   took effect, which a fetch date cannot answer.
6. **The skill is shaped as a whole-platform reference and 100% of its use is pricing** —
   Impact: M, Effort: M. Both query strings are cost lookups; one of eight digests read.

### Hypotheses applied

- **H2** — the `NO HITS` text now requires a second query form before absence may be
  reported, and requires the queries run to be named beside the claim (`scripts/kb_search.py`).
  Closes 1.
- **H3** — plain queries AND their whitespace-separated terms instead of matching the phrase
  literally; regex mode and single-term behaviour unchanged. `--stale` now reports searchable
  vs archived, and `SKILL.md` says the same number (`scripts/kb_search.py`, `SKILL.md`).
  Closes 1's mechanism and 3.
- **H9** — rule 4 is stated as overriding rule 3; rule 3 is marked as able only to add a
  reason to check, never to supply one to skip; and the inverse of the existing
  `[NAV]`-as-corpus anti-pattern is added — corpus-as-live, which is worse because it
  manufactures verification invisibly (`SKILL.md`). Closes 2.

**Not applied:** patterns 4, 5 and 6. Named here so they are not lost. 4 and 5 are cheap and
real but nothing has yet been *wrong* because of them; 6 is a shape question that one
consultation cannot settle — a skill used once for pricing is not evidence that pricing is
all it is for.

### Validation results (settling Round 1's list)

- **Two independent real consultations** → **PENDING** (1 of 2, and the apparent second was
  a child of the first — same session, same task, same day). What the one achieved is real:
  its output was cross-checked by a separate adversarial verifier and marked CONFIRMED.
- **Validate the distilled claims against real use** → **REVISED**. True for exactly one
  file: `messaging-and-cost.md` is the only digest ever consulted, and its figures held
  against independent verification. The other seven inherit `PENDING`. "The digests are
  unvalidated" was too broad — it is false for one and untested for seven.
- **A fresh-context dogfood** → **PENDING** (none run; the 2026-08-09 critic that mentions
  this skill 33 times was auditing `evolution`, never asked a Zalo question).
- **A re-research round by someone other than the author** → **PENDING** (never attempted;
  `crawl_zalo.py` and `staleness_check.py` have never been executed in any session).
- **Confirm 55đ and the 500/2.000 allowances against an invoice or sales quote** →
  **PENDING**, and now blocked on a phone call rather than on research: the three exact
  Vietnamese questions are drafted in `D-zalo-cogs.md:71–73` and the item is on massrec's
  call list. No call made.

New, for a later run:

- [ ] Count NO HITS in the next consultation — the 4-of-5 rate should not recur.
- [ ] Any absence claim names the queries that produced it.
- [ ] A client-facing Zalo number is accompanied by a `[NAV]` performed *in that run*.

**Verdict: PENDING.** Still one real consultation. Two script changes and one rule change,
all measured against a reproduction of the original failure, none validated by later use.

## Validation list (what must happen before `KEEP`)

- [ ] **Two independent real consultations** where the skill answers a live Zalo
      question and the answer survives contact with reality (a client meeting, a
      build decision, a vendor conversation).
- [ ] **Validate the distilled claims against real use** — mandatory for a
      distilled skill; internal consistency is not evidence
      (`skill-builder/references/authoring-checklist.md` step 1).
- [ ] **A fresh-context dogfood** by an agent that has not seen this build, using
      the skill on a real task, briefed with
      `skill-builder/references/templates/dogfood-brief.md`.
- [ ] **One re-research round run by someone other than the author**, to prove the
      protocol is followable from the documentation alone.
- [ ] Confirm the 55đ outside-48h price and the 500/2.000 allowances against a
      real invoice or a Zalo sales quote — the highest-consequence numbers here
      are still only page-deep.

## Harvest sources
- Consultations where the answer was wrong, incomplete, or not in the corpus.
- Each re-research round's correction table — the single best signal.
- Downstream: any Zalo fact that reached a client document and had to be retracted.
