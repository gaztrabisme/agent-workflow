# Identity & authentication on Zalo

The question that breaks most Zalo architectures: *"we have this id — can we
reach that person, and can we prove who they are?"* The answer is governed by
**three disjoint id namespaces** that do not join, and one bridge that does.

Claims are keyed `[S#]` (documentation) or `[T#]` (live test) to the **Sources**
table at the bottom.

---

## 1. Three id namespaces — not joinable by id

| Namespace | Where it comes from | Scope |
|---|---|---|
| **Global uid** | unofficial personal-account library | Zalo-wide |
| **OA-scoped UID** | OA APIs / webhooks | one specific OA |
| **UID by App** | Zalo App / Mini App | one specific App |
| **Zalo Login id** | Social API OAuth | one App's login |

The platform's own terminology table names UID and "UID by App" as **different
ids for the same human** [S1]. There is no documented mapping between them, and
none between either and the global uid.

> **The rule:** you cannot join these by id. Two systems holding "the uid" for
> the same person are usually holding **different, non-comparable strings**.

**The one bridge is the phone number:**

| Direction | Available? |
|---|---|
| phone → uid | ✅ via `findUser`-style lookup on the unofficial leg [T1]; ✅ via ZBS send-by-phone on the official leg [S2] |
| **uid → phone** | ❌ **does not exist** |

Design consequence: **hold the phone number yourself.** It is the only durable
cross-namespace key. An architecture that plans to "get the phone from Zalo
later" has a hole in it.

---

## 2. A uid is an identifier, not a credential

Never authenticate on a uid alone. Proven concretely: possessing a member's uid
from a shared group does **not** grant a 1:1 channel to them, let alone identity
proof [T1]. Treat every uid as a routing hint that arrived over an untrusted path.

---

## 3. Where a phone number can legitimately come from

| Route | Returns phone? | Gate |
|---|---|---|
| **Social API `/me`** (web "Login with Zalo") | ❌ **never** — id, name, picture only | OAuth consent |
| **Mini App `getPhoneNumber`** | ✅ | SDK ≥2.13.0 · user consent · **Mini App review of the permission flow**; single-use token, 2-min expiry [S3] |
| **OA `request_user_info`** | ✅ (consented, from a follower) | OA flow; ⚠ exact behaviour unverified in this corpus |
| **The client's own HR/CRM records** | ✅ | none — you already have it |

> ⚠ **Correction to a common belief:** phone number is **not** a web Zalo-Login
> scope. It is a **Mini App capability** [S3]. A plain web dashboard cannot pull
> a phone from Zalo login, no matter which permissions are requested. Any design
> premised on that is broken and must change shell (→ Mini App) or change source.

---

## 4. The auth pattern that works without any of this

For an internal tool where the client already holds a staff roster:

```
roster phone (client's own data)
  → ZBS Template Message OTP to that phone
  → user enters code
  → bind session to the employee record
```

Why this is the strong default:
- It **never needs a phone number from Zalo** — sidestepping §3 entirely.
- It works for **brand-new users** who have never touched the OA. The
  send-window rules carve out an explicit exception for authentication codes
  sent to a user creating a new account — meaning an OTP can reach a cold
  contact where an ordinary message cannot.
- It survives the loss of the unofficial leg completely: auth runs on the client's
  phone list plus a verified OA, so a burner-account ban degrades group
  monitoring and touches nothing security-relevant.
- Zalo Login is then **optional convenience** (id/name/avatar SSO), not the spine.

**Costs to model:** OTP is the **most expensive** ZBS template class — 400đ +
VAT, plus any button/component surcharges (`messaging-and-cost.md` §5). Model OTP
volume as `logins × retry-rate`, not as headcount.

⚠ **Verify before building:** the OTP/new-user send exemption is recorded from
earlier desk research and is **not** confirmed by a page in this corpus. It is
load-bearing for this whole pattern — confirm it live before committing (see
`open-questions.md`).

---

## 5. Choosing the identity spine — decision order

1. **Does the client already hold phone numbers for these people?**
   → Yes: use them. Roster-phone + OTP. Stop here; this is the simplest correct
   answer and it needs nothing from Zalo's identity stack.
2. **No, and the users are the public?** → You need consented phone capture →
   **Mini App** `getPhoneNumber` (accept the review gate), or an OA
   `request_user_info` flow.
3. **Only need "some stable id per user", not a phone?** → OA-scoped UID from the
   webhook is fine. Just never let it cross into another namespace, and never
   treat it as proof of identity.
4. **Need to attribute messages inside an existing group?** → global uid from the
   unofficial leg, **for attribution only** (`unofficial-zca-js.md`).

**The recurring mistake** is step 2 done by reflex — reaching for Zalo Login to
get a phone number it structurally cannot return, discovering this late, and
having to change shell mid-build.

---

## Sources

| Key | Evidence |
|---|---|
| S1 | `text/platform-docs/docs.zaloplatforms.com__docs__OA__phu-luc__cac-tuong-tac-cua-nguoi-dung-voi-oa.txt` · https://docs.zaloplatforms.com/docs/OA/phu-luc/cac-tuong-tac-cua-nguoi-dung-voi-oa · 2026-08-06 — terminology table (UID vs UID by App) |
| S2 | `text/solutions/zalo.solutions__business-message__pricing.txt` · https://zalo.solutions/business-message/pricing · 2026-07-21 — send by SĐT vs by UID |
| S3 | `text/platform-docs/docs.zaloplatforms.com__docs__MA__api__user__user-information__getPhoneNumber.txt` · https://docs.zaloplatforms.com/docs/MA/api/user/user-information/getPhoneNumber · 2026-08-06 |
| T1 | Live test, 2026-07-15 — uid reach model; see `unofficial-zca-js.md` §2 |
