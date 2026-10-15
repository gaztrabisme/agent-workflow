# Reward-beat review checklist

Reader: a reviewer inspecting an existing deck, video, graphic or working UI. Use the actual artifact and current mandate. This is a reviewer-synthesized instrument, not a validated psychological scale. Tiers describe methods in [SKILL.md](../SKILL.md); source tasks, evidence roles and citations are in [evidence-map.md](evidence-map.md). Start with the skill's Critique mode, then use stages as diagnostic destinations.

## Scope and scoring

Record the actual reader and decision, sample audience, delivery mode, artifact version, coordinator/acceptance owner and evidence access. Scope file content separately from host/player behavior. A finite video does not establish a host exit route; depicting coins does not establish gambling; a pictured completion message does not establish a triggered success state. Use the delivery modes and provenance states in [timing-and-structure.md](timing-and-structure.md).

For each applicable subcheck record two separate fields:

| Field | Values and decision rule |
|---|---|
| Inspection verdict | **meets**: observed conditions satisfied; **partly**: observed conditions mixed, naming the unmet condition; **misses**: an observed condition fails; **not applicable**: predicate absent, with reason |
| Evidence status | **measured**: directly measured with method/precision; **reviewer-judged**: located inspection or interpretation; **not judged**: applicable evidence unavailable; **skipped**: inapplicable or deliberately omitted, with reason |

Leave the verdict unset (`—`) for an unavailable condition. Use not applicable / skipped only when the predicate is absent, not when required evidence is missing. An applicable check deliberately omitted is — / skipped with its gate consequence. Use PASS/FAIL only for a declared, fully observed acceptance condition.

Split mixed rows into **a. Artifact evidence present, truthful and located** and **b. Intended audience succeeds at the specified task**. Score both; no composite pass may conceal a pending b. The table supplies each subcheck's concrete evidence or proposed task. If truth sources are unavailable, scope a to observable presence/internal consistency and leave fidelity not judged. An audience response is not established by a caption, screenshot, loudness value or scene score. Audience tasks below are proposed prompts, not validated instruments.

Each record contains check/subcheck ID, predicate/reason, location, observation and evidence, provenance, both fields, observed-defect severity, priority-to-test/release implication, owning stage/skill, and one concrete change or next test. Lead with artifact evidence; Rationale IDs explain the recommendation, not the observed finding. Cite their role: direct task evidence, mechanistic analogy, craft precedent or ethical constraint. Do not rank fixes by tier count.

## Severity and evidence gaps

Apply severity only to observed defects. These are review priorities, not psychological measurements.

| Severity | Decision rule | Media example |
|---|---|---|
| High | Wrong/deceptive critical inference, missing essential decision information or unfulfilled core promise | A training demo promises a quality test but ends with samples alone |
| Medium | Materially obscures a relationship or completion | A chart annotation appears after its narrated explanation |
| Low | Optional refinement with no essential loss | A redundant decorative accent competes with an already clear label |
| None | No observed defect | An opening and its supported answer agree |

For unavailable evidence, set severity to — and record **priority-to-test** (high/medium/low, with decision risk) and **release implication** (which claim or acceptance depends on it). Example: missing training logs leave source fidelity pending; missing enjoyment responses leave enjoyment unjudged. Neither proves a false chart or dissatisfied audience. Where an observed defect and an evidence gap coexist, record them separately.

## Questions

Use a and b independently. “—” in the audience column means no audience task is required to close that structural subcheck; it does not certify an audience benefit.

