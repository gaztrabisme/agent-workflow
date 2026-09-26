# Evolution Log — domestika-course-archive

The loop that turns real uses into skill improvements. Mechanism: `../evolution/references/loop.md`. Harvest source: real signed-in course archive runs, PDF render reviews, and fresh-context dogfood.

---

## Evolution 1 — 2026-09-26 — Birth and first dogfood

### Harvest scope
- Authored from hands-on runs on two accessible Domestika courses: Logo Design: From Concept to Presentation (5 units, 16 lessons) and Color Theory: How to Apply It to Your Images (4 units, 18 lessons). Both produced complete ZIPs with per-unit PDFs, MP4s and VTT captions. A fresh-context dogfood on a third real task is pending below. Classify: authored from real practice, not distilled from a course-export method.
- Grounded: core and skill-builder authoring guidance plus the two courses' signed-in unit pages and HLS playlist metadata → collect unit metadata through the logged-in page, probe every playlist for requested audio/captions and encryption, and verify the archive artifact before claiming completion.

### Patterns found
1. **The course ID cannot be hardcoded.** Impact: H, Effort: L. The first tool launcher only handled course 1049; a second course exposed that limitation and led to selecting the newest manifest or accepting an explicit path.
2. **PDF usefulness depends on the video marker and file pair.** Impact: H, Effort: M. Visual review showed that marker placement, exact MP4/VTT stems and surrounding transcripts let the PDF cross-reference the archive.
3. **Bulk success depends on playlist metadata, not one sample alone.** Impact: H, Effort: M. A probe of all 18 playlists confirmed the requested English tracks and unencrypted HLS before downloading a 1.3 GB archive.
4. **The preflight needs a repeatable operator path.** Impact: H, Effort: M. The cold dogfood had to write a one-off `yt-dlp` probe because the skill described the gate but did not give a command or built-in mode.
5. **Resume must respect requested settings.** Impact: M, Effort: M. The dogfood found the earlier code could reuse a valid-length video without proving its resolution or chosen language matched the current run.
6. **Completion needs an artifact-level ZIP gate.** Impact: H, Effort: L. The dogfood had to run a separate CRC and member-set check because the packager printed “Complete” immediately after writing.
7. **The prerequisite error referenced a missing README.** Impact: L, Effort: L. A failure message would have pointed to a file outside the skill.
8. **The selected audio language was not recorded in the MP4.** Impact: M, Effort: L. The second dogfood selected English but ffprobe reported the audio stream tag as `und`, so libraries and players could not identify its language.
9. **A task heading could be orphaned at a page boundary.** Impact: L, Effort: L. Visual review found the “Redesign a Logo” heading at the foot of one page while its instructions started on the next.
10. **The PDF metadata title used an em dash.** Impact: L, Effort: L. The PDF skill's metadata convention uses ASCII hyphens; the visible page was unaffected.

### Hypotheses applied
1. **`SKILL.md` and `references/operations.md`** define an entitlement boundary, a no-DRM stop condition, a full-playlist preflight, filename matching and artifact checks — closes pattern 3 and documents the existing access condition.
2. **`scripts/`** carry the collector and packager with the skill — the reproducing toolchain stays with the instructions.
3. **`SKILL.md`** separates course archiving from PDF-only, general software and color-advice tasks — closes trigger ambiguity.
4. **`scripts/package_domestika.py` adds `--probe-only` and runs preflight before every package.** It checks the exact selected video/audio formats, requested caption track and DRM indicators without printing media URLs — closes pattern 4.
5. **The packager records the requested language/height settings beside each work video and only reuses matching verified files.** It checks actual video height — closes pattern 5.
6. **The ZIP builder checks expected members and CRC before replacing the destination or printing completion.** It also updates the missing-prerequisite hint to `references/operations.md` — closes patterns 6 and 7.
7. **The packager writes and verifies the selected audio language tag** using an ISO 639-2 mapping and refuses reuse when the tag is wrong — closes pattern 8.
8. **The PDF print CSS keeps list items together across pages.** A rendered Unit 1 copy confirmed the final task heading and instructions now start together — closes pattern 9.
9. **The PDF document title now uses an ASCII hyphen** to follow the PDF skill's metadata convention — closes pattern 10.

