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
- [ ] A later independent course run exercises generic course selection and the output checks without new friction.
- **Verdict: PENDING** — three cold runs exercised the skill and the third passed all artifact gates. The metadata convention note from that run is fixed; one later independent course run is still required to validate discoverability and scope.
