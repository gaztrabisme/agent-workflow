# Unit F fix report — 2026-10-10-reward-skill

Date: 2026-10-11. **Status: PASS for the requested revision and local acceptance. Overall skill verdict: PENDING.** All 20 findings have instruction changes and retrieval links. Local checks do not establish complete workflow usability or audience effects.

## Scope and grounding

Read root `AGENTS.md` first. Grounded in the reward-design manual and references, first-use feedback/critique/report, supplied research findings and V's corrected claims, core manual/canonical references, skill-builder refine workflow, and evolution loop. V remains authoritative; no new psychological research or unsupported technique was added. Source-task qualifications, rather than tier count, govern the recipes.

Writes are confined to `skills/reward-design/SKILL.md`, `references/**`, `EVOLUTION.md`, and this report. Research and dogfood records, other skills, registration, scripts and wiki were not edited. The owner's Unit F request authorizes this internal revision; no additional approval is needed. Existing changes elsewhere in the working tree belong to the preceding work and were left alone. Installation, cloud packaging, commit and push were excluded by the write boundary.

The original media and measurement files linked by dogfood 1 are absent from this repository packet. This run repairs the procedure from the supplied records; it cannot independently reproduce the reported five scene changes, 26 caption transitions or chart callout times. The reported 27-slide PDF and 57.500-second explainer are one critique task with two artifacts, not two independent real uses.

## Decisions and reasons

- Separate verdict, evidence status and source provenance so observable presence cannot certify comprehension or source truth.
- Keep the seven stages as diagnostic destinations and give existing-artifact critique one executable order.
- Retain every frame score and inspect content, captions and chart regions separately because captions and small builds can defeat an undifferentiated cut scan.
- Put detailed measurement/scoring procedures in linked references; the main skill remains 142 lines with a 24-line Quick start.
- Consolidate duplicate findings into ranked changes with one accountable owner; label expected benefit as reviewer inference.

## Finding resolutions

Paths below are relative to `skills/reward-design/`. **20 resolved; none rejected or deferred as an instruction edit.** Later-use tests remain pending.

| ID | Disposition | File and section / concrete change |
|---|---|---|
| F01 | Resolved | `references/review-checklist.md`, Scope and scoring; `SKILL.md`, Execution and output: separate inspection verdict/evidence status, observed partial conditions, unset unavailable verdict, PASS/FAIL only for fully observed acceptance |
| F02 | Resolved | `references/review-checklist.md`, Questions and Scope and scoring: explicit predicates for all 27 checks, especially R10/R19/R20/R21/R22/R26; file/host split and absent mechanism versus unavailable evidence |
| F03 | Resolved | `references/review-checklist.md`, Scope and scoring and a/b table columns: artifact and intended-audience subchecks scored independently; no composite pass hides untested response |
| F04 | Resolved | New `references/measure-playback.md`, Review existing playback; linked from `SKILL.md`, Critique mode and References: ffprobe duration/fps/time base, native timestamp/frame views, all-frame full/content/caption/region scores, ebur128/silencedetect, visual confirmation and analyst-choice crops/thresholds |
| F05 | Resolved | `SKILL.md`, Execution and output; `references/timing-and-structure.md`, Beat-plan fields; `references/measure-playback.md`, Exact-time and exact-frame views: separate observed time, method/precision, reported transcript time and proposed prototype time; pixel/readable/perceived onset distinctions |
| F06 | Resolved | `SKILL.md`, Critique mode — existing artifacts; `references/review-checklist.md`, Test record: ordered inspection-only path for immutable exports; production checks and affected recheck only after a candidate exists |
| F07 | Resolved | `references/review-checklist.md`, Severity and evidence gaps: high/medium/low/none rules with media examples; unavailable evidence has test priority and release implication rather than observed-defect severity |
| F08 | Resolved | `references/timing-and-structure.md`, Source provenance; `SKILL.md`, Grounding gate: artifact report, internal check, supplied-source verification and unavailable source separated per claim; continue inspection, request exact source, withhold dependent certification |
| F09 | Resolved | `references/timing-and-structure.md`, Reader, mandate and delivery mode; `SKILL.md`, stage 1 and Critique mode: actual reader/decision versus embedded sample audience, provisional assumptions, prior briefs treated as context |
| F10 | Resolved | `references/timing-and-structure.md`, Reader, mandate and delivery mode; `references/review-checklist.md`, R12 and Delivery and sound prerequisites: reader-paced/live/narrated/interactive modes; no invented PDF advance schedule |
| F11 | Resolved | `references/sound.md`, Event cues and functional feedback; `references/review-checklist.md`, R07/R15 and Delivery and sound prerequisites: four event-pair kinds, semantic narrated-reference/mark check versus device-perceived synchrony, no universal offset threshold |
| F12 | Resolved | `references/sound.md`, Check before handoff; `references/review-checklist.md`, Delivery and sound prerequisites; `references/measure-playback.md`, Audio loudness and signal onsets: stream/decoded/auditioned/stems/listener prerequisites, proxy limits, confirmed-bed predicate and actual spoken-pace evidence |
| F13 | Resolved | `SKILL.md`, Execution and output; `references/review-checklist.md`, Test record; `references/timing-and-structure.md`, Evaluation and return stages: provisional decision-based prompts, pending acceptance when thresholds/participants are absent, memory delay only for an objective |
| F14 | Resolved | `SKILL.md`, principle 1 and stage 4; `references/mechanisms.md`, Vocabulary and decisions; `references/timing-and-structure.md`, Map, promise, progress, payoff; checklist Test record: fulfillment first, excess optional and requires pre-answer expectation measure |
| F15 | Resolved | `references/review-checklist.md`, Rationale IDs column and Scope and scoring; `references/evidence-map.md`, Evidence roles and source-task limits; `SKILL.md`, Evidence tiers: direct task evidence/analogy/craft/ethical roles, actual source context and reviewer-synthesis boundary |
| F16 | Resolved | `references/review-checklist.md`, R11; `references/visual.md`, Reveal and memory: instructional, demonstrated-output and expressive roles; implied claims and distraction checked separately |
| F17 | Resolved | `references/review-checklist.md`, Converge into a ranked handoff; `SKILL.md`, Critique mode step 4: consolidate overlapping checks, rank top three/full essential list by risk/expected benefit, one owner, dependencies and test; ranking/context limits explicit |
| F18 | Resolved | `SKILL.md`, opening dopamine paragraph: workflow/method boundary replaces occupational absolute; specialized research does not estimate a new edit; behavioral/ordinary-imaging proxies cannot establish release |
| F19 | Resolved | `SKILL.md`, Critique mode tailoring note; checklist Test record: allowed report serves as project record, internal inspection completion versus separate coordinator-owned cold/audience/release gates, core release restrictions retained |
| F20 | Resolved | `SKILL.md`, Quick start near the top: five media, three imperative moves each, all with V-corrected tiers/IDs; design inference and honest dopamine framing retained |

