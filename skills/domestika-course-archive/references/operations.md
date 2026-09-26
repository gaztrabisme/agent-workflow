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
