# -*- coding: utf-8 -*-
"""v8 drawn data, modules and footer. Replaces everything below line 227 of build_v8.py.

EVERY CHART IS DRAWN AT 1:1. A chart's viewBox width equals the number of CSS pixels it is
shown at, so a label declared 16px renders at 16px. In v7 the three AI Adoption charts were
drawn in a 322-unit box shown at 216px, which silently shrank an 11px label to 7.38px - the
smallest text on the sheet and the reason it could not be read. Nothing here is scaled.

TYPE FLOOR. The bar is a printed A3 landscape read at 50 cm, k = 0.84, on a 1754px canvas:
x-height >= 7.29px and cap height >= 9.72px. BR Omega Regular is x/em 0.470 and cap/em 0.700,
so mixed case is never below 16px and ALL CAPS is never below 14.5px, anywhere, including
inside every chart.
"""
FS_BODY = 16        # mixed case floor: 16 * 0.470 = 7.52px x-height = 12.4 arcmin
FS_CAPS = 14.5      # all caps floor:  14.5 * 0.700 = 10.15px cap height = 16.7 arcmin


def _t(x, y, s, size=FS_BODY, fill="var(--ink)", weight=None, anchor=None,
       family="body", ls=None):
    a = [f'x="{x}"', f'y="{y}"', f'font-family="var(--font-{family})"',
         f'font-size="{size}"', f'fill="{fill}"']
    if weight:
        a.append(f'font-weight="{weight}"')
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    if ls:
        a.append(f'letter-spacing="{ls}"')
    return "<text " + " ".join(a) + f">{s}</text>"


def _cap(x, y, s, fill="var(--ink-muted)"):
    return _t(x, y, s, FS_CAPS, fill, weight="700", ls=".7")


def chart_wins(num, WINS, OFF, SLOT):
    """Win count as a pictogram. Counts from the internal template."""
    n = WINS[num][0]
    if n is None:
        return ""
    c = SLOT[OFF[num][1]]
    w = 6 + n * 26
    marks = "".join(f'<circle cx="{13 + i * 26}" cy="14" r="9" fill="{c}" stroke="var(--ink)" '
                    f'stroke-width="1.5"/>' for i in range(n))
    return (f'<svg data-viz="magnitude:wins-{num}" class="cv wins" viewBox="0 0 {w} 28" '
            f'style="width:{w}px">{marks}</svg>')


def chart_phases(PHASES, w=1020):
    """Step flow + dimensioned durations. Phase names slide 7; 2 wks and 7 wks slide 18."""
    gap, n = 12, len(PHASES)
    cw = (w - gap * (n - 1)) / n
    chips = ""
    for i, p in enumerate(PHASES):
        x = i * (cw + gap)
        chips += (f'<rect x="{x:.1f}" y="2" width="{cw:.1f}" height="34" '
                  f'fill="var(--surface-2)" stroke="var(--ink)" stroke-width="1.25"/>'
                  + _t(x + cw / 2, 25, p, FS_BODY, anchor="middle"))
        if i < n - 1:
            chips += (f'<path d="M{x + cw + 1:.1f} 19 H{x + cw + gap - 1:.1f}" '
                      f'stroke="var(--ink-muted)" stroke-width="1.25" fill="none"/>')
    y0 = 74
    unit = w / 9.0
    w2, w7 = 2 * unit, 7 * unit
    return f'''<svg data-viz="process:datahub-phases" class="cv" viewBox="0 0 {w} 150">
  {chips}
  {_t(0, y0 - 8, "assessment", FS_BODY, "var(--ink-muted)")}
  {_t(w2 + 8, y0 - 8, "proof of concept", FS_BODY, "var(--ink-muted)")}
  <rect x="0" y="{y0}" width="{w2:.1f}" height="26" fill="url(#hxd)"
        stroke="var(--ink)" stroke-width="1.5"/>
  <rect x="{w2:.1f}" y="{y0}" width="{w7:.1f}" height="26" fill="var(--c-blue)"
        stroke="var(--ink)" stroke-width="1.5"/>
  <g stroke="var(--ink)" stroke-width="1.25" fill="none">
    <path d="M1 {y0 + 30} V{y0 + 52}"/><path d="M{w2:.1f} {y0 + 30} V{y0 + 52}"/>
    <path d="M{w - 1} {y0 + 30} V{y0 + 52}"/>
    <path d="M3 {y0 + 43} H{w2 - 3:.1f}" marker-start="url(#al)" marker-end="url(#ar)"/>
    <path d="M{w2 + 3:.1f} {y0 + 43} H{w - 3}" marker-start="url(#al)" marker-end="url(#ar)"/>
  </g>
  <rect x="{w2 / 2 - 34:.1f}" y="{y0 + 31}" width="68" height="24" fill="var(--bg)"/>
  {_t(w2 / 2, y0 + 49, "2 WKS", FS_CAPS, weight="700", anchor="middle", ls=".7")}
  <rect x="{w2 + w7 / 2 - 34:.1f}" y="{y0 + 31}" width="68" height="24" fill="var(--bg)"/>
  {_t(w2 + w7 / 2, y0 + 49, "7 WKS", FS_CAPS, weight="700", anchor="middle", ls=".7")}
</svg>'''


