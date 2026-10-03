---
name: domestika-course-archive
description: "Builds a personal ZIP archive of an accessible Domestika course, with per-unit annotated PDFs, lesson videos and timed captions, plus an English reading copy (one PDF translated from the teacher's own-language captions, with frames cut from the videos, marketing removed) that replaces watching the course. USE WHEN the user asks to archive or export their own purchased Domestika course, or to turn an archived course into reading or reference material for building skills. Not `pdf` for PDF-only work or `dev` for general software builds; `color-theory` owns color advice, not course packaging. Keywords: Domestika course download, archive, offline course, MP4, VTT, lesson PDF, subtitles, reading copy, transcript, translate captions, video frames, course notes."
---

# Domestika Course Archive

Creates a local ZIP archive of a Domestika course the user can access. Each unit folder contains a readable PDF of the unit page with a marker at each video position, the corresponding MP4, and timed VTT captions. An optional second phase turns the archive into one English reading copy: prose translated from the teacher's native captions, frames cut from the video where material is shown, and the unit tasks and resources with marketing removed by rule. It is written as source material for building skills and for reference. The skill includes the browser collector, local packager and reading-copy tool so the work can be repeated without rebuilding the tools.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## When it fires — and when a sibling owns it

- **This skill:** the user asks to preserve or organize their own Domestika course pages, lessons and timed captions into a unit-by-unit local archive.
- **`pdf:pdf` instead:** the user wants a PDF created, inspected or repaired without collecting course media. This skill calls it for PDF rendering and visual QA.
- **`dev` instead:** the user asks for general software development, a browser automation system, or a downloader for another service.
- **`color-theory` instead:** the user asks for color theory or palette advice; a course title containing “color” does not make this an archive task.
> **Disambiguation:** use the artifact and audience — this skill produces a private course archive for the learner; `pdf` produces standalone PDF work; `dev` builds general software.

## Principles / anchoring rules

1. **Use the user's existing access.** Work only on a course page the user is signed into and can view. Fetch same-origin unit pages through that browser session. Do not extract, print, store or transmit browser cookies or account tokens.
2. **Do not defeat protection.** Use only media streams the signed-in course page exposes for playback. If a lesson is encrypted, DRM-protected, unavailable, or lacks the requested caption language, stop and report the specific gap. Do not decrypt, evade access checks, or use another account's media.
3. **Probe before the full transfer.** Confirm the course ID/title, unit and lesson totals, one playable lesson, requested audio/caption availability across selected lesson playlists, and whether streams are encrypted. Use the included `--probe-only` mode before a costly run; the packager repeats the check automatically. Tell the user the expected size or duration when it is material.
4. **Keep the files cross-referenced.** Use one stable lesson stem for the `.mp4` and language-suffixed timed captions (for example `.en.vtt` and `.es.vtt`). Preserve the requested caption language and each lesson's `DEFAULT=YES` HLS audio language; include one file when they are the same. Put an explicit video marker, every filename, the lesson link, duration, and page transcript at each video's place in the PDF.
5. **Protect the manifest.** It contains playback URLs. Keep it local, never include it in the archive or a public bundle, and do not paste its contents into chat. Retain it privately when needed for a resumable run.
6. **Report only checked results.** A command finishing is not proof. Count files against the manifest, verify video/audio streams and the selected audio language tag, check timed caption cues, inspect rendered PDFs, and check ZIP integrity before saying the archive is complete.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Scope and ground | Identify the signed-in course, user's language preferences and expected output | Course ID, title and requirements |
| Collect | Read unit pages in the browser session and save sanitized metadata | Private local JSON manifest |
| Probe | Check playlist accessibility, requested audio/caption tracks and encryption before bulk transfer | Go/no-go evidence and size estimate |
| Package | Render one annotated PDF per unit, save each lesson as MP4/VTT, assemble ZIP | Course ZIP with one folder per unit |
| Verify | Match PDFs, videos and captions to the manifest; inspect PDF pages and archive integrity | Verified counts and final output path |
| Reading copy (optional) | Per unit: transcripts and candidate frames by script; frame choice, translation and captions by the agent; `check` per lesson; marketing removed by rule | One English course PDF beside the ZIP and in its root; `removed.log` |

## Gates (declared, inherited from core)

- **Grounding gate** — use the currently signed-in course pages, their lesson metadata, and `yt-dlp`'s selected playlist metadata as the substrate. Record the selected audio/caption languages and any missing or protected stream. See `../core/references/grounding-gate.md`.
- **Output Contract** — completion requires the ZIP itself, one PDF per selected unit, one MP4 and captions for the requested language plus the default audio language for every selected lesson (deduplicated when identical), exact manifest membership, visually inspected PDFs, correct audio stream and language metadata, and successful CRC validation. When a reading copy is requested, completion also requires `reading_copy.py check` passing for every included lesson, the anchor of every included lesson in the PDF text, a full read of `removed.log`, visually inspected sample pages, and the ZIP member/CRC check after the PDF is added. Keep the generators in this skill. See `../core/references/wiki-protocol.md`.
- **Pushback & teach** — explain material size, time, language, or access limits before choosing a different quality or track. See `../core/references/pushback-and-teach.md`.
- **Approach declaration** — state `probe-first` for a new course or changed page/player structure; use `direct` for a known course and unchanged workflow. For single-actor packaging, parallel agents are optional.

## Anti-patterns (hard no-list)

- Do not archive a course the user cannot access or infer that purchase of one course grants access to another.
- Do not crawl unrelated account pages, download other members' projects, or use the manifest as a public data source.
- Do not bypass DRM, extract decryption keys, work around access checks, or silently switch to a lower quality, different language or missing captions.
- Do not claim the full archive is done when only PDFs, one unit, or a sample lesson exists.
- Do not put media URLs, cookies, or the private manifest in the ZIP or final response.
- Do not silently omit lesson pages, transcripts, caption files or unit folders when counts differ.
- Do not write reading-copy prose from Domestika's English captions when native captions exist, summarize outside `Key points (derived)`, or hand-edit marketing out; extend `scripts/marketing_rules.json` instead.

## Composition

- **Inherits:** `core`.
- **Consumes / hands off to:** `pdf:pdf` for PDF-specific rendering and visual quality; `dev` for changes to the code or for general software beyond this course workflow; `color-theory` for color subject matter rather than archiving; `skill-builder` when a reading copy is distilled into a skill: run `reading_copy.py export --pdf`, then follow `../skill-builder/references/distill-course.md`.
- **Included tools:** `scripts/collect_domestika.js` collects signed-in page metadata; `scripts/package_domestika.py` renders PDFs, downloads media/captions, and assembles the ZIP; `scripts/pdf_layout.py` produces the annotated unit PDFs; `scripts/reading_copy.py` (with rules in `scripts/marketing_rules.json`) prepares, checks, cleans, builds and exports the English reading copy.

## References

- `references/operations.md` — requirements, commands, output layout, and known limits for the included tools.
- `references/reading-copy.md` — the per-unit agent loop, `lesson.md` format and writing rules for the reading copy.
- `references/audit-loop.md` — independent audit of every lesson instead of owner review: roles, severity, rounds, what a blocked lesson may still be used for.
- `EVOLUTION.md` — authoring trace, dogfood findings and unsettled hypotheses.
