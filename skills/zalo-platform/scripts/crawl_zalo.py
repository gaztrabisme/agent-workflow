#!/usr/bin/env python3
"""Re-crawl the Zalo documentation surfaces into the skill's knowledge base.

TWO UNLOCKS THIS SCRIPT ENCODES
-------------------------------
**1. Sitemaps, not link-following.** Every Zalo doc site is Docusaurus, and
Docusaurus renders its *sidebar tree client-side*. The server HTML of a doc page
contains only the top-level product nav — about a dozen links. A link-following
crawler therefore reaches ~12 pages and quietly reports success. Each site
publishes a `sitemap.xml` with the full page list; that is the only reliable
frontier. (Measured: link-following got 12 developer pages, the sitemap has 318.)

**2. The iframe/CDN substitution (legacy hosts).** `developers.zalo.me` serves
its docs inside an IFRAME pointing at a Docusaurus CDN, so fetching the
developers.zalo.me URL returns a contentless shell — which once led a research
round to conclude the docs were un-crawlable and to hand-drive a browser instead.
The sitemap lists `developers.zalo.me/docs/<path>`; rewrite the host and insert
`/v2/` and it is ordinary server-rendered HTML:

    https://developers.zalo.me/docs/<path>
      -> https://stc-developers.zdn.vn/docs/v2/<path>

**Documentation moved (observed 2026-08-06).** Zalo consolidated its developer
docs onto a new unified hub, `docs.zaloplatforms.com`, covering Mini App (MA),
Official Account (OA), ZBS, Social, Bot (BOT) and TS in one sitemap.
`miniapp.zaloplatforms.com/documents/*` now 302s there, and the legacy CDN has
been **decommissioned in place**: all 317 of its URLs still answer 200, but every
one serves a ~450-character placeholder instead of its article. It is still
crawled, as a tripwire — see the `developers-legacy` entry below.

WHAT IT DOES NOT DO
-------------------
Values a page computes in the browser are invisible here: accordion bodies that
expand on click, price tables behind a 6-month/1-year toggle, and estimator
widgets. Those need `chrome-devtools` navigation — the crawl records the page,
navigation reads the state. See references/re-research-protocol.md §3.

Usage:
    crawl_zalo.py                          # crawl every source into the KB
    crawl_zalo.py -s bot -s miniapp        # only these sources
    crawl_zalo.py --out /tmp/zalo-new      # crawl elsewhere (for a diff)
    crawl_zalo.py --max-pages 50           # smoke test
    crawl_zalo.py --dry-run                # resolve sitemaps, print counts, exit

Then diff against the shipped corpus:
    staleness_check.py --new /tmp/zalo-new
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

DEFAULT_OUT = Path(__file__).resolve().parent.parent / "references" / "knowledge-base"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)

def _cdn(url: str) -> str:
    """developers.zalo.me/docs/X -> the CDN host that actually serves content."""
    return url.replace(
        "https://developers.zalo.me/docs/", "https://stc-developers.zdn.vn/docs/v2/"
    )


# Per source:
#   sitemaps  — the authoritative frontier (Docusaurus renders its sidebar in JS,
#               so link-following is not a substitute; see module docstring)
#   keep      — substring a sitemap URL must contain to be crawled
#   rewrite   — optional URL transform applied after filtering
#   seeds     — extra pages absent from any sitemap
#   allow     — prefixes a *discovered link* may match (link-following is only a
#               top-up for sites with no usable sitemap, i.e. the marketing hosts)
SOURCES: dict[str, dict] = {
    # The new unified hub: Mini App, OA, ZBS, Social, Bot, TS.
    "platform-docs": {
        "sitemaps": ["https://docs.zaloplatforms.com/sitemap.xml"],
        "keep": "docs.zaloplatforms.com/docs/",
        "seeds": [],
        "allow": [],
    },
    # Legacy developer CDN. DECOMMISSIONED IN PLACE as of 2026-08-06: all 317
    # sitemap URLs still return HTTP 200, but every one now serves a ~450-char
    # marketing placeholder ("Tell me about it! Explore our guide to your
    # suitable solutions by our latest documentation") instead of its article.
    # The content lives on `platform-docs`.
    #
    # Kept in the crawl deliberately, as a TRIPWIRE: if these pages ever regain
    # content, or if the new hub loses some, the diff says so. A 200 with a
    # placeholder body is exactly the failure a status-code check cannot see —
    # which is why staleness_check compares text, not status.
    "developers-legacy": {
        "sitemaps": ["https://stc-developers.zdn.vn/docs/sitemap.xml"],
        "keep": "developers.zalo.me/docs/",
        "rewrite": _cdn,
        "seeds": [],
        "allow": [],
    },
    "bot": {
        "sitemaps": ["https://bot.zapps.me/sitemap.xml"],
        "keep": "bot.zapps.me/",
        "seeds": ["https://bot.zapps.me/"],
        "allow": ["bot.zapps.me/"],
    },
    # Commercial + policy pages. No usable sitemap -> link-following, which is
    # adequate here because these are ordinary server-rendered marketing pages.
    "solutions": {
        "sitemaps": [],
        "keep": "",
        "seeds": [
            "https://zalo.solutions/",
            "https://zalo.solutions/oa/pricing",
            "https://zalo.solutions/business-message/pricing",
            "https://zalo.solutions/zns/pricing",
            "https://oa.zalo.me/home",
            "https://oa.zalo.me/home/documents/guides",
        ],
        "allow": ["zalo.solutions/", "oa.zalo.me/home"],
    },
}

SKIP_EXT = re.compile(r"\.(png|jpe?g|gif|svg|webp|ico|css|js|zip|pdf|mp4|woff2?)$", re.I)
LOC = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.I)


class _Text(HTMLParser):
    """Minimal HTML -> text. Keeps <title>, drops script/style/noscript."""

    _DROP = {"script", "style", "noscript", "svg"}
    _BREAK = {
        "p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
        "section", "article", "header", "footer", "nav", "td", "th",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.links: list[str] = []
        self.title = ""
        self._drop = 0
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in self._DROP:
            self._drop += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)
        if tag in self._BREAK:
            self.parts.append("\n")
        if tag in ("td", "th"):
            self.parts.append("\t")

    def handle_endtag(self, tag):
        if tag in self._DROP and self._drop:
            self._drop -= 1
        elif tag == "title":
            self._in_title = False
        if tag in self._BREAK:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._drop:
            return
        if self._in_title:
            self.title += data.strip()
        else:
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts)
        raw = re.sub(r"[ \t\xa0]+", " ", raw)
        lines = [ln.strip() for ln in raw.splitlines()]
        return "\n".join(ln for ln in lines if ln)


def slug(url: str) -> str:
    """URL -> stable filename, matching the 2026-07-21 archive's convention."""
    p = urllib.parse.urlsplit(url)
    path = p.path.rstrip("/")
    name = (p.netloc + path).replace("/", "__")
    name = re.sub(r"[^A-Za-z0-9_.\-]", "_", name)
    return name[:180]


