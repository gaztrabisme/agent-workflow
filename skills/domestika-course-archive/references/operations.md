# Operating the Domestika course archiver

## Requirements

- A Domestika account currently signed in to the course in Zen or another supported browser.
- Python 3, Google Chrome, `yt-dlp`, `ffmpeg` and `ffprobe` on the local Mac.
- The user must have access to the course and enough disk space for the working files and ZIP. 1080p media can be large.

The packager currently looks for Chrome at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. If the browser or operating system differs, update the `CHROME` path in `scripts/package_domestika.py` after confirming the executable.

## Collect the course manifest

1. Open a unit page for the intended course while signed in.
2. Run `scripts/collect_domestika.js` in that page's developer console.
3. Confirm the collector reports the expected number of units and lessons. It saves `domestika-course-<course-id>-manifest.json` in Downloads.
4. Keep the manifest private: it contains lesson playback URLs.

The collector uses the course's visible unit links and same-origin page requests. It does not read cookies directly. It expects the current Domestika unit-page markup and the page's embedded lesson metadata; if those change, stop and inspect the new structure rather than guessing.

## Probe before packaging

- Compare unit and lesson counts with the manifest and course page.
- Confirm the requested audio and caption tracks exist for every lesson playlist, including the caption track that matches the HLS `DEFAULT=YES` audio language.
- Check playlists for encryption indicators. If protected, stop; this tool does not handle DRM.
- Download one short lesson and confirm the MP4 has audio and video and the VTT has timed cues.
- Estimate disk space from a representative video or playlist metadata when practical.

The current packager selects English audio and English timed captions by default. For every lesson, it also reads the HLS master playlist's `DEFAULT=YES` audio language and includes that caption track. If it differs from the requested caption language, both are saved; if it matches, only one file is saved. For example, English captions plus a Spanish default audio track produce `.en.vtt` and `.es.vtt` beside the video. If the playlist has no default audio track, the selected `--audio-language` is used as the caption fallback. If any required caption is unavailable or has an unusable language tag, stop and report the gap rather than silently substituting another language. Audio selection accepts the ISO 639-1 codes listed in `LANGUAGE_TAGS` near the top of `scripts/package_domestika.py`; an optional region suffix such as `_la` is used for track selection. The packager writes and verifies the corresponding ISO 639-2 language tag in the MP4 audio stream.

The packager offers a repeatable preflight. It uses `yt-dlp` metadata with the exact requested video/audio selector, verifies an eligible video height and audio language, reads each HLS master playlist's default audio language, checks for both required caption tracks, and stops if selected media is marked protected. It suppresses raw playlist URLs.

```sh
python3 scripts/package_domestika.py /path/to/domestika-course-<id>-manifest.json \
  --probe-only --unit 1 --max-height 720 \
  --audio-language en --caption-language en
```

Omit `--unit 1` to check every unit. A normal packaging run repeats the preflight automatically before rendering PDFs or downloading media. The preflight confirms that each required subtitle track is listed; the downloaded VTT files are subsequently checked for timed cues. Existing valid videos can be reused while only newly required caption files are downloaded.

## Package

```sh
python3 scripts/package_domestika.py /path/to/domestika-course-<id>-manifest.json \
  --output /path/to/domestika-course-<id>.zip
```

Options:

- `--max-height 720` lowers the video resolution limit; the default is 1080p.
- `--audio-language en` selects the audio language; the default is English.
- `--caption-language en` selects the VTT caption language; the default is English.
- `--unit 1` packages one unit as a focused run; repeat `--unit N` to choose several.
- `--workdir PATH` selects where resumable working files are stored. The default is a `.work` directory beside the ZIP.

The packager checks every video for exactly one video and audio stream, requested height, plausible duration, and the correct MP4 audio language tag. It checks VTT structure and timed cues, renders each PDF, then checks exact ZIP membership and CRC before replacing the destination ZIP. It keeps a private settings note beside each work video, reuses a valid video when its height and audio language match, and downloads only missing captions when possible. It stops on missing requested media or captions and leaves working files so the user can resume after addressing the issue.

## Output layout

```text
domestika-course-<id>.zip
├── Unit 01 - <title>/
│   ├── Unit 01 - <title>.pdf
│   ├── 01-<lesson>.mp4
│   ├── 01-<lesson>.en.vtt
│   ├── 01-<lesson>.es.vtt  # when the default audio language is Spanish
│   └── ...
└── Unit 02 - <title>/
    └── ...
```

Each PDF preserves the unit introduction, lesson order and transcripts, tasks and linked resources. A clearly marked placeholder at each video position names the MP4 and every language-suffixed VTT, and links to the lesson page. It is a readable annotated copy, not a pixel-perfect print of the live webpage. Extra downloadable course attachments are linked in the PDF but are not added to the ZIP unless the user asks.

## Verify before delivery

- Confirm the ZIP contains exactly one unit folder and PDF per selected unit.
- Confirm there is exactly one MP4 and one VTT per required caption language for every included lesson; verify the names are `<lesson-stem>.<language>.vtt` and that the PDF marker lists every one.
- Compare counts to the selected manifest units; a partial `--unit` run is not a complete-course archive.
- Check `pdfinfo` page counts and `pdftotext` marker/filename matches; render and visually inspect PDFs with the `pdf:pdf` skill.
- The packager runs exact member-set and `ZipFile.testzip()` CRC checks before reporting completion; if inspecting a ZIP made elsewhere, run the same checks.
- Report the actual archive path, size, unit/lesson/file counts, selected audio/caption languages, and any limits. Keep playback URLs out of the report.

