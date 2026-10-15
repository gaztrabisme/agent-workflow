---
name: domestika-course-archive
description: "Archive authorized Domestika and Coursera courses, local PDF/EPUB books, exact-version papers and selected repository commits through one private core. Emit verified portable files, a sanitized manifest and a pending knowledge-base handoff. Preserve Domestika's per-unit ZIP, native/requested captions and optional English reading-copy workflow. Use for collecting or preserving learning sources; not standalone PDF editing, general software builds, or knowledge-base indexing."
---

# Archive and ingest

One shared core preserves authorized learning sources through five adapters: Domestika, Coursera, book, paper and repository. It reconciles discovery, transfers permitted assets, hashes bytes, builds portable documents, verifies releases and emits a pending handoff. The knowledge base remains a separate consumer; this skill neither indexes nor imports models. Keep the existing skill directory/name for compatibility.

For the common workflow, read [archive-core.md](references/archive-core.md). Run `python3 scripts/archive.py run <source.json> --output <source-workdir>` with a stable logical source ID and an explicit selection. Inspect `CURRENT` to find the immutable verified release. Emit `archive-manifest/v1`, `kb-handoff/v1`, `text-chunks.jsonl`, `image-records.jsonl` and their blobs; handoff remains pending until a matching consumer receipt exists.

Locked, unsupported, unresolved and extraction-failed members stay listed. Unknown counts/dates use null with reason `not found`. Lost access or narrower selection preserves earlier evidence; only authoritative rediscovery of the same scope can tombstone members. Keep `.state/` (including its restricted transport projection) and `outbox/` outside replaceable releases. Run `bash scripts/fp/accept-archive.sh` for offline adapter, contract, reuse and crash checks.

## Domestika compatibility workflow

Creates a local ZIP of a course the user can access, retaining annotated unit PDFs, MP4s, and language-suffixed captions. `package_domestika.py` and `reading_copy.py` retain their command lines and use the shared packaging/privacy gates. The optional English copy translates the teacher's native captions, retains original transcripts and cue links, uses saved video frames and applies the versioned marketing-removal rules. The generic core's portable reading PDF is a derived layout of original text; it does not generate a translation.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, don't copy them.

## When it fires — and when a sibling owns it

- **This skill:** the user asks to preserve or organize their authorized courses, local books, exact-version papers or selected repository files into a verified private archive and pending handoff.
- **`pdf:pdf` instead:** the user wants a PDF created, inspected or repaired without collecting course media. This skill calls it for PDF rendering and visual QA.
- **`dev` instead:** the user asks for general software development, a browser automation system, or an adapter for a service outside the five supported source types.
- **`color-theory` instead:** the user asks for color theory or palette advice; a course title containing “color” does not make this an archive task.
> **Disambiguation:** use the artifact and audience — this skill produces a private course archive for the learner; `pdf` produces standalone PDF work; `dev` builds general software.

## Principles / anchoring rules

1. **Use the user's existing access.** Work only on a course page the user is signed into and can view. Fetch same-origin unit pages through that browser session. Do not extract, print, store or transmit browser cookies or account tokens.
2. **Do not defeat protection.** Use only media streams the signed-in course page exposes for playback. If a lesson is encrypted, DRM-protected, unavailable, or lacks the requested caption language, stop and report the specific gap. Do not decrypt, evade access checks, or use another account's media.
3. **Probe before the full transfer.** Confirm the course ID/title, unit and lesson totals, one playable lesson, requested audio/caption availability across selected lesson playlists, and whether streams are encrypted. Use the included `--probe-only` mode before a costly run; the packager repeats the check automatically. Tell the user the expected size or duration when it is material.
4. **Keep the files cross-referenced.** Use one stable lesson stem for the `.mp4` and language-suffixed timed captions (for example `.en.vtt` and `.es.vtt`). Preserve the requested caption language and each lesson's `DEFAULT=YES` HLS audio language; include one file when they are the same. Put an explicit video marker, every filename, the lesson link, duration, and page transcript at each video's place in the PDF.
5. **Separate transport capabilities from evidence.** The original browser collector JSON contains playback URLs and remains restricted local input. The persistent `manifest.json` is sanitized and distributable only within the owner-authorized scope. Cookies and account tokens are never exported; signed URLs stay in `.state/transport.json` or restricted compatibility input, never in releases, PDFs, reports or handoffs. Scan rendered content as well as metadata.
6. **Report only checked results.** A command finishing is not proof. Count files against the manifest, verify video/audio streams and the selected audio language tag, check timed caption cues, inspect rendered PDFs, and check ZIP integrity before saying the archive is complete.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Scope and ground | Identify the signed-in course, user's language preferences and expected output | Course ID, title and requirements |
| Collect | Read unit pages in the browser session and save restricted collection data | Restricted collector JSON; sanitized core manifest after normalization |
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

- `references/archive-core.md` — shared CLI, five adapter inputs, recovery, privacy, contracts and handoff.
- `references/operations.md` — requirements, commands, output layout, and known limits for the included tools.
- `references/reading-copy.md` — the per-unit agent loop, `lesson.md` format and writing rules for the reading copy.
- `references/audit-loop.md` — independent audit of every lesson instead of owner review: roles, severity, rounds, what a blocked lesson may still be used for.
- `EVOLUTION.md` — authoring trace, dogfood findings and unsettled hypotheses.