| Check | Review question | Applicability | a. Artifact evidence | b. Audience task / evidence | Return stage / skill | Rationale IDs |
|---|---|---|---|---|---|---|
| R01 | Is the promised outcome relevant to the actual reader's decision? | A valued outcome is promised | Named reader, decision, benefit and brief basis | Ask whether the answer helps the stated decision | 1 / reward-design | (T4; D7) craft; (T1; A2) analogy |
| R02 | Does the opening accurately promise what the piece delivers? | An opening promise exists | Pair opening with actual resolution | — | 2 / reward-design | (T4; D1) craft; (T1; A1) analogy |
| R03 | Can a viewer identify the specific missing answer? | A question or curiosity gap is used | Locate the question and necessary context | Ask the viewer to state the missing answer before reveal | 2 / reward-design | (T3; A4) analogy; (T1; A5) task evidence: trivia |
| R04 | Does every open loop close at its promised location? | An unresolved question or promised result exists | Located promise-to-answer pairs | — | 4 / reward-design | (T4; D3) craft, attribution unverified; (T3; A4) analogy |
| R05 | Is essential decision information available before action? | An action or consequential inference is invited | Terms, consequences and supporting evidence visible | — | 2 / UX, information-design | (T4; B13) craft; (T4; D24) ethical constraint |
| R06 | Can viewers locate the intended focal information at delivery size? | A focal element is specified | Inspect the actual size, contrast and location | Ask viewers to find that element in the intended task | 3 / visual-design | (T2; B1) task evidence: search; (T3; B3, B23) analogy |
| R07 | Does each cue identify the relationship being explained? | A visual cue or narrated reference to a mark exists | Relevant cue, label and mark; measure narrated-reference/mark event pair | Ask viewers to explain the cued relationship | 3 / visual-design, information-design | (T1; B16, B18) task evidence: multimedia learning |
| R08 | Can viewers explain the revealed answer from its evidence? | An explanatory answer is delivered | Answer and supporting evidence; record source provenance | Ask for an explanation; check it against the supplied source | 4 / information-design, reward-design | (T1; B17) task evidence: learning; (T1; A17) analogy |
| R09 | Does a data reveal preserve its original mapping? | Data are transformed or progressively revealed | Compare scales, marks, units and qualifications | — | 4 / information-design | (T3; B20) task evidence: chart transitions; (T4; D21, D22) craft |
| R10 | Is prediction participation optional and respectful? | A prediction invitation exists | Private/skip route and immediate data access | — | 4 / UX, information-design | (T3; B12) task evidence: mixed graphical-prediction results; (T4; D22) craft |
| R11 | Does each striking detail serve its brief-defined role? | Striking instructional, example or expressive detail exists | Explanation, demonstrated-output or experiential role; implied claims checked separately | If distraction matters, ask for the core message under the intended task | 3 / visual-design, reward-design | (T1; B19) task evidence: irrelevant learning details; (T3; B14) analogy |
| R12 | Does delivery allow the audience to process the content? | Content must be read or understood | Use the mode-specific evidence below; locate boundaries and persistent context | Observe task reading or explanation in that delivery mode | 3 / motion, presentation | (T1; B17) task evidence: segmentation; (T3; B25) analogy |
| R13 | Does varied content retain recognizable cues and labels? | Content or feedback varies across a sequence/repeated use | Whole-sequence labels and motifs remain consistent | Test recognition across the sequence; repeat-use claims need repeat-use evidence | 5 / reward-design, visual-design | (T2; A19) analogy; (T1; A20) task evidence: visual exposure |
| R14 | Does sound reinforce the event's actual meaning? | Sound accompanies an event; meaning may be unknown | Audition cue-only, silent and combined versions; record event pair | Ask what event or meaning the sound conveys | 3 / presentation, motion | (T4; C9) craft; (T3; C19, C21) task evidence: music/advertising |
| R15 | Do sight and sound appear synchronous in delivered playback? | Impact/contact, visible speech or musical-transition/reveal pair exists | Measure physical event offsets; review normal-speed delivery | Record perceived synchrony on the intended device | 3 / presentation, motion | (T2; C7, C8) task evidence: audiovisual integration |
| R16 | Is essential meaning understandable without sound or extra motion? | Sound or motion carries meaning; assess each channel separately | Inspect muted and, when relevant, reduced-motion equivalents | Ask viewers to explain the essential answer in each equivalent | 3 / presentation, frontend | (T4; D5, D18) craft |
| R17 | Does the sound bed preserve verbal comprehension? | A bed under verbal content is confirmed; unknown bed remains not judged | Record mix audition and availability of comparable bed/silence versions | Compare the same verbal task with bed and silence | 3 / presentation | (T1; C22) task evidence: reading; (T3; C23) task evidence: digit memory |
| R18 | Is the voice understandable at its actual pace and expression? | Spoken voice exists | Audition the mix; transcribe difficult terms/numbers and actual phrasing | Ask listeners to explain the argument and key facts | 3 / presentation | (T3; C15, C16) analogy: charisma correlations |
| R19 | Does feedback report the milestone actually reached? | A triggered state change exists | Trace trigger, progress, success and error against actual state | — | 4 / UX, frontend | (T4; B22, D18, D20) craft |
| R20 | Does any celebration correspond to a real net benefit? | Celebration implies a net user outcome | Verify milestone, outcome and all costs | — | 4 / UX, frontend | (T2; C12) ethical constraint: gambling sound; (T4; D19) craft |
| R21 | Can the person stop without deception or emotional penalty? | Product/host continuation, exit or reminder route exists | Inspect actual routes and deadlines; scope host separately from file | — | 7 / UX, frontend | (T4; D9) craft for recognition; (T4; D24) ethical constraint; (T3; D10) task evidence: first-party retention |
| R22 | Is paid random-reward pressure absent? | A payment/random-benefit route exists | Inspect payment, reward odds/cost presentation and pressure | — | 7 / UX | (T1; D25) ethical constraint: harm association |
| R23 | Does the ending deliver substantive resolution? | The piece or task has an ending | Final answer, supported implication or actual completion | — | 6 / reward-design, presentation | (T1; A8) analogy; (T4; D14, D20) craft |
| R24 | Is the whole experience worthwhile before its final flourish? | Experience value is assessed | Inspect the full sequence for gaps, friction and false claims | Observe task success and ask about value across the experience | 6 / reward-design, UX | (T1; A25) analogy: remembered evaluation |
| R25 | Are enjoyment and usefulness assessed separately from continuation? | An outcome evaluation is requested or an effect is claimed | Separate measures/prompts and observation period, if supplied | Collect task success and reports of enjoyment/usefulness separately | 7 / reward-design | (T1; A2) analogy; (T4; D2) craft |
| R26 | Does a memory claim have a content-specific test at a stated delay? | Memory benefit is claimed or the brief requires it | Content prompt, answer rubric, relevant delay and participant plan | Collect recall results; score message separately from picture recognition | 7 / reward-design | (T1; A5, A6) task evidence: trivia/faces; (T3; B12, B14, B15) task evidence: graphical prediction/recognition; (T3; A23) ethical constraint: fabricated percentages |
| R27 | Do rationale and evidence avoid unsupported universal rules? | Design rationale, source claim or effect claim is supplied | Check source task, tiers, IDs and myths | — | 7 / reward-design | (T3; A21, A22, A24, D23) ethical constraint; (T4; B24) craft |

