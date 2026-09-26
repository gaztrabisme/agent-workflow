# Reading copy: the agent loop

Reader: the agent turning an archived course into one English PDF that replaces watching the videos. The PDF is source material for building skills and for later reference, so it must be complete and traceable to the video.

Terms used below:
- **Work directory (`W`)**: the packager's resumable folder, holding one `Unit NN - <title>/` folder per unit with the MP4, VTT and unit PDF.
- **Native captions**: the caption track in the language the teacher speaks, recorded by the packager as the lesson's HLS default audio language (`.es.vtt` for a Spanish teacher).
- **Anchor**: the citation printed under every heading, `<course> · U<unit> · L<lesson> · mm:ss–mm:ss`.

## Division of work

The script `scripts/reading_copy.py` does everything mechanical: transcripts, candidate frames, contact sheets, frame extraction, marketing removal, checks and the PDF. You do only three things: choose frames, translate and write the prose, and write frame captions. Do not remove or soften marketing yourself; translate everything that was said and let `clean` remove it by the rules in `scripts/marketing_rules.json`.

## Commands

```sh
R=scripts/reading_copy.py; M=<manifest.json>; W=<work directory>
python3 $R prepare $M --workdir $W [--unit N]      # transcripts, candidates, contact sheets
python3 $R frames $W/reading/UNN/LNN --at 03:12 --at 05:48.5   # extract kept frames
python3 $R check $M --workdir $W [--unit N] [--lesson N]       # must pass before build
python3 $R status $M --workdir $W                  # progress per lesson
python3 $R clean $M --workdir $W                   # preview removals into reading/removed.log
python3 $R build $M --workdir $W --output <pdf> [--unit N] [--zip <course zip>] [--teacher "<name>"]
```

`prepare` skips lessons whose title matches an intro rule (for example "Presentation (Who am I)"); they appear only in the sources appendix.

## The loop, per unit

Run `prepare` for the unit, then for each lesson in `W/reading/UNN/LNN/`:

1. **Read the unit PDF** in the unit folder for lesson order, summaries, tasks and linked resources.
2. **Read the native transcript** `transcript.<lang>.txt` in full. `transcript.en.txt` is Domestika's translation; use it only to check your reading. Long transcripts can be truncated by the tool output, so read in chunks until the last timestamp is near the video's end.
3. **Mark visual moments.** Look at every `sheet-NN.png`. Each thumbnail is labelled `#index  mm:ss  (seconds)`. Keep frames that show material: slides, diagrams, examples, screen recordings, sketches, palettes, before/after comparisons. Drop talking-head shots, logo stings, transitions and near-duplicates. When a slide changes over several thumbnails, apply the density rule:
   - keep the finished state of each slide;
   - keep an intermediate state only when it shows content the finished state does not: a new answer, a new image set, a new label or step;
   - when intermediate states differ only in what is highlighted, keep one figure and list the highlights in its `Shows:` line, e.g. "Highlighted in turn: happy, terrifying, mysterious.";
   - when an overlay (an answer banner, a stamp) hides the content, keep the clear frame and put the overlay's content in `Shows:`;
   - keep a zoomed close-up only when the prose refers to a detail unreadable in the full view;
   - a later return to an earlier image is a new figure when the teacher uses it again (for example as the "before" of a comparison).

   Also scan the transcript for spoken cues ("as you can see", "este ejemplo", "look at this") and make sure each one has a frame.
4. **Extract and inspect.** Run `frames` with the exact seconds from the sheet labels, then open each extracted `frames/F*.jpg` at full resolution and confirm it shows what you expect. This is required: `On screen:` text must be copied from the full frame, not the thumbnail. Re-extract at a nearby time if it caught a transition. Frames you extract but do not reference are ignored by `build`; delete them or leave them.
5. **Write `lesson.md`** in the lesson directory (format below).
6. **Run `check`** for the lesson and fix every failure.

After the last unit, run `build` for the whole course with `--zip`. To distill a skill from the course, also run `export` into the skill's `references/course/`; the Markdown is easier to search and cite than the PDF.

## `lesson.md` format

```markdown
---
lesson_id: 7021
native_language: es
sources: transcript.es.txt (primary), transcript.en.txt (check), frames
---
## Concept heading [02:10–04:05]
Prose for what the teacher explains in this span.

::: figure 03:12 F0312.jpg
On screen: "TÚ YA ERES UN EXPERTO EN COLOR" (You are already a color expert)
Shows: Title card for the lesson.
:::

## Next concept [04:05–06:30]
...

### Key points (derived)
- ...
```

- `lesson_id` and `native_language` must match `lesson.json`.
- Every `##` heading names one concept and carries its time range. Ranges run in order, do not overlap, leave no gap over 60 s, and cover the video from its first minute to its last minute.
- Figures sit inside the section whose range contains their timestamp; range ends are inclusive and adjacent ranges may share an endpoint. Within a section, order figures by timestamp. Section boundaries follow the speech; when a figure falls outside its section, re-cut the frame inside the section that discusses it rather than moving the boundary. Only when the image first appears after the teacher has moved on, and no earlier frame exists, extend the section to include it. The file name is the one `frames` printed.
- Use `###` for sub-headings inside a section if needed. `### Key points (derived)` is optional, must be last, and is the only place for summary.
- Add `compression_note: <reason>` to the front matter only when the prose is legitimately shorter than 35% of the native transcript (for example, long silent painting demos). `check` enforces the floor otherwise.

## Writing rules

**Translation.** Translate from the native captions. Where they and the English captions disagree, the native captions win. At the first use of a technical term that could translate differently, give the original in brackets: "value (*valor*)".

**Faithfulness.** Follow what was taught, in the teacher's order, edited for clarity: remove filler, false starts and repetition; keep every point, example, number, name, step, warning and piece of advice. Add nothing the teacher did not say or show. Keep the teacher's voice in the first person only where it carries meaning ("I always start with…"). Put your own summary only under Key points (derived).

**Frame captions.**
- `On screen:` copies on-screen text exactly as shown, in quotes. If it is not English, follow it with an English translation in brackets. Use `[none]` when there is no text and `[illegible]` for text you cannot read. For dense screens, or text cut off at the frame edge, copy what is readable and relevant and add `[rest omitted]`. When the native captions mis-transcribe a word and the correction changes the meaning, translate what was said and note the caption reading once in brackets, e.g. "smelling the lavender (captions: *oler la banda*)".
- Interface screens (Photoshop panels, dialogs): copy only the labels and values the lesson is about, then `[rest omitted]`; a frame whose only text is interface chrome is `[none]`. Text repeated across many frames (a poster tagline, a course title) is quoted in full once per lesson, then `[rest omitted]`. Artist signatures count as on-screen text when they identify the work discussed; site watermarks and the platform logo do not.
- Promotional screens (the platform's sting, a course advert) are not figures; drop them.
- A teacher's own slip of the tongue is handled like a caption error: translate what was meant and note the words spoken once in brackets.
- `Shows:` is one plain line on what the frame shows (layout, image content, what is highlighted). No interpretation; interpretation belongs in the prose where the teacher gives it.

**Marketing.** Translate it like everything else. `clean` removes it by rule and records each removal in `W/reading/removed.log`.

## Resuming and delegation

`W/reading/progress.json` records each lesson as `excluded`, `prepared`, `drafted` or `checked`; `status` prints it. Lessons are independent, so they can be written by parallel subagents. A subagent must be able to view images (it reads contact sheets and frames). The coordinator runs `check` itself and reviews a sample of figures before `build`.
