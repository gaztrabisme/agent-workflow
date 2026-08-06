# Open questions — the UNRESOLVED register

What this skill **does not know**, kept explicit so it is never quietly filled in
with a plausible guess. Each entry names what would settle it, because several
of these **cannot be closed by research at all** — they need a support answer or
a live test, and pretending otherwise wastes rounds.

Status: `OPEN` · `CLOSED` (with date and finding) · `BLOCKED` (needs an action
outside our control).

---

## Closed — 2026-08-06

**✅ Can a Zalo Bot send proactively?** — **No cold-messaging.** The product FAQ:
*"Bạn có thể chủ động nhắn tin cho người dùng **đã từng tương tác**, nhưng cần
tuân theo chính sách nhắn tin chủ động của Zalo."* Prior interaction is required,
as on OA. Bot therefore does **not** undercut ZBS pricing — a hypothesis the
silent API docs had made tempting. `[NAV: bot.zapps.me · 2026-08-06 · FAQ accordion]`
→ folded into `bot-platform.md` §4.

**✅ The ZBS image surcharge.** It is **300đ**, printed plainly in the price table
— and it was in the 2026-07-21 archive all along. An earlier note claimed the
figure rendered as `NaN` and had to be captured live; that was wrong and it sent
a research round chasing a non-problem. Re-confirmed live 2026-08-06.
→ `messaging-and-cost.md` §5.

**✅ OA 6-month pricing and the full entitlement table.** Tăng trưởng 1.400.000đ /
Toàn diện 3.400.000đ per 6 months; Tiêu chuẩn has no 6-month option. The
comparison table has **four** tiers, and carries an **API rate limit of 100 vs
2.000 req/min** that no other surface shows.
`[NAV: zalo.solutions/oa/pricing · 2026-08-06]` → `messaging-and-cost.md` §4.

**✅ Mini App coverage gap — closed by the re-crawl.** 48 pages → **439**. ZaUI
(236), the full SDK API surface (99), openApis, checkoutSdk, eKYC, publishing and
review guidance are all now in the corpus. → `mini-app.md`.

**✅ Mini-App-interaction → OA-message-class mapping.** The dedicated page
(`quyen-loi-gui-tin-tu-oa-khi-nguoi-dung-tuong-tac-voi-mini-app`) is now in the
corpus. Search it rather than inferring. → `mini-app.md` §3.

---

## Closed — but the answer was "the ground moved"

**⚠ The developer documentation was rehosted, and the old host was hollowed out
rather than retired.** As of 2026-08-06, all **317** legacy
`stc-developers.zdn.vn/docs/v2/*` URLs still return **HTTP 200** while serving a
~450-character marketing placeholder. Content now lives at
`docs.zaloplatforms.com/docs/{MA,OA,ZBS,Social,BOT,TS}`.

Consequences absorbed into this skill:
- every legacy citation was re-pointed to the new hub, and the facts re-verified
  on the new pages (they survived verbatim);
- the legacy host is still crawled **as a tripwire**;
- `staleness_check.py` compares text, never status codes — a status check would
  have called this run a clean success.

**Newly opened by the move:** the legacy host carried **SDK** (37 pages) and a
standalone **ZNS** section (32 pages). The new hub has `Social/sdk` (19) and folds
ZNS into `ZBS` (34) — so some legacy SDK/ZNS material may have been **dropped, not
migrated**. The 2026-07-21 text is preserved under `archive-developers`; if a
client build needs a platform SDK, check whether its documentation still exists
anywhere current.

---

## Open — closable by research

**🔴 What flips `can_join_groups` to `true`, and does it cover *existing* groups?**
*The highest-value question in this skill.* If an official Bot can be added to a
group the client already has, the entire ToS/ban exposure of the unofficial leg
becomes droppable — decisive for listed or compliance-sensitive clients. Docs are
silent; the field's existence proves *some* state changes it.
**Settled by:** Zalo support (`support@zalo.solutions`), or a live test once Pro
exists. **Not** by more reading. → `bot-platform.md` §2.

**🔴 Zalo Bot Pro limits and availability.** 129.000đ/month, *"sắp ra mắt"*, caps
undisclosed. Basic (50 users/bot) is a prototype tier; Enterprise redirects to OA.
Until Pro's numbers exist, Bot cannot be scoped into a client deliverable.
**Settled by:** the pricing page publishing them, or support.

