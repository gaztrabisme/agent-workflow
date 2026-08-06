# Zalo Official Account (OA)

The business account surface: tiers, verification, groups, webhooks, API shape.
For **who you may message, when, and at what cost** see `messaging-and-cost.md` —
that is the question this surface exists to answer and it has its own page.

Claims are keyed `[S#]` to the **Sources** table at the bottom.

---

## 1. Two account tiers — and only one of them is a product

| | **Hồ sơ quảng cáo** | **OA xác thực** |
|---|---|---|
| Who | No business registration | Business / household with Giấy phép ĐKKD |
| Purpose | Running Zalo ads **only** | Full business/CSKH platform |
| Nhắn tin, Broadcast, Bài viết, **Chatbot**, Gọi thoại | **❌ cannot use** | ✅ |
| Verified tick | ❌ | ✅ |
| Multiple admins across devices | ❌ | ✅ |

Verbatim [S1]: *"Hồ sơ quảng cáo không thể sử dụng các tính năng: Nhắn tin,
Broadcast và Bài viết, Chatbot, Gọi thoại."*

> **The one sentence to take away:** for any messaging or chatbot product,
> **verification is the on-switch, not a polish step.** An unverified OA cannot
> send a message at all. Every delivery plan must treat verification as a
> schedule-critical prerequisite, and it is the client's action, not ours.

An ad-profile account can later add a business licence and become verified [S1].

---

## 2. Verification — the client-action gate

Three routes; pick by how the OA is named and by industry [S2]:

| Route | Basis |
|---|---|
| **Cách 1** | Company name, or the name of a store/branch/business location of the company |
| **Cách 2** | A trademark/brand with a protection certificate from Cục Sở hữu trí tuệ |
| **Cách 3** | Any other name, **or** a business in a conditional-industry list |

**Documents** — scans/photos of originals [S2]:
- **Công văn xác thực (CVXT)** on Zalo's template
- **Giấy Đăng ký kinh doanh** (or equivalent licence) — *all* information pages,
  bearing the issuing authority's seal and signature
- Zalo may request further documents mid-review [S2]

**Two hard scheduling facts** [S2]:
1. **14-day deadline:** *"OA cần nộp hồ sơ xác thực trong vòng 14 ngày từ khi tạo
   OA."* → **do not let the client create the OA early and sit on it.** Creating
   the OA starts a clock.
2. **The legal representative must personally approve inside their own Zalo app:**
   for document sets 1A/2A/3A, *"Người đại diện pháp luật của doanh nghiệp sẽ nhận
   được yêu cầu xác nhận qua Zalo để đồng ý việc tạo và xác thực tài khoản OA."*

> For a listed company or any org where the legal rep is a busy executive, item 2
> is a **willingness-and-calendar risk, not a paperwork risk**. Surface it in
> planning as a named person's action with a date, not as "submit documents".

⚠ **Not verified in this corpus:** the commonly-cited "2–3 business days, free"
SLA. It comes from earlier desk research, not from a crawled page. Do not quote a
review SLA to a client without confirming live.

---

## 3. Groups: GMF is the only official group surface

An OA **cannot join a user's existing group chat.** It can only operate **GMF
groups that the OA itself owns**, whose members must be followers. This is the
single structural fact that shapes every "can the bot sit in our staff group"
conversation — see `unofficial-zca-js.md` and `bot-platform.md` for the two
alternatives, and `../SKILL.md` §"Choosing a surface".

Sizes and costs are in `messaging-and-cost.md` §4 (GMF-10/50/100/1000, monthly
maintenance, OA→group messages free until 31/12/2026).

Messages a user sends **in a GMF group count as an interaction** that opens a
`Tin Tư vấn` window [S3] — a genuinely useful property: group participation
licenses 1:1 follow-up.

---

## 4. API surface (v2, `openapi.zalo.me`)

Doc areas in the corpus (`docs/OA/*`, 179 pages, fetched 2026-08-06) — a map of
where detail exists:

| Area | Pages | What lives there |
|---|---|---|
| `webhook/` | 35 | Inbound events (messages, follow/unfollow, permission grants) |
| `tin-nhan/` | 24 | Send APIs per message type + message management |
| `nhom-chat-gmf/` | 24 | GMF group management |
| `quan-ly/` | 22 | OA info, user info, tags, followers, quota |
| `v2/` | 21 | Legacy v2 (unsupported for OA Doanh nghiệp since 20/6/2023) |
| `extension/` | 16 | Zalo OA Extension (embedded apps inside OA Manager) |
| `noi-dung/` | 12 | Articles, videos, media |
| `phu-luc/` | 11 | Appendix: OAuth codes, rate limits, `buttons`/`elements` structures, error codes |
| `goi-thoai/` | 8 | Voice calls |

Auth is OAuth: authorization code → access token + refresh token, with the app
acting on the OA's behalf [S4]. App Secret Key is retrieved from the developer
console; rate limits and the full error-code table are in `phu-luc/` [S4].

**API request-rate limits are a package feature**, not a constant — the pricing
comparison names "số lượng request/phút tối đa của 1 OA khi tích hợp Zalo OpenAPI
(không bao gồm ZBS Template Message)" and "số lượng App được ủy quyền" as
per-package rows [S5]. Size these against the package before designing a polling
or bulk-sync integration.

---

## 5. Key terminology (get these right in client documents)

| Term | Meaning |
|---|---|
| **OA** | The business's official account on Zalo |
| **Zalo App** | The developer-console application that manages an OA or other Zalo services (ZCA, Mini App). One App can hold several Mini Apps |
| **ZCA** — Zalo Cloud Account | The **spend-management** account for OA and ZNS/ZBS services |
| **ZBS** — Zalo Business Solutions | The commercial umbrella; ZBS Template Message is the renamed ZNS |
| **UID** | A user's id **scoped to one OA** |
| **UID by App** | A user's id scoped to one App — a *different* namespace |
| **GMF** | The OA-owned group-chat product |

All from the terminology table [S6]. The ZCA/ZBS/App distinction matters at
contract time: billing is set up on ZCA, messaging entitlements on the OA package,
API access on the App.

---

## Sources

| Key | Corpus file · URL · fetched |
|---|---|
| S1 | `text/solutions/oa.zalo.me__home__documents__guides__khoi-tao-zalo-official-account_61.txt` · https://oa.zalo.me/home/documents/guides/khoi-tao-zalo-official-account_61 · 2026-07-21 |
| S2 | `text/solutions/oa.zalo.me__home__documents__guides__huong-dan-xac-thuc_70.txt` · https://oa.zalo.me/home/documents/guides/huong-dan-xac-thuc_70 · 2026-07-21 |
| S3 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__tin-nhan__tong-quan.txt` · https://docs.zaloplatforms.com/docs/OA/tin-nhan/tong-quan · 2026-08-06 |
| S4 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__phu-luc__cac-tuong-tac-cua-nguoi-dung-voi-oa.txt` · https://docs.zaloplatforms.com/docs/OA/phu-luc/cac-tuong-tac-cua-nguoi-dung-voi-oa · 2026-08-06 |
| S5 | `text/solutions/zalo.solutions__oa__pricing.txt` · https://zalo.solutions/oa/pricing · 2026-07-21 |
| S6 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__bat-dau__kham-pha.txt` · https://docs.zaloplatforms.com/docs/OA/bat-dau/kham-pha · 2026-08-06 |
