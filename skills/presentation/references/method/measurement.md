# Measurement and review methods

Use code for properties the artifact exposes exactly. Use a reviewer who can see the rendered images or play the media for message, hierarchy, continuity, and legibility judgments. A missing reviewer is **not judged**; automated accessibility checks identify only some issues. [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “The loop”; [book:playwright-docs], “Accessibility testing”.

## Render-kit

Run the owning renderer from the render-kit installation. The HTML template is a local artifact; test it with the acceptance command below and retain its report and images for inspection. [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “Quick start” and “The loop”.

```sh
~/.agent-workflow/tools/render-kit/bin/rk check templates/deck-shell.html --out-dir out/presentation-shell
# Add --pdf when a PDF handout is part of the output.
```

For a produced deck, check each slide artifact and every PDF page or exported page view; fix each `fail`, read all `skipped` and `incomplete` details, and repeat after material changes. Use the render-kit brief and verify path if a vision review is requested. [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “The loop”.

Vision questions should be yes-means-pass and specific to the output, for example:

- “Can you identify the slide's point within a few seconds, and do the evidence and labels support it?” [book:storytelling-with-data], “The 3‐minute story & Big Idea”; (derived: test the stated point, not generic attractiveness.)
- “Can you read the smallest required text from the intended seat or screen size?” (field rule (pptx)); [book:storytelling-with-data], “Chapter 5: think like a designer”.
- “Does each chart's encoding, label, unit, and caveat make the intended comparison clear?” [information-design/SKILL.md](../../../information-design/SKILL.md#principles--anchoring-rules).
- “Does the exported video show the approved state and keep captions/narration aligned with that state?” (field rule (screencast)); [src:output-pipelines/report.md], “F4. Audio: narration, timestamps, captions, music, loudness”.

## MP4 stream probe

Probe the final MP4, not an intermediate file. For the PowerPoint-oriented delivery target, expect H.264 High profile at level 4.1, `yuv420p`, 1920×1080, constant 30 fps, limited range, BT.709 color tags, and AAC-LC at 48 kHz stereo. This is the measured target in the source study; playback in PowerPoint remains a separate owner check. [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”; [src:output-pipelines/experiments/README.md], “01-mp4-for-powerpoint”.

```sh
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,profile,level,pix_fmt,width,height,r_frame_rate,avg_frame_rate,color_range,color_primaries,color_transfer,color_space \
  -of default=noprint_wrappers=1 out/movie.mp4

ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,profile,sample_rate,channels \
  -of default=noprint_wrappers=1 out/movie.mp4

ffprobe -v error -show_entries format=duration,size \
  -of default=noprint_wrappers=1 out/movie.mp4
```

Expected video fields: `codec_name=h264`, `profile=High`, `level=41`, `pix_fmt=yuv420p`, `width=1920`, `height=1080`, `r_frame_rate=30/1`, `avg_frame_rate=30/1`, `color_range=tv`, and BT.709 primaries, transfer, and matrix. Expected audio fields: `codec_name=aac`, `profile=LC`, `sample_rate=48000`, `channels=2`. Use `ffprobe` duration/size to compare with the brief; if embedding in PowerPoint for the web, the cited study records a 256 MB insert limit. [src:output-pipelines/report.md], “F5. MP4 for PowerPoint, embedding, native motion and fonts”.

## PDF structure and fonts

Check dimensions, number of pages, tagging, and fonts with the available PDF inspection tools, and render the pages for visual inspection. Variable fonts and synthetic bold were measured as Type 3 in the tested Chromium path; its tagged PDF is not PDF/UA certification. [src:output-pipelines/report.md], “F6. HTML to PDF with Chromium”; [src:output-pipelines/experiments/README.md], “05-html-pdf”.

```sh
pdfinfo out/handout.pdf
pdffonts out/handout.pdf
```

## PPTX reopen and editability inventory

Reopen the exported file with python-pptx and record slide count, text frames, native shapes, charts, tables, and picture fallbacks. Inspect expected chart series and values; native charts are the tested path for retaining an embedded workbook. This structural read-back does not establish that PowerPoint renders or plays the file correctly. [src:output-pipelines/report.md], “F8. Editable PowerPoint from code”; [src:output-pipelines/report.md], “Risks and unknowns”.

```python
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation("out/deck.pptx")
for slide_no, slide in enumerate(prs.slides, 1):
    text_frames = shapes = charts = tables = pictures = 0
    chart_data = []
    for shape in slide.shapes:
        if shape.has_chart:
            charts += 1
            chart_data.append([
                {"name": series.name, "values": list(series.values)}
                for series in shape.chart.series
            ])
        elif shape.has_table:
            tables += 1
        elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            pictures += 1
        else:
            shapes += 1
            if shape.has_text_frame and shape.text.strip():
                text_frames += 1
    print({"slide": slide_no, "text_frames": text_frames,
           "native_shapes": shapes, "charts": charts,
           "tables": tables, "pictures_or_fallbacks": pictures,
           "chart_data": chart_data})
```

Compare that inventory with the export report: required title/body text must appear as text frames; intended chart objects and expected series must appear as charts; each picture fallback must be accounted for. [src:output-pipelines/report.md], “F8b. The design subset that maps one-to-one from a scene to native PowerPoint”.

For an editable PPTX, add a throwaway edit/save/reopen check after the inventory. Use an output copy so the check never changes the delivered deck; include the chart branch when a native chart is expected. A surviving text edit and chart data edit establish that those objects remain editable through this file round-trip, not that every target application behaves the same. (derived: dogfood 2026-10-02, F13)

```python
from pathlib import Path
from pptx import Presentation
from pptx.chart.data import CategoryChartData

source = Path("out/deck.pptx")
roundtrip = Path("out/deck-roundtrip.pptx")
roundtrip.parent.mkdir(parents=True, exist_ok=True)
editable = Presentation(source)
text_shape = next((shape for slide in editable.slides for shape in slide.shapes
                   if shape.has_text_frame and shape.text.strip()), None)
assert text_shape is not None, "no editable text frame found"
marker = " [round-trip edit]"
text_shape.text = text_shape.text + marker

chart_shape = next((shape for slide in editable.slides for shape in slide.shapes
                    if shape.has_chart), None)
expected_chart_value = None
if chart_shape:
    chart = chart_shape.chart
    data = CategoryChartData()
    data.categories = list(chart.plots[0].categories)
    for series_no, series in enumerate(chart.series):
        values = list(series.values)
        if series_no == 0:
            expected_chart_value = float(values[0]) + 0.123
            values[0] = expected_chart_value
        data.add_series(series.name, values)
    chart.replace_data(data)

editable.save(roundtrip)
reopened = Presentation(roundtrip)
assert any(marker in shape.text for slide in reopened.slides for shape in slide.shapes
           if shape.has_text_frame), "text edit did not survive reopen"
if expected_chart_value is not None:
    reopened_chart = next(shape.chart for slide in reopened.slides for shape in slide.shapes
                          if shape.has_chart)
    assert abs(float(reopened_chart.series[0].values[0]) - expected_chart_value) < 1e-9, \
        "chart edit did not survive reopen"
print("ROUNDTRIP text=pass chart=" + ("pass" if expected_chart_value is not None else "n/a"))
```

## Owner checks

Follow scene-engine's [PowerPoint and Keynote owner checks](../../../../tools/scene-engine/AGENTS.md#powerpoint-and-keynote-owner-checks). Record AT37 as `owner-check` until the named PowerPoint checks are performed; record the AT33/AT36 Keynote automation result separately if it returns a nested owner check. [scene-engine AGENTS.md](../../../../tools/scene-engine/AGENTS.md), “PowerPoint and Keynote owner checks”.

## Vision record

For every reviewed item, record the question, reviewer, artifact/version, answer, and repair stage. For every item not judged, skipped, or incomplete, record why. Keep a separate list of open owner checks. (field rule (pptx)); [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “The loop”.