**🟡 Zalo's "chính sách nhắn tin chủ động" for Bot.** Named in the FAQ, linked
nowhere, and **not found in the 2026-08-06 corpus** despite the new hub's
`docs/BOT` section (19 pages) now being crawled. It is the *only* stated
constraint on Bot's proactive sending, so it is load-bearing. **Settled by:**
support, or the Bot terms page read live — not by another crawl of the same
sitemap.

**🟡 Did SDK / ZNS documentation survive the rehost?** The legacy host carried 37
SDK and 32 ZNS pages; the new hub has `Social/sdk` (19) and folds ZNS into `ZBS`
(34). Some material may be gone rather than moved. **Settled by:** comparing the
`archive-developers` snapshot against the new hub page by page.

**🟡 Does replying to / tapping a ZBS Template Message count as an "interaction"
that opens the 48h free window?** The ten-action list does not name it. This one
fact decides whether the cheap **"knock once via ZBS, then converse free"**
pattern works — and the whole per-month cost estimate for any conversational
product hinges on it. **Settled by:** the ZBS docs on the new hub, or a live test
on a dev OA. → `messaging-and-cost.md` §2.

**🟡 The OTP / new-account send exemption.** The claim that authentication codes
may reach a brand-new user outside the normal window is **not confirmed by any
page in this corpus**, yet it is the foundation of the recommended auth pattern.
**Settled by:** the ZBS template-policy pages. → `identity-and-auth.md` §4.

**🟡 OA verification review SLA.** The widely-repeated "2–3 business days, free"
is not in the corpus. The 14-day submission deadline and the legal-representative
approval step *are* [→ `official-account.md` §2]. **Settled by:** the verification
policy pages, or oa@zalo.me.

**🟡 `request_user_info` — the OA route to a consented phone.** Exact flow and
webhook return shape unverified. Would give a phone number without a Mini App.
**Settled by:** the OA docs on the new hub, then a dev-OA test.

**🟢 Two primary pages disagree on the interaction list** (10 actions vs 6). We
prefer `tin-nhan/tong-quan` with a stated reason; upstream has not reconciled
them. **Settled by:** a Zalo clarification. Low stakes unless a client decision
turns on one of the four disputed actions. → `messaging-and-cost.md` §2.

**🟢 Bot free-tier quota: 3.000 messages per month or per day?** The pricing card
and the FAQ disagree on the same page — a 30× spread. **Settled by:** support, or
measuring it. → `bot-platform.md` §3.

---

## Blocked — need a live test or a real account

These cannot be researched. Listing them as "open research" wastes rounds.

- **Stand up a dev OA end-to-end** — register OA + app, wire the inbound webhook,
  send a list/CTA template, run a `request_user_info` capture, fire one ZBS OTP to
  a test phone. This single exercise closes several 🟡 items above at once and is
  the highest-leverage unblocking action available.
- **OTP round-trip auth POC** — phone → OTP → verify → session bound to an
  employee record. Measure delivery latency and failure modes (non-Zalo phone,
  template rejection).
- **`getGroupMembersInfo` at realistic scale** — verified on 5 members; real
  groups are 50–200. Pagination, rate limits, missing profiles, `memVerList` edge
  cases all unknown at that size.
- **Passive uid attribution in a busy group** — is `uidFrom` reliably present on
  *every* message type, not just text? The attribution layer's trustworthiness
  depends on it.
- **Ban-risk / session-durability probe** — run the unofficial bot under realistic
  monitoring load over time; characterise session death rate, challenge triggers,
  and whether harvest/mention patterns raise flags. **This quantifies a governance
  risk we currently carry unmeasured.**
- **DM-gate mitigation for the nudge path** — does friend-request-then-accept at
  onboarding reliably open the 1:1 channel?

---

## How to use this file

- **Before answering**, check whether the question is listed here. If it is,
  say so and give the status — do not synthesise an answer around a known gap.
- **After any research round**, move what closed into the Closed section **with
  the finding and its citation**, and add anything newly discovered to be unknown.
- **A question that keeps reappearing as "open research" but is actually in the
  Blocked list** is a process bug: it will never close by reading. Escalate it to
  a test or a support ticket instead of re-researching it.
