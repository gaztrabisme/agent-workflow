"""Build the GEU AI Service Offering sheet v7. One landscape shape, two audiences.

    python work/v7.py client       -> 1754x1240, cleared names only, no money
    python work/v7.py internal     -> 1754x1240, every account name, TCV and pipeline

Design language : cutaway (epic-infographics/references/design-languages/cutaway.md) -
                  bright plate paper, ink linework, numbered callouts, museum placard,
                  hatched cut bands, tiny figures for scale.
Composition     : Big Object - the drawn energy estate, bleeding past the plate edge.
Brand           : FPT Software Brand Guidelines v4.0, Aug 2026.

THREE RECORDED DEPARTURES from the style file, all deliberate:
  1. Palette. Cutaway's brick/steel/amber slots are replaced by FPT Blue #034EA2,
     Dark Violet Blue #19226D and Green #50B848, with Orange #F37021 reserved for the
     hero figure and the call to action. A company brand outranks a design language
     on a company artifact.
  2. Typeface. Bitter and Source Sans 3 are replaced by BR Omega, the brand's primary,
     embedded as woff2 so the file stays self-contained.
  3. Scale of the sectioned subject. Cutaway asks for it at 55-75% of the canvas. This
     sheet carries five offerings, ten figures and a proof strip, so the estate is the
     object at roughly a third of the upper plate.

Content         : v6's, revised on Phuong's five comments of 2026-09-18 - the "2 Weeks"
                  hero removed and the title made the dominant element, wins carrying money
                  on the internal output, the delivery chart redrawn from its source, and
                  the footer rebuilt as two logo slot grids.
Standing rules  : business/goals/2026-09-18-geu-offering-v7.md.

THE AUDIENCE SPLIT IS THE SAFETY RULE. The client output is the sheet An emails cold. It
carries no money at all and no customer name outside slide 44's cleared TRUSTED BY list, so
CTBC never sees its own deal value. The internal output carries everything the template holds.
One builder, one layout, two dictionaries - see WINS_CLIENT and WINS_INTERNAL below.
"""
import base64
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(os.path.dirname(HERE))
BASE = HERE                     # outputs land beside this file
sys.path.insert(0, os.path.join(SKILL, "scripts"))
import fonts as _fonts                                                   # noqa: E402

LOGO = base64.b64encode(
    io.open(os.path.join(SKILL, "assets", "logo", "fpt-logo.png"), "rb").read()).decode()
# Inlined at build time so the sheet survives being emailed; the woff2 files stay on
# disk in the skill, diffable. scripts/fonts.py explains why they are not .otf.
FONTCSS = _fonts.font_css()

# CLIENT ONLY, deliberately. The internal variant of this sheet carries every account
# name, every deal value and the whole forward pipeline on one page, in a file that looks
# exactly like the customer's. That does not belong in a skill directory. The mechanism
# for building both from one source is described in SKILL.md, "Two audiences".
AUDIENCE = "client"
INTERNAL = False
W, H = 1754, 1240

# ==================================================================== content (data, not layout)

KICKER = "GROWTH ENGINE FOR 2027+"
TITLE = "GEU AI Service Offering"
STANDFIRST = "From governed data to AI that runs the business"

Q = {"01": "Our data isn&rsquo;t ready. Where do we start?",
     "02": "We have promising AI ideas, but how do we prove value and fund the first step?",
     "03": "How much value can this use case deliver with our data, and how far can AI take it?",
     "04": "Our team cannot drive the transformation alone.",
     "05": "We need proven AI solutions for Energy operations."}

# WINS. Counts and figures come verbatim from resources/GEU - AI Service Offerings.pdf.
#
# CLIENT: names appear only where slide 44's cleared TRUSTED BY list covers them, so Duy Tan,
# PwC, SCG CBM, Maybank, CTBC, ABMB, LSP, HAL, PET and TOGIS are withheld, and no money of any
# kind appears. FleziNergy's source states money won but no win count, so it carries a name and
# no number.
# INTERNAL: every name, every TCV, every pipeline figure. Never sent outside FPT.
WINS_CLIENT = {"01": (3, "SCGC, Danone", ""), "02": (3, "", ""), "03": (2, "", ""),
               "04": (1, "", ""), "05": (None, "QSOL", "")}

# WINS_INTERNAL lived here: win counts, TCV and pipeline per offering, with the
# account names. Removed on the way into the skill - see the CLIENT ONLY note above.

WINS = WINS_CLIENT

# Offering 03 is where FPT recommends a customer starts. Slide 44 says so in words -
# "Start with a 2-week AI Fast Track". v6 carried that as a footer block; Phuong asked for the
# block to go, so the recommendation moves onto the offering it names.
START_HERE = "03"

