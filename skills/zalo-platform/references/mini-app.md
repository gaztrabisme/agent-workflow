# Zalo Mini App

A web app that runs **inside the Zalo client**, with access to Zalo identity,
native device capabilities, payment, and a consented phone number that no web
page can obtain. It is the right shell whenever the user must be identified as a
Zalo user, or the flow needs the phone number without asking the user to type it.

Claims are keyed `[S#]` to the **Sources** table at the bottom.

> **Coverage: good, as of 2026-08-06.** 439 pages from the unified hub
> `docs.zaloplatforms.com/docs/MA/*`. `miniapp.zaloplatforms.com/documents/*`
> now 302s there, and the old 48-page snapshot it replaced is retained under
> `archive-miniapp`.
>
> | Section | Pages | |
> |---|---|---|
> | `zaui` | 236 | the component library (versioned, e.g. `zaui/1.7.0/...`) |
> | `api` | 99 | SDK surface — user, routing, storage, media, UI, location |
> | `openApis` | 36 | server-side APIs |
> | `checkoutSdk` | 24 | payment |
> | `eKYC` | 18 | identity verification |
> | `intro` | 16 | lifecycle, publishing, permissions, guidelines |
> | `devtools` | 10 | |
>
> ZaUI is versioned in-path, so **`kb_search` will return several versions of the
> same component** — check which version a hit belongs to before quoting a prop.

---

## 1. What it is, and when to choose it

A Mini App lives inside a **Zalo App** (the developer-console application); one
Zalo App can contain several Mini Apps [S1]. Creating one yields a **Mini App ID**.

**Choose a Mini App over a plain web app when you need any of:**
- the user's **phone number**, consented, without typing (§2) — *the usual reason*
- Zalo user identity without building a login
- OA follow/interaction from inside the app
- Zalo-native payment
- distribution through Zalo's own entry points

**A Mini App does not solve group chat.** It cannot join a user's existing group
conversation any more than an OA can — see `unofficial-zca-js.md`. Choosing a
Mini App shell changes the *front end* of one leg; it never replaces the group leg.

**Setup path** [S1]: register a Zalo App at Zalo for Developers → *Kích hoạt ứng
dụng* so external users can use it → create the Mini App in the management page →
receive the Mini App ID. ⚠ **Information entered at creation is not freely
editable**: changing it later requires a support ticket and a review-team
confirmation [S1]. Get the name and details right the first time.

---

## 2. `getPhoneNumber` — the capability that justifies the shell

The one Zalo capability with no web equivalent. **Social API `/me` returns only
id, name and picture — never a phone number.** Phone comes only from the Mini App
SDK.

**Flow** [S2]:

1. Client (SDK **≥ 2.13.0**): `const { token } = await getPhoneNumber();`
   → consent popup → a **token**.
2. Send that token to *your* server. (Doing the exchange from the Mini App fails —
   the docs explicitly warn server-to-server APIs error if called client-side [S2].)
3. Server exchanges it:

```http
GET https://graph.zalo.me/v2.0/me/info
  access_token: <user_access_token>   # from sdk.getAccessToken({...})
  code:         <token from step 1>
  secret_key:   <your Zalo App secret key>
```

Returns the number as `{"data": {"number": "84…"}}`.

**Token properties that bite** [S2]: *"Mỗi token được cung cấp chỉ có thể truy
xuất thông tin được 1 lần với thời gian hết hạn sau 2 phút."* — **single use,
2-minute expiry.** Never cache the token; cache the resolved phone against your
own user record. Never retry the exchange with the same token.

**Gates:** per-user consent at the popup, plus **Mini App review of the permission
flow**. Zalo rejects permission requests that do not state a clear purpose. App
admins can test the flow **without** review [S2] — so "it works for me" during
development says nothing about whether it will pass review.

Not metered — no per-call cost.

---

## 3. Related user/OA APIs in the corpus

| API | Purpose |
|---|---|
| `getUserID`, `getUserInfo` | Zalo identity inside the Mini App |
| `getAccessToken` | the `access_token` used in the phone exchange |
| `authorize`, `getSetting` | request and inspect granted permissions |
| `followOA`, `unfollowOA`, `interactOA`, `showOAWidget`, `openChat` | drive the OA relationship from inside the app |
| `requestSendNotification` | ask permission to send notifications |
| `events` | app lifecycle events |

**`followOA` / `interactOA` are the interesting pair**: a Mini App interaction is
one of the actions that can open an OA messaging window (see
`messaging-and-cost.md` §2), so a Mini App can *feed* the OA channel rather than
compete with it.

The precise mapping — which Mini App interactions license which OA message class
— has its own page, `quyen-loi-gui-tin-tu-oa-khi-nguoi-dung-tuong-tac-voi-mini-app`,
which the 2026-07-21 archive lacked and the current corpus now contains. **Search
it before designing a Mini-App-feeds-OA funnel**; don't infer the mapping from the
general interaction list.

---

## 4. Payment

Shape: **create order → receive method → receive callback → update status**, with
`createOrder`, `getOrderStatus`, `checkTransaction`, `createRefund`,
`getRefundStatus`, `updateOrderStatus`, plus a `notify` callback.

Provider settings exist for **ZaloPay, VNPay, MoMo, PayMe, bank transfer, COD**,
and a **custom method** path for anything else. Merchant registration is a
prerequisite. The current corpus carries this as `checkoutSdk` (24 pages).

---

## 5. Publishing and review — the gate people forget

`intro` (16 pages) covers app creation, **permission requests**, **publishing**,
design guidelines, common technical errors, and best practices. Two recurring
traps worth naming up front:

- **Permission requests must state a clear purpose** or review rejects them — and
  **admins can test permission flows without review**, so a flow that works in
  development tells you nothing about whether it will ship (§2).
- **Details entered at Mini App creation are not freely editable** afterwards;
  changing them needs a support ticket and review-team confirmation [S1].

Search `-s platform-docs` for the specific page before advising on a submission;
review criteria are the fastest-moving part of this surface.

---

## Sources

| Key | Corpus file · URL · fetched |
|---|---|
| S1 | `text/platform-docs/docs.zaloplatforms.com__docs__MA__intro__getting-started.txt` · https://docs.zaloplatforms.com/docs/MA/intro/getting-started · 2026-08-06 |
| S2 | `text/platform-docs/docs.zaloplatforms.com__docs__MA__api__user__user-information__getPhoneNumber.txt` · https://docs.zaloplatforms.com/docs/MA/api/user/user-information/getPhoneNumber · 2026-08-06 |
| S3 | `references/knowledge-base/manifest.json`, source `platform-docs`, `docs/MA/*` (439 pages) — the section inventory cited in the coverage table and §3–§5 · 2026-08-06 |
