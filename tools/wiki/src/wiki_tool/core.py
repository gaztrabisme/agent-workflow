"""Shared wiki operations. Lint only reads; mutations keep whole dated entries."""

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import os
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
LINK = re.compile(r'(?<!!)\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[^)\n]*)?\)|\[\[([^\]\n]+)\]\]')
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
POINTER = re.compile(r"^Older entries: \[(log-\d{4}-\d{2}\.md)\]\(\1\)\s*$", re.MULTILINE)


def _folder(wiki: str | Path) -> Path:
    folder = Path(wiki).expanduser().resolve()
    if not folder.is_dir():
        raise ValueError(f"wiki folder does not exist: {folder}")
    return folder


def _nonnegative(**values: int) -> None:
    for name, value in values.items():
        if value < 0:
            raise ValueError(f"{name} must be zero or greater")


def _markdown_lines(text: str):
    """Yield prose lines, with fenced and inline code hidden from link parsing."""
    fence = ""
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE.match(line)
        if match:
            marker = match[1]
            if not fence:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = ""
            continue
        if not fence:
            yield number, re.sub(r"(`+).*?\1", "", line)


def _links(text: str):
    for number, line in _markdown_lines(text):
        for match in LINK.finditer(line):
            raw, wikilink = match.groups()
            raw = (wikilink.split("|", 1)[0] if wikilink else raw.strip("<>")).strip()
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                continue
            target = unquote(url.path)
            if wikilink and not Path(target).suffix:
                target += ".md"
            # Only Markdown page links are in scope; anchors are not validated.
            if target.lower().endswith(".md"):
                yield number, target


def _targets(page: Path, folder: Path, target: str) -> tuple[Path, Path]:
    return ((page.parent / target).resolve(), (folder.parent / target).resolve())


def _resolve_link(page: Path, folder: Path, target: str) -> Path | None:
    return next((path for path in _targets(page, folder, target) if path.is_file()), None)


def _reachable(folder: Path, pages: dict[Path, str]) -> set[Path]:
    """Follow resolved Markdown links, including external intermediates and cycles."""
    cached = {path.resolve(): text for path, text in pages.items()}
    pending = [folder / "index.md"]
    visited = set()
    while pending:
        page = pending.pop()
        if page in visited or not page.is_file():
            continue
        visited.add(page)
        text = cached.get(page)
        if text is None:
            text = page.read_text(encoding="utf-8")
        for _, target in _links(text):
            resolved = _resolve_link(page, folder, target)
            if resolved is not None and resolved not in visited:
                pending.append(resolved)
    return visited


def wiki_lint(wiki: str | Path, index_cap: int = 200, log_cap: int = 400) -> dict:
    """Report seven wiki rules, resolving links locally and against the repo root."""
    _nonnegative(index_cap=index_cap, log_cap=log_cap)
    folder = _folder(wiki)
    pages = {p: p.read_text(encoding="utf-8") for p in sorted(folder.rglob("*.md")) if p.is_file()}
    findings = []

    def add(rule, path, message, line=None):
        item = {"rule": rule, "path": str(path.relative_to(folder)), "message": message}
        if line is not None:
            item["line"] = line
        findings.append(item)

    index = folder / "index.md"
    for name, cap, rule in [("index.md", index_cap, "index-over-cap"),
                            ("log.md", log_cap, "log-over-cap")]:
        path = folder / name
        count = len(pages.get(path, "").splitlines())
        if count > cap:
            add(rule, path, f"{count} lines exceeds cap {cap}")

    reachable = _reachable(folder, pages)
    run_links = set()
    for number, target in _links(pages.get(index, "")):
        candidates = _targets(index, folder, target)
        existing = _resolve_link(index, folder, target)
        if existing is None:
            add("index-dead-entry", index, f"missing target: {target}", number)
        resolved = existing or candidates[0]
        try:
            parts = resolved.relative_to(folder).parts
        except ValueError:
            parts = Path(target).parts
        if resolved.name.startswith("run-") or "runs" in parts:
            run_links.add(resolved)
    if len(run_links) > 1:
        add("run-report-in-index", index, f"{len(run_links)} run report links; at most one roll-up allowed")

    for page, text in pages.items():
        relative = page.relative_to(folder)
        # Source copies retain their original link bases and metadata. Exempt
        # them from these page findings, while allowing graph traversal above.
        if {"inputs", "raw"}.intersection(relative.parts[:-1]):
            continue
        journal = page.name.startswith("log") and page.suffix == ".md"
        if page != index and not journal:
            if not {"runs", "goals"}.intersection(relative.parts[:-1]) and page.resolve() not in reachable:
                add("unreachable", page, "page is unreachable from index.md")
            if not DATE.search(page.name) and not DATE.search("\n".join(text.splitlines()[:15])):
                add("undated-page", page, "no date in filename or first 15 lines")
        for number, target in _links(text):
            if _resolve_link(page, folder, target) is None:
                add("broken-link", page, f"missing target: {target}", number)
    return {"wiki": str(folder), "findings": findings}