# The two outputs are the same drawing. Without a mark on the face of it, the wrong file gets
# attached to an email. The client output carries no stamp; the internal one cannot be mistaken.
STAMP = ("" if not INTERNAL else
         '<span class="stamp">FPT INTERNAL &mdash; DO NOT SEND</span>')

PHASES = ["Discovery", "Assessment", "Solution &amp; Plan", "MVP", "Continuous Improve"]
DOMAINS = [("Enterprise", 5), ("Oil &amp; Gas", 3), ("Renewable", 1), ("HSE", 1)]

RED = [("80%", 80, "PPE Detection", "safety incidents"),
       ("70%", 70, "OSDU AI Agent", "query time"),
       ("60%", 60, "FleziIQ", "data operations cost"),
       ("45%", 45, "Corrosion", "maintenance cost"),
       ("30%", 30, "Flezi AssetIQ", "downtime"),
       ("25%", 25, "Churn Detection", "churn rate")]
ACC = [("95%", "Seismic Fault", "accuracy"), ("92%", "Solar/Wind Forecasting", "forecast accuracy")]
INC = [("50%", "Ivy Chat", "productivity"), ("40%", "Flezi NovaAgent", "efficiency")]

OFF = {
    "01": ("Enterprise AI Data Hub", "d",
           "Consolidated, governed data &mdash; the foundation AI needs before it can scale.",
           ["Governed data products &amp; lineage", "Lakehouse platform modernization"], ""),
    "02": ("AIX Hub", "a",
           "Partner-funded AI experiments &mdash; explore before committing internal budget.",
           ["Co-funded use-case sprints", "Fast screening of AI use cases"], ""),
    "03": ("AI Fast Track", "a",
           "A two-week proof of value that unlocks the full project.",
           ["One measurable outcome, 2 weeks", "Scope + business case to scale"], ""),
    "04": ("Forward Deployed AI Pod", "a",
           "An embedded engineering pod that carries AI from pilot into production.",
           ["FPT AI engineers embedded in the team", "MLOps, hardening, run &amp; scale"], ""),
    "05": ("FleziNergy Suite", "e",
           "Energy-specific AI solutions built for generation, grid and plant assets.",
           ["APM, forecasting, maintenance", "Built on AssetIQ &amp; VisionIQ IP"], "FLAGSHIP"),
}
SLOT = {"d": "var(--c-blue)", "a": "var(--c-dvb)", "e": "var(--c-green)"}

# ==================================================================== shared SVG defs

DEFS = '''<svg class="defs" aria-hidden="true"><defs>
  <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"
          orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#2B2A26"/></marker>
  <marker id="al" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7"
          orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#2B2A26"/></marker>
  <pattern id="cut" width="5" height="5" patternTransform="rotate(45)"
           patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="5" stroke="#2B2A26" stroke-width="1" opacity=".5"/></pattern>
  <pattern id="hxd" width="6" height="6" patternTransform="rotate(45)"
           patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="6" stroke="#034EA2" stroke-width="2"/></pattern>
  <pattern id="hxa" width="6" height="6" patternTransform="rotate(45)"
           patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="6" stroke="#19226D" stroke-width="2"/></pattern>
  <pattern id="hxe" width="6" height="6" patternTransform="rotate(45)"
           patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="6" stroke="#50B848" stroke-width="2"/></pattern>
</defs></svg>'''

# ==================================================================== the big object

