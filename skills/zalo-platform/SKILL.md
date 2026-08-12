---
name: zalo-platform
description: "Answer Zalo OA / Mini App / Bot / ZBS questions from an archived, citation-carrying documentation corpus — and re-research them by crawl + browser navigation when the answer must be current. USE WHEN designing, scoping, costing or debugging anything on Zalo: messaging windows and quotas, OA packages and ZBS/ZNS per-message pricing, OA verification, Mini App getPhoneNumber and publishing, Zalo Bot, GMF groups, group-chat reach, uid-vs-phone identity, or auth via OTP; also when a Zalo fact must be verified before it enters a quote, proposal or contract. Not `dev`, which builds the software — this supplies and grounds the platform facts it is built on. Keywords: Zalo, Zalo OA, Official Account, Mini App, zmp-sdk, getPhoneNumber, ZNS, ZBS Template Message, Zalo Bot, bot.zapps.me, GMF, Tin Tư vấn, 48h window, 7-day window, quota, uid, findUser, zca-js, Zalo Login, OA verification, xác thực OA, Zalo pricing, ZaUI, zalo.solutions."
license: MIT
---

# Zalo Platform

The in-house specialist on Vietnam's Zalo platform. It answers questions about
**Official Account, Mini App, Bot Platform, ZBS Template Message, GMF groups and
the unofficial group-chat leg** from a **1,376-page searchable documentation
corpus** (1,968 including superseded snapshots; `kb_search.py --stale` is the
live count),
with a citation on every claim — and it **re-researches itself** by crawl and
browser navigation when the answer has to be current.

It exists because Zalo's rules move fast (the messaging model changed 01/01/2026,
packages were discontinued 01/06/2026, and between 2026-07-21 and 2026-08-06 the
developer docs were **rehosted onto a new domain and the old one hollowed out —
every legacy URL still returns HTTP 200 while serving a placeholder**), the primary sources are Vietnamese, and most
third-party writing about Zalo — including our own older notes — is confidently
out of date. Getting this wrong puts a wrong number in a client contract.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity
> Constraints; declare its gates; reference its files, don't copy them.

## When it fires — and when a sibling owns it

- **This skill:** any question about how Zalo *works*, what it *costs*, what is
  *permitted*, or whether a Zalo fact is *still true*.
- **`dev` instead:** building the software. This skill supplies the platform
  facts and constraints; `dev` designs, writes and tests the code that uses them.
- **`solution-architect` instead:** the shape of a client solution and its
  commercial framing. This skill feeds it the channel constraints and unit costs.
- **`business-intelligence` instead:** research about a *company*. This is
  research about a *platform*.

> **Disambiguation:** artifact + audience. This produces **grounded platform
> facts with citations**; `dev` produces **working code**; `solution-architect`
> produces **a solution and a price** the client reads.

## Anchoring rules

1. **Cite or don't claim.** Every factual statement resolves to a corpus file
   with a URL and a fetch date, a dated live test, or a dated browser reading.
   *"Not in the corpus"* is a real, useful answer — and the honest one. Never
   patch a gap from memory: model recall of Zalo specifics is systematically
   stale, and Zalo is exactly the domain where stale reads as authoritative.
2. **Distinguish the evidence classes.** Documentation `[S#]` ≠ live test `[T#]`
   ≠ browser reading `[NAV]` ≠ a BSP's blog post (not a primary source, however
   confident). Undocumented never means unlimited — a lesson this skill learned
   the day it was built.
3. **Age is part of the answer.** State the fetch date on anything commercial or
   policy-bound. Run `kb_search.py --stale` first; >30 days plus a pricing
   question means verify live before quoting. **This rule can only add a reason
   to check — it never supplies a reason to skip.** A fresh corpus is not a
   substitute for rule 4; freshness says the page has not moved *since we
   fetched it*, which is not the same as knowing what it says today.
4. **Never let an unverified number reach a client.** Quote, proposal, contract →
   re-read the live page, whatever the corpus says. Non-negotiable, and it
   **overrides rule 3** — a corpus 0 days old still does not clear a number for
   a client document.

   This has already failed once, in the only real consultation the skill has
   had. Both agents ran `--stale`, saw `0 days old`, read rule 3 as permission
   to skip, and never navigated. Round 1's `[NAV · 2026-08-06]` readings were
   then restated in `D-zalo-cogs.md` as *"official price page, read live
   2026-08-06"* — a first-hand reading nobody performed, in a document that
   fed an investor proposal.
5. **Two gates, not one.** The single most-confused thing on the platform:
   **7 days = permission, 48 hours = free.** Anyone stating one number is telling
   you half the rule.
6. **Only an unofficial personal account can join a group the client already
   has** — and it violates Zalo's ToS. State that plainly every time it is
   proposed; it is the client's risk to accept, never ours to carry silently.
7. **Surface the corrections.** When this skill's own prior belief was wrong,
   say so in the answer. The corrections are the most valuable thing it holds —
   they are what stops a bad number appearing in a second proposal.

## The flow (at a glance)

| Mode | Trigger | What you do | Artifact |
|---|---|---|---|
| **Consult** | A Zalo question | `kb_search.py` → read the digest → answer **with citations + dates** | A cited answer |
| **Verify** | A number is heading for a client | Navigate the live page, compare to the corpus, report drift | A dated `[NAV]` finding |
| **Re-research** | Corpus stale / gap / Zalo changed something | Crawl → diff → read → update digests → promote → record | Updated digests + EVOLUTION entry |
| **Advise** | "Which surface should we use?" | Apply the decision table below; name the constraint that decides it | A recommendation with its binding constraint |