## Known limits

- The collector depends on current Domestika page paths and embedded `__INITIAL_PROPS__` metadata. Site changes can break it; fail clearly.
- The included packager targets HLS playlists on `cdn-videos.domestika.org`, language tracks exposed by `yt-dlp`, and Chrome on macOS. English audio and requested captions are the defaults; captions also include each lesson's HLS default audio language. Pass other language codes only when the course exposes those tracks and the audio code is supported by `LANGUAGE_TAGS`.
- The tool archives unit lessons, not a separate final project page or unrelated course resources.
- Do not attempt alternate endpoints, credentials, decryption, or access workarounds if the expected page data is unavailable.

## Reading copy

An optional phase after packaging. It turns the archive into one English PDF that replaces watching the course: prose translated from the teacher's native captions, frames cut from the videos where material is shown, and the unit tasks and resources with marketing removed by the rules in `scripts/marketing_rules.json`. The agent loop and writing rules are in `references/reading-copy.md`.

Requirements beyond packaging: Python packages `markdown` and `Pillow`, and the packager's work directory (the reading copy reads the MP4s and VTTs there, not the ZIP).

```sh
python3 scripts/reading_copy.py prepare  <manifest> --workdir <workdir> [--unit N]
python3 scripts/reading_copy.py frames   <workdir>/reading/UNN/LNN --at mm:ss [--at ...]
python3 scripts/reading_copy.py check    <manifest> --workdir <workdir> [--unit N] [--lesson N]
python3 scripts/reading_copy.py status   <manifest> --workdir <workdir>
python3 scripts/reading_copy.py clean    <manifest> --workdir <workdir>
python3 scripts/reading_copy.py build    <manifest> --workdir <workdir> --output <pdf> [--unit N] [--zip <zip>] [--teacher "<name>"]
python3 scripts/reading_copy.py export   <manifest> --workdir <workdir> --out <dir> [--unit N] [--pdf <reading copy pdf>]
```

- `prepare` picks each lesson's native caption language from `default_language` in the packager's `<lesson>.download.json`. Work directories made before that field existed fall back to the last entry of `caption_languages`, which the packager always writes as (requested, default). It writes `transcript.<lang>.txt` and `transcript.en.txt`, detects scene cuts and static stretches with ffmpeg, and lays candidate frames out on `sheet-NN.png` contact sheets. It is resumable: an unchanged MP4 reuses its candidates. Lessons whose title matches an `intro_lessons` rule are skipped and listed only in the sources appendix.
- `check` must pass for every included lesson before `build` runs. It checks the time ranges, coverage, frames, caption lines and the prose-length floor described in `references/reading-copy.md`.
- `clean` writes every removal (rule, location, text) to `<workdir>/reading/removed.log`. `build` runs it again. To change what is removed, edit the rules file, not the output.
- `build --unit N` renders a partial copy for review. `--zip` needs the whole course: it adds `<course title> - reading copy.pdf` to the ZIP root and re-runs the member-set and CRC checks.
- `export` writes the same cleaned content as Markdown, for building a skill from the course: one `UNN-LNN-<slug>.md` per lesson with the anchor under every heading and figures linked from `frames/` (renamed `UNNLNN-Fmmss.jpg`), one `UNN-unit.md` per unit with the introduction, tasks and resources, and a `README.md` index. It refuses to run unless every included lesson passes `check`, and it logs removals like `build`. Unlike `build`, it also applies the sentence-level `prose_cta` rules to the unit introduction and tasks, so forum prompts inside task paragraphs are removed without losing the task. Unit HTML is converted with `markdownify` when installed, otherwise kept as HTML. With `--pdf`, the built reading copy is copied into the same folder and `pdf-index.md` lists the PDF page of every section anchor. The command fails if any anchor is missing from the PDF, which means the PDF is older than the lessons, so rebuild it first.

Output layout inside the work directory:

```text
<workdir>/reading/
├── progress.json           # excluded / prepared / drafted / checked per lesson
├── removed.log             # every rule-based removal
├── reading-copy.html       # last rendered source
└── U02/L05/
    ├── lesson.json         # lesson metadata written by prepare
    ├── transcript.es.txt   # native captions, one [mm:ss] line per cue
    ├── transcript.en.txt   # Domestika's English captions, for checking
    ├── candidates.json, sheet-01.png …, thumbs/
    ├── frames/F0312.jpg …, frames.json   # frames kept by the agent
    └── lesson.md           # the agent's English write-up
```

Verify before delivery: `check` passes for every included lesson; `pdftotext` of the PDF contains every included lesson's anchor (`<course> · U<n> · L<nn>`) and nothing matching the rules file; the figure count equals the frames referenced; `removed.log` has been read in full; the prose has been scanned for spoken plugs the rules missed (search `lesson.md` files for the platform name, "course", "subscribe", social networks) and any found have become new rules followed by a rebuild; sample pages have been inspected visually; the ZIP check passed.

Known limits: frame choice and translation are agent judgement, so review a sample against the video. The prose-length floor (35% of the native transcript's words) catches over-summarising, not mistranslation. Attachments stay as links.
