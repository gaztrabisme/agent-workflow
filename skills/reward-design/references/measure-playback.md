# Review existing playback

Reader: a reviewer measuring a supplied video export. This is a local extraction procedure, not a perceptual or neurological test. Use it before the playback questions in [review-checklist.md](review-checklist.md). Timing fields and provenance are in [timing-and-structure.md](timing-and-structure.md); listening prerequisites are in [sound.md](sound.md).

## Inputs and probe

Use ffprobe and ffmpeg installed on the review machine. Put measurement output in the project's allowed evidence location, outside the reusable skill. Record the artifact version and tool version. These shell examples use a new output directory; change paths to your artifact and allowed destination.

```bash
media='explainer.mp4'
out='review-playback'
mkdir -p "$out"
ffmpeg -version > "$out/ffmpeg-version.txt"
ffprobe -v error -show_entries 'format=duration,start_time:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,time_base,start_time,duration,nb_frames,sample_rate,channels' -of json "$media" > "$out/probe.json"
ffprobe -v error -select_streams v:0 -show_frames -show_entries 'frame=best_effort_timestamp_time,pkt_duration_time' -of csv=p=0 "$media" > "$out/frame-times.csv"
```

Read duration, dimensions, nominal/average fps (frames per second), time base and stream start offsets. A time base is the unit used to store timestamps. Use frame PTS (presentation timestamps) for variable-rate video; average fps alone does not locate a frame. Some containers omit frame count or duration: retain that absence and use decoded frame timestamps/count. Check the decoded count against any supplied count rather than assuming a successful command covered the file.

## Exact-time and exact-frame views

Decode from the start and select the first native frame at or after the requested export timestamp. This avoids presenting a keyframe seek as an exact frame. The example time is an **analyst choice**, not a recommended reveal time.

```bash
ffmpeg -hide_banner -i "$media" -map 0:v:0 -vf "select='gte(t,12.500)',showinfo" -frames:v 1 -fps_mode passthrough "$out/frame-at-12.500.png" 2> "$out/frame-at-12.500.log"
```

Read `pts_time` from the showinfo log and record both requested and returned time. They can differ when no frame lands exactly at the request. To select a known frame index, count from zero:

```bash
ffmpeg -hide_banner -i "$media" -map 0:v:0 -vf "select='eq(n,375)',showinfo" -frames:v 1 -fps_mode passthrough "$out/frame-375.png" 2> "$out/frame-375.log"
```

Frame 375 is at 12.500 s only for zero-origin constant 30 fps. At 30 fps the native frame interval is 1/30 s; decimals beyond that interval do not improve certainty. Inspect frames on both sides of a candidate boundary. For a fade/build, log first detectable pixels and readable state separately; a one-second contact sheet only brackets an onset and does not establish a frame-precise time. Keep audience-perceived onset not judged until tested.

## All-frame change scores and crops

Compute change scores for **every decoded frame**, including zero scores. `gte(scene,0)` evaluates the scene score while retaining all frames; a high-threshold selection would discard subtle builds before inspection. The metadata logs contain frame indices, timestamps and `lavfi.scene_score`.

The crop below is an **analyst choice for a 1920 × 1080 export** whose caption band starts at y=900. Confirm the band visually, choose the actual crop and record it. Do not copy it into another format or remove explanatory labels with the captions. Metadata output paths below must not contain filter-special characters such as colons or commas; use a simple relative output directory.

```bash
ffmpeg -hide_banner -i "$media" -map 0:v:0 -an -vf "select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=$out/changes-full.txt" -fps_mode passthrough -f null - 2> "$out/changes-full.log"
ffmpeg -hide_banner -i "$media" -map 0:v:0 -an -vf "crop=iw:900:0:0,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=$out/changes-content.txt" -fps_mode passthrough -f null - 2> "$out/changes-content.log"
ffmpeg -hide_banner -i "$media" -map 0:v:0 -an -vf "crop=iw:ih-900:0:900,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=$out/changes-captions.txt" -fps_mode passthrough -f null - 2> "$out/changes-captions.log"
```

Check that each score log has one record per decoded frame. Compare full-frame, content-only and caption-only peaks; visually confirm candidates and classify **main-content boundary**, **caption transition**, **within-scene build**, or **other change** separately. Scores nominate locations; they do not classify events or count scenes by themselves. If using a numerical candidate threshold, state its exact value and purpose as an analyst choice, retain all scores, and inspect below-threshold intervals where the explanation changes. No universal threshold is supplied.

Fades, small annotations, similar scenes and stable charts can evade a scene detector. Inspect the full sequence as well as peaks. For a specific chart build, crop its region, retain every score and inspect successive native frames for pixel presence or mark change. This example region is an analyst choice and must fit the actual frame:

```bash
ffmpeg -hide_banner -i "$media" -map 0:v:0 -an -vf "crop=640:360:1280:300,select='gte(scene,0)',metadata=print:key=lavfi.scene_score:file=$out/changes-region.txt" -fps_mode passthrough -f null - 2> "$out/changes-region.log"
```

Record the region coordinates, any pixel-presence/change rule and its threshold. A scene score alone cannot establish first readable annotation. Match a narrated reference to the mark being discussed, not merely to the changing caption band. (T1; B16, B18)

## Audio loudness and signal onsets

First confirm an audio stream in the probe. If none exists, apply the checklist's channel predicates; do not run an audio filter and infer silence from its failure. Decode the actual selected stream:

```bash
ffmpeg -hide_banner -i "$media" -map 0:a:0 -vn -af ebur128=peak=true -f null - 2> "$out/loudness.txt"
ffmpeg -hide_banner -i "$media" -map 0:a:0 -vn -af silencedetect=noise=-45dB:duration=0.10 -f null - 2> "$out/silence.txt"
```

`ebur128` reports integrated loudness in LUFS (loudness units relative to full scale), loudness range in LU and true peak relative to digital full scale. These describe the decoded mix, not intelligibility, emotional meaning or a target that every piece must meet. Record stream/channel selection; mono region statistics and whole stereo-mix loudness are different measures. (T3; C18)

The −45 dBFS threshold (decibels relative to full scale) and minimum 0.10 s gap are **analyst choices** for signal-event detection. A `silence_end` nominates return above that threshold; it is not automatically a spoken-word onset. Record minimum-gap detection delay and stream timestamp offsets; inspect/listen around candidates before naming speech, impacts or music events. A sustained music bed may prevent silence detection, and quiet syllables may remain below the threshold. Filter logs do not establish the speech content. (T3; C16) (T2; C7)

Keep measured audio events, supplied caption/transcript windows and independently auditioned spoken references in separate fields. Caption-derived word rates are text-window proxies. LUFS, waveform alignment and captions cannot establish voice comprehension, mood or perceived synchrony. Normal-speed device listening and an intended-listener task remain separate evidence. Confirm a bed before requesting a bed/silence comparison. (T2; C7, C8) (T3; C15, C16) (T1; C22)

## Measurement handoff

Deliver the probe, frame timestamps, selected views and their actual PTS, all-frame score logs, crop/threshold choices, classified events and separate audio/transcript records. For each event retain `observed_time`, `measurement_method/precision`, `reported_transcript_time` and `proposed_time`; proposed edits are prototype choices. State which timing was measured, visually judged, auditioned or not judged. Use [review-checklist.md](review-checklist.md) to turn the observations into ranked edits and pending tests.

Maintainer: reward-design skill owner. Recheck commands against local tool help and native-frame coverage when the export format or ffmpeg changes.
