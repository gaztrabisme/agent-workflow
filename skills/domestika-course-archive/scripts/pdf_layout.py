"""Create annotated, printable reading copies of Domestika unit pages."""

from __future__ import annotations

import html
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ALLOWED = {
    'a', 'b', 'blockquote', 'br', 'code', 'div', 'em', 'h2', 'h3', 'h4',
    'i', 'img', 'li', 'ol', 'p', 'span', 'strong', 'u', 'ul',
}
VOID = {'br', 'img'}
HTML_VOID = VOID | {'area', 'base', 'col', 'embed', 'hr', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class SafeHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if tag not in ALLOWED:
            if tag not in HTML_VOID:
                self.stack.append('')
            return
        attr = dict(attrs)
        extras = ''
        if tag == 'a':
            url = attr.get('href', '')
            if urlparse(url).scheme in ('http', 'https'):
                extras = f' href="{html.escape(url, quote=True)}"'
        elif tag == 'img':
            url = attr.get('src', '')
            if urlparse(url).scheme in ('http', 'https'):
                extras = (f' src="{html.escape(url, quote=True)}"'
                          f' alt="{html.escape(attr.get("alt") or "", quote=True)}"')
            else:
                return
        self.parts.append(f'<{tag}{extras}>')
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]):
        self.handle_starttag(tag, attrs)
        if tag not in HTML_VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str):
        if not self.stack:
            return
        opened = self.stack.pop()
        if opened:
            self.parts.append(f'</{opened}>')

    def handle_data(self, data: str):
        self.parts.append(html.escape(data))

    def finish(self) -> str:
        while self.stack:
            opened = self.stack.pop()
            if opened:
                self.parts.append(f'</{opened}>')
        return ''.join(self.parts)


def safe_fragment(fragment: str) -> str:
    parser = SafeHTML()
    parser.feed(fragment)
    return parser.finish()