def chart_funding(w=210):
    """AIX Hub: the funding arrangement slide 44 states in words. No values exist, none drawn.
    Stacked, not side by side: at 210px there is no room for two labelled tracks in a row."""
    return f'''<svg data-viz="relation:aix-funding" class="cv" viewBox="0 0 {w} 132">
  {_cap(0, 13, "CO-FUNDED SPRINT")}
  <rect x="0" y="20" width="{w}" height="26" fill="url(#hxa)" stroke="var(--ink)"
        stroke-width="1.5"/>
  <path d="M{w / 2} 48 V{60}" stroke="var(--ink)" stroke-width="1.25" fill="none"/>
  <circle cx="{w / 2}" cy="69" r="9" fill="var(--bg)" stroke="var(--ink)" stroke-width="1.25"/>
  {_t(w / 2 + 16, 74, "screening", FS_BODY, "var(--ink-muted)")}
  <path d="M{w / 2} 78 V{90}" stroke="var(--ink)" stroke-width="1.25" fill="none"
        marker-end="url(#ar)"/>
  {_cap(0, 108, "INTERNAL BUDGET")}
  <rect x="0" y="114" width="{w}" height="18" fill="none" stroke="var(--ink-muted)"
        stroke-width="1.25" stroke-dasharray="6 5"/>
</svg>'''


def chart_gate(w=210):
    """AI Fast Track: two weeks, then the full project it unlocks. Duration slide 44."""
    bw = w * 0.56
    return f'''<svg data-viz="time:fasttrack-gate" class="cv" viewBox="0 0 {w} 132">
  {_cap(0, 13, "PROOF OF VALUE")}
  <rect x="0" y="20" width="{bw:.0f}" height="26" fill="var(--c-dvb)" stroke="var(--ink)"
        stroke-width="1.5"/>
  <g stroke="var(--ink)" stroke-width="1.25" fill="none">
    <path d="M1 50 V68"/><path d="M{bw:.0f} 50 V68"/>
    <path d="M3 60 H{bw - 3:.0f}" marker-start="url(#al)" marker-end="url(#ar)"/>
  </g>
  <rect x="{bw / 2 - 34:.0f}" y="49" width="68" height="23" fill="var(--bg)"/>
  {_t(bw / 2, 66, "2 WKS", FS_CAPS, weight="700", anchor="middle", ls=".7")}
  <path d="M{w / 2} 76 V{90}" stroke="var(--ink)" stroke-width="1.25" fill="none"
        marker-end="url(#ar)"/>
  {_cap(0, 108, "FULL PROJECT")}
  <rect x="0" y="114" width="{w}" height="18" fill="none" stroke="var(--ink-muted)"
        stroke-width="1.25" stroke-dasharray="6 5"/>
</svg>'''


def chart_pod(w=210):
    """Forward Deployed Pod: the nesting slide 44 states, FPT engineers inside the team."""
    return f'''<svg data-viz="relation:pod-nesting" class="cv" viewBox="0 0 {w} 132">
  {_cap(0, 13, "CLIENT TEAM")}
  <rect x="0" y="20" width="{w}" height="86" fill="none" stroke="var(--ink-muted)"
        stroke-width="1.25" stroke-dasharray="6 5"/>
  <g stroke="var(--ink-muted)" stroke-width="1.5" fill="none">
    <circle cx="28" cy="42" r="10"/><circle cx="60" cy="42" r="10"/>
    <circle cx="92" cy="42" r="10"/><circle cx="124" cy="42" r="10"/>
  </g>
  <rect x="12" y="66" width="{w - 24}" height="30" fill="url(#hxa)" stroke="var(--ink)"
        stroke-width="1.5"/>
  <rect x="{w / 2 - 56:.0f}" y="70" width="112" height="22" fill="var(--bg)"/>
  {_t(w / 2, 87, "FPT AI POD", FS_CAPS, weight="700", anchor="middle", ls=".7")}
  {_t(0, 126, "embedded, not adjacent", FS_BODY, "var(--ink-muted)")}
</svg>'''


