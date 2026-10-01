# scene-engine specification report

The research did not settle several design choices required for a buildable contract. SPEC.md §9 records the trade-offs: the version-one JSON storyboard and its fixed 1920×1080/30 fps canvas; millisecond time and interpolation rules; each PPTX slide's sampled pose at `pptxAtMs`; the app-demo frame-sequence boundary; CLI exit codes and JSON shape; render-kit invocation on key frames and rendered PPTX slides; raster fallback order; Node orchestration with a Python writer; and deferring soundtrack authoring while the phase 4 row requires narration and captions. These are implementation decisions, not claims from the research.

Questions left unanswered by the permitted sources are listed in SPEC.md §10. They include exact Node and Python patch versions, the macOS Playwright shell path, the LibreOffice pin, the FFmpeg build feature set, actual Microsoft PowerPoint playback and WebVTT storage, capture parity on a real framework app, local voice quality and Vietnamese alignment accuracy, immutable TTS model revisions, cross-machine identity, and a measured frame-difference tolerance between renderers. The experiment used XlsxWriter without an exact version; the spec avoids making it a dependency and records the risk of generating the small embedded workbook with standard-library ZIP/XML. Sources: `output-pipelines/report.md` F4, F8, F9 and Risks; `synthesis.md` “Inputs for the scene engine” and “Open questions”.

Acceptance command:

```text
test $(grep -c '^| AT' SPEC.md) -ge 15 && for p in 'scene model' 'timeline' 'seek' 'narration' 'PPTX' 'app-demo' 'fallback'; do grep -i '^| AT' SPEC.md | grep -qi "$p" || { echo "no AT for $p"; exit 1; }; done && git log --oneline -1
```

The test-count and part-name checks passed silently. The command then failed at its final `git log` check:

```text
fatal: your current branch 'master' does not have any commits yet
```

Exit code: 128. The requested commit could not be created because the workspace permission profile makes `.git` read-only: `git branch -m main` failed when Git attempted to write `.git/HEAD.lock` (`Operation not permitted`). The working tree remains on `master` with the four requested files uncommitted.