All 129 research IDs retain exact V tier/verdict coverage and use links. `references/evidence-map.md` also maps F01–F20 to current instruction sections. All 11 references are linked directly from SKILL.md. Evolution 2 records Codex reviewer/date, deck + explainer, first-use FAIL, changes, owner/revisit dates and PENDING; Evolution 1 remains historical.

## Acceptance output

Command: `bash skills/reward-design/audit/verify.sh`. Exit code: 0. Exact output:

```text
PASS: 129 finding IDs mapped, SKILL.md 142 lines
```

## Additional checks

Command: `python3 skills/reward-design/audit/check_build.py`. Final exit code: 0. Exact output:

```text
Inputs: skills/reward-design; A–E/V; skills.txt; five authorized siblings
PASS: 129 unique original/V/map IDs; exact corrected tiers and verdicts; 0 unused
PASS: 390 evidence tags match V; 148 technique/check lines carry tags
PASS: 622 local Markdown links and anchors resolve
PASS: SKILL.md 142 lines; description 524 characters
PASS: 29 ranked books, exactly 5 buy-first, corrected book-kind labels
PASS: alphabetical registration; exactly 1 added pointer per authorized sibling; unchanged checker copy
```

The first additional-check run failed with `AssertionError: map: duplicate IDs`: single-ID rows in the new source-task legend looked like research-map rows to the existing parser. Those legend cells now use code formatting; canonical research rows remain unique. The checker was not changed.

Command: `python3 skills/reward-design/scripts/check_refs.py skills/reward-design --no-anchor-check --format`. Exit code: 0. Summary:

```text
WARNING: source-anchor check was explicitly skipped; no citation coverage is claimed.
12 files scanned, 0 local paths checked, 0 anchors cited, 0 known, 0 problem(s), 0 warning(s)
```

This checker supplies local package/format fallback evidence, not official skills-ref validation. No external validator lookup/install or new source search was performed under the repository-only boundary. The separate ID/tier/link check above verifies this ID-based audit and its local Markdown anchors.

A synthetic 13-second, 1920 × 1080, 30-fps export was generated and decoded entirely in memory. It had a caption-only change, a separate main-content change and two audio bursts. The documented filter/probe recipes ran against it (memory streams replaced file destinations; no fixture files were written). Exact test output:

```text
PASS: ffprobe stream/time-base recipe and decoded-frame count (390 at 30 fps)
PASS: exact-time and zero-based frame selection both return PTS 12.500 s
PASS: full/content/caption/region score recipes retain all 390 frames, including zero scores
PASS: caption-only change at 0.500 s is excluded from content crop; content change at 1.000 s is excluded from caption crop
PASS: ebur128 summary/true peak and silencedetect signal-return candidates from synthetic bursts
LIMIT: synthetic command behavior only; no real-media scene counts, speech comprehension or perceived synchrony validated. Fixture and outputs stayed in memory.
```

Manual instruction checks: captions can be observed while comprehension stays not judged; a PDF does not acquire R19/R22 failures from a completion message/coins; unknown host routes stay not judged when in scope; internally checked arithmetic does not verify missing ledgers; chart-label alignment and perceived synchrony use different checks; R25 missing audience responses do not establish a failed experience. These are author checks of rule clarity, not new dogfood or reviewer-agreement evidence.

## Output sample — exact Quick start

```markdown
## Quick start

Use these moves as design choices to test. Tiers describe the source method, not a guaranteed effect; see Evidence tiers below. Make the promised answer useful before adding surprise.

- **Slides / live talk**
  - Open with a specific question the talk will answer. (T3; A4) (T4; D14)
  - Show progress toward a visible working result; make its evidence part of the reveal. (T4; D11) (T1; B16)
  - End on the answer and a feasible next action; keep the middle worthwhile. (T4; D14) (T1; A25)
- **Explainer video**
  - Open with the question and show the context needed to understand it. (T3; A4) (T4; D17)
  - Show each label when its mark is explained; sync any sound accent to the visual change. (T1; B16, B18) (T2; C7)
  - Break complex changes into meaningful steps, then hold the complete answer for inspection. (T1; B17) (T4; D17)
- **Short video**
  - Make the opening deliver on the title or thumbnail promise. (T4; D1)
  - Make the subject and essential words understandable with sound off. (T4; D5)
  - Show useful progress, then close with the promised answer. (T4; D3, D4)
- **UI**
  - Show real progress; distinguish submitted, waiting and completed. (T4; D18, D20)
  - Make celebrations optional and use them only after actual success. (T4; D19, D20)
  - Keep essential terms visible and give the person a clear stopping choice. (T4; B13, D24)
- **Infographic**
  - Put the supported takeaway in the title. (T3; B15)
  - Reveal one meaningful relationship at a time and label its evidence nearby. (T1; B16, B18)
  - Keep scales consistent and leave a complete static view people can inspect. (T3; B20) (T4; D21)
```

## Output sample — revised checklist header and first five rows

```markdown
| Check | Review question | Applicability | a. Artifact evidence | b. Audience task / evidence | Return stage / skill | Rationale IDs |
|---|---|---|---|---|---|---|
| R01 | Is the promised outcome relevant to the actual reader's decision? | A valued outcome is promised | Named reader, decision, benefit and brief basis | Ask whether the answer helps the stated decision | 1 / reward-design | (T4; D7) craft; (T1; A2) analogy |
| R02 | Does the opening accurately promise what the piece delivers? | An opening promise exists | Pair opening with actual resolution | — | 2 / reward-design | (T4; D1) craft; (T1; A1) analogy |
| R03 | Can a viewer identify the specific missing answer? | A question or curiosity gap is used | Locate the question and necessary context | Ask the viewer to state the missing answer before reveal | 2 / reward-design | (T3; A4) analogy; (T1; A5) task evidence: trivia |
| R04 | Does every open loop close at its promised location? | An unresolved question or promised result exists | Located promise-to-answer pairs | — | 4 / reward-design | (T4; D3) craft, attribution unverified; (T3; A4) analogy |
| R05 | Is essential decision information available before action? | An action or consequential inference is invited | Terms, consequences and supporting evidence visible | — | 2 / UX, information-design | (T4; B13) craft; (T4; D24) ethical constraint |
```

## Remaining validation and handoff

The owner's/coordinator's acceptance and any required independent multi-model/cold review remain separate from this internal edit/check record. Audience effects, intended-device listening, source truth for the absent media packet and inter-reviewer agreement are not judged here. No production artifact was modified.

Skill owner/coordinator: run a fresh-context reviewer on a real packet without the prior critique's conclusions; compare applicability, evidence separation, event classification and ranked handoff. Exercise UI/infographic scope in another independent task. Evolution 2 keeps these repairs PENDING, with first revisit 2026-10-18 and overall revisit 2026-10-25 or after the required uses. This revision and its synthetic checks do not count as a second real use.