def fetch(url: str, timeout: int) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "vi,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            if "html" not in ctype and "text" not in ctype:
                return r.status, ""
            charset = r.headers.get_content_charset() or "utf-8"
            return r.status, r.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # noqa: BLE001 — a dead link must not kill the crawl
        print(f"    ! {type(e).__name__}: {e}", file=sys.stderr)
        return 0, ""


def sitemap_urls(cfg: dict, timeout: int) -> list[str]:
    """Resolve a source's sitemaps into a crawl frontier.

    Handles sitemap indexes (a sitemap whose <loc>s are themselves .xml) one
    level deep, and applies the source's keep-filter and URL rewrite.
    """
    found: list[str] = []
    pending = list(cfg.get("sitemaps") or [])
    fetched: set[str] = set()
    depth = 0
    while pending and depth < 2:
        nxt: list[str] = []
        for sm in pending:
            if sm in fetched:
                continue
            fetched.add(sm)
            status, body = fetch(sm, timeout)
            if status != 200 or not body:
                print(f"    ! sitemap {status}: {sm}", file=sys.stderr)
                continue
            for loc in LOC.findall(body):
                (nxt if loc.lower().endswith(".xml") else found).append(loc)
        pending, depth = nxt, depth + 1

    keep = cfg.get("keep") or ""
    rewrite = cfg.get("rewrite")
    out, seen = [], set()
    for u in found:
        if keep and keep not in u:
            continue
        if rewrite:
            u = rewrite(u)
        u = u.split("#")[0]
        if u not in seen and not SKIP_EXT.search(u):
            seen.add(u)
            out.append(u)
    return out


