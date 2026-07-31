# Grounding Gate

Ground domain decisions in a substrate rather than improvising from memory. This is a **gate**, not a suggestion: on a covered domain, consult the substrate *before* deciding and record one line.

## The gate

1. **Before** designing/implementing/claiming in a covered domain, consult the substrate for prior art / exact terms / theory.
2. **Record one line** where decisions live (Key Decisions / decisions.md / the response):
   - `Grounded: <query/source> → applied <finding>`, or
   - `Grounded: <query/source> → nothing relevant`.
3. **Skippable only** by stating the domain isn't covered (e.g. glue code, pure logistics). A silent skip on a covered domain is a gate violation.

The point is cheap, honest grounding — one consult, one line — not ceremony.

## Substrate by role

| Role-skill | Substrate | Covered domains |
|------------|-----------|-----------------|
| `dev` | Knowledge Base MCP (46 books) | ML, RAG, databases, security, distributed systems, cryptography |
| `business-intelligence` | External sources, graded by the Admiralty Code | any factual claim about a client, market, competitor, or person |
| `solution-architect` | Internal/client docs + KB for the tech layer | the RFI/RFP itself, architecture patterns, NFRs, the client's stated constraints |
| `ms-ai-discovery` | The Microsoft partner-training source + internal docs | BXT, discovery methods, Azure Accelerate, the stack |
| `skill-builder` | Existing skills + this `core` kernel | conventions, the spine, prior skills' patterns |

## The honesty corollary (why this is also an integrity gate)

Grounding is the mechanism behind three integrity rules at once:

- **A claim you cannot ground, you do not make** — or you flag it explicitly as an assumption/unknown. (This is the enforceable form of "demand evidence, yours and theirs" and "don't overconfident-consult.")
- **Grade what you ground.** In research/presale, attach a source grade (Admiralty A–F / 1–6) so the reader knows how load-bearing a claim is. Two grounded-but-weak sources ≠ one strong one.
- **Record the negative space.** Note what you *couldn't* ground — the unknowns — as first-class output. Getting caught by a follow-up you can't answer is the failure this prevents.

An ungrounded confident claim is the single highest-severity defect in client-facing work, exactly as a faked test result is in code. Same gate, different substrate.

## Tier in the schema, not the prose

The corollary above is a prose rule, and prose rules fail silently at scale. Where values are **tabular**, carry provenance **structurally**:

- **Separate the column.** A value a subagent or a source *reported* lives in `<field>_reported`. The unsuffixed field holds only what you measured or verified yourself. Never write a reported value into the measured field "for now" — that is where the drift starts.
- **Make the wrong state unrepresentable.** Add an invariant a script can assert: *"no row carries a `page_count` without a `sha256`."* A tier you can grep is a gate; a tier you remembered is a hope.
- **Grade in a column**, not a footnote, where the substrate is external sources (Admiralty A–F / 1–6).

**Why this exists.** On a real engagement, values reported by research subagents were written into artifacts using the word *"measured"* — the underlying files had never been downloaded. The prose rule *"a claim you cannot ground, you do not make"* was present, correct, and did not fire. The schema-level version was then authored in-project as the fix, and is stronger than the rule it repairs.

## For anything attributed to another party: record the speaker

A citation to a *source* is not attribution. Transcripts, threads and meeting notes record **everyone in the room in the same voice** — the client, the broker, and your own colleagues — so "it's in the call transcript" does not establish who said it. Where a claim constrains you (a date, a volume, an accuracy bar, a budget, a requirement), the provenance you need is **the mouth it came out of**.

**The check is one question, asked of every attributed constraint: *whose sentence is this?*** If the answer is "ours", it is not the other party's constraint, whatever file it lives in.

> *Observed three times on one engagement — each instance surviving the purge of the one before it.*
> **(a)** *"Their extraction runs at ~80%"* shipped across four documents as a client statement. The client never gave a figure; it originated in our own internal chat. Purged.
> **(b)** *"Deadline ~10 Sep"* was recorded as a **confirmed** client constraint and every downstream plan worked backwards from it. In the transcript: our account lead asks for a timeline → **the broker** answers *"within September"* → **our own account lead** offers *"the 10th September"* → the client says *"Correct"*, to the preceding remark about the *decision* timing. **No client voice states the date at all.**
> **(c)** *"A Tax analyst needs ~200 figures from **40 statements**"* and *"**Three** Lines of Service need the same statement **in one quarter**"* — two invented quantities on the **same slide**, wrapped around one genuine client figure (`~200`). The client names *five* lines of service and his own duplication example uses *two*; no timeframe is stated anywhere. `40` was caught one round earlier and `Three` survived, **because the fix swept the digit and not the card.**

**What (c) adds: an invented number hides best next to a real one.** `~200` is the client's own, and its
presence made the whole sentence read as sourced. When you verify one quantity in a clause, **verify every
quantity in that clause** — and when you correct one, re-sweep the artifact it sat in rather than the string
you replaced. Grep for the number **as a word as well as a digit** (`40` / *"forty"*, `3` / *"three"*); the
digit search is what let (c) live through a round.

Both are the same mechanism and neither is dishonest: a colleague's helpful clarification hardens into a client requirement because the record captures both in one voice. The defence is not more caution — it is **reading the primary source rather than the summary**, and writing the speaker down beside the claim. Where the substrate is tabular, carry it as a column (`stated_by`), per the schema rule above; a speaker you remembered is a hope.

**Corollary for anything you are asked to "refresh" from memory.** A request to restate what a number or date means is the moment to re-read the source, not to recall the summary. Both defects above were found that way, and (b) had already been re-summarised several times without anyone re-opening the transcript.

## A limitation is a claim, and it needs grounding too

The gate above is written for positive claims — *"X is true."* It applies with equal force to the negative
ones you make about **your own ability**: *"that can't be rendered here", "the API doesn't expose that",
"there's no way to test this offline", "we have no source for that."*

These are the most dangerous ungrounded claims you will make, for two reasons. They are **self-fulfilling** —
nobody checks a capability you said you lacked — and they are **load-bearing on scope**, because work gets
silently dropped rather than visibly deferred.

> *Observed.* A deck review recorded *"no rasteriser on this machine, so there is no visual QA"* and carried
> it through **three review rounds**, eventually writing it into a pre-registered check plan as a stated
> method limitation. The tool was installed the whole time, at the vendor's default path, absent only from
> `PATH`. When finally probed, it surfaced **every structural defect in the deliverable within ten minutes** —
> defects that were invisible to the text-based checks that had run in its place. The limitation had been
> asserted once, then inherited by every later pass as established fact.

**The rule: probe, then declare.** A limitation is reportable once you have run the check that establishes
it, and the check goes in the record beside it — `Probed: pdftoppm, soffice, mutool, gs → none on PATH; no
LibreOffice at the default install path either.` That line is falsifiable. *"No rasteriser available"* is not.

Three habits that follow:

- **`which` is not a probe.** Installers routinely skip `PATH`. Check the platform's default install
  locations, and the language-level equivalents (a library that does the same job) before concluding.
- **Re-probe when the environment could have changed** — a new session, a different machine, a dependency
  someone installed. An inherited limitation is a memory, not a measurement.
- **Never let a limitation you asserted become a premise you plan around.** The moment a constraint starts
  shaping scope — *"since we can't check X, we'll rely on Y"* — it has become load-bearing and must be
  re-verified before the plan hardens around it.

The symmetry is the point: *a claim you cannot ground, you do not make* — **including a claim about what you
cannot do.**
