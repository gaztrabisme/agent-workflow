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

### Hypotheses applied
1. **`SKILL.md` and `references/operations.md`** define an entitlement boundary, a no-DRM stop condition, a full-playlist preflight, filename matching and artifact checks — closes pattern 3 and documents the existing access condition.
2. **`scripts/`** carry the collector and packager with the skill — the reproducing toolchain stays with the instructions.
3. **`SKILL.md`** separates course archiving from PDF-only, general software and color-advice tasks — closes trigger ambiguity.

Not modified (validated as already-sound): per-unit folders, captions sharing video stems, transcript-bearing PDFs, and resumable work directory.

### Validation results (settled by a later run's step 0)
- [ ] Fresh-context dogfood uses this skill to create and inspect a real unit archive; fold ranked findings into this entry.
- [ ] A later independent course run exercises generic course selection and the output checks without new friction.
- **Verdict: PENDING** — two real archive runs grounded the skill, but the newly written instructions still need fresh-context dogfood and another independent use to validate their discoverability and scope.
