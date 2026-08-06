# EVOLUTION — zalo-platform

The ledger. Every re-research round and every refinement lands here, with the
verdict kept honest. Shape defined in `../core/references/evolution-loop.md`.

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
