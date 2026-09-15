# Evolution Log — ceric

The loop that turns real use into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: CERIC reads and audits done with this skill (their `ceric_check.py` output and scorecards), and unaided reads graded with its instrument. Fixtures and the calibration traces: `$CERIC_FIXTURES` (default `~/Documents/Work/lab/ceric`, private).

---

## Evolution 1 — 2026-09-15 — birth: distilled from the workshop, harvested from three unaided reads, dogfooded cold

### Harvest scope
- **Distilled** from the CERIC workshop packet (Bjorn & Burgasser, Vietnam National University HCMC, 2026-09-13) and the workshop's answer deck with Prof. Burgasser's annotated marking of the same paper. Classification: distilled → ships `PENDING`; the distilled claims must be validated against real use before `KEEP`.
- **Harvested** from three real, unaided reads of Event Horizon Telescope Collaboration (2019), ApJL 875, L1, each completing the packet as a participant, one per model (Claude Opus 5; Codex; Grok 4.6), graded against the key with the instrument this skill now carries (`references/grading.md`). Representative because the three readers are strong, independent, and made the same mistakes.
- **Dogfooded** by a fresh-context agent on a different model lane using the skill cold on the same paper at hunt depth (`lab/ceric/dogfood/`), graded the same way.

### Patterns found
Ranked (Impact ÷ Effort), with the proof each bit:
1. **Measured results filed as Evidence** — Impact: H, Effort: L. All three readers put the resolved ring, its diameter, the flux ratio and the four-day stability under Evidence; the key files them under Reasoning and grades the same error in an unaided DeepSeek run as ○ on Evidence, Claim and Reasoning at once (3.5/5). Two readers filed the derived mass as a Claim; one filed the paper's broad conclusion as an Implication.
2. **Quotes without pages** — Impact: H, Effort: L. `check_quotes.py --freeform` over the three runs: Opus pinned 248 of 311 quotations to a page and 234 verified in place; Codex pinned 0 of 13; Grok pinned 0 of 18 (section numbers only). An unpinned quote is unverifiable without re-reading the paper.
3. **Hedges dropped in the paraphrase** — Impact: H, Effort: L. Grok's sentence builders carry no hedge from the paper ("the image is the shadow of a supermassive Kerr black hole" where the paper says "consistent with"; "candidate" absent); `check_narrative.py` strengthener lint: "is the shadow" (not in paper). Codex and Opus kept "consistent with" and "candidate".
4. **Unbounded depth** — Impact: M, Effort: L. Opus's Activity 3 file is 218 KB against a 15-minute box; its 15 questions and 100 corrections are excellent and nobody in a workshop could use them. The packet's time-boxes had no agent equivalent.
5. **Out-of-lane findings mixed into the read** — Impact: M, Effort: L. Opus audited the packet itself (wrong abstract, wrong link, shifted translations) inside its participant folder; the audit was correct and drove the packet fix, and it does not belong in the notes.
6. **Figures and tables lost to text extraction** — Impact: M, Effort: L. `check_quotes.py` sends 5 of Opus's Table 1 and error-bar quotes to eye-check; Grok rendered every page to PNG and read tables there. Text extraction is not the paper.
7. **Pair disagreement is real and resolvable** — Impact: M, Effort: M. Opus's two independent markups of the same abstract disagreed on 9–10 of ~22 phrases; the definitions settled every one. Worth its cost only when the read leaves the building.

### Hypotheses applied
1. **`references/elements.md` §Boundary rules 1–4 + the M87 worked example** — closes pattern 1. The test is one question: *could this sentence exist before any analysis ran?*
2. **`references/templates/ceric-notes.md` Page column on every quote row; `scripts/check_quotes.py` scores each quote on its stated page ± 1 and reports page-hint coverage** — closes pattern 2.
3. **`references/elements.md` §Hedge lexicon; SKILL.md principle 4; `check_narrative.py` hedge/strengthener lints; `grading.md` failure mode (d)** — closes pattern 3.
4. **`references/hunt.md` §Declare the depth first (abstract · hunt · full with size boxes)** — closes pattern 4.
5. **`references/hunt.md` §Out of lane (`issues.md` beside the notes)** — closes pattern 5.
6. **`references/hunt.md` step 0 (render pages); `check_quotes.py` eye-check bucket; `grading.md` procedure step 1** — closes pattern 6.
7. **`references/hunt.md` §Pair read, declared under the approach gate when stakes justify** — closes pattern 7.

