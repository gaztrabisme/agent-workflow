# The unofficial leg (`zca-js` and friends)

A personal-account automation library that drives Zalo Web's private endpoints.
It exists in this skill for one reason: **it is the only thing that can sit in a
group chat the client already has.** Everything else about it is a liability.

Evidence here is a different class from the rest of the skill. Claims keyed `[T#]`
come from **live tests on a dedicated burner account**, not from documentation —
Zalo publishes nothing about these endpoints. Dates matter: private endpoints
change without notice.

---

## 1. The structural fact that creates the need

| Surface | Can join a group the client already has? |
|---|---|
| OA | **Never.** Only GMF groups the OA itself owns, followers-only |
| Mini App | Never — it is a UI shell, not a chat participant |
| Zalo Bot | **Unresolved** — `can_join_groups: false` on Basic; see `bot-platform.md` §2 |
| **zca-js (personal account)** | **Yes — currently the only option** |

If the requirement is *"monitor and reply in our existing staff group"*, the
official platform has no answer today. That is the whole case for this leg, and
it is the first thing to re-test whenever Zalo Bot's group support moves.

---

## 2. What was actually verified (live, 2026-07-15)

Tested with a bot account added to a 5-person group it was **not** friends with [T1]:

**Group threads are privacy-independent.** From inside a group the bot:
- enumerated **every member's uid + name in one call** — no friending, no phone
  lookup, no waiting for anyone to speak
- posted to the group
- **@-mentioned members**, producing real notifications

**Membership *is* the authorization.** A mention is just `{pos, uid, len}`
metadata attached to the text — not a credential, not a permission.

**1:1 DM is still fully gated, and co-membership does not relax it** [T1]:

| Recipient state | Direct-to-uid DM |
|---|---|
| Friend | ✅ delivered |
| Stranger, open privacy | ✅ delivered |
| **Stranger who blocks strangers — but shares the bot's group** | ❌ **refused, `code 122`** |
| Blocked-you / harder block | ❌ `code 127` |

That third row is the load-bearing one: it **kills the "a shared group unlocks
DM" hypothesis**. The uid is not a skeleton key. Holding it lets you address the
group, tag inside it, and attribute inbound messages; it does **not** open a 1:1
channel to someone who blocks strangers.

**Architecture consequence.** Monitoring and group reply need nothing from
members — put them in the group thread. The 1:1 nudge path requires the
individual to friend the bot or run open stranger-messaging → **treat direct DMs
as opt-in, enrolled at onboarding.**

**API shape observed** [T1]: `getAllGroups` → `getGroupInfo` →
`getGroupMembersInfo`; `memVerList` entries arrive as `"<uid>_<ver>"` — strip the
suffix. Mentions are assembled server-side.

---

## 3. The liabilities — state all of these before anyone commits

1. **It violates Zalo's Terms of Service.** This is not a grey area. For a listed
   company or any compliance-sensitive client, saying so plainly is mandatory —
   it is their risk to accept, not ours to quietly carry on their behalf.
2. **Ban-prone.** Use a **dedicated burner account**, never a personal account and
   never anything belonging to the client.
3. **Fragile session.** One web listener per account; opening Zalo Web on that
   account elsewhere kills the listener.
4. **Rides private endpoints** — can break with no notice and no changelog.
5. **Brand-new accounts face restrictions.** Create the burner **early** on its
   own Vietnamese SIM and warm it up before it matters.
6. **Never the auth authority.** A uid is an identifier, not a credential
   (`identity-and-auth.md` §2). Nothing security-relevant may rest on this leg.

**De-risking that actually works:** put *only* group monitoring on this leg. Keep
authentication, dashboards, and all official messaging on the OA/ZBS side. Then a
ban degrades one feature instead of taking down the product.

---

## 4. Recipient resolution — a real failure mode worth designing against

An observed production-shaped bug [T2]: outbound resolution ran through a
**roster keyed by short name**, while the caller supplied the person's **full
name** → lookup miss → `404`, presented to the user as "not in contacts" despite
the recipient genuinely being a friend.

Two lessons that generalise:

- **Friendship is not the gate your code thinks it is.** Delivery needs it;
  *selection* ran entirely off an internal roster. Be explicit about which gate
  a failure came from — they produce identical-looking errors.
- **Normalise names deterministically before the send call, and let unmatched
  names fail loudly** rather than being coerced to a nearest match. A mis-routed
  Zalo message to the wrong manager is worse than a visible 404.

Roster files loaded once at startup need a restart to take effect — an easy
source of "I fixed it and nothing changed" [T2].

---

## 5. Open experiments

Carried in `open-questions.md`; summarised here because they gate any commitment:
group-member harvest at realistic scale (50–200, not 5), uid attribution
reliability across message types in a busy group, and a ban-risk/session-durability
probe under sustained load. **None of these can be answered from documentation.**

---

## Sources

| Key | Evidence |
|---|---|
| T1 | Live test, **2026-07-15** — burner account added to a 5-person group it was not friended into; group enumeration, group post, @-mentions, and four direct-to-uid DM cases (friend / open stranger / stranger-blocking-strangers / blocked). Recorded in the originating project's `wiki/gotchas.md`, "Zalo reach model" entry. |
| T2 | Live debugging, **2026-07-07 → 2026-07-08** — outbound recipient-resolution failure and its two-layer fix. Same source, "Zalo outbound recipient resolution" entry. |

⚠ Both are **point-in-time observations of undocumented endpoints**. Re-verify
before designing on them; do not treat them as platform guarantees.
