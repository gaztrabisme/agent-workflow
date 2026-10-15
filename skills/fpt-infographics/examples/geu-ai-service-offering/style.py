"""Style and page shell for build_v8.py. Landscape 1754x1240, cutaway, FPT brand, BR Omega.

THE TYPE SCALE IS SET BY MEASUREMENT, NOT BY EYE.
Bar: printed A3 landscape read at 50 cm -> k = 420/500 = 0.84 on a 1754px canvas.
  angle(arcmin) = (glyph_px / 1754) * 0.84 * 3437.75  =  glyph_px * 1.6462
  x-height  >= 12 arcmin (Legge & Bigelow 2011, critical print size)  -> >= 7.29px
  cap height >= 16 arcmin (ISO 9241-303 minimum)                      -> >= 9.72px
BR Omega: x/em 0.470, cap/em 0.700.  So nothing mixed-case below 16px, nothing all-caps
below 14.5px, anywhere on the sheet, including inside every chart.

Changed from v7_style.py:
  - Every size raised to that floor. Body 12 -> 16, captions 10.5-11.5 -> 16,
    all-caps labels 9.5-12.5 -> 14.5, h3 19 -> 21, zone tags 26 -> 28, stats 28 -> 30.
  - The title follows N3 (>= 8x body): 100 -> 128px, one line.
  - .dm and .srcline are gone. The delivery-model block moved off the sheet; the source
    line's provenance moved into the footer.
  - Three contrast fixes, each keeping the brand colour in a non-text role:
      .kick     orange text 2.45:1  -> ink text with an orange rule before it
      .sx b     green figures 2.35:1 -> ink figures with a coloured rule on the group
      .start    white on orange 2.94:1 -> ink on orange, 4.99:1
  - .morerow / .prov - the accounts pictogram and the provenance line in the footer.
  - The masthead stacks: one row of kicker, internal stamp and provenance, then the title,
    then the standfirst. The title is 945px wide on two lines, so nothing fits beside it in
    a 1000px placard - which is what leaves the estate drawing 660px to be a big object.
    At 128px the title's ink rides above its own line box, so the placard's top padding
    carries the clearance rather than a margin on the heading.
"""

CSS_BASE = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
svg { display: block; }

:root {
  --bg:#FAF6EC; --surface:#F1EADA; --surface-2:#E4DBC4;
  --ink:#2B2A26; --ink-muted:#6E695D; --de-emphasis:#CFC7B2;
  --c-orange:#F37021; --c-blue:#034EA2; --c-green:#50B848;
  --c-dvb:#19226D; --c-emerald:#33B2C1;
  --font-display:'BR Omega','Segoe UI',sans-serif;
  --font-body:'BR Omega','Segoe UI',sans-serif;
  --radius:0;
}

html, body { background: var(--bg); }
body { font-family: var(--font-body); color: var(--ink); -webkit-font-smoothing: antialiased; }

