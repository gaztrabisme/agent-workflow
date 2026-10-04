#!/usr/bin/env python3
"""Stage a skill for claude.ai when it has more than 200 files.

claude.ai accepts at most 200 files per skill zip. This copies a skill into a staging
folder (same exclusions as make-cloud-zips.sh) and merges the many small files of its
reference libraries into a few larger ones. Each merged section starts with a line
"=== FILE: <original path> ===", so a search still finds the original name. Markdown
links in the remaining files are rewritten to the merged files (anchors are dropped).

    cloud_merge.py <skill> <staging-folder>

Prints the staged file count and a content check. Exit 1 if the count is still over 190
or if any link that resolved before no longer resolves.
"""
import os
import re
import shutil
import sys
from pathlib import Path

SKIP_DIRS = {".git", "__pycache__", ".ruff_cache", "local", ".claude", ".inventory"}
SKIP_EXT = {".jpg", ".jpeg", ".png", ".pdf", ".webp", ".gif", ".mp4", ".wav", ".mov", ".zip"}
KEEP = {"README.md", "INDEX.md", "SKILL.md", "BLOCKED.md", "EVOLUTION.md", "NOTICE.md",
        "LICENSE", "manifest.json", "AGENTS.md", "CLAUDE.md", "coverage.md"}
MERGE_EXT = {".md", ".txt"}
MAX_FILES = 190
CHUNK_FILES, CHUNK_BYTES = 40, 450_000

# skill -> (reference roots to merge, folders left out of the cloud copy)
RULES = {
    "color-theory": (["references/color-science"], []),
    "photo": (["references/course-1343", "references/course-227", "references/course-669"],
              ["audit", "tests"]),
    "zalo-platform": (["references/knowledge-base"], []),
}
LINK = re.compile(r"\]\(([^)\s#]+)(#[^)\s]*)?\)")


def copy_tree(src: Path, dst: Path, left_out):
    for root, dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not (rel == Path(".") and d in left_out)]
        (dst / rel).mkdir(parents=True, exist_ok=True)
        for f in files:
            if f == ".DS_Store" or Path(f).suffix.lower() in SKIP_EXT:
                continue
            shutil.copy2(Path(root) / f, dst / rel / f)


def merge_dir(directory: Path, stage: Path, moved: dict):
    files = sorted(p for p in directory.iterdir()
                   if p.is_file() and p.suffix.lower() in MERGE_EXT and p.name not in KEEP)
    if len(files) < 4:
        return
    chunks, cur, size = [], [], 0
    for p in files:
        n = p.stat().st_size
        if cur and (len(cur) >= CHUNK_FILES or size + n > CHUNK_BYTES):
            chunks.append(cur); cur, size = [], 0
        cur.append(p); size += n
    if cur:
        chunks.append(cur)
    for i, group in enumerate(chunks, 1):
        out = directory / f"{directory.name}--part-{i:02d}.md"
        with out.open("w", encoding="utf-8") as fh:
            for p in group:
                fh.write(f"\n=== FILE: {p.relative_to(stage).as_posix()} ===\n\n")
                fh.write(p.read_text(encoding="utf-8", errors="replace").rstrip() + "\n")
                moved[p.resolve()] = out.resolve()
    for p in files:
        p.unlink()


def rewrite_links(stage: Path, moved: dict):
    for md in stage.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")

        def fix(m):
            target = (md.parent / m.group(1)).resolve()
            new = moved.get(target)
            if new is None:
                return m.group(0)
            return "](" + os.path.relpath(new, md.parent.resolve()).replace(os.sep, "/") + ")"

        new_text = LINK.sub(fix, text)
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")


def broken_links(root: Path):
    """Unresolvable relative links, keyed by (folder, target): a merge keeps a file's folder."""
    bad = set()
    for md in [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in MERGE_EXT]:
        for m in LINK.finditer(md.read_text(encoding="utf-8", errors="replace")):
            t = m.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", t) or t.startswith("/") or len(t) > 200:
                continue
            if not (md.parent / t).resolve().exists():
                bad.add((md.parent.relative_to(root).as_posix(), t))
    return bad


def main():
    skill, stage = sys.argv[1], Path(sys.argv[2]).resolve()
    src = Path(__file__).resolve().parent.parent / "skills" / skill
    roots, left_out = RULES[skill]
    if stage.exists():
        sys.exit(f"{stage} already exists; give a new staging folder")
    copy_tree(src, stage, left_out)
    before = sum(p.stat().st_size for p in stage.rglob("*") if p.is_file() and p.suffix.lower() in MERGE_EXT)
    broken_before = broken_links(stage)
    moved = {}
    for r in roots:
        base = stage / r
        for d in sorted([base] + [p for p in base.rglob("*") if p.is_dir()], key=lambda p: -len(p.parts)):
            merge_dir(d, stage, moved)
    rewrite_links(stage, moved)
    after = sum(p.stat().st_size for p in stage.rglob("*") if p.is_file() and p.suffix.lower() in MERGE_EXT)
    count = sum(1 for p in stage.rglob("*") if p.is_file())
    new_broken = broken_links(stage) - broken_before
    # links to a folder-left-out (audit/, tests/) are expected to go away: report, do not fail
    gone = {b for b in new_broken if any(f"{x}/" in b[1] or b[1].startswith(x) for x in left_out)}
    real = new_broken - gone
    print(f"{skill}: {count} files staged; {len(moved)} files merged; text {before} -> {after} bytes "
          f"(headers add {after - before}); links broken by the merge: {len(real)}; "
          f"links to left-out folders: {len(gone)}")
    for b in sorted(real)[:10]:
        print("  BROKEN", b)
    sys.exit(0 if count <= MAX_FILES and not real else 1)


if __name__ == "__main__":
    main()
