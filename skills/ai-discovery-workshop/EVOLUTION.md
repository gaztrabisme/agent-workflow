# Evolution Log — ai-discovery-workshop

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: workshop outcomes measured against the distilled method — which of the method's steps actually ran, where BXT scoring produced a decision vs. a number nobody used, where the scope/honesty principles overrode the playbook.

---

## Evolution 0 — 2026-08-09 — the ledger this skill claimed to have

### Harvest scope

No harvest. This entry exists because the skill was found without one.

`SKILL.md:49` states that this skill inherits the `core` spine "and the evolution loop", and correctly marks its method `PENDING` because no real workshop has yet been run through it. It then shipped no `EVOLUTION.md` — so the verdict it declared had nowhere to live, and no later run could settle it. Found by `evolution`'s triage on the day that skill was extracted; the missing artifact is itself the finding.

The only traces available were three commits to this repo, none of them method changes — frontmatter conformance, kernel inheritance, and the initial repo setup with a cross-link to `solution-architect`.

No workshop has been run through this skill and written up. That is the honest state.

### Patterns found

1. **A declared verdict with no ledger is not a verdict** — Impact: H, Effort: L. The skill did the hard part (admitting borrowed confidence) and skipped the cheap part (somewhere to record it). Proof: `SKILL.md:49` says `PENDING`; nothing on disk tracked what would move it.

### Hypotheses applied

1. **Create this file** — closes pattern 1. No method content was changed; there is no evidence that would justify changing any.

Not modified: the entire method. It is distilled and unvalidated, and editing it without a workshop trace would be inventing patterns — the exact failure `../evolution/references/triage.md` gates against.

### Validation results (settled by a later run's step 0)

- [ ] A real AI Discovery / Envisioning workshop has been run using this skill, and its outcome written up.
- [ ] The distilled claims are checked against that workshop: which of the five golden questions produced usable answers, whether BXT scores changed a scoping decision or merely decorated one, whether the Discovery Cards were used at all.
- [ ] The scope/honesty overlay is checked against what the client conversation actually required.
- **Verdict: PENDING** — distilled from documents, zero real workshops recorded. It cannot reach `KEEP` on internal consistency; borrowed confidence is not evidence.

---

## Evolution 1 — 2026-08-10 — generalized for publication

### Harvest scope

Not a use-harvest. A publication pass: the skill was written inside a specific employer and named that employer, a named colleague, and four reference client accounts throughout. The method underneath is generic; the surrounding specifics were not publishable.

### Patterns found

1. **The specifics that made it credible were also what blocked it** — Impact: H, Effort: M. Four anchoring principles were attributed to a named individual, which added nothing a reader could use and everything a scrub had to remove. Proof: 16 name mentions, none load-bearing to the rule being stated.
2. **Page citations to a third-party deck are themselves a disclosure** — Impact: M, Effort: L. Sixteen page-number citations pointed into a partner training document. The citation is evidence of holding the document, independent of whether it is quoted.
3. **Partner funding tables were both proprietary and perishable** — Impact: M, Effort: L. Exact dollar tiers change every fiscal year; a skill file is the wrong home for them regardless of who may read it. Proof: they were stated as fact with no as-of date.

### Hypotheses applied

1. **State the anchoring principles unattributed** — they generalize with no loss; provenance moved to a gitignored local overlay. Closes 1.
2. **Strip all page citations**, replace with "consult the source methodology". Closes 2.
3. **Rewrite `commercial_framing.md` around the funding *shape*** — deal size selects the track, the numbers are an internal pathway, get current tiers from the vendor — rather than the tiers themselves. Closes 3.
4. **Move the source deck, the funding tables, the qualification checklist and the reference accounts to `local/`**, which is gitignored by category.

Not modified: the method itself — Discover/Define/Develop/Deliver, BXT, the cards, the golden questions, the facilitator scripts. Generalizing the setting must not blunt the mechanism, and none of the scrubbed material was mechanism.

### Validation results (settled by a later run's Phase 2)

- [ ] A reader with no context can run a workshop from this skill alone — the test of whether generalization cost anything.
- [ ] `commercial_framing.md` still answers a real commercial question now that the tiers are gone; if it does not, it should shrink further rather than have them restored.
- **Verdict: PENDING** — the scrub is verified (0 denylist hits, clean-clone checked), but "still useful after generalization" is a claim about future use and has no evidence yet.

---

## Evolution 2 — 2026-08-10 — vendor-neutral: renamed, and the platform stripped out

### Harvest scope

A second publication pass, one day after the first. Evolution 1 generalized the *setting* (employer, colleague, accounts) but left the *platform* throughout: 44 product- and vendor-name mentions across the tracked files, plus the vendor's initials in the skill's own name.

### Patterns found

1. **Generalizing the setting but not the vendor left the skill half-neutral** — Impact: H, Effort: M. Evolution 1 treated "whose engagement was this" as the risk and stopped there. The residue was a method that read as one vendor's sales motion, which narrows who can use it and quietly assumes a stack the client may not run. Proof: `SKILL.md` named a specific managed LLM service in its own anti-pattern about tech-first framing.
2. **Product names were doing the work that category names should** — Impact: M, Effort: M. Decision rules routed to named products ("adopt/extend *X*" vs "build custom *X*" vs "build on *Y*"). The *shape* of that decision — off-the-shelf vs custom vs platform — is the transferable part; the product names were incidental and dated. Proof: the same rule now reads correctly against any cloud.
3. **The name was the last mention and the most load-bearing** — Impact: M, Effort: H. `ai-discovery-workshop` carried the vendor in the directory, the frontmatter, the repo URL, and 21 files across 8 sibling skills. Renaming cost more than every content edit combined, which is the argument for not encoding a vendor in a skill name in the first place.