ESTATE = '''<svg class="estate" viewBox="0 0 860 330" fill="none" stroke="var(--ink)"
     stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <!-- ground: the section cut, hatched, per cutaway device 1 -->
  <rect x="0" y="292" width="860" height="13" fill="url(#cut)" stroke="none"/>
  <path d="M0 292 H860" stroke-width="3"/>
  <path d="M0 305 H860" stroke="var(--de-emphasis)" stroke-width="1"/>
  <!-- solar array -->
  <path d="M16 270 L48 246 H70 L38 270 z"/><path d="M46 270 L78 246 H100 L68 270 z"/>
  <path d="M27 270 V292 M57 270 V292 M87 270 V292" stroke-width="1"/>
  <!-- wind turbine, near -->
  <path d="M152 292 L160 96 L168 292" stroke-width="2"/>
  <circle cx="164" cy="92" r="8" stroke-width="2"/>
  <path d="M164 84 L196 12" stroke-width="2"/><path d="M172 98 L258 124" stroke-width="2"/>
  <path d="M156 98 L98 168" stroke-width="2"/>
  <path d="M146 292 H182"/>
  <!-- tiny figure at the mast, the scale bar (cutaway device 4) -->
  <g stroke-width="1.5"><circle cx="194" cy="272" r="4"/><path d="M194 276 V284"/>
    <path d="M190 280 H198"/><path d="M194 284 L190 292 M194 284 L198 292"/></g>
  <!-- wind turbine, far -->
  <g stroke-width="1.25">
    <path d="M246 292 L251 172 L256 292"/><circle cx="251" cy="168" r="5"/>
    <path d="M251 163 L272 122"/><path d="M256 172 L306 186"/><path d="M246 172 L208 202"/>
  </g>
  <!-- lattice pylon, near -->
  <path d="M332 292 L350 76 L368 292" stroke-width="2"/>
  <path d="M316 104 H384" stroke-width="2"/><path d="M324 84 H376" stroke-width="2"/>
  <path d="M350 76 V64" stroke-width="2"/>
  <path d="M341 168 H359"/><path d="M337 212 H363"/><path d="M334 256 H366"/>
  <g stroke-width="1">
    <path d="M337 212 L359 168 M363 212 L341 168 M334 256 L363 212 M366 256 L337 212"/>
    <path d="M341 168 L357 124 M359 168 L343 124"/>
    <circle cx="320" cy="104" r="3"/><circle cx="380" cy="104" r="3"/>
    <circle cx="328" cy="84" r="3"/><circle cx="372" cy="84" r="3"/>
  </g>
  <!-- lattice pylon, far -->
  <g stroke-width="1.25">
    <path d="M436 292 L450 132 L464 292"/><path d="M426 154 H474"/><path d="M432 138 H468"/>
    <path d="M450 132 V122"/><path d="M442 202 H458"/><path d="M438 248 H462"/>
    <g stroke-width="1"><path d="M438 248 L458 202 M462 248 L442 202"/></g>
  </g>
  <!-- conductor spans -->
  <g stroke="var(--de-emphasis)" stroke-width="1.25">
    <path d="M316 104 Q262 122 210 126"/><path d="M384 104 Q412 126 426 154"/>
    <path d="M324 84 Q400 112 432 138"/><path d="M474 154 Q502 178 528 212"/>
  </g>
  <!-- substation -->
  <g stroke-width="1.25">
    <path d="M512 292 V246 h52 v46"/><path d="M512 268 h52" stroke-width="1"/>
    <path d="M520 246 V226 M538 246 V218 M556 246 V226" stroke-width="1"/>
    <circle cx="520" cy="222" r="4" stroke-width="1"/><circle cx="538" cy="214" r="4" stroke-width="1"/>
    <circle cx="556" cy="222" r="4" stroke-width="1"/>
  </g>
  <path d="M498 292 V276 M578 292 V276" stroke="var(--de-emphasis)" stroke-width="1"/>
  <!-- stack, with a hatched wall band at its base: you are looking at a slice -->
  <path d="M600 292 V112 h24 V292" stroke-width="2"/>
  <path d="M596 112 h32"/>
  <rect x="600" y="266" width="24" height="26" fill="url(#cut)" stroke="none"/>
  <path d="M600 156 h24 M600 200 h24" stroke="var(--de-emphasis)" stroke-width="1"/>
  <!-- process hall -->
  <path d="M646 292 V206 h114 v86" stroke-width="2"/>
  <g stroke-width="1">
    <path d="M646 206 L703 182 L760 206"/><path d="M646 232 h114"/>
    <path d="M674 232 V292 M703 232 V292 M732 232 V292"/>
    <path d="M660 250 h8 M688 250 h8 M717 250 h8 M746 250 h8"/>
    <path d="M700 258 h14 v34 h-14 z"/>
  </g>
  <!-- second tiny figure, at the hall door -->
  <g stroke-width="1.5"><circle cx="726" cy="272" r="4"/><path d="M726 276 V284"/>
    <path d="M722 280 H730"/><path d="M726 284 L722 292 M726 284 L730 292"/></g>
  <!-- storage tanks, the right one crosses the plate edge -->
  <path d="M790 292 v-58 a24 12 0 0 1 48 0 v58" stroke-width="2"/>
  <path d="M790 234 a24 12 0 0 0 48 0"/>
  <path d="M796 262 h36" stroke-width="1"/>
  <!-- pipe rack -->
  <g stroke="var(--de-emphasis)" stroke-width="1.25">
    <path d="M624 274 H790"/><path d="M624 282 H790"/>
    <path d="M660 274 V292 M712 274 V292 M764 274 V292"/>
  </g>
</svg>'''

