# scene-engine

Status: built. scene-engine validates seekable JSON storyboards, renders normalized MP4 explainers and local app demos, captures fixture-backed web apps, and exports editable PowerPoint slides.

## Requirements

- Node.js 24 or later
- FFmpeg 8.0 with libx264, AAC and libass
- Python 3 with the repository `.venv` dependencies
- LibreOffice for optional PowerPoint render checks
- `../render-kit/bin/rk` for visual checks

Install from the lockfile and prepare the Python writer once:

```sh
npm ci
python3 -m venv .venv
.venv/bin/pip install python-pptx==1.0.2
```

## Commands

```sh
npm run scene-engine -- validate samples/explainer/storyboard.json --root samples/explainer
npm run scene-engine -- render samples/explainer/storyboard.json --root samples/explainer --out out/explainer.mp4
npm run scene-engine -- export-pptx samples/explainer/storyboard.json --root samples/explainer --out out/explainer.pptx
npm run scene-engine -- check samples/explainer/storyboard.json --at 5000,12000 --rk ../render-kit/bin/rk
npm run samples
npm test
```

`npm run samples` reads `samples/explainer/chart.csv`, renders the 32-second explainer and its editable PPTX, then starts `samples/fixture-app/` and renders the 32-second app demo. HyperFrames telemetry is disabled for every HyperFrames process. Sample deliverables go to ignored `out/`.

See [AGENTS.md](AGENTS.md) for the storyboard format and the render-kit/ffprobe check loop. The complete behavior contract and acceptance IDs remain in [SPEC.md](SPEC.md).