@dataclass(frozen=True)
class Entry:
    when: date
    text: str


def _parse_log(text: str) -> tuple[str, list[Entry]]:
    """Split only at dated level-two headings, including date-range headings."""
    starts = []
    offset = 0
    prose_lines = {n for n, _ in _markdown_lines(text)}
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        if number in prose_lines and line.startswith("## "):
            match = DATE.search(line)
            if match:
                try:
                    starts.append((offset, date.fromisoformat(match[0])))
                except ValueError:
                    pass
        offset += len(line)
    if not starts:
        return text, []
    entries = [Entry(when, text[start:starts[i + 1][0] if i + 1 < len(starts) else len(text)])
               for i, (start, when) in enumerate(starts)]
    return text[:starts[0][0]], entries


def _read_log(path: Path) -> tuple[str, list[Entry]]:
    return _parse_log(path.read_text(encoding="utf-8")) if path.exists() else ("# Log\n\n", [])


def _newest_first(entries: list[Entry]) -> bool:
    return len(entries) < 2 or entries[0].when >= entries[-1].when


def _join(parts) -> str:
    """Keep entry bytes, adding just enough newline separation at boundaries."""
    result = ""
    for part in parts:
        if not part:
            continue
        if result:
            result += "\n" * max(0, 2 - (len(result) - len(result.rstrip("\n"))))
        result += part
    if result and not result.endswith("\n"):
        result += "\n"
    return result


def _render(prefix: str, entries: list[Entry]) -> str:
    return _join([prefix, *(entry.text for entry in entries)])


def _write(path: Path, text: str) -> None:
    """Replace one file atomically; temporary files stay beside the destination."""
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=f".{path.name}.", delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(text)
            stream.close()
            if path.exists():
                temporary.chmod(path.stat().st_mode)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def _git(folder: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(folder), *args], capture_output=True, text=True, check=False)
    except FileNotFoundError:
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def _log_path(folder: Path) -> Path:
    common = _git(folder, "rev-parse", "--path-format=absolute", "--git-common-dir")
    git_dir = _git(folder, "rev-parse", "--path-format=absolute", "--git-dir")
    if common and git_dir and Path(common).resolve() != Path(git_dir).resolve():
        branch = _git(folder, "branch", "--show-current")
        if not branch:
            branch = "detached-" + (_git(folder, "rev-parse", "--short", "HEAD") or "HEAD")
        return folder / f"log.{branch.replace('/', '-')}.md"
    return folder / "log.md"


