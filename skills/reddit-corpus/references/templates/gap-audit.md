# `gap-audit.md` — the phase 5 output shape

Every other phase ships an output shape; phase 5 shipped only a prompt, and two independent runs of it produced artifacts with different fields and different ranking schemes — so neither could be diffed against the other, and neither could tell whether the *previous* audit's items had survived. That is how three recovered items got dropped a second time. Use this shape.

```markdown
# Gap audit — <pass name>

**Inputs:** <digests> · versus <delta path>.
**Standing condition:** <is this delta already audited once? then yield is residue —
say so, and expect the remainder to skew toward method claims and toward
contradictions the previous revision introduced.>
No crawl. Corpus not re-verified. Project's own config/status files: in scope.

## A · Items the delta does not carry, ranked by consequence

### A1. <one-line claim>
**<source digest, section>**
> <the quote>

**Why it matters here:** <in terms of a decision this project makes>
**Reachable today:** yes / no — <needs a version bump? custom nodes? new hardware?>
**Changes output at fixed seed:** yes / no / n-a
**Why dropped:** <your best guess — this is data about the brief>
**Should have outranked:** <name a section the delta DID include, or "no">

## B · Checked, and NOT a gap
<Items you verified were correctly carried or correctly cut, so a later reader
does not re-litigate them. Both independent runs invented this section
unprompted; that is why it is mandatory.>

## C · Prior audit's items — did they survive?
| Prior item | In final delta? | Where / why not |
|---|---|---|
<Mandatory whenever the delta carries a recovered-items section. An item an
audit recovered and the synthesis dropped twice is the strongest signal in
the pass — stronger than anything found fresh.>

## D · What this says about the pass, not the topic
<Method findings. Feeds the delta's "About this pass" section. If this is
empty, you audited the topic and not the pass.>
```

## The two fields that matter most

`Reachable today` and `Changes output at fixed seed` are the axes one real project decided on — substitute your own, but **have some**. Without them the audit produces a list you *read*; with them it produces a list you *act on*. That difference was the clearest gap between two runs of the same phase, and the shape is what caused it, not the auditor.

## Rules

- **Rank by consequence, and say what each item should have outranked.** That single instruction is what turns an audit into a thesis instead of an inventory — both runs confirmed it as the highest-value line in the brief.
- **Read digest preambles, not just their verdict lists.** The most consequential findings in the measured pass were framing prose that no verdict list contained.
- **Section B is not optional.** Two independent auditors both invented it; a "not a gap" list is what stops the next pass re-deriving the same dead ends.
- **Quote, with the source digest and section.** An audit item that cannot be traced back is an opinion.
