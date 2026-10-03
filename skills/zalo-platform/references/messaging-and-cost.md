# Messaging windows & cost — the load-bearing reference

Every "can we message this user, and what does it cost" question resolves here.
This is the most-consulted and most-often-wrong area of the platform: the rules
changed on **01/01/2026** and most third-party blog posts (and several of our own
earlier notes) still describe the old model.

All claims are keyed `[S#]` to the **Sources** table at the bottom. A claim with
no key is not grounded and must not be repeated.

---

## 1. The two gates — the single most important thing on this page

There are **two independent gates**, not one. Confusing them is the classic error,
and both "it's 48 hours" and "it's 7 days" are half-right.

| Time since the user's last interaction | Tin Tư vấn allowed? | Cost |
|---|---|---|
| **0 – 48h** | ✅ free-form, no template | **Free, unlimited** [S1][S2] |
| **48h – 7 days** | ✅ still free-form, no template | **Paid** — package allowance, then 55đ/msg [S1][S3] |
| **> 7 days** | ❌ not permitted | Must use a **ZBS Template Message** [S1] |

- **7 days = the permission gate.** `Tin Tư vấn` requires an interaction "trong vòng
  7 ngày" and the user not blocking the OA [S1].
- **48 hours = the free gate.** "Trong vòng 48 giờ kể từ tương tác cuối của người
  dùng, tin Tư vấn hoàn toàn miễn phí. Sau 48 giờ… giá tin Tư vấn được tính theo
  bảng giá" [S1].

> **⚠ Dead fact — do not repeat: "8 free messages per 48h, then 55đ".**
> The per-user cap is gone. Verbatim [S2]: *"Từ ngày 1/1/2026, đối tác có thể gửi
> tin Tư vấn **miễn phí không giới hạn** trong khung 48h."* The `remain: 8` still
> returned by the quota API is a **vestigial constant** — "Từ ngày 1/1/2026: luôn
> trả về giá trị remain = 8; Sau ngày 1/3/2026: sẽ dừng trả về thuộc tính này" [S2].
> Any code branching on `cs_reply.remain` is testing a constant and will break when
> the field disappears.

> **⚠ But 55đ/tin is NOT dead.** It is the live price for `Tin Tư vấn` sent
> **outside** the 48h window once the package allowance is spent [S3]. An earlier
> internal note said to delete 55đ from all cost models — that was an over-correction.
> What died is *"8 free then 55đ inside 48h"*; what lives is *"free inside 48h,
> 55đ outside it beyond allowance"*.

### There is no daytime / quiet-hours window
No clock-based send window exists in the current docs. The interaction window is
the only gate [S1]. If a reseller or BSP asserts a "no sending after 9pm" rule,
ask them to cite it.

---

## 2. What counts as an "interaction" — and which ones only buy a greeting

`Tổng quan` [S1] lists **ten** recognised interactions, and — crucially — splits
them into two classes:

**Opens a full `Tin Tư vấn` window** (7 actions):
1. Gửi tin nhắn đến OA
2. Gửi tin nhắn trong nhóm chat GMF
3. Gọi thoại đến OA
4. Đồng ý nhận cuộc gọi từ OA
5. Bình luận (comment) bài viết của OA
6. Tương tác với OA Chatbot
7. Nhấn Menu / CTA query / Widget của OA

