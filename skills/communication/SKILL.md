---
name: communication
description: "Produces an audience-tailored client message or update brief from agreed engagement facts for a client-facing engagement lead. USE WHEN drafting a kickoff, status update, escalation, change explanation, meeting recap, or close message for a client. Disambiguation: delivery owns engagement trackers and signed-client controls; business-intelligence and solution-architect supply presale evidence and approved solution decisions; this skill turns agreed inputs into client communication. Keywords: client update, status report, client email, escalation, scope change message, project communication."
license: Proprietary (private; cites a paid course)
---

# Communication

This skill produces an audience-tailored client message or update brief from agreed facts for a client-facing engagement lead. It covers kickoff, status, escalation, scope-change, demo or prototype cover notes, meeting-recap, and close communications. Draw status, scope, schedule, and cost facts from delivery records; use presale evidence or approved solution decisions where relevant. Treat the client's latest request as evidence of what they asked or want decided, not as proof of what is built or agreed. Keep facts, uncertainty, and requests distinct. Internal engineering announcements and general launch copy are outside this skill.

It inherits the shared `core` kernel. See [core](../core/SKILL.md); use its canonical gates instead of copying their definitions here.

## When it fires — and when a sibling owns it

- **This skill:** a client needs a kickoff note, status update, escalation, change explanation, written recap, or close message built from agreed facts.
- **`delivery` instead:** the work is to establish or maintain the signed-engagement baseline, tracker, acceptance record, or change decision that supplies the facts.
- **`business-intelligence` or `solution-architect` instead:** the work is to research presale evidence or decide the proposed solution. Once their findings or decisions are agreed, this skill shapes the client-facing message.

> **Disambiguation:** choose by artifact and audience. This skill writes client-facing communication; it does not own the trackers, presale research, or solution decisions the message draws on.

## Principles / anchoring rules

1. **Agree the communication arrangement before the first recurring cycle.** Set the reporting cadence, format, and escalation path with the client. Choose the measures and level of detail that help the client follow the work. [book:project-management-with-ai], Customizing reports to meet stakeholder needs. Keep clients informed throughout the work so progress and changes do not arrive as an end-stage surprise. [course:5907 · U3 · L26 · 04:15–05:59]
2. **Build from settled facts.** Use the current source of record for status and agreement facts, label what is still uncertain, and do not turn a guess into an agreed fact. The client's latest request is evidence of what was asked, not what is built or in scope. Return meeting notes or unclear feedback to the client for confirmation before relying on them. [course:5907 · U3 · L24 · 00:00–02:10]
3. **Write for this client’s context and decision.** Shape the entire message around what the recipient needs to know and cares about, including their context and the consequence for them; translating an internal label into client vocabulary alone is not enough. [book:hbr-guide-business-writing], Tailor your message. Use the client’s defined audience, objectives, and tone as context where they are available. [course:5907 · U3 · L20 · 03:41–05:12]
4. **Keep a new request inside change control.** When a new stakeholder asks for a change, treat it as a scope change to evaluate through the agreed change-control path. Do not treat a copy of the signed annex as a sufficient response to the request. [book:head-first-pmp], Why scope changes. The rule followed a live engagement where multiple authors let scope disagree across several artifacts, including language versions; evaluating the request preserves one decision instead of letting each message reset the agreement.
5. **Keep difficult messages calm, neutral, and useful.** Do not answer an unreasonable message in kind. Be courteous and direct; if the team made a mistake, acknowledge it and say what will correct it. [book:hbr-guide-business-writing], Don’t write in anger. Pause before replying if needed so stress does not spill into the client exchange. [course:5907 · U3 · L27 · 00:00–01:13]

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Set up | Name the readers; agree the recurring cadence, format, channel, and escalation route | Communication arrangement |
| Ground | Assemble source facts, compare the latest request with confirmed build and scope, and record chronology | Fact packet |
| Draft | Explain status or change in the client’s context, with its consequence | Client message or update brief |
| Close | Name any client decision or input needed, its owner and due date when known, and next work | Actionable next step |
| Check | Confirm accuracy, tone, and alignment with approved decisions | Ready-to-send message |

## Agree the reporting rhythm before the first update

At kickoff, agree the reporting cadence, format, and escalation path with the client. Set the rhythm before an issue arrives, so both sides know when an update is due and where a concern goes. Keep the client in the loop at the agreed rhythm as work progresses. [book:project-management-with-ai], Customizing reports to meet stakeholder needs. [course:5907 · U3 · L26 · 04:15–05:59]

For a one-off, post-handover, or pre-contract message with no agreed arrangement, record that none is on file, choose a channel and timing deliberately, and propose a cadence only if the work continues. Do not hold a promised one-off message while trying to establish a recurring rhythm. (derived: dogfood 2026-10-01)

### Name the direct recipient and end reader

Record who will receive the message directly and who is expected to read it at the end. If it will pass through an intermediary, choose language and register for each layer and state whether the body should be forwarded unchanged. If one body cannot serve both readers, prepare separate versions from the same agreed facts. (derived: dogfood 2026-10-01)

### Choose the channel deliberately

