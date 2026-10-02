# Claim audit

Writer: codex
Auditor: glm
Round: 1

Scope: `references/method/select-keepers.md` — 15 citations (4 claims; 7 unique anchors). The two source-lesson links and the unit link in that file carry no time-range anchor and are not claim citations; they are not counted.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/select-keepers.md | 227 · U4 · L11 · 00:08–01:38 | Instagram course marks favorites before editing; edits one image per shot type | supported | Section: mark with the heart the one you like most from each kind of shot, then edit those from Favorites. |
| 2 | references/method/select-keepers.md | 669 · U4 · L10 · 15:06–17:56 | Portrait course exports edited photos, then decides keepers and repeats | supported | Section: "That's the editing of the photos we took earlier. Now we export them and decide which ones we keep... and which are repeated without adding anything." |
| 3 | references/method/select-keepers.md | 669 · U4 · L11 · 00:00–03:14 | Portrait course compares exports by space and lets images cool off | supported | 216 exported, already edited; chooses per space, very different perspectives; images must "cool off" a few days before returning. |
| 4 | references/method/select-keepers.md | 669 · U4 · L11 · 03:14–06:44 | Portrait course compares candidates set by set; look through all, then revisit | supported | Works through glass, reflected-light, CD and balcony sets in turn; "look all the way through the photos and then go back to see which ones you left out". |
| 5 | references/method/select-keepers.md | 669 · U4 · L11 · 08:22–12:37 | Selection at least a day after editing; compares set by set | supported | Section: furniture/floor/table sets in turn; "important to make this selection at least a day after editing the photos". |
| 6 | references/method/select-keepers.md | 669 · U4 · L11 · 12:37–15:44 | 63 kept; reduce to ten favorites after letting photos rest | supported | Section: 63 selected; "we need to digest the photos, forget about them, and let them surprise us" before narrowing to ten. |
| 7 | references/method/select-keepers.md | 227 · U4 · L11 · 00:08–01:38 | Derived: mark promising frames before detailed retouch; reject misses first | supported | Labelled derived. Anchor grounds the "mark promising frames before retouch" half (mark favorites before editing). "Reject technical misses" is the writer's own step, covered by the label; no cited section states it. |
| 8 | references/method/select-keepers.md | 669 · U4 · L11 · 08:22–12:37 | Derived: after base edits, compare finalists again and let them rest | supported | Labelled derived. Section compares near-duplicates after editing and advises selecting a day or more later. |
| 9 | references/method/select-keepers.md | 669 · U4 · L11 · 12:37–15:44 | Derived: rest before a consequential final selection | supported | Labelled derived. Section: narrowing 63 to ten "can't be done all at once"; digest, forget, let them surprise you. |
| 10 | references/method/select-keepers.md | 669 · U4 · L11 · 00:00–03:14 | Compare near-duplicates by expression, gaze, gesture, detail, focus, background, viewpoint value | overstated | Section compares smoke clarity, eye definition and very different perspectives per space; it never mentions judging focus. The "focus" axis is the writer's addition (focus rejection appears only in uncited 669 · U4 · L10 · 12:22–13:56, about editing, not comparing keepers). |
| 11 | references/method/select-keepers.md | 669 · U4 · L11 · 03:14–06:44 | Compare near-duplicates by expression, gaze, gesture, detail, focus, background, viewpoint value | overstated | Section compares centeredness, shoulder/head position, gaze, face angle and a sweeter gesture; no mention of judging focus. |
| 12 | references/method/select-keepers.md | 669 · U4 · L11 · 06:44–08:22 | Compare near-duplicates by expression, gaze, gesture, detail, focus, background, viewpoint value | overstated | Section compares diffusion, looking at camera, and gestures still in progress; no mention of judging focus. |
| 13 | references/method/select-keepers.md | 669 · U4 · L11 · 08:22–12:37 | Compare near-duplicates by expression, gaze, gesture, detail, focus, background, viewpoint value | overstated | Section compares the door covering more or less of the frame, hand and shoulder details, and expression; no mention of judging focus. (Background and detail are the only grounds for those axes.) |
| 14 | references/method/select-keepers.md | 669 · U4 · L11 · 00:00–03:14 | T3: selections serve the set; 216-to-63-to-fewer is example, not quota | supported | Section frames ~80/216 as this session's aim ("about 80, or a little fewer"), best photos from each space — a demonstration, not a rule. |
| 15 | references/method/select-keepers.md | 669 · U4 · L11 · 12:37–15:44 | T3: selections serve the set; 216-to-63-to-fewer is example, not quota | supported | Section counts 63, then narrows toward ten favorites by returning to the photos "each time we... use them for something" — no general quota. |

## Check before moving on

- Rows 10–13 fail as a group for one reason: the instruction sentence adds **focus** as a comparison axis, and none of the four cited sections mentions judging focus. The second sentence of the same claim (smoke clarity, eye definition, hand and shoulder placement, gesture still developing) is fully supported by these sections; dropping "focus" — or anchoring it and the label "derived" — would clear all four rows.
- Citations not reached: none — all 15 in scope were checked.

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' .../SKILL.md .../references/method
(no output)
grep exit: 1
```

No matches; nothing in scope ties the skill to another skill's names or to specific tool/subagent machinery.