Not modified (validated as already-sound): per-unit folders, captions sharing video stems, transcript-bearing PDFs, and resumable work directory.

### Validation results (settled by a later run's step 0)
- [x] Fresh-context dogfood used this skill on Unit 1 of course 1049: 3 MP4/VTT pairs, a 3-page annotated PDF, all-page visual review, and ZIP member-set/CRC checks passed. Its four findings were folded above.
- [x] Second fresh-context dogfood exercised the probe, settings-aware resume, ZIP membership/CRC, media, captions and PDF. It passed, and surfaced the missing MP4 language tag and an orphaned task heading; both fixes were added.
- [x] Third fresh-context dogfood passed on a clean Unit 1 archive: all 3 MP4/VTT pairs, `eng` audio tags, exact ZIP membership/CRC, PDF text markers, and visual page review succeeded. It surfaced the PDF metadata dash convention, corrected afterward.
- [x] A later independent course run exercised generic course selection and the output checks without new friction (the course 1140 archive and course 1049 English-default check below).
- **Verdict: SETTLED** — three cold runs passed the original artifact gates, and subsequent runs validated generic course selection and language-specific caption naming. Keep using the gates when page/player structures change.

## Evolution 2 — 2026-09-26 — Preserve captions for default audio

### Harvest scope
- Follow-up request on a real archive: keep English captions and also retrieve captions in the language of the lesson's default/original audio. Course 1140 exposes Spanish `DEFAULT=YES` audio while English audio is selectable; course 1049 exposes English as its default. Playback URLs remain private.
- Evidence from course 1140: all 18 lesson playlists expose English and Spanish captions; a complete archive contains 18 `.en.vtt` and 18 `.es.vtt` files, and every PDF video marker names both. All VTTs have cues and the ZIP CRC/member-set checks passed.
- Evidence from course 1049 Unit 1: the three playlist preflights report English as both requested and default caption language; the ZIP contains one `.en.vtt` per lesson, no duplicate captions, all files have timed cues, and CRC/member checks passed.

### Pattern found
1. **One caption language misses original-language speech on dubbed courses.** Impact: H; Effort: M. Selecting English audio/captions alone omitted the Spanish text track matching the course's default Spanish audio.

### Hypothesis applied
1. **`package_domestika.py` reads the HLS master playlist's `DEFAULT=YES` audio language for each lesson and requires captions for that track plus the requested caption language.** Matching languages deduplicate; saved VTTs carry language suffixes; unit PDFs list every suffix. If the playlist has no default audio track, the selected audio language is used as fallback. Missing/ambiguous/invalid default language tags or unavailable captions stop preflight with a clear error.

### Validation results
- [x] Spanish-default course 1140 completed end-to-end: 4 PDFs, 18 MP4s, 18 English VTTs and 18 Spanish VTTs; every PDF rendered and visually inspected; stream/audio tags, caption cues, exact members, and ZIP CRC passed.
- [x] English-default course 1049 Unit 1: 1 PDF, 3 MP4s, 3 English VTTs, no duplicates; preflight, cues, exact membership, and ZIP CRC passed.
- **Verdict: REVISED** — the default-language caption rule is supported by an end-to-end Spanish-default archive and an English-default deduplication run. Retain the behavior and monitor for playlist formats that omit or mislabel `DEFAULT=YES`.

## Evolution 3 — 2026-09-26 — English reading copy from native captions and video frames

### Harvest scope
- Request: turn an archived course into one English PDF that replaces watching it, written from the teacher's native captions with frames cut where material is shown, learning content only, for use as source material when building skills. Marketing removal must be a mechanical rule set, not agent judgement.
- Real run: course 1140 (4 units, 18 lessons, 3 h 52 min, Spanish speaker), from its existing archive and work directory. 17 fresh-context subagents each wrote one lesson from `references/reading-copy.md`; one more re-applied the figure density rule to Unit 2. They acted as the dogfood: each reported where the instructions were unclear.
- Grounded: core and skill-builder guidance, the existing packager/PDF code (reused `basename`, `tidy`, `validate_manifest`, `caption_path`, `inspect_captions`, `render_pdf`, `safe_fragment`), and the real unit HTML of course 1140 for the cleaning rules.

