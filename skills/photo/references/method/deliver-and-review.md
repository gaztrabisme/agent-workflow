# Deliver and review: make the selected set usable

**Reader:** the editor preparing approved photographs for a client, web or social destination. **Scope:** final review, color/profile conversion, dimensions, and handoff.

**Source lessons:** [669 U4 L10–L12](../course-669/U04-L10-editing-with-lightroom.md), [227 U4 L14](../course-227/U04-L14-how-to-manage-instagram-and-schedule-posts.md), [227 U5 L15](../course-227/U05-L15-taking-photos.md), [1343 U54 L81–L82](../course-1343/U54-L81-delivering-files-to-a-client-1.md).

## Prepare the actual deliverable

- Confirm each chosen image, crop, pixel dimensions, file type, and color profile against the receiving brief. The Photoshop course distinguishes screen JPEG sizing from print dimensions and resolution, soft proofing, and profile conversion; preserve a layered working file when one exists. (1343 · U54 · L81 · 01:19–04:29; 1343 · U54 · L81 · 04:29–07:57; 1343 · U54 · L82 · 00:00–02:58; 1343 · U54 · L82 · 02:58–07:55; 1343 · U54 · L82 · 07:55–10:48; 1343 · U54 · L82 · 10:48–13:38)
- **Derived review format:** for multiple images, use a gallery or contact sheet to compare candidates by set and near-duplicates before final selection. This adapts the portrait teacher’s set-by-set comparison of exported photographs in Finder and her advice to return after time away. (derived from 669 · U4 · L11 · 00:00–03:14; 669 · U4 · L11 · 03:14–06:44; 669 · U4 · L11 · 08:22–12:37; 669 · U4 · L11 · 12:37–15:44)
- Course 227's Snapseed lesson calls its Story crop 16:9; its Story unit says the format is 9:16 and advises keeping important things out of the parts a phone-camera crop will remove. (227 · U4 · L11 · 14:31–16:48; 227 · U5 · L15 · 02:07–03:20) **Derived:** when the course examples give different Story ratios, check the receiving brief and destination specification to decide which ratio applies (derived from the differing ratios in the two lessons and the delivery brief).
- The portrait teacher exports candidates, compares them, and allows time before narrowing the final set. (669 · U4 · L10 · 15:06–17:56; 669 · U4 · L11 · 08:22–12:37; 669 · U4 · L11 · 12:37–15:44)
- Keep the output list mapped to original filenames and record actual formats/dimensions, chosen versions, and any limitations. (field rules FR-01, FR-02, FR-07, FR-08)

### Delivery presets and export

The recipient's current specification wins. These named presets are starting points from the course example and this skill's dogfood run; check the receiving brief before using them. The Photoshop lesson shows a 2000 px approval copy checked at 100%, converts the screen copy to sRGB, and sets its pixel dimensions (1343 · U54 · L81 · 01:19–04:29; 1343 · U54 · L81 · 04:29–07:57). That is an example, not a universal web size. (derived: dogfood 2026-10-02, F3)

| Preset | Crop and dimensions | Format and quality | Profile and notes |
|---|---|---|---|
| Master/archive | Full frame; preserve source pixel dimensions | JPEG 95 when a JPEG is requested; use the recipient's lossless format when required | Convert/tag sRGB for a screen master; retain the editable working file separately |
| Course-style approval | Full frame; 2000 px as requested by the brief | JPEG 90 starting point | sRGB; inspect the actual approval copy at 100% |
| Web approval | Full frame; long side 1200 px | JPEG 85 | Embedded sRGB; keep the original aspect ratio |
| Feed portrait 4:5 | Crop to the named subject, then 1080×1350 | JPEG 90 | Embedded sRGB; check face, hands, and text after crop |
| Vertical Story 9:16 | Crop to the named subject, then 1080×1920 | JPEG 90 | Embedded sRGB; keep faces, text, and other essential content clear of the destination's top and bottom interface overlays. Use its current safe-area preview and record the crop in the spec. |

The four preset rows after the course example are operational defaults, not claims about a platform's permanent limits. Confirm current dimensions and overlays with the receiving brief or destination preview. (derived: dogfood 2026-10-02, F3)

Use `python3 scripts/grade.py deliver delivery.json --out out/` to make a batch. In the JSON spec, each item has an input path (relative to the spec file or absolute), a plain output filename, optional `crop: [x0,y0,x1,y1]` pixel bounds, optional `size: [width,height]`, `format: JPEG|PNG|WEBP|TIFF`, and `quality` for JPEG/WEBP. The command resizes with Lanczos, embeds an sRGB ICC profile, refuses to overwrite outputs, and writes `manifest.json`. Its code check reopens every output and records file count, dimensions, format, and whether the embedded profile is sRGB. For PNG/TIFF, omit `quality`. (derived: dogfood 2026-10-02, F3)

Example spec:

```json
{
  "items": [
    {"input": "work/portrait-graded.png", "file": "portrait-master.jpg", "size": [2000, 1333], "format": "JPEG", "quality": 95, "note": "2000 px approval example"},
    {"input": "work/social-graded.png", "file": "social-feed-4x5.jpg", "crop": [560, 1, 1864, 1631], "size": [1080, 1350], "format": "JPEG", "quality": 90, "note": "feed crop centered on the subject"}
  ]
}
```

The delivery tool rejects any resize that enlarges either dimension unless that item explicitly sets `"allow_upscale": true`. Prefer a smaller output or a different crop when the source cannot supply the requested pixels. If upscaling is approved, the manifest records the scale and marks the output as upscaled; inspect the final file at 100%. (derived: dogfood 2026-10-02, F3)

## Check before moving on

Run T11 and T12. The delivered set passes when requested files and variants are present, dimensions/profile match the brief, and the gallery shows the approved selection without accidental omissions. See [review-checklist.md](review-checklist.md).

**Practice the teacher sets:** resize, convert/proof, and save delivery formats for a client while retaining the working file. See [Unit 54](../course-1343/U54-unit.md).

**Freshness:** Maintainer: skill owner. Last reviewed: 2026-10-02. Recheck when the destination's delivery specification changes.