# ==================================================================== drawn data

# Every chart is drawn at 1:1 - viewBox width == rendered px - so no label is ever scaled
# below the size it declares. See work/v8_charts.py for the type floor and why it is that.
import charts as V                                                    # noqa: E402

FS_BODY, FS_CAPS = V.FS_BODY, V.FS_CAPS

# Widths each chart is shown at. Passed in, not guessed, so viewBox == box.
W_PHASES, W_ZB, W_SOLUTIONS, W_REDUCTIONS, W_TRUSTED = 1036, 184, 240, 470, 280


def chart_wins(num):
    return V.chart_wins(num, WINS, OFF, SLOT)


def chart_phases():
    return V.chart_phases(PHASES, W_PHASES)


def chart_funding():
    return V.chart_funding(W_ZB)


def chart_gate():
    return V.chart_gate(W_ZB)


def chart_pod():
    return V.chart_pod(W_ZB)


def chart_solutions():
    return V.chart_solutions(DOMAINS, W_SOLUTIONS)


def chart_reductions():
    return V.chart_reductions(RED, W_REDUCTIONS)


def chart_trusted():
    return V.chart_trusted(len(TRUSTED), 10, W_TRUSTED)


def statrows(items, cls):
    return V.statrows(items, cls)


# ==================================================================== modules

def module(num, chart_html, extra=""):
    name, cls, pos, bul, flag = OFF[num]
    n, names, money = WINS[num]
    f = f'<span class="flag">{flag}</span>' if flag else ""
    if num == START_HERE:
        f += '<span class="start">START HERE</span>'
    b = "".join(f"<li>{x}</li>" for x in bul)
    bits = ['<span class="wl">WINS</span>', chart_wins(num)]
    if n is not None:
        bits.append(f'<b class="wc">{n}</b>')
    if names:
        bits.append(f'<span class="wnames">{names}</span>')
    winrow = '<div class="winrow">' + "".join(bits) + "</div>"
    if money:
        winrow += f'<div class="winmoney">{money}</div>'
    return (f'<div class="mod {cls} {extra}">'
            f'<div class="mt">'
            f'<div class="oh"><span class="on {cls}">{num}</span><h3>{name}</h3>{f}</div>'
            f'<div class="qn">&ldquo;{Q[num]}&rdquo;</div>'
            f'<p>{pos}</p><ul>{b}</ul>{winrow}</div>'
            f'{chart_html}</div>')


# ==================================================================== footer slot grid

# Phuong asked for logos in both footer columns. No logo file exists anywhere in resources/ -
# slide 44 sets every one of these names as text, and its five images are generic icons. So each
# slot is built at logo size and carries the wordmark until an approved file is dropped into
# resources/logos/<slug>.<svg|png|jpg>, at which point it is picked up with no layout change.
LOGO_DIR = os.path.join(SKILL, "assets", "logos")
TRUSTED = ["SCGC", "Danone", "GE Vernova", "RWE", "QSOL", "Aboitiz Power", "Bangchak"]
PARTNERS = ["Microsoft Frontier", "Databricks"]
ACCEL = ["AssetIQ", "DataIQ", "VisionIQ", "AIND"]
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg"}


def slot(name, cls=""):
    for ext in (".svg", ".png", ".jpg"):
        p = os.path.join(LOGO_DIR, re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") + ext)
        if os.path.exists(p):
            b = base64.b64encode(io.open(p, "rb").read()).decode()
            return (f'<div class="slot {cls}"><img src="data:{MIME[ext]};base64,{b}" '
                    f'alt="{name}"></div>')
    return f'<div class="slot {cls}"><span class="wm">{name}</span></div>'


def footer():
    """Two columns. Left: who bought, named and counted. Right: who we build with, and what
    we build from. The provenance line moved here when the source line came off the sheet."""
    t = "".join(slot(n) for n in TRUSTED)
    p = "".join(slot(n, "big") for n in PARTNERS)
    a = "".join(slot(n, "big accel") for n in ACCEL)
    return ('<div class="fcol left">'
            '<div class="lb">TRUSTED BY</div>'
            f'<div class="slots">{t}</div>'
            f'<div class="morerow">{chart_trusted()}'
            '<div class="more">and 10 more energy, utility and enterprise accounts '
            'across ASEAN &amp; North Asia</div>'
'</div></div>'
            '<div class="fcol right">'
            '<div class="frow"><div class="lb">PARTNERS</div>'
            f'<div class="slots">{p}</div></div>'
            '<div class="frow"><div class="lb wide">OUR ACCELERATORS</div>'
            f'<div class="slots">{a}</div></div></div>')