**Always start Consult with `scripts/kb_search.py`** — not with recall. It returns
the citation with the hit, so grounding is automatic; and it exits 1 when the
corpus genuinely lacks the page, which is information you need.

```bash
S=~/.claude/skills/zalo-platform
python3 $S/scripts/kb_search.py --stale                 # how old is what I know?
python3 $S/scripts/kb_search.py "han muc" -C 2          # diacritic-insensitive
python3 $S/scripts/kb_search.py "getPhoneNumber" -s platform-docs -l
```

## Choosing a surface (the question most often asked)

| Requirement | Answer | The constraint that decides it |
|---|---|---|
| Message customers who contacted us | **OA**, `Tin Tư vấn` | Free ≤48h, paid to 7 days, template beyond |
| Message someone cold | **ZBS Template Message** | The only route past 7 days; priced per template |
| Get the user's phone number | **Mini App** `getPhoneNumber` | Web Zalo Login **cannot** return a phone — ever |
| Sit in the client's **existing** group | **Unofficial leg only** | OA and Mini App structurally cannot; Bot unresolved |
| Run a group we own | **OA GMF group** | Followers-only; monthly maintenance fee |
| Internal alerts / prototype bot | **Zalo Bot** | Free, minutes to set up; 50 users/bot; no cold-messaging |
| Authenticate staff | **Roster phone → ZBS OTP → session** | Needs no phone *from* Zalo at all |
| Chatbot or any OpenAPI integration | **Verified OA, Tăng trưởng tier** | A hard feature gate: 2.5M đ/yr floor |

**Verification is the on-switch.** An unverified OA cannot send at all, and
verification requires the client's legal representative to tap approve in their
own Zalo app within 14 days of OA creation. Treat it as a scheduled client action
with a named owner — never as "submit some documents".

## Gates (declared, inherited from core)

- **Grounding gate** — substrate is `references/knowledge-base/` via
  `scripts/kb_search.py`, plus the live sites when currency matters. Record
  `Grounded: kb_search "<query>" → <file · date>` or `→ not in corpus`. A Zalo
  claim with no citation is a violation, not a shortcut. See
  `../core/references/grounding-gate.md`.
- **Output Contract** — a Consult is done when the answer carries citations *and*
  dates. A Re-research is done when the digests are updated, the corpus promoted,
  and `EVOLUTION.md` records what moved and **which prior belief was wrong**. See
  `../core/references/wiki-protocol.md`.
- **Pushback & teach** — when someone asks for a cost model on stale numbers, or
  proposes the unofficial leg to a compliance-sensitive client, say so before
  executing. See `../core/references/pushback-and-teach.md`.
- **Approach declaration** — state whether you are answering from the corpus,
  verifying live, or re-researching, and why. The three have very different
  confidence and cost. (core SKILL.md §7.)

## Anti-patterns (hard no-list)

- Answering a Zalo question from model memory. The corpus exists precisely
  because recall here is unreliable and sounds authoritative anyway.
- Quoting a price without its fetch date, or mixing VAT bases — **OA packages
  include VAT, ZBS excludes it**.
- Repeating the dead *"8 free messages per 48h"* rule, or branching code on
  `cs_reply.remain` (a constant, removed after 01/03/2026).
- Treating an undocumented limit as no limit.
- Proposing the unofficial leg without stating the ToS violation and ban risk.
- Promoting a fresh crawl before updating the digests it invalidated — that
  destroys the evidence for the edits still owed.
- Presenting a `[NAV]` reading as a corpus citation. The next crawl won't
  reproduce it and the mismatch will read as corruption.
- **The reverse, which is worse: presenting a corpus citation as a live
  reading.** *"Read live on <date>"* means someone opened the page that day.
  Inheriting a `[NAV]` from an earlier round, or restating a fetch date as a
  reading date, manufactures verification that never happened — and it is
  invisible downstream, because the sentence says exactly what a real check
  would have said.
- Letting `open-questions.md` rot: a closed question left open causes repeat
  work; an open one quietly answered is a fabrication.

## Composition

- **Inherits:** `core`.
- **Feeds:** `dev` (platform constraints for the build), `solution-architect`
  (channel options, unit costs, phasing risks), `delivery` (verification and
  client-action prerequisites that gate a schedule).
- **Consumes:** its own corpus, and the live Zalo sites via crawl + navigation.

## References

- `references/messaging-and-cost.md` — **start here for anything commercial**: the
  two gates, interaction classes, OA packages, full entitlement table, ZBS pricing,
  the quota API, and a costing checklist.
- `references/official-account.md` — tiers, verification and its client-action
  gate, GMF groups, API surface, terminology.
- `references/mini-app.md` — `getPhoneNumber`, lifecycle, payment. **Carries a
  coverage warning** — the archive is thin here.
- `references/bot-platform.md` — the Telegram-shaped official bot, its tiers, and
  the unresolved `can_join_groups` question.
- `references/unofficial-zca-js.md` — the group-chat leg: what was empirically
  verified, and every liability that comes with it.
- `references/identity-and-auth.md` — three id namespaces, phone as the only
  bridge, and the auth pattern that needs nothing from Zalo's identity stack.
- `references/re-research-protocol.md` — crawl + navigate loop, the two crawl
  traps, and citation discipline.
- `references/open-questions.md` — the UNRESOLVED register. **Check it before
  answering**; several entries can never close by reading.
- `scripts/kb_search.py` — cited search over the corpus (diacritic-insensitive).
- `scripts/crawl_zalo.py` — sitemap-driven re-crawl of all four sources.
- `scripts/staleness_check.py` — diff a fresh crawl and name the digests to fix.
- `references/knowledge-base/` — the corpus itself: `text/` + `manifest.json`.