Not modified (validated as already-sound): the packet's own sequence (mark → copy → status → questions → hunt → missing → builders → CCERI) is carried as written; the five failure modes and the ✓/○/✗ instrument are the workshop's and are used unchanged.

### Validation results (settled by a later run's step 0)
- [ ] The boundary rule (hypothesis 1) is exercised on a second paper in a different field without new friction.
- [ ] A read produced with the templates passes `ceric_check.py` on first run without the checker needing a change.
- [ ] The dogfood scorecard beats the best unaided baseline and the DeepSeek 3.5 (see §Calibration below).
- [ ] `audit` mode catches, on a real synthesis or dossier, a claim without evidence or a dropped hedge that the existing gates missed.
- **Verdict: PENDING** — distilled from documents plus one calibration run on one paper; a single dogfood; no second field yet.

### Calibration (measured, this run)

Three unaided reads of the same paper, graded with the instrument (source: `lab/ceric/ASSESSMENT.md`; seven of twelve grader groups by cold Claude graders, the rest by a GLM grader against the key digest; no adversarial verification ran, every deduction re-checked once by the GLM grader, 42 CONFIRMED). Then one read with this skill, cold, on a GLM agent at hunt depth.

| Reader | Skill | A2 abstract /5 | A3 main text /5 | Narrative /5 | Failure modes | Quotes pinned to a page |
|---|---|---|---|---|---|---|
| DeepSeek (workshop's own run, key p.35) | no | 3.5 | — | — | — | — |
| Claude Opus 5 | no | 3.0 | 4.0 | 3.0 | b FAIL | 248 / 311 |
| Codex | no | 3.0 | 3.5 | 3.0 | b FAIL | 0 / 13 |
| Grok 4.6 | no | 3.0 | 2.5 | 3.0 | b, d FAIL | 0 / 18 |
| GLM 5.3 flash, dogfood | **yes** | not yet graded against the key | not yet graded | not yet graded | `ceric_check.py` green: 25 / 25 quotes verified on their page, 0 flagged, hedges kept (consistent with ×6, candidate ×3, not inconsistent ×4), strengtheners none, copied runs 0 | 25 / 25 |

What the dogfood settled: the boundary rule applied by a fresh reader reproduced the key's marking of the abstract (its fourteen boundary calls are listed in the dogfood report; calls 2, 3, 4, 6, 7 match the key's rulings exactly). What it did not settle: an element-by-element grade of the dogfood read against the key; that is the first validation item below, unchanged. Its own size (69 table rows, 2,840 words) overshot the hunt box that was then written into `hunt.md` from its finding F6.

### Dogfood findings and their disposition
Critic: a fresh-context GLM agent, briefed with `skill-builder`'s dogfood brief, report at `lab/ceric/dogfood/dogfood-report.md`. Nine findings, none rejected; all applied by a GLM edit run, acceptance re-run green.
- F1 high — no worked hunt example and no rule for what a Quote cell may contain → `templates/ceric-notes.md` §4 three worked rows and the one-quote-per-cell rule; `hunt.md` steps 2 and 5.
- F2 high — symbol-dropping misquotes (≳ → nothing) pass every gate → `check_quotes.py` `pass-eye` status for quotes carrying ratios or limit symbols; `extract_pages.py` per-page glyph report and warning.
- F3 med — template Page cells were bare digits the checker cannot pin → `p1` style in every example; one clause in `hunt.md`.
- F4 med — stem check was a substring match → sentence-initial match; docstring and `grading.md` corrected.
- F5 med — CCERI lint printed like a verdict → labelled advisory; ladder sentences neutral.
- F6 med — size box unmeasurable → rows and words per depth; `ceric_check.py` prints the notes size.
- F7 low — several documents in one turn unowned → one line in SKILL.md.
- F8 low — grading without a key unspecified → clause in `grading.md`.
- F9 low — freeform globbed reports and READMEs → skipped, files picked are printed.