def chart_solutions(DOMAINS, w=300):
    """Ten FleziNergy solutions across four domains, part to whole. The domain names sit in a
    legend rather than under 30px segments, where they were unreadable and collided."""
    total = sum(n for _, n in DOMAINS)
    seg, x = "", 0.0
    for i, (name, n) in enumerate(DOMAINS):
        sw = w * n / total
        fill = "var(--c-green)" if i < 2 else "url(#hxe)"
        op = "1" if i != 1 else ".55"
        seg += (f'<rect x="{x:.1f}" y="20" width="{sw - 2:.1f}" height="30" fill="{fill}" '
                f'fill-opacity="{op}" stroke="var(--ink)" stroke-width="1.5"/>'
                + _t(x + (sw - 2) / 2, 41, n, FS_BODY, weight="700", anchor="middle"))
        x += sw
    leg = ""
    for i, (name, n) in enumerate(DOMAINS):
        lx, ly = (0 if i % 2 == 0 else w / 2 + 6), (70 if i < 2 else 94)
        fill = "var(--c-green)" if i < 2 else "url(#hxe)"
        op = "1" if i != 1 else ".55"
        leg += (f'<rect x="{lx:.0f}" y="{ly - 12}" width="14" height="14" fill="{fill}" '
                f'fill-opacity="{op}" stroke="var(--ink)" stroke-width="1.25"/>'
                + _t(lx + 20, ly, f'<tspan font-weight="700">{n}</tspan> {name}', FS_BODY))
    return f'''<svg data-viz="part-to-whole:flezi-solutions" class="cv" viewBox="0 0 {w} 172">
  {_cap(0, 12, "10 SOLUTIONS")}
  {seg}
  {leg}
  <rect x="0" y="110" width="{w}" height="28" fill="var(--surface-2)"
        stroke="var(--ink-muted)" stroke-width="1.25"/>
  {_t(w / 2, 129, "core services in energy", FS_BODY, anchor="middle")}
  <rect x="0" y="142" width="{w}" height="28" fill="var(--surface-2)"
        stroke="var(--ink-muted)" stroke-width="1.25"/>
  {_t(w / 2, 161, "foundation for AI platform", FS_BODY, anchor="middle")}
</svg>'''


def chart_reductions(RED, w=520, pitch=34):
    """Six self-reported reductions. One unit, one direction, zero based (standing rule)."""
    x_track, track = 48, 160
    x_lab = x_track + track + 16
    rows, y = "", 4
    for lab, v, name, what in RED:
        bw = track * v / 100.0
        rows += (_t(0, y + 19, lab, FS_BODY, "var(--c-blue)", weight="800")
                 + f'<rect x="{x_track}" y="{y + 4}" width="{track}" height="21" '
                   f'fill="var(--surface-2)" stroke="var(--ink-muted)" stroke-width="1.25"/>'
                 + f'<rect x="{x_track}" y="{y + 4}" width="{bw:.1f}" height="21" '
                   f'fill="var(--c-blue)" stroke="var(--ink)" stroke-width="1.25"/>'
                 + _t(x_lab, y + 19,
                      f'<tspan font-weight="700">{name}</tspan> '
                      f'<tspan fill="var(--ink-muted)">{what}</tspan>', FS_BODY))
        y += pitch
    return (f'<svg data-viz="category:flezi-reductions" class="cv" viewBox="0 0 {w} '
            f'{4 + 6 * pitch}">{rows}</svg>')


def chart_trusted(named, more, w=430):
    """Accounts, as a count rather than a footnote. Slide 44 names seven and says
    "and 10 more", so seventeen marks: seven filled, ten open. Added in v8 to hold the
    eleven-representation floor when the delivery-model block came off the sheet."""
    total = named + more
    step = w / total
    marks = ""
    for i in range(total):
        cx = step / 2 + i * step
        if i < named:
            marks += (f'<circle cx="{cx:.1f}" cy="14" r="7.5" fill="var(--c-blue)" '
                      f'stroke="var(--ink)" stroke-width="1.25"/>')
        else:
            marks += (f'<circle cx="{cx:.1f}" cy="14" r="7.5" fill="none" '
                      f'stroke="var(--ink-muted)" stroke-width="1.25"/>')
    return f'''<svg data-viz="magnitude:trusted-count" class="cv" viewBox="0 0 {w} 28"
     style="width:{w}px">{marks}</svg>'''


def statrows(items, cls):
    return "".join(f'<div class="sx"><b class="{cls}">{v}</b>'
                   f'<span class="nm">{n}</span><span class="wt">{d}</span></div>'
                   for v, n, d in items)