def crawl_source(
    name: str, cfg: dict, out: Path, *, delay: float, timeout: int, max_pages: int
) -> list[dict]:
    seen: set[str] = set()
    frontier = sitemap_urls(cfg, timeout)
    if cfg.get("sitemaps"):
        print(f"  sitemap frontier: {len(frontier)} urls")
    queue: deque[str] = deque(list(cfg["seeds"]) + frontier)
    records: list[dict] = []
    tdir = out / "text" / name
    tdir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    while queue and len(records) < max_pages:
        url = queue.popleft()
        canon = url.split("#")[0]
        if canon in seen:
            continue
        seen.add(canon)

        status, html = fetch(canon, timeout)
        if status != 200 or not html:
            if status:
                records.append(
                    {"source": name, "url": canon, "title": "", "status": status,
                     "text_chars": 0, "text": "", "fetched": today}
                )
                print(f"  [{status}] {canon}")
            continue

        parser = _Text()
        try:
            parser.feed(html)
        except Exception:  # noqa: BLE001 — malformed markup shouldn't abort
            pass
        body = parser.text()

        rel = f"text/{name}/{slug(canon)}.txt"
        # The 3-line header is the citation anchor — kb_search.py and every
        # digest in this skill depend on it. Do not change its shape.
        (out / rel).write_text(
            f"# SOURCE: {canon}\n# FETCHED: {today}\n# TITLE: {parser.title}\n\n{body}\n",
            encoding="utf-8",
        )
        records.append(
            {"source": name, "url": canon, "title": parser.title, "status": 200,
             "text_chars": len(body), "text": rel, "fetched": today}
        )
        print(f"  [200] {len(body):7d}ch  {canon}")

        for href in parser.links:
            nxt = urllib.parse.urljoin(canon, href).split("#")[0]
            if not nxt.startswith(("http://", "https://")) or SKIP_EXT.search(nxt):
                continue
            bare = nxt.split("://", 1)[1]
            if any(bare.startswith(a) or a in bare for a in cfg["allow"]) and nxt not in seen:
                queue.append(nxt)

        time.sleep(delay)

    return records


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-s", "--source", action="append", choices=sorted(SOURCES), help="repeatable; default all")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output root (default {DEFAULT_OUT})")
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests (default 0.4 — be polite)")
    ap.add_argument("--timeout", type=int, default=25)
    ap.add_argument("--max-pages", type=int, default=1200, help="cap PER SOURCE")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    names = args.source or list(SOURCES)
    if args.dry_run:
        total = 0
        for n in names:
            cfg = SOURCES[n]
            urls = sitemap_urls(cfg, args.timeout)
            total += len(urls) + len(cfg["seeds"])
            print(f"\n{n}: {len(urls)} from sitemap + {len(cfg['seeds'])} seeds")
            for u in urls[:4]:
                print(f"    {u}")
            if len(urls) > 4:
                print(f"    … {len(urls) - 4} more")
        print(f"\ntotal frontier: {total} (plus links discovered while crawling)")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    all_records: list[dict] = []
    for n in names:
        print(f"\n=== {n} ===")
        all_records += crawl_source(
            n, SOURCES[n], args.out,
            delay=args.delay, timeout=args.timeout, max_pages=args.max_pages,
        )

    mpath = args.out / "manifest.json"
    if mpath.exists() and args.source:
        # Partial crawl: keep records for the sources we did not touch.
        existing = json.load(mpath.open(encoding="utf-8"))
        all_records += [r for r in existing if r["source"] not in names]
    all_records.sort(key=lambda r: (r["source"], r["url"]))
    json.dump(all_records, mpath.open("w", encoding="utf-8"), ensure_ascii=False, indent=1)

    ok = sum(1 for r in all_records if r["status"] == 200)
    thin = sum(1 for r in all_records if r["status"] == 200 and r["text_chars"] < 500)
    print(f"\n{len(all_records)} records · {ok} ok · {thin} thin(<500ch) · manifest {mpath}")
    print("Next: staleness_check.py --new <out> to see what changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
