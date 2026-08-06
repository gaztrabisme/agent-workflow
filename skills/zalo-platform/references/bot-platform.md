# Zalo Bot Platform (`bot.zapps.me`)

An **official, ToS-clean bot account** with a Telegram-Bot-API-shaped surface.
Operated by Công Ty TNHH Zalo Platforms [S1]. It matters far out of proportion to
its size because it is the **only official surface that names group chat as a
first-class concept outside GMF** — which makes it the only credible challenger to
the unofficial-library leg (`unofficial-zca-js.md`).

Claims are keyed `[S#]` to the **Sources** table at the bottom.

---

## 1. Why this product deserves a second look

An internal assessment in **2026-07-02** rejected Zalo Bot because it was 1:1 only
and groups were "coming soon". **That rejection is stale.** The webhook now types
`chat_type` as `PRIVATE | GROUP (Beta)`, and the Basic tier advertises "Tương tác
với 3 nhóm Chat (Beta)" [S1][S2].

For a listed or compliance-sensitive client, an official bot that can sit in a
group would remove the entire ToS/ban risk we otherwise carry. That is a large
enough prize to justify re-testing rather than inheriting the old verdict.

---

## 2. The blocking unknown: `can_join_groups`

`getMe` on a Basic account returns [S3]:

```json
{"ok": true,
 "result": {"id": "1459232241454765289",
            "account_name": "bot.VDKyGxQvc",
            "account_type": "BASIC",
            "can_join_groups": false}}
```

**The field exists and is `false`.** Its existence implies some tier or state
flips it to `true` — but **nothing in the documentation says what.** Two distinct
questions remain open, and they have different answers:

1. What flips `can_join_groups` to `true`? (Tier? A setting? A review?)
2. Even when true, can the bot be added to an **existing** group, or only to one
   it creates? *Only the first would replace the unofficial leg* — every real
   use case involves groups the client already has.

Both are in `open-questions.md`. **Neither can be closed from documentation** —
they need a support answer or a live test.

---

## 3. Tiers

| | **Basic** | **Pro** | **Enterprise** |
|---|---|---|---|
| Price | Free | 129.000đ/month, *sắp ra mắt* | — |
| Bots | 3 | undisclosed | — |
| Users per bot | **50** | undisclosed | — |
| Messages/month | **3.000** | undisclosed | — |
| Group chats | 3 (Beta) | undisclosed | — |

All from the landing page [S1]. **Enterprise is not a tier** — the page redirects
enterprise enquiries to Zalo Official Account [S1].

⚠ **The page contradicts itself on the free quota.** The pricing card says
"3.000 tin nhắn mỗi **tháng**"; the FAQ says the free tier limits messages "mỗi
**ngày**" [S1][N1]. Do not plan against either number until it is confirmed —
the two readings differ by 30×.

⚠ **A Bot is created from a *personal* Zalo account** — "Bạn cần có **tài khoản
Zalo cá nhân đã được xác thực**, sau đó tạo Bot" [N1]. This is a governance
problem for corporate work that the API surface does not reveal: the bot is tied
to an individual's personal identity, not to a company entity, so it leaves with
that person. Raise it explicitly before proposing Bot to a business client.

> **Sizing reality:** at 50 users per bot and 3,000 messages/month, Basic is a
> prototype tier. Any workforce- or customer-scale deployment depends entirely on
> undisclosed Pro limits, or is not viable on this product. **Do not scope a
> client deliverable on Zalo Bot until Pro's caps are published or confirmed.**

---

## 4. API surface

Host: `https://bot-api.zaloplatforms.com/bot<BOT_TOKEN>/<method>`, `POST`,
JSON — token in the path, exactly like Telegram [S3].

| Method | Notes |
|---|---|
| `getMe` | token check; returns `account_type`, `can_join_groups` |
| `getUpdates` | long-polling — no public URL needed |
| `setWebhook` / `deleteWebhook` / `getWebhookInfo` | push delivery |
| `sendMessage` | rich text; markdown/HTML |
| `sendPhoto`, `sendSticker`, `sendVoice` | media |
| `sendChatAction` | typing indicator |

Inventory from [S4]. The Telegram-shaped surface means Telegram bot patterns
(and much of their client-code structure) port over with little friction.

**Footguns:**
- **`sendVoice` does not support groups and returns success while silently not
  delivering.** A silent-failure path in a send API is the worst kind — never
  trust its `ok: true` in a group context.
- **Proactive send is gated on prior interaction — RESOLVED 2026-08-06** [N1].
  The API reference documents no send window, which had left open the tempting
  reading that Bot can cold-message and thereby undercut ZBS pricing. The product
  FAQ answers it directly, verbatim:
  > *"Bạn có thể chủ động nhắn tin cho người dùng **đã từng tương tác**, nhưng cần
  > tuân theo **chính sách nhắn tin chủ động của Zalo**."*

  So: **a Bot cannot cold-message.** Prior interaction is required, exactly as on
  OA, and a separate "proactive messaging policy" governs the rest — a policy the
  bot documentation never links to and which is **not in this corpus**. Undocumented
  was never unlimited. Treat Bot's reach as *no better than OA's* until that policy
  is found and read.

---

## 5. Where it sits against the alternatives

| Need | OA | **Bot** | zca-js (unofficial) |
|---|---|---|---|
| Officially sanctioned | ✅ | ✅ | ❌ ToS violation |
| Sit in the client's **existing** group | ❌ ever | **❓ unresolved** | ✅ only option |
| Cold-message a user | ✅ via ZBS template | **❌ prior interaction required** [N1] | ✅ (at ban risk) |
| Scale to 1,000+ users | ✅ | ❌ at Basic; ❓ at Pro | ✅ (at ban risk) |
| Business verification required | ✅ | ❌ — but ties to a **personal** account [N1] | ❌ |
| Documented send-window rules | ✅ precise | ⚠ policy referenced, not published | n/a |

**Reading:** the 2026-08-06 findings **narrowed** Bot's appeal. It cannot
cold-message, so it does not undercut ZBS; and it hangs off an individual's
personal account, which is awkward to propose to a company. It remains the
*preferred* answer if — and only if — question 2 in §2 resolves yes and Pro's caps
are adequate. Until then: a good fit for **internal tooling, alerts and
prototypes**, not for a client-scale deployment.

---

## Sources

| Key | Corpus file · URL · fetched |
|---|---|
| S1 | `text/bot/bot.zapps.me.txt` · https://bot.zapps.me/ · 2026-07-21 |
| S2 | `text/bot/bot.zapps.me__docs__webhook.txt` · https://bot.zapps.me/docs/webhook/ · 2026-07-21 |
| S3 | `text/bot/bot.zapps.me__docs__apis__getMe.txt` · https://bot.zapps.me/docs/apis/getMe/ · 2026-07-21 |
| S4 | `references/knowledge-base/manifest.json`, source `bot` (18 pages) · 2026-07-21 |
| N1 | **[NAV]** https://bot.zapps.me/ · read **2026-08-06** · expanded all five "Các câu hỏi thường gặp" accordion items and read their bodies from the rendered DOM |
