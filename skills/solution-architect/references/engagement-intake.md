# Phase 0 — Engagement intake (the front gate)

**Fires when the input is informal.** Site-visit notes, a conversation you're recalling from memory, a
voice-memo transcript, a chat scroll, a forwarded email thread, "we met the owner and she wants AI." No
document to answer, no requirement list, no structure — just context, some of it wrong.

The rest of the lifecycle assumes a formal input. This phase manufactures one. Its output is what Phase 1
(Frame) consumes.

**Skip it** only when the engagement genuinely starts from a formal document (an RFI/RFP arrives cold). Even
then, run steps 2 and 4 on the surrounding context — the document is never the whole story.

---

## The protocol

### 1. Take the whole dump first

Don't interrogate mid-flow. Let the human finish, however unstructured. Interrupting to ask "what's the
budget?" trains them to give you a filtered account, and the unfiltered one is where the negative space
lives. Read it all, *then* work.

### 2. Tier every statement

Nothing downstream is trustworthy if this is skipped. Tag each material claim:

| Tier | Means | Example phrasing in the frame |
|---|---|---|
| **Confirmed** | You saw it, or a primary document states it | "38,000 m² plant (site visit)" |
| **Reported** | A named person at the client said it — attribute it | "Chair says the technical team resists efficiency changes" |
| **Hearsay** | Someone told you what someone else said | "Via the supplier: they're replacing the line next year" |
| **Marketing** | Self-reported by a party with an interest | "Supplier catalogue claims 8-hour service response" |
| **Inference** | Nobody said it; we concluded it | "Their machines likely have no digital interfaces" |
| **Speculation** | We're guessing and should say so | "Possibly a budget cycle driving the timing" |

**A statement never changes tier silently.** If an inference later gets confirmed, say what confirmed it.
Downstream artifacts inherit the tier — an assumption built on hearsay is a weaker assumption, and the
register should show that.

### 3. Fill the frame slots

Whatever the dump covered, these are the slots. Empty ones become asks or assumptions — never silence.

- **Outcome** — what changes for the business if this works, in their words, not technology.
- **Baseline** — what it costs or looks like today. If nobody knows, that's finding #1.
- **Economic buyer** — who releases money. Distinguish from **sponsor** (who wants it), **users** (who
  touch it), and **blockers** (who loses if it succeeds — see step 4).
- **Trigger** — why now? An expansion, an audit, a loss, a new hire, a competitor. No trigger usually means
  no budget.
- **Decision process** — who else signs, what forum, what timeline, what happens if it slips.
- **Hard constraints** — budget shape (CapEx vs OpEx, one-time vs recurring), existing systems, regulatory,
  physical/site access, data availability.
- **Relationship context** — warm or cold, who brokered it, what obligation that creates, who else is
  circling.
- **What winning looks like personally** for the buyer. Executives buy outcomes that make them look right.
- **Deal shape** — enterprise bid or fixed-price delivery (`deal-shapes.md`). This determines the machinery.

### 4. Name the negative space

The highest-value part of intake, and the part that never appears in the dump. Forcing questions:

- **What would make us lose?**
- **What did they *not* ask for** that an organisation like this should obviously need? Absence is data.
- **Who loses if this succeeds?** Every efficiency or visibility project takes discretion away from
  someone. Name them. They will surface later as delay, missing access, or "the data isn't ready."
- **What are we being told that's too convenient?**
- **What does the enthusiastic sponsor not control?**

### 5. Collapse opportunities into candidate projects

An informal dump typically yields a list of "opportunities." **A list of opportunities is zero projects.**
Say this out loud — it is the most useful pushback in the phase.

Promote an opportunity to **candidate project** only if all four hold:

1. **Named beneficiary** — a specific role that behaves differently afterwards.
2. **Observable outcome** — something that can be measured, or at minimum witnessed.
3. **A data/access path that exists** — or a named owner who can grant it.
4. **A definition of done** — what you'd demo to call it finished.

Anything failing one or more is a **lead**, not a project. Park it with the *single named dependency* that
would promote it ("needs CCTV playback access — owner: plant security"). This converts a vague list into a
short buildable set plus an explicit parking lot, which is the actual fog→walkway transition.

Then rank the candidates by *(value to the economic buyer) ÷ (dependency risk)* — not by technical interest.

### 6. Declare the ID spine

Before any artifact exists, decide what everything will key to (`artifact-integrity.md`): requirement refs
for an enterprise bid, acceptance-criteria IDs for fixed-price delivery. Declaring it now is what stops the
engagement fragmenting into files that disagree with each other later.

### 7. Hand back

Terminate with `docs/engagement-frame.md` on disk **and** a four-part report:

1. **Decided** — what you resolved without asking, each with the assumption it rests on. This is the point
   of the gate; handing back a question list is a failure, not a deliverable.
2. **Asks** — ranked, ideally ≤5, strictly things only the human can answer. Anything you could research,
   decide, or assume does not belong here.
3. **Proposed deliverables** — named artifacts, with dates, and what each unblocks.
4. **Pushback** — where you think the framing is wrong, with the reason.

---

## Sensitive-inference handling

Some inferences are not merely uncertain — they are damaging if they surface. A read on someone's
competence, a suspicion about internal conduct, a guess at a political motive. These reframe an entire
engagement and are genuinely useful internally.

**Test:** *if the client read this sentence, what happens?* If the answer is "the relationship ends" or
"someone gets fired," it needs a **handling rule**, not just an Inference tag.

The rule, stated in the frame beside the inference:

- **Internal-only**, with a named holder.
- **Never in a shared, exported, or client-facing artifact** — including diagrams, decks, and the wiki
  section you would screen-share.
- **Never used as stated justification.** Pitch the resulting solution on its legitimate merits —
  objectivity, automation, evidence quality, efficiency — which are true independently of the inference.
- If it drives a scope decision, record the *decision* and its defensible rationale, not the suspicion.

A sensitive inference that turns out to be **wrong** and was written into a shared document is
unrecoverable. Treat labelling as necessary but not sufficient.

---

## Anti-patterns

- **Interviewing instead of ingesting** — interrupting the dump for structure you could impose afterwards.
- **Handing back a question list** and calling it a frame. Decide what you can; ask only what you can't.
- **Asking what you could look up.** Public company facts, market context, and product ranges are research,
  not client questions. Burn goodwill only on what's genuinely private.
- **Treating the opportunity list as a scope.** It's raw material; step 5 is the work.
- **Letting an inference harden into a fact** across retellings because nobody re-checked the tier.
- **Skipping the negative space** because the meeting went well. Enthusiasm is not access.

## Done means

`docs/engagement-frame.md` exists, every frame slot is filled or explicitly marked as an ask, every material
claim carries a tier, the opportunity list is split into candidate projects and parked leads with named
dependencies, the deal shape and ID spine are declared, and the human has ≤5 ranked asks in front of them.