.canvas { position:relative; overflow:hidden; background:var(--bg); }
/* the ground is never flat (composition.md): centre a touch lighter than the edges */
.canvas::before { content:""; position:absolute; inset:0; pointer-events:none; z-index:0;
  background:radial-gradient(118% 76% at 50% 22%, #FFFCF4 0%, rgba(255,252,244,0) 62%),
             radial-gradient(90% 60% at 92% 96%, rgba(207,199,178,.34), rgba(207,199,178,0) 70%); }
.defs { position:absolute; width:0; height:0; }
.sheet { position:relative; z-index:3; height:100%; display:flex; flex-direction:column; }

/* museum placard - cutaway device 6. Holds the title, which is the hero. */
.placard { background:var(--surface); border:2px solid var(--ink); position:relative; z-index:2; }
.kickrow { display:flex; align-items:center; justify-content:space-between; gap:20px; }
/* orange keeps its highlight role as the rule; the words are ink, so they clear 4.5:1 */
.kick { font-weight:700; color:var(--ink); display:flex; align-items:center; }
.kick::before { content:""; display:block; background:var(--c-orange); flex:none; }
.stamp { font-weight:700; color:var(--ink); background:var(--c-orange);
  border:1px solid var(--ink); white-space:nowrap; }
h1 { font-family:var(--font-display); font-weight:900; line-height:.84;
     letter-spacing:-.022em; color:var(--ink); white-space:nowrap; }
.kickrow { display:flex; align-items:baseline; gap:24px; }
.prov { margin-left:auto; }
.standfirst { color:var(--ink-muted); line-height:1.3; }
.estate { position:absolute; z-index:1; }

/* drafting zones */
.zone { display:flex; border-top:2px solid var(--ink); }
.ztag { flex:none; }
.ztag .zn { font-family:var(--font-display); font-weight:900; text-transform:uppercase;
  line-height:.95; color:var(--ink); letter-spacing:-.01em; }
.zbody { flex:1 1 auto; min-width:0; }

/* offering module */
.mod .oh { display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
.on { font-family:var(--font-body); font-weight:700; color:var(--bg);
  display:inline-flex; align-items:center; justify-content:center; border-radius:50%;
  flex:none; border:1.5px solid var(--ink); }
.on.d { background:var(--c-blue); } .on.a { background:var(--c-dvb); }
.on.e { background:var(--c-green); color:var(--ink); }
.mod h3 { font-family:var(--font-display); font-weight:800; color:var(--ink);
  line-height:1.05; letter-spacing:-.008em; }
.flag { font-weight:700; color:var(--ink); background:var(--c-green);
  border:1px solid var(--ink); white-space:nowrap; }
/* the recommended entry point. Ink on orange is 4.99:1; white on orange was 2.94:1. */
.start { font-weight:700; color:var(--ink); background:var(--c-orange);
  border:1px solid var(--ink); white-space:nowrap; }
.qn { font-style:italic; color:var(--ink-muted); line-height:1.27; }
.mod p { color:var(--ink); line-height:1.29; }
.mod ul { list-style:none; display:flex; flex-direction:column; }
.mod li { color:var(--ink); line-height:1.25; position:relative; }
.mod li::before { content:""; position:absolute; left:0; background:var(--ink); }
.winrow { display:flex; align-items:center; border-top:1px solid var(--de-emphasis);
  flex-wrap:wrap; }
.wl { font-weight:700; color:var(--ink-muted); }
.wc { font-family:var(--font-display); font-weight:800; color:var(--ink); }
.wins { width:auto; flex:none; }
.wnames { color:var(--ink-muted); }
.winmoney { font-family:var(--font-display); font-weight:700; color:var(--c-blue); }
.cv { width:100%; }

/* figures. The number is ink; the pillar colour is the rule beside it. */
.sub { font-weight:700; color:var(--ink-muted); }
.rows { display:flex; }
.sx { flex:1 1 0; min-width:0; }
.sx b { font-family:var(--font-display); font-weight:900; line-height:1; display:block;
  color:var(--ink); }
.sx .nm { display:block; font-weight:700; color:var(--ink); line-height:1.25; }
.sx .wt { display:block; color:var(--ink-muted); line-height:1.3; }
.sg { border-left-style:solid; }
.sg.acc { border-left-color:var(--c-blue); }
.sg.inc { border-left-color:var(--c-green); }

/* footer: two columns of logo slots */
.spacer { flex:1 1 auto; min-height:0; }
.foot { flex:none; display:flex; align-items:flex-start; border-top:2px solid var(--ink); }
.fcol.left { flex:1 1 auto; min-width:0; }
.fcol.right { flex:none; }
.lb { font-weight:700; color:var(--ink-muted); }
.slots { display:flex; flex-wrap:wrap; }
.slot { border:1px solid var(--de-emphasis); background:var(--surface);
  display:flex; align-items:center; justify-content:center; }
.slot img { max-width:100%; object-fit:contain; }
.slot .wm { font-family:var(--font-display); font-weight:800; color:var(--ink);
  letter-spacing:-.012em; white-space:nowrap; }
.slot.accel { border:1px solid var(--c-green); background:transparent; }
.morerow { display:flex; align-items:center; }
.more { color:var(--ink-muted); line-height:1.25; }
.prov { color:var(--ink-muted); line-height:1.3; }
"""

CSS_PAGE = """
@page { size: 1754px 1240px; margin: 0; }
html, body { width:1754px; height:1240px; }
.canvas { width:1754px; height:1240px; }
.sheet { padding:16px 40px 0; }

.top { position:relative; flex:none; height:308px; }
.estate { right:-58px; top:6px; width:700px; }
.placard { width:1000px; padding:18px 22px 9px; }
.kick { font-size:14.5px; letter-spacing:2.2px; }
.kick::before { width:26px; height:4px; margin-right:11px; }
.stamp { font-size:14.5px; letter-spacing:1.2px; padding:2px 9px; }
h1 { font-size:128px; margin-top:9px; }
.standfirst { font-size:18px; margin-top:8px; }
.logo { position:absolute; right:0; top:0; width:78px; z-index:4; }

.zone { gap:18px; padding-top:6px; margin-top:6px; }
.ztag { width:124px; }
.ztag .zn { font-size:26px; }
.ztag .zr { height:6px; width:72px; margin-top:9px; }
.on { width:28px; height:28px; font-size:16px; }
.mod h3 { font-size:21px; }
.flag, .start { font-size:14.5px; letter-spacing:1px; padding:2px 8px; }
.qn { font-size:16px; margin-top:6px; }
.mod p { font-size:16px; margin-top:5px; }
.mod ul { margin-top:4px; gap:0; }
.mod li { font-size:16px; padding-left:18px; }
.mod li::before { top:10px; width:10px; height:1.5px; }
.winrow { margin-top:5px; padding-top:4px; gap:10px; }
.wl { font-size:14.5px; letter-spacing:1.2px; }
.wc { font-size:16px; } .wnames { font-size:16px; }
.winmoney { font-size:16px; margin-top:3px; line-height:1.3; }

/* every module runs text beside its chart - height is the scarce axis here */
.zA .mod { display:flex; gap:22px; align-items:flex-start; }
.zA .mt { width:470px; flex:none; }
.zA .cvw { flex:1 1 auto; min-width:0; padding-top:4px; }
.zB { display:flex; gap:20px; }
.zB .mod { flex:1 1 0; min-width:0; display:flex; gap:20px; align-items:flex-start; }
.zB .mt { flex:1 1 auto; min-width:0; }
.zB .mod > .cv { width:184px; flex:none; margin-top:4px; }
.zC { display:flex; gap:24px; }
.zC .cl { width:700px; flex:none; }
.zC .cr { width:470px; flex:none; }
.zC .cs { flex:1 1 auto; min-width:0; }
.zC .cl .mod { display:flex; gap:20px; align-items:flex-start; }
.zC .cl .mt { flex:1 1 auto; min-width:0; }
.zC .cl .mod > .cv { width:240px; flex:none; margin-top:4px; }
.sub { font-size:14.5px; letter-spacing:1.2px; }
.statband { display:block; }
.sg { border-left-width:5px; padding-left:13px; }
.statband .sg + .sg { margin-top:9px; }
.rows { gap:18px; margin-top:6px; }
.sx b { font-size:30px; }
.sx .nm { font-size:16px; margin-top:4px; }
.sx .wt { font-size:16px; }

.foot { gap:30px; margin-top:6px; padding-top:6px; padding-bottom:5px; }
.fcol.right { width:640px; }
.lb { font-size:14.5px; letter-spacing:1.3px; }
.slots { gap:8px; margin-top:5px; }
.slot { height:40px; min-width:136px; padding:0 10px; }
.slot .wm { font-size:17px; }
.slot img { max-height:34px; }
.frow { display:flex; align-items:center; gap:10px; }
.frow + .frow { margin-top:8px; }
.frow .lb { flex:none; width:96px; line-height:1.2; }
.frow .lb.wide { width:118px; }
.frow .slots { margin-top:0; }
.slot.big { height:58px; min-width:196px; }
.slot.big .wm { font-size:21px; }
.slot.big img { max-height:38px; }
.slot.big.accel { min-width:120px; }
.morerow { gap:12px; margin-top:4px; flex-wrap:wrap; }
.more { font-size:16px; }
.prov { font-size:16px; margin-left:auto; }
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>GEU AI Service Offering</title>
<!-- DESIGN LANGUAGE : cutaway. Bright plate paper, ink linework, numbered callouts,
                       hatched cut bands, tiny figures for scale, museum placard.
     COMPOSITION     : Big Object. The drawn energy estate crosses the plate edge.
     BRAND           : FPT Software Brand Guidelines v4.0, Aug 2026.
     HERO            : the title, marked data-hero, at eight times body size.
     LEGIBILITY      : every glyph at or above 12 arcmin x-height / 16 arcmin cap height
                       for a printed A3 read at 50cm. Measured by scripts/legibility.mjs,
                       not judged. Sources in content-brief-v8.md.
     SOURCES         : every claim and charted value in content-brief-v8.md.
     STANDING RULES  : business/goals/2026-09-18-geu-offering-v8.md.
     AUDIENCE        : %AUDIENCE%. -->
<style>%FONTS%</style>
<style>%CSS%</style>
</head>
<body>
<div class="canvas">
%DEFS%
  <div class="sheet">
%SHEET%
  </div>
</div>
</body>
</html>
"""