### Hypotheses applied

1. **Renamed to `ai-discovery-workshop`** — directory, frontmatter, repo, and every sibling cross-reference. Closes 3.
2. **Replaced product names with capability categories** — off-the-shelf assistant, low-code agent builder, managed LLM service, unified data platform. Closes 2.
3. **Rewrote the funding section around the shape** of partner programmes rather than one vendor's programme name. Closes 1.
4. **Dropped the provenance statement.** The `PENDING` verdict now rests on the fact that no workshop has been run through this skill — which is true, checkable, and independent of where the method came from.
5. **Added a vendor-neutrality section to the README** stating the mapping rule explicitly: map to the client's stack, not yours.

Not modified: the method. Discover/Define/Develop/Deliver, BXT, the pillars, the cards, the golden questions and the facilitator scripts are unchanged. Stripping the vendor must not blunt the mechanism, and the mechanism was never vendor-specific — which is precisely why this was possible.

### Validation results (settled by a later run's Phase 2)

- [ ] A workshop is run against a client on a different cloud from the one the method was written around, and the card-to-service mapping still works without improvisation. This is the real test of hypothesis 2; until then, the categories are a plausible generalization, not a proven one.
- [ ] No sibling skill still routes to the old name (`grep -rn ai-discovery-workshop` across the constellation returns nothing but historical ledger entries).
- [ ] The decision rules still discriminate. A rule that says "off-the-shelf vs custom vs platform" without naming products risks being *true but useless* — check whether a facilitator can actually act on it in a room.
- **Verdict: PENDING** — zero workshops run, and the generalization is one author's judgement about what was incidental. Pattern 2 in particular could be wrong in the direction that matters: the product names may have been carrying more decision weight than they appeared to.

---

## Evolution 3 — stage B rebuild (2026-10-01)

### Harvest scope

- **Dogfood 2026-10-01:** a fresh model used the skill to prepare a past presale's prework brief; findings were 3 high, 3 medium, and 2 low, with 8 fixed and 0 rejected. No live workshop was run, so the verdict remains `PENDING`.
- **Sources read:** approved skill-set proposal; the ai-discovery-workshop and business-intelligence rule ledgers and crosswalks; practitioner review; the old skill and surviving references; shared core skill and references; skill-builder instructions, checklist, and skeleton; and the cited chapters in the 17 named source books: agentic-mesh, art-of-ai-product-development, challenger-sale, data-science-for-business, designing-ai-interfaces, flawless-consulting, flow-architectures, human-in-the-loop-ml, laws-of-ux, lean-ux, learning-agile, meddicc, pmbok-guide-7e, semantic-software-design, software-architect-elevator, user-story-mapping, and value-based-fees. No course anchor was needed for a routed rule.
- **Coverage:** all 120 routed rules were carried into the workshop skill: 119 workshop rules and one BXT field rule from business-intelligence.
- **Evidence limits:** the cited sources and practitioner review support this authoring pass; they do not establish that the rewritten method works in a live workshop. No workshop outcome was available.
- **Evidence class:** authoring-time.

### Patterns found

1. **The old scope mixed a client decision brief with vendor qualification and architecture work** — Impact: H; Effort: M. The practitioner review and routing table put account research upstream, architecture and proposal downstream, and general product decisions elsewhere.
2. **Some scoring and agenda rules needed correction to preserve evidence and client judgment** — Impact: H; Effort: M. Crosswalk corrections reject averaged pillar scores, a rigid agentic-case target, and a fixed-minute opening; the review also makes Day 8 outputs conditional.
3. **The references had useful examples and facilitation practice that a bare checklist would lose** — Impact: M; Effort: M. The factory example, question-bank guidance, workflow mapping, and score caveats explain how to use the rules.

### Hypotheses applied

1. **Reframed SKILL.md around the client-validated AI use-case brief** — closes pattern 1; preserved upstream business-intelligence input, core references, and downstream solution-architect handoff.
2. **Rebuilt the seven existing references around the workshop flow** — closes pattern 2; corrected BXT aggregation, four-pillar scope, agenda timing, and evidence-dependent decisions.
3. **Adopted 23 relevant candidate practices** — closes pattern 3: 21 ai-discovery-workshop candidates and two business-intelligence candidates. These add user validation, current-workflow and AI-suitability checks, expected value and pain-cost framing, confidence notes, resistance handling, and client-agreed success measures.
4. **Removed routed-out partner-program and unrelated rules** — the rebuild does not restore funding tiers, marketplace steps, vendor qualification counters, or generic product-management and architecture deliverables.

### Validation plan

| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Brief scope and handoff | Facilitator and client decision group produce a validated use-case brief and route architecture and implementation questions to the right owner. | Two real workshops with a documented handoff and client feedback. | natural | skill owner | after two real uses | PENDING |
| BXT scoring and caveats | Participants can trace each score to evidence, see uncertainty, and revise the shortlist without treating the matrix as a verdict. | Two real workshops with completed scorecards and decision notes. | natural | skill owner | after two real uses | PENDING |
| Agenda and facilitation practices | The session reaches a client-owned decision while retaining time for evidence, user feedback, and next steps. | Two real workshops with agenda timing and client feedback. | natural | skill owner | after two real uses | PENDING |

**Verdict: PENDING** — the source-grounded rebuild is complete as an authoring change, but its usefulness remains a hypothesis until two real uses are reviewed.