## Delivery and sound prerequisites

For R12 choose **reader-paced document**, **live slides**, **narrated deck/video** or **interactive states** before scoring timing. In a reader-paced document inspect navigation and legibility, then observe task reading time without inventing an advance deadline. Live slides need an actual advance sequence or rehearsal; video needs playback; states need a trigger/state trace. If live delivery is unknown, retain the visible density finding and leave processing-before-advance not judged. (T1; B17) (T3; B25)

For R14–R18 record: audio stream present, signal decoded, mix auditioned, stems known and listener task tested. These are separate prerequisites. LUFS (loudness units relative to full scale), waveforms and captions do not establish spoken content, intelligibility or mood. Confirm a bed by audition or production evidence before proposing its comparison; no stems may prevent a valid bed/silence comparison. Caption-derived word rates are text-window proxies, not measured spoken pace. Use actual listening/transcription when pace matters. (T3; C15, C16, C18) (T1; C22)

Record the event pair: **impact/contact**, **visible speech**, **narrated reference-to-mark**, or **musical transition-to-reveal**. Narrated chart-reference/mark alignment belongs to R07; perceived audiovisual synchrony belongs to R15. A caption/audio clock match does not establish chart-cue alignment, and a late label is not a lip-sync diagnosis. Physical offsets support a finding; they are not a universal perceptual pass threshold. See [sound.md](sound.md) and [measure-playback.md](measure-playback.md). (T1; B16, B18) (T2; C7, C8)

## Test record

Record baseline/candidate, actual reader and decision, task, delivery device, observation period, prompts, participants and acceptance condition. Keep content and conditions comparable. Separate behavior from reported feelings; a small pilot is not a population effect estimate. Derive provisional factual task questions from the reader's decision if the brief supplies none. If thresholds or participant plans are missing, leave effect acceptance pending while completing the inspection. (T1; A2) (T3; A23)

Ask about curiosity before the answer and understanding/usefulness afterward, without stating a desired response. Fulfillment of the promise comes first; exceeding expectation is optional and requires a pre-answer expectation measure with its limits. For a memory objective, agree a relevant recall delay and answer rubric before testing; without them, memory acceptance remains pending. Trivia/face-memory transfer and prediction results stay qualified. (T1; A1, A5, A6) (T3; B12, B14, B15)

An existing immutable artifact can be inspected without editable source or a renderer rerun. After a candidate exists, get its production checks, review actual playback/working states and rerun affected subchecks. A renderer pass, longer retention or a replay spike cannot substitute for meaning or audience evidence. Name remaining independent/cold review and audience gates with their coordinator; this inspection does not certify production or audience effects. (T2; C7) (T4; D2)

## Converge into a ranked handoff

Consolidate overlapping check findings into changes that repair the same cause. For example, one measured label lag may affect R07/R12/R15; one missing assessment may affect R03/R04/R08/R23. Keep the contributing IDs and locations attached rather than issuing competing fixes. (T1; B16, B17, B18) (T4; D18)

Rank the top three changes by decision risk and expected task benefit, then dependencies and effort; include any remaining essential fixes in the full list. For each change record rank, observation/cause, concrete edit, linked check IDs, one accountable production owner, dependencies, test and release implication. Separate observed repairs from requests for missing sources/tests. Ranking is reviewer inference, not measured uplift; state how an uncertain audience or delivery context could reorder it. Never use tier count as an effect estimate. (T1; A2) (T4; D7)

Hand off the ranked list and pending gates to the acceptance owner. Review changed promise/content/timing/cues after the production candidate exists; keep unknown responses pending until tested. (T2; C7) (T4; D2)

Maintainer: reward-design skill owner. Recheck applicability, evidence separation and ranked handoff in fresh-context real use; audience effects remain unproven.