Match the channel to urgency and importance: use a direct call or conversation for important, urgent matters; use a planned email or regular meeting for important work that is not urgent; reserve quick messages for prompt, lower-stakes coordination. Do not make every item an interruption. [course:5907 · U2 · L17 · 00:09–01:07]

## Build the update from facts and chronology

Start with the current delivery tracker or other agreed source of record. Separate completed work, current status, risks, client obligations, decisions, and assumptions. If something is not yet verified, name it as open rather than presenting it as settled.

### Compare the client's latest request with confirmed work

List each item in the client's most recent request or input. Using delivery's confirmed status and scope records, mark it built as asked, built differently, outside the agreed scope, or unresolved. The request is authoritative for what the client asked; it does not establish build status, scope, price, or schedule. For each built-differently item, frame a client decision with the available options and confirmed consequences, identify who must decide, and give the needed-by date only if it is recorded. If the owner or date is not set, say so and ask for confirmation or propose a date clearly as a proposal. Route possible out-of-scope items to delivery for change-control evaluation before describing scope or price as settled. (derived: dogfood 2026-10-01)

### Check that the source and attachment are current

Before drafting, compare the record's update time with the newest working artifact and the latest client input. Confirm the attachment, version, and length named in the message against the exact file intended to be sent. If the record predates the newest artifact, reconcile or update the source record before drafting. Follow the [core wiki protocol](../core/references/wiki-protocol.md) freshness checks. (derived: dogfood 2026-10-01)

### Resolve conflicting source pages

If source pages disagree, use the latest dated entry to identify what needs checking, flag the conflict in the fact packet, and do not present either version as settled until the responsible owner resolves it. Follow the [core wiki protocol](../core/references/wiki-protocol.md) contradiction check. (derived: dogfood 2026-10-01)

### Build a chronology before drafting

For a status update, first list the relevant events in order: where the work stood at the last update, what changed since then, and what is expected next. Keep only facts that help the client understand the sequence. A short chronology keeps the message from reading like a jumble of events and opinions. [book:hbr-guide-business-writing], Plot out what happened, and when.

### Confirm meeting notes and unclear feedback

When meeting notes or client feedback could be read more than one way, send the summary back and ask the client to correct or confirm it before the team acts on it. Ask specific questions about what the client likes, dislikes, or means; examples and references can turn a vague reaction into usable direction. [course:5907 · U3 · L19 · 02:31–03:25] [course:5907 · U3 · L24 · 00:00–02:10]

## Tailor the whole message to the client

Build the whole message around the reader’s role, context, and concern—not just a translation of internal terminology. Explain what changed, why it matters to the client, and what decision or action follows. [book:hbr-guide-business-writing], Tailor your message. Where different stakeholders need different detail, produce audience-specific versions from the same agreed facts rather than sending each person a copy of the same report. [book:project-management-with-ai], Customizing reports to meet stakeholder needs.

### State impacts in the client's terms

Name schedule and acceptance effects in the client's terms, rather than calling a change “medium” or using an internal status label. For example: “This adds six days and moves acceptance of criteria F3.1–F3.4 from 12 May to 22 May.” When confirmed and material to the choice, also state the cost or operating impact in the client's terms. Then connect the impact to the client’s priority and decision. [course:5907 · U3 · L19 · 00:00–00:59] (derived: dogfood 2026-10-01)

### Handle scope requests through change control

#### When a new stakeholder asks

When a new client stakeholder makes a request, log and evaluate it as a potential scope change through the agreed change-control path. Communicate the decision and its approved schedule, cost, or acceptance effects once they are known. A signed-annex link alone does not evaluate the new request or establish its impact. [book:head-first-pmp], Why scope changes. Explain the available solution or trade-off with the client, including the consequence of a requested change. [course:5907 · U3 · L26 · 06:00–07:49]

#### When any request appears outside scope

Whoever makes the request, route a possible out-of-scope item to delivery's change-control process; delivery owns the scope decision and any evaluation or price. Once delivery confirms the position, the client message names what was asked, says it is outside the agreed scope, and offers to have it evaluated or priced. State options, consequences, decision owner, and timing only when confirmed; do not imply that an evaluation or price is already approved. (derived: dogfood 2026-10-01)

## Report client delay with a neutral record

On the second silent-client cycle, report the overdue obligation with its age and named owner. A dated, named record keeps the delay visible instead of letting it disappear into delivery variance and look like a team-caused slip. [course:5907 · U3 · L24 · 03:10–04:20]

For difficult exchanges, keep the record factual and neutral. Do not answer an unreasonable message in kind; the aim is to document what happened and the next action, not to win an argument. [book:hbr-guide-business-writing], Don’t write in anger. If bad news is known, communicate it promptly with the effect and the next step the client can take. [course:5907 · U3 · L24 · 02:11–03:09]

## State the next-cycle work

Include the work intended for the next reporting cycle so the client can see what the team expects to finish before the next update. This takes the “what we intend to finish by the next meeting” idea from a Daily Scrum and deliberately carries it into the client status report. [book:scrum-masters-path], Daily Scrum.