def duration(seconds: float) -> str:
    minutes, seconds = divmod(round(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours}:{minutes:02}:{seconds:02}' if hours else f'{minutes}:{seconds:02}'


def unit_html(course: dict, unit: dict, names: dict[int, str],
              caption_languages_by_lesson: dict[int, list[str]]) -> str:
    e = html.escape
    title = e(unit['title'])
    original = e(unit['url'], quote=True)
    lessons = []
    for lesson in sorted(unit['lessons'], key=lambda item: item['number']):
        basename = names[lesson['id']]
        caption_rows = ''.join(
            f'<div class="file"><span>CAPTIONS</span> {e(basename)}.{e(language.replace("-", "_").lower())}.vtt</div>'
            for language in caption_languages_by_lesson[lesson['id']])
        source = e(lesson['url'], quote=True)
        lessons.append(f'''
          <section class="lesson">
            <div class="lesson-head">
            <div class="lesson-number">LESSON {lesson['number']:02d} · {duration(lesson['duration_seconds'])}</div>
            <h2>{e(lesson['title'])}</h2>
            <div class="video-slot">
              <div class="play-icon">▶</div>
              <div>
                <strong>Video at this point in the original page</strong>
                <div class="file"><span>VIDEO</span> {e(basename)}.mp4</div>
                {caption_rows}
                <div class="source"><a href="{source}">Open this lesson on Domestika</a></div>
              </div>
            </div>
            </div>
            <div class="lesson-text">{safe_fragment(lesson.get('transcript_html') or '')}</div>
          </section>''')
    extras = []
    for extra in unit.get('extras', []):
        extras.append(f'<section class="extras">'
                      f'{safe_fragment(extra.get("html") or "")}</section>')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
      <title>Unit {unit['number']:02d} - {title}</title>
      <style>
        @page {{ size: A4; margin: 16mm 17mm 16mm; }}
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, Helvetica, sans-serif; color: #202020; font-size: 10pt; line-height: 1.42; margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
        a {{ color: #aa270d; text-decoration: none; overflow-wrap: anywhere; }}
        .eyebrow {{ color: #ad2b12; font-size: 8pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }}
        .cover {{ border-bottom: 2px solid #232323; padding: 0 0 17px; margin-bottom: 23px; }}
        h1 {{ font-size: 25pt; line-height: 1.14; margin: 6px 0 8px; letter-spacing: -.03em; }}
        .course {{ color: #777; font-size: 10pt; }}
        .original {{ margin-top: 7px; font-size: 8pt; }}
        h2 {{ font-size: 16pt; line-height: 1.2; letter-spacing: -.02em; margin: 4px 0 13px; break-after: avoid; }}
        h3 {{ font-size: 11pt; margin: 13px 0 5px; break-after: avoid-page; page-break-after: avoid; }}
        p {{ margin: 0 0 8px; }}
        ul,ol {{ padding-left: 21px; }}
        li {{ margin: 0 0 3px; break-inside: avoid-page; page-break-inside: avoid; }}
        img {{ max-width: 100%; max-height: 95mm; object-fit: contain; }}
        .intro {{ margin-bottom: 22px; }}
        .lesson {{ border-top: 1px solid #d7d7d7; padding-top: 14px; margin-top: 20px; break-inside: auto; }}
        .lesson-head {{ break-inside: avoid; }}
        .lesson-number {{ color: #777; font-size: 8pt; letter-spacing: .07em; font-weight: 700; }}
        .lesson h2 {{ break-after: avoid; }}
        .video-slot {{ display: flex; gap: 16px; background: #f5f3f1; border-left: 4px solid #e43a15; padding: 12px 16px; margin: 10px 0 13px; break-inside: avoid; }}
        .play-icon {{ font-size: 22pt; color: #e43a15; line-height: 1; }}
        .video-slot strong {{ display: block; margin: 0 0 8px; }}
        .file {{ font-family: Menlo, Consolas, monospace; font-size: 8.5pt; overflow-wrap: anywhere; margin: 4px 0; }}
        .file span {{ color: #777; display: inline-block; width: 75px; font: 700 7pt Arial, sans-serif; letter-spacing: .04em; }}
        .source {{ font-size: 8pt; margin-top: 9px; }}
        .lesson-text {{ margin: 14px 0; }}
        .extras {{ border-top: 1px solid #d7d7d7; padding-top: 16px; margin-top: 20px; }}
        .extras h2 {{ text-transform: uppercase; font-size: 12pt; letter-spacing: .04em; }}
        .extras section, .extras .section {{ margin-bottom: 13px; }}
        .extras img {{ display: block; margin: 8px 0; }}
        .footnote {{ color: #888; font-size: 8pt; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 22px; }}
      </style></head><body>
      <header class="cover"><div class="eyebrow">Domestika · Unit {unit['number']:02d}</div>
      <h1>{title}</h1><div class="course">{e(course['course_title'])}</div>
      <div class="original"><a href="{original}">Original unit page</a></div></header>
      <div class="intro">{safe_fragment(unit.get('intro_html') or '')}</div>
      {''.join(lessons)}{''.join(extras)}
      <div class="footnote">Annotated reading copy · Video files and timed captions are stored beside this PDF in the unit folder.</div>
      </body></html>'''


def render_pdf(chrome: str, html_path: Path, pdf_path: Path) -> None:
    from archive_core.packaging import localize_images
    from archive_core.privacy import scan_file
    document = localize_images(html_path.read_text(encoding='utf-8'))
    html_path.write_text(document, encoding='utf-8')
    scan_file(html_path)
    command = [chrome, '--headless', '--disable-gpu', '--no-first-run',
               '--disable-background-networking', '--host-resolver-rules=MAP * ~NOTFOUND', '--virtual-time-budget=10000',
               '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}', html_path.as_uri()]
    run = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if run.returncode or not pdf_path.exists() or pdf_path.stat().st_size < 3000:
        raise RuntimeError(f'Chrome could not make {pdf_path.name}.')
    scan_file(pdf_path)
