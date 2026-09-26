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
- Confirm the requested audio and caption tracks exist for every lesson playlist.
- Check playlists for encryption indicators. If protected, stop; this tool does not handle DRM.
- Download one short lesson and confirm the MP4 has audio and video and the VTT has timed cues.
- Estimate disk space from a representative video or playlist metadata when practical.

The current packager selects English audio and English timed captions. If English is unavailable or the user asked for another language, don't silently substitute: adjust the selector only after checking availability and telling the user what will be used.

## Package

```sh
python3 scripts/package_domestika.py /path/to/domestika-course-<id>-manifest.json \
  --output /path/to/domestika-course-<id>.zip
```

Options:

- `--max-height 720` lowers the video resolution limit; the default is 1080p.
- `--unit 1` packages one unit as a focused run; repeat `--unit N` to choose several.
- `--workdir PATH` selects where resumable working files are stored. The default is a `.work` directory beside the ZIP.

The packager checks every video for audio/video streams and plausible duration, checks VTT structure and timed cues, renders each PDF, then creates the ZIP. It stops on missing requested media or captions and leaves working files so the user can resume after addressing the issue.

## Output layout

```text
domestika-course-<id>.zip
├── Unit 01 - <title>/
│   ├── Unit 01 - <title>.pdf
│   ├── 01-<lesson>.mp4
│   ├── 01-<lesson>.vtt
│   └── ...
└── Unit 02 - <title>/
    └── ...
```

Each PDF preserves the unit introduction, lesson order and transcripts, tasks and linked resources. A clearly marked placeholder at each video position names the paired MP4 and VTT and links to the lesson page. It is a readable annotated copy, not a pixel-perfect print of the live webpage. Extra downloadable course attachments are linked in the PDF but are not added to the ZIP unless the user asks.

## Verify before delivery

- Confirm the ZIP contains exactly one unit folder and PDF per selected unit.
- Confirm there is exactly one MP4 and one same-stem VTT for every included lesson.
- Compare counts to the selected manifest units; a partial `--unit` run is not a complete-course archive.
- Check `pdfinfo` page counts and `pdftotext` marker/filename matches; render and visually inspect PDFs with the `pdf:pdf` skill.
- Run `ZipFile.testzip()` or an equivalent CRC check before delivery.
- Report the actual archive path, size, unit/lesson/file counts, selected audio/caption languages, and any limits. Keep playback URLs out of the report.

## Known limits

- The collector depends on current Domestika page paths and embedded `__INITIAL_PROPS__` metadata. Site changes can break it; fail clearly.
- The included packager targets HLS playlists on `cdn-videos.domestika.org`, an English audio track, English VTT captions, and Chrome on macOS.
- The tool archives unit lessons, not a separate final project page or unrelated course resources.
- Do not attempt alternate endpoints, credentials, decryption, or access workarounds if the expected page data is unavailable.
