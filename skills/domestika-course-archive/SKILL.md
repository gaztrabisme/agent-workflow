---
name: domestika-course-archive
description: "Builds a personal ZIP archive of an accessible Domestika course, with per-unit annotated PDFs, lesson videos and timed captions. USE WHEN the user asks to archive or export their own purchased Domestika course. Not `pdf` for PDF-only work or `dev` for general software builds; `color-expert` owns color advice, not course packaging. Keywords: Domestika course download, archive, offline course, MP4, VTT, lesson PDF, subtitles."
---

# Domestika Course Archive

Creates a local ZIP archive of a Domestika course the user can access. Each unit folder contains a readable PDF of the unit page with a marker at each video position, the corresponding MP4, and timed VTT captions. The skill includes the browser collector and local packager so the work can be repeated without rebuilding the tools.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## When it fires — and when a sibling owns it

- **This skill:** the user asks to preserve or organize their own Domestika course pages, lessons and timed captions into a unit-by-unit local archive.
- **`pdf:pdf` instead:** the user wants a PDF created, inspected or repaired without collecting course media. This skill calls it for PDF rendering and visual QA.
- **`dev` instead:** the user asks for general software development, a browser automation system, or a downloader for another service.
- **`color-expert` instead:** the user asks for color theory or palette advice; a course title containing “color” does not make this an archive task.
> **Disambiguation:** use the artifact and audience — this skill produces a private course archive for the learner; `pdf` produces standalone PDF work; `dev` builds general software.

## Principles / anchoring rules

1. **Use the user's existing access.** Work only on a course page the user is signed into and can view. Fetch same-origin unit pages through that browser session. Do not extract, print, store or transmit browser cookies or account tokens.
2. **Do not defeat protection.** Use only media streams the signed-in course page exposes for playback. If a lesson is encrypted, DRM-protected, unavailable, or lacks the requested caption language, stop and report the specific gap. Do not decrypt, evade access checks, or use another account's media.
3. **Probe before the full transfer.** Confirm the course ID/title, unit and lesson totals, one playable lesson, audio/caption language availability across the lesson playlists, and whether streams are encrypted. Tell the user the expected size or duration when it is material.
4. **Keep the files cross-referenced.** Use the same stable lesson stem for `.mp4` and `.vtt`. Put an explicit video marker, filename pair, lesson link, duration, and the page transcript at each video's place in the PDF.
5. **Protect the manifest.** It contains playback URLs. Keep it local, never include it in the archive or a public bundle, and do not paste its contents into chat. Retain it privately when needed for a resumable run.
6. **Report only checked results.** A command finishing is not proof. Count files against the manifest, verify video/audio streams and timed caption cues, inspect rendered PDFs, and check ZIP integrity before saying the archive is complete.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Scope and ground | Identify the signed-in course, user's language preferences and expected output | Course ID, title and requirements |
| Collect | Read unit pages in the browser session and save sanitized metadata | Private local JSON manifest |
| Probe | Check playlist accessibility, requested audio/caption tracks and encryption before bulk transfer | Go/no-go evidence and size estimate |
| Package | Render one annotated PDF per unit, save each lesson as MP4/VTT, assemble ZIP | Course ZIP with one folder per unit |
| Verify | Match PDFs, videos and captions to the manifest; inspect PDF pages and archive integrity | Verified counts and final output path |

## Gates (declared, inherited from core)

- **Grounding gate** — use the currently signed-in course pages, their lesson metadata, and actual playlist metadata as the substrate. Record what was checked and any missing language/stream. See `../core/references/grounding-gate.md`.
- **Output Contract** — completion requires the ZIP itself, one PDF per unit, one MP4 and one matching VTT per lesson, correct manifest counts, visually inspected PDFs, and a successful ZIP CRC check. Keep the generator in this skill. See `../core/references/wiki-protocol.md`.
- **Pushback & teach** — explain material size, time, language, or access limits before choosing a different quality or track. See `../core/references/pushback-and-teach.md`.
- **Approach declaration** — state `probe-first` for a new course or changed page/player structure; use `direct` for a known course and unchanged workflow. For single-actor packaging, parallel agents are optional.

## Anti-patterns (hard no-list)

- Do not archive a course the user cannot access or infer that purchase of one course grants access to another.
- Do not crawl unrelated account pages, download other members' projects, or use the manifest as a public data source.
- Do not bypass DRM, extract decryption keys, work around access checks, or silently switch to a lower quality, different language or missing captions.
- Do not claim the full archive is done when only PDFs, one unit, or a sample lesson exists.
- Do not put media URLs, cookies, or the private manifest in the ZIP or final response.
- Do not silently omit lesson pages, transcripts, caption files or unit folders when counts differ.

## Composition

- **Inherits:** `core`.
- **Consumes / hands off to:** `pdf:pdf` for PDF-specific rendering and visual quality; `dev` for changes to the code or for general software beyond this course workflow; `color-expert` for color subject matter rather than archiving.
- **Included tools:** `scripts/collect_domestika.js` collects signed-in page metadata; `scripts/package_domestika.py` renders PDFs, downloads media/captions, and assembles the ZIP; `scripts/pdf_layout.py` produces the annotated reading copies.

## References

- `references/operations.md` — requirements, commands, output layout, and known limits for the included tools.
- `EVOLUTION.md` — authoring trace, dogfood findings and unsettled hypotheses.