### Patterns found
1. **Domestika's English captions are not a faithful translation.** Impact: H. Every lesson had passages where the English reverses or invents meaning: "arrastrándoles colores" (stripping colour) became "adding colors"; the Photoshop path Filter > Noise > Dust & Scratches became a vague sentence; lines such as "red can also represent warmth, love, or joy" have no Spanish source.
2. **The native captions carry speech-recognition errors,** mostly proper nouns and homophones ("oler la banda" for "la lavanda", nine misspelt artist names in lesson 2). On-screen title cards resolve most of them.
3. **Unit page text is mostly clean; the marketing is concentrated** in a "Follow me!" resource, social "present yourself"/"course board" tasks and per-task "Share on the forum" links. The spoken plugs ("see my other courses on Domestika", "the great Domestika community") surfaced only in the translated prose, and the first rule set missed them.
4. **Sentence-level removal can take teaching with it** when a plug shares a sentence with content ("Yes, we can, as long as…; for that, I invite you to see my courses").
5. **Contact sheets make frame choice cheap and complete;** slides that build up produced runs of near-identical figures until a density rule was added (Unit 2: 104 → 94).
6. **Instruction gaps reported by subagents:** unused frames, text cut off at the frame edge, caption and teacher slips, figures near section boundaries, interface-heavy screens, repeated taglines, signatures and watermarks, promotional screens, transcript truncation in tool output.

### Hypotheses applied
1. **`scripts/reading_copy.py`** (`prepare`, `frames`, `check`, `status`, `clean`, `build`) does the mechanical work; the agent only chooses frames, translates and writes captions. `check` gates every lesson on time ranges, coverage, frame references, caption lines and a 35% prose-length floor.
2. **`scripts/package_domestika.py` records each lesson's `default_language`;** older work directories fall back to the last `caption_languages` entry.
3. **Marketing removal is data** in `scripts/marketing_rules.json`, applied to manifest HTML (item headings, calls to action, link unwrapping), lesson titles (intro lessons) and prose (sentence, then clause). Every removal goes to `removed.log`. Closes patterns 3 and 4.
4. **`references/reading-copy.md`** holds the loop, the `lesson.md` format, the density rule and the caption conventions. Closes patterns 1, 2, 5 and 6.
5. **Operations verify step** now requires scanning the prose for plugs the rules missed and extending the rules. Closes the gap in pattern 3.

### Validation results
- [x] 17 unit tests pass (caption merging, native-language choice, `check` pass and fail cases, cleaning, clause-level removal, empty sections).
- [x] Course 1140: `check` passes for all 17 included lessons (lesson 1 excluded by the intro rule); the PDF has 299 pages and 432 figures, equal to the figure blocks written; every lesson anchor is in the text; no rule pattern matches the text; `removed.log` (21 entries) was read in full and holds no teaching content; sample pages were inspected visually; the ZIP gained exactly the PDF (59 members) and passed CRC.
- [x] English prose length is 0.99–1.13× the Spanish transcript's word count per Unit 2 lesson, so the copy is a translation, not a summary.
- [x] Gary reviewed the full PDF and approved it (2026-09-26).
- [x] `export` added (2026-09-26): the same cleaned content as Markdown plus renamed frames, for distilling skills. Course 1140 exported 17 lessons, 4 unit files and 432 frames; first consumer is the `color-theory` skill. The export also runs sentence-level cleaning over the unit tasks, which caught forum and peer-feedback prompts that element-level rules had to leave inside task paragraphs (12 more removals, 33 total, all read). Four `prose_cta` rules were added (`forum`, `receive comments/feedback`, `share it with your colleagues`, `do not be upset if I`), and clauses now also split before ", you can also". The PDF build still cleans unit HTML at element level only, so its tasks keep those prompts.
- [ ] A second course, ideally one with English native audio and one with dense screen recordings, run under the updated instructions.
- **Verdict: PENDING** — one real course end to end, approved on review; settle after a second course.