Use the current delivery plan for this statement. If the sender does not own the next cycle, name the responsible lead when the record identifies one; if work or ownership is missing, check with delivery and mark it unconfirmed rather than inventing a team commitment. (derived: dogfood 2026-10-01)

## Set the client's next action

For each client decision or input that is needed, name the person, the requested action, and the date needed. If no client action is needed, say so. If an owner is not recorded, mark it unconfirmed and ask who will own it. If a needed-by date is not recorded, state that it is not set and label any proposed date as a proposal; do not invent an agreed owner or deadline. When an update reports a problem or a departure from plan, pair it with a workable solution or option and say what information or sign-off is needed to move forward. [course:5907 · U3 · L19 · 00:00–00:59] (derived: dogfood 2026-10-01)

### Cover a demo or prototype

When a message accompanies a demo or prototype, include a short, fact-checked block that separates: what is real in the current build; what is simulated on screen; and what is not built or is outside scope. Check each line against the exact artifact being sent and confirmed delivery records. (derived: dogfood 2026-10-01)

## Client update check

Before sending, confirm:

- the facts match the current agreed source and any open uncertainty is visible;
- the source record is current against the newest working artifact, and the named attachment, version, and length match the file to be sent;
- the client's latest request is compared with confirmed build and scope facts, with out-of-scope items routed through delivery;
- the recipient, purpose, and level of detail fit this client;
- direct recipient, end reader, language, register, and forwarding intent are clear for relayed messages;
- events are in a clear order and impacts use the client’s terms;
- change requests follow the agreed control path;
- delays and difficult exchanges are dated, owned, neutral, and factual;
- any needed client action has an owner and needed-by date, or the message says no action is needed or that the date is not set; next-cycle work and ownership come from the current delivery plan;
- a demo or prototype distinguishes current build, simulation, and what is not built or out of scope;
- the channel and timing fit the urgency and the agreed communication arrangement.

## Gates (declared, inherited from core)

- **Grounding gate** — ground client claims in agreed trackers, evidence, and approved decisions; label unresolved facts. See [core grounding gate](../core/references/grounding-gate.md).
- **Output Contract** — the message or update brief and its supporting fact packet must be accurate and ready for the named client audience. See [core output contract](../core/references/output-contract.md) and [core wiki protocol](../core/references/wiki-protocol.md).
- **Pushback and teach** — explain a material scope or schedule consequence and give the client a workable option. See [core pushback and teach](../core/references/pushback-and-teach.md).
- **Reader-focused writing** — use the shared artifact-writing guidance for audience fit and editing. See [core artifact writing](../core/references/artifact-writing.md).
- **Client-message cold review** — before a primary message ships, pre-register expected weaknesses in the shared gate review record. Every client-facing message gets a cold reader fluent in its language, preferably a native reader where local voice or idiom matters, who checks it against the fact packet and the exact attachment; record the outcome. When the artifact warrants the full review floor, use core's three distinct passes; when a judgment is likely to be tested, also use the two cold reviewers on different models with the same facts and isolated conclusions. If a required review is unavailable, mark it DEFERRED and hold the send until it is complete. (derived: dogfood 2026-10-01; see [core output contract](../core/references/output-contract.md))

## Anti-patterns (hard no-list)

- Sending a recurring status report before agreeing its rhythm, format, and escalation path. For an ad hoc message with no arrangement, record that fact and use the one-off path above.
- Presenting a disputed assumption or stale tracker value as an agreed fact.
- Writing a status update as a stream of events without a reader-oriented chronology.
- Sending the same level of detail to stakeholders with different roles and needs.
- Describing a change only with internal categories when the client needs the impact.
- Treating a new stakeholder’s request as resolved by pointing at the old agreement rather than evaluating the request through change control.
- Omitting the age or named owner from the second-cycle silent-client delay report.
- Responding to frustration with blame, anger, or unsupported conclusions.
- Leaving a needed client action or next-cycle work implicit, or inventing an owner, deadline, or team commitment to fill a gap.
- Describing a demo or prototype without separating what is built, simulated, and not built or outside scope.
- Naming a stale or superseded attachment as the deliverable being sent.

## Composition

- **Inherits:** `core` for shared gates and reader-focused writing.
- **Consumes:** delivery trackers and change-control decisions for status, scope, cost, schedule, and obligation facts; the client's latest request as evidence of what they asked or want decided; business-intelligence for agreed presale evidence; solution-architect for approved solution decisions.
- **Hands back:** client messages and update briefs that reflect the agreed facts and request the next client action when needed.

## References

- [core](../core/SKILL.md) — shared operating contract.
- [core grounding gate](../core/references/grounding-gate.md) — source grounding and uncertainty.
- [core output contract](../core/references/output-contract.md) — completion evidence and review.
- [core wiki protocol](../core/references/wiki-protocol.md) — durable records.
- [core pushback and teach](../core/references/pushback-and-teach.md) — cooperative pushback with a workable option.
- [core artifact writing](../core/references/artifact-writing.md) — audience fit and editing.
- [update brief template](references/templates/update-brief.md) — audience, fact, decision, and review fields for a one-off client update. (derived: dogfood 2026-10-01)
