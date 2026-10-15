"""Runner: the GEU AI Service Offering sheet, v8. One landscape shape, one audience.

    python work/v8.py client       -> cleared names only, no money   (the sheet An emails)
    python work/v8.py internal     -> every name, every TCV and pipeline figure (FPT only)
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C           # content, charts, modules, footer
import style as S             # css, page shell

AUD, W, H = C.AUDIENCE, C.W, C.H

ZONES = [("d", "Data<br>for AI", "var(--c-blue)"),
         ("a", "AI<br>Adoption", "var(--c-dvb)"),
         ("e", "Energy<br>AI", "var(--c-green)")]

# The hero. 128px, which is 8x the 16px body floor (standing criterion N3). Broken by
# hand onto two lines so the placard leaves the estate drawing room to be a big object.
TITLE_HTML = "GEU AI<br>Service Offering"


def ztag(name, colour):
    return (f'<div class="ztag"><div class="zn">{name}</div>'
            f'<div class="zr" style="background:{colour}"></div></div>')


def zone(cls, name, colour, body):
    return f'<div class="zone">{ztag(name, colour)}<div class="zbody">{body}</div></div>'


top = f'''    <div class="top">
      <img class="logo" src="data:image/png;base64,{C.LOGO}" alt="FPT Software">
      {C.ESTATE}
      <div class="placard">
        <div class="kickrow"><div class="kick">{C.KICKER}</div>{C.STAMP}
          <div class="prov">fptsoftware.com &nbsp;&middot;&nbsp; September 2026</div></div>
        <h1 data-hero>{TITLE_HTML}</h1>
        <div class="standfirst">{C.STANDFIRST}</div>
      </div>
    </div>'''

zA = zone("d", *ZONES[0][1:],
          body='<div class="zA">'
               + C.module("01", '<div class="cvw">' + C.chart_phases() + '</div>')
               + '</div>')

zB = zone("a", *ZONES[1][1:], body=(
    '<div class="zB">'
    + C.module("02", C.chart_funding())
    + C.module("03", C.chart_gate())
    + C.module("04", C.chart_pod())
    + '</div>'))

stats = (f'<div class="statband">'
         f'<div class="sg acc"><div class="sub">ACCURACY</div>'
         f'<div class="rows">{C.statrows(C.ACC, "lvl")}</div></div>'
         f'<div class="sg inc"><div class="sub">INCREASE</div>'
         f'<div class="rows">{C.statrows(C.INC, "up")}</div></div></div>')

zC = zone("e", *ZONES[2][1:], body=(
    f'<div class="zC">'
    f'<div class="cl">{C.module("05", C.chart_solutions())}</div>'
    f'<div class="cr"><div class="sub">REDUCTION &mdash; SELF-REPORTED</div>'
    f'{C.chart_reductions()}</div>'
    f'<div class="cs">{stats}</div></div>'))

sheet = "\n".join([top, zA, zB, zC,
                   '    <div class="spacer"></div>',
                   f'    <div class="foot">{C.footer()}</div>'])

css = S.CSS_BASE + S.CSS_PAGE
html = (S.HEAD.replace("%FONTS%", C.FONTCSS).replace("%CSS%", css)
              .replace("%DEFS%", C.DEFS).replace("%SHEET%", sheet)
              .replace("%AUDIENCE%", AUD))

out = os.path.join(C.BASE, "sheet.html")
io.open(out, "w", encoding="utf-8").write(html)
print(f"built {AUD} {W}x{H}  {len(html) // 1024} KB -> {out}")