def wiki_log(wiki: str | Path, kind: str, text: str) -> dict:
    """Add a local-date entry, preserving the log's direction and existing text."""
    if not kind.strip() or not text.strip() or "\n" in kind + text or "\r" in kind + text:
        raise ValueError("kind and text must be nonempty single lines")
    folder = _folder(wiki)
    path = _log_path(folder)
    prefix, entries = _read_log(path)
    today = date.today()
    entry = Entry(today, f"## [{today.isoformat()}] {kind} | {text}\n")
    original = prefix + "".join(item.text for item in entries)
    if _newest_first(entries):
        title, separator, rest = original.partition("\n")
        if title.startswith("# "):
            updated = _join([title + separator, entry.text, rest.lstrip("\n")])
        else:
            updated = _join([entry.text, original])
    else:
        updated = _join([original, entry.text])
    _write(path, updated)
    return {"wiki": str(folder), "path": str(path), "entry": entry.text.strip()}


def wiki_rotate(wiki: str | Path, max_lines: int = 400, keep_days: int = 30,
                dry_run: bool = False) -> dict:
    """Archive old whole entries only when log.md exceeds its line cap."""
    _nonnegative(max_lines=max_lines, keep_days=keep_days)
    folder = _folder(wiki)
    path = folder / "log.md"
    result = {"wiki": str(folder), "dry_run": dry_run, "moved_entries": 0, "archives": {}}
    if not path.exists() or len(path.read_text(encoding="utf-8").splitlines()) <= max_lines:
        return result
    original = path.read_text(encoding="utf-8")
    # Archive pointers are log metadata; don't let them move with a later entry
    # when that entry itself eventually ages out.
    pointers = set()
    content = []
    prose_lines = {n for n, _ in _markdown_lines(original)}
    for number, line in enumerate(original.splitlines(keepends=True), 1):
        match = POINTER.fullmatch(line.rstrip("\r\n")) if number in prose_lines else None
        if match:
            pointers.add(match[1])
        else:
            content.append(line)
    prefix, entries = _parse_log("".join(content))
    cutoff = date.today() - timedelta(days=keep_days)
    moved = defaultdict(list)
    remaining = []
    for entry in entries:
        if entry.when < cutoff:
            moved[f"log-{entry.when:%Y-%m}.md"].append(entry)
        else:
            remaining.append(entry)
    result["moved_entries"] = sum(len(group) for group in moved.values())
    result["archives"] = {name: len(group) for name, group in sorted(moved.items())}
    if dry_run or not moved:
        return result
    for name, group in sorted(moved.items()):
        archive = folder / name
        archive_prefix, archived = _read_log(archive)
        direction = _newest_first(archived if archived else entries)
        combined = sorted([*archived, *group], key=lambda entry: entry.when, reverse=direction)
        _write(archive, _render(archive_prefix, combined))
    text = _render(prefix, remaining)
    for name in sorted(pointers | moved.keys()):
        text = _join([text, f"Older entries: [{name}]({name})\n"])
    _write(path, text)
    return result


def wiki_merge_logs(wiki: str | Path, dry_run: bool = False) -> dict:
    """Merge all branch logs in log.md's date direction, then remove branch files."""
    folder = _folder(wiki)
    path = folder / "log.md"
    prefix, entries = _read_log(path)
    branch_files = sorted(p for p in folder.glob("log.*.md") if p.is_file())
    incoming = []
    for branch in branch_files:
        branch_prefix, branch_entries = _read_log(branch)
        # Refuse to silently discard unstructured branch content on deletion.
        if any(line.strip() and not line.startswith("# ") for line in branch_prefix.splitlines()):
            raise ValueError(f"branch log has text before its dated entries: {branch.name}")
        incoming.extend(branch_entries)
    result = {"wiki": str(folder), "dry_run": dry_run, "merged_entries": len(incoming),
              "branch_files": [p.name for p in branch_files]}
    if dry_run or not branch_files:
        return result
    combined = sorted([*entries, *incoming], key=lambda entry: entry.when, reverse=_newest_first(entries))
    _write(path, _render(prefix, combined))
    for branch in branch_files:
        branch.unlink()
    return result