**Buys only a greeting** ("OA có thể gửi **lời chào** ngay sau khi người dùng thực
hiện hành động") — not a conversation window [S1]:
8. Quan tâm OA (following)
9. Nhấn nút "Nhắn tin" trên trang Thông tin OA

> **Design consequence:** a follow is *not* a licence to converse. Funnels that
> assume "they followed us, so we can message them" are built on the wrong class.

> **⚠ Two primary pages disagree.** The appendix page [S4] lists only six
> interactions, omits comment/chatbot/GMF/widget, and adds "Nhấn biểu tượng hoặc
> nút Gọi OA". **Prefer `tin-nhan/tong-quan` [S1]** — it is the page that governs
> send rights, it is more granular, and it is the only one that distinguishes
> full-window from greeting-only. Treat [S4] as stale. This disagreement is
> unresolved upstream; flag it if a client decision turns on it.

---

## 3. Message families

| Family | Members | Gate |
|---|---|---|
| **Tin nhắn Cơ bản** | Tin Tư vấn · tin OA→nhóm GMF · Tin Broadcast | Interaction window (above); Broadcast requires the user to *follow* the OA [S1] |
| **ZBS Template Message** | Tin Giao dịch · Tin Hậu mãi | Pre-approved template; sent by **UID or phone**; no interaction window [S1] |

**"ZNS" is the old name.** Since the 01/01/2026 restructure the product is **ZBS
Template Message**; older deep links 404. Economically the earlier ZNS findings
still hold, but use the ZBS pages and vocabulary with clients [S1][S5].

Broadcast volume is capped by the OA package's monthly Broadcast allowance, and
the platform separately rate-limits how much promotional messaging one follower
may receive per period [S1].

---

## 4. OA package pricing (VAT **included**)

Verified OA only — an unverified OA cannot buy these [S3].

| Package | 1 year | ≈ /mo | 6 months | ≈ /mo | Seats |
|---|---|---|---|---|---|
| **Tiêu chuẩn** | 1.000.000đ | ~83.000đ | *not offered* | — | 5 |
| **Tăng trưởng** | 2.500.000đ | ~208.000đ | 1.400.000đ | ~233.000đ | 15 |
| **Toàn diện** | 6.000.000đ | ~500.000đ | 3.400.000đ | ~566.000đ | 100 |

Annual figures [S3]; 6-month figures [N1] (behind a client-side toggle the crawl
cannot see). **The annual term is genuinely cheaper per month** (~11–12%), and
**Tiêu chuẩn has no 6-month option at all** — it vanishes from the card list when
the toggle flips [N1].

*"Chi phí đề cập bao gồm thuế GTGT (10%)"* — OA package prices **include** VAT
[S3]. (ZBS prices do not — §5. Mixing the two bases in one quote is a real and
easy error.)

### The full entitlement table — **four** tiers, not three [N1]

The crawl rendered this table as bare `---` separators, which is why an earlier
reading missed both the fourth tier and every number in it. Read live:

| Entitlement | Cơ bản | Tiêu chuẩn | Tăng trưởng | Toàn diện |
|---|---|---|---|---|
| Tin Tư vấn outside-48h /month | — | — | **500** | **2.000** |
| Free GMF-100 groups | — | — | 1 | 3 |
| Chatbot | — | — | ✅ | ✅ |
| Chatbot scripts | — | — | 10 | 50 |
| Zalo Open API integration | — | — | ✅ | ✅ |
| **API rate limit** | — | — | **100 req/min** | **2.000 req/min** |
| Authorised Apps | 1 | 1 | 3 | unlimited |
| MCC agents | — | 1 | 5 | 10 |
| ZCC agents | — | — | unlimited | unlimited |
| Articles /month | — | 15 | unlimited | unlimited |
| Free Broadcast receipts /follower /month | — | — | 4 | 4 |
| Staff accounts | 3 | 5 | 15 | 100 |

**"Cơ bản" is a real fourth tier** — the entry level, 3 staff accounts, 1 app, and
none of the messaging or automation entitlements [N1].

**Three things this table decides:**
- **Chatbot and OpenAPI are gated at Tăng trưởng.** Any build that talks to the OA
  programmatically has a **2.5M đ/yr floor** — not an option, a prerequisite [S3][N1].
- **The API rate limit is a 20× cliff: 100 → 2.000 req/min.** For a bulk sync,
  a migration, or any high-traffic integration, *this* is what forces Toàn diện —
  not seats and not message volume. It is invisible on the pricing cards.
- **Broadcast is capped at 4 free receipts per follower per month**, identically on
  both paid tiers — so Broadcast volume never justifies the upgrade.

**Overage:** once the monthly outside-48h allowance is spent, "hệ thống bắt đầu
tính phí theo lượt tin nhắn" at **55đ/tin** [S3].

Older "Nâng cao"/"Premium" packages were discontinued **01/06/2026** [S6].

### GMF group costs (separate from the package) [S3]

| Group type | Max members (incl. OA) | Maintenance /month |
|---|---|---|
| GMF-10 | 10 | 25.000đ |
| GMF-50 | 50 | 55.000đ |
| GMF-100 | 100 | 75.000đ |
| GMF-1000 | 1000 | 300.000đ |

- OA→group messages: **free until 31/12/2026**. Member→group messages: free [S3].
- Groups included in a package are exempt from the maintenance fee [S3].

---

## 5. ZBS Template Message pricing (VAT **excluded**)

*"Đơn giá chưa bao gồm thuế GTGT"* [S7] — the opposite basis from OA packages.

**By template type** (successful delivery) [S7]:

| Template type | đ/msg |
|---|---|
| Template xác thực (OTP) | **400** |
| Template voucher | **400** |
| Template yêu cầu chuyển khoản | 300 |
| Template vé xe khách (Beta) | 300 |
| **Các loại còn lại** | **300** |
| Template hành trình, special logistics/passenger-transport verticals | from 200 (conditions apply; contact support@zalo.solutions) |

All prices **re-confirmed live 2026-08-06** [N2] — unchanged from the archive.
One rename: *"Template yêu cầu **thanh toán**"* is now *"Template yêu cầu
**chuyển khoản**"* [N2]. Same price; use the current wording with clients.

> **⚠ Three corrections to our earlier internal notes**, all of which would have
> gone into a client quote wrong:
> - OTP/xác thực is **400đ, the top tier** — not 300đ. (The earlier note said
>   "OTP is not the cheapest" — right direction, wrong number.)
> - "Các loại còn lại" is **300đ**, not 200đ. Only the special-vertical journey
>   template starts at 200đ.
> - The image surcharge is **not** un-crawlable. It is **300đ**, printed in the
>   table [S7]. The earlier note claimed it rendered as `NaN` and had to be read
>   live — that was wrong, and it sent a research round chasing a non-problem.

**UID vs phone send** — for a base custom template [S7]:

| Send method | đ/msg |
|---|---|
| Gửi qua SĐT | 300 |
| Gửi qua UID | **210** |

> **Reading the estimator correctly.** The estimator's headline figures ("Từ
> 210đ/tin" for a custom template, "Từ 280đ/tin" for xác thực) are **UID prices**,
> while the tables above are **phone prices**. 210/300 and 280/400 are both exactly
> **0.70** [N2] — so the current UID subsidy is a flat **30% discount** on these
> classes. Quoting the estimator figure alongside the table figure as if they were
> alternatives for the same send method is a straightforward double-count.

The UID discount "sẽ thay đổi dựa trên phân loại, thành phần (component), CTA,…
và có thể sẽ thay đổi cho đến khi có thông báo mới" [S7] — **never hard-code the
0.70 ratio**; recompute per template shape.

**Buttons (CTA)** — first button in a category is 0đ, each additional button in
that category is 100đ [S7]:

| Button destination | đ |
|---|---|
| Đến dịch vụ mặc định (Sao chép, Thanh toán, Xem chi tiết) | 0 |
| Trang thông tin OA · Zalo Mini App của DN · bài viết OA · trang DN · tra cứu hoá đơn | 100 |
| Gọi điện | 200 |
| Trang ứng dụng của Doanh nghiệp | 600 |
| Trang web / Zalo Mini App **khác** | 500 |
| Trang ứng dụng khác | 1.000 |
| Trang đích kêu gọi tải ứng dụng | 3.000 |

**Special components & advanced services** [S7]:

| Item | đ |
|---|---|
| Hình ảnh | 300 |
| Nút phản hồi (Beta) | 100 |
| Lệnh cấp quyền gọi | 400 |

**Costing rule:** a ZBS message price = template-type base + per-button charges +
special components, **excl. VAT**, discounted if sent by UID. A "cheap OTP" that
carries an image and an external-web button is 400 + 300 + 500 = **1.200đ + VAT**,
six times the naive 200đ estimate. Always itemise.

---

## 6. The quota API — read the window, don't guess it

`POST https://openapi.zalo.me/v3.0/oa/quota/message`, header `access_token`,
body `{"user_id": "<uid>"}`. Requires the "gửi tin và thông báo qua OA" permission.
The user need not follow the OA [S2].

```json
{"data": {
   "last_interaction": "1690184100000",
   "cs_reply":  {"remain": 8, "total": 8},
   "promotion": {"daily_remain": 0, "daily_total": 1,
                 "monthly_remain": 4, "monthly_total": 6}},
 "error": 0, "message": "Success"}
```

- **`last_interaction`** (unix ms) is the field that matters — compute both gates
  from it yourself. This is the trustworthy input [S2].
- **`cs_reply`** is the vestigial one. Constant since 01/01/2026, removed after
  01/03/2026 [S2]. Do not branch on it.
- **`promotion`** carries the real per-user promotional caps, daily and monthly [S2].

**Implementation rule:** derive send-eligibility from `last_interaction` + the
two gates. Any code that counts messages against a per-48h cap is modelling a
rule that no longer exists.

---

## 7. Cost-model checklist (before any number reaches a client)

1. Which family — Cơ bản (window-gated) or ZBS (template-gated)? They price on
   different bases and **different VAT bases**.
2. What fraction of sends land inside 48h? Those are free; only model the rest.
3. Does the monthly outside-48h volume exceed the package allowance (500 / 2.000)?
   That, not the headline price, is what forces Tăng trưởng → Toàn diện.
4. For ZBS: itemise base + buttons + components. Never quote the base alone.
5. UID-send discount applies only where you hold a UID — phone is the universal
   fallback for cold contact (see `identity-and-auth.md`).
6. VAT: OA packages include it, ZBS excludes it. State the basis in the quote.
7. **Re-read the live pricing pages** if the corpus is >30 days old (`kb_search.py
   --stale`). Pricing is the fastest-moving surface here.

---

## Sources

| Key | Corpus file · URL · fetched |
|---|---|
| S1 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__tin-nhan__tong-quan.txt` · https://docs.zaloplatforms.com/docs/OA/tin-nhan/tong-quan · 2026-08-06 |
| S2 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__tin-nhan__quan-ly-tin-nhan__kiem-tra-han-muc-gui-tin-nhan.txt` · https://docs.zaloplatforms.com/docs/OA/tin-nhan/quan-ly-tin-nhan/kiem-tra-han-muc-gui-tin-nhan · 2026-08-06 |
| S3 | `text/solutions/zalo.solutions__oa__pricing.txt` · https://zalo.solutions/oa/pricing · 2026-07-21 |
| S4 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__phu-luc__cac-tuong-tac-cua-nguoi-dung-voi-oa.txt` · https://docs.zaloplatforms.com/docs/OA/phu-luc/cac-tuong-tac-cua-nguoi-dung-voi-oa · 2026-08-06 *(stale — see §2)* |
| S5 | `text/platform-docs/docs.zaloplatforms.com__docs__ZBS__bat-dau__gioi-thieu-zbs-template-message.txt` · https://docs.zaloplatforms.com/docs/ZBS/bat-dau/gioi-thieu-zbs-template-message · 2026-08-06 |
| S6 | `text/solutions/oa.zalo.me__home__documents__guides__Quan-ly-goi-zalo-oa_5417812380640953602.txt` · https://oa.zalo.me/home/documents/guides/Quan-ly-goi-zalo-oa_5417812380640953602 · 2026-07-21 |
| S7 | `text/solutions/zalo.solutions__business-message__pricing.txt` · https://zalo.solutions/business-message/pricing · 2026-07-21 |
| N1 | **[NAV]** https://zalo.solutions/oa/pricing · read **2026-08-06** · clicked the *6 tháng* toggle, then read the "So sánh quyền lợi gói" table (4 columns: Cơ bản / Tiêu chuẩn / Tăng trưởng / Toàn diện) from the rendered DOM |
| N2 | **[NAV]** https://zalo.solutions/business-message/pricing · read **2026-08-06** · read the rendered price tables and the estimator's per-class headline figures |
