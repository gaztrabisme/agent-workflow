#!/usr/bin/env python3
"""Check corrected ID/tier coverage, links, recipe tags and permitted sibling diffs.

Run from the repository root: python3 skills/reward-design/audit/check_build.py
Checks only this build's package and the five authorized siblings; does not edit files.
"""

import re
import subprocess
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
ROOT = REPO / "skills/reward-design"
EXPECTED = {f"{unit}{number}" for unit in "ABCDE"
            for number in range(1, 30 if unit == "E" else 26)}
SIBLINGS = ["presentation", "motion", "visual-design", "information-design", "ux"]


def rows(path):
    return [[cell.strip() for cell in line.strip("|").split("|")]
            for line in path.read_text().splitlines()
            if re.match(r"^\| [A-E]\d+ \|", line)]


def slug(heading):
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def main():
    print("Inputs: skills/reward-design; A–E/V; skills.txt; five authorized siblings")
    original_ids = []
    for unit in "ABCDE":
        original_ids.extend(re.findall(
            r"(?m)^### ([A-E]\d+)\b",
            (ROOT / f"audit/research/{unit}/findings.md").read_text(),
        ))
    verified_rows = rows(ROOT / "audit/research/V/claims-verified.md")
    mapped_rows = rows(ROOT / "references/evidence-map.md")
    for name, ids in [("original", original_ids),
                      ("V", [row[0] for row in verified_rows]),
                      ("map", [row[0] for row in mapped_rows])]:
        assert set(ids) == EXPECTED, f"{name}: incorrect ID coverage"
        assert all(count == 1 for count in Counter(ids).values()), f"{name}: duplicate IDs"
    verified = {row[0]: row for row in verified_rows}
    for row in mapped_rows:
        assert len(row) == 5, f"Malformed map row: {row[0]}"
        assert row[2:4] == [verified[row[0]][3], verified[row[0]][2]], row[0]
        assert row[4] != "not used", f"Unmapped use: {row[0]}"
    counts = Counter(row[2] for row in verified_rows)
    assert counts == {"supported": 122, "weakened": 7}, counts
    print("PASS: 129 unique original/V/map IDs; exact corrected tiers and verdicts; 0 unused")

    documents = [ROOT / "SKILL.md", ROOT / "NOTICE.md", ROOT / "EVOLUTION.md"]
    documents += sorted((ROOT / "references").glob("*.md"))
    local_links = 0
    tags = 0
    technique_lines = 0
    cited = set()
    for path in documents:
        content = path.read_text()
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in target or target.startswith("mailto:"):
                continue
            filename, _, anchor = target.partition("#")
            destination = (path.parent / filename).resolve() if filename else path
            assert destination.is_file(), f"Missing link in {path.name}: {target}"
            if anchor:
                headings = re.findall(r"(?m)^#{1,6}\s+(.+)$", destination.read_text())
                assert anchor in {slug(heading) for heading in headings}, target
            local_links += 1
        if path.name == "evidence-map.md":
            continue
        assert not re.search(r"\b(?:hack|addictive)\b", content, re.I), path.name
        for tier, identifiers in re.findall(
            r"\((T[1-4]);\s*([A-E]\d+(?:,\s*[A-E]\d+)*)\)", content,
        ):
            tags += 1
            for ident in re.findall(r"[A-E]\d+", identifiers):
                assert ident in EXPECTED, ident
                assert tier == verified[ident][3], f"{path.name}: {ident} {tier}"
                assert verified[ident][2] != "unsupported", ident
                cited.add(ident)
        if path.parent == ROOT / "references":
            for line in content.splitlines():
                is_recipe = line.startswith("- ") or bool(re.match(r"\d+\. ", line))
                is_check = bool(re.match(r"\| R\d+ \|", line))
                if is_recipe or is_check:
                    technique_lines += 1
                    assert re.search(r"\(T[1-4]; [A-E]\d+", line), (
                        f"Untagged technique/check in {path.name}: {line}"
                    )
    assert cited == EXPECTED, f"IDs without corrected-tier tags: {EXPECTED - cited}"
    print(f"PASS: {tags} evidence tags match V; {technique_lines} technique/check lines carry tags")
    print(f"PASS: {local_links} local Markdown links and anchors resolve")

    skill = (ROOT / "SKILL.md").read_text()
    assert len(skill.splitlines()) < 200
    description = re.search(r'(?m)^description: "(.+)"$', skill).group(1)
    assert len(description) <= 1024
    for keyword in ["USE WHEN", "Keywords:", "dopamine", "hook", "retention", "payoff",
                    "reveal", "anticipation", "curiosity gap", "sound design", "juice", "engagement"]:
        assert keyword in description, keyword
    registry = (REPO / "skills.txt").read_text().splitlines()
    assert registry.count("reward-design") == 1 and registry == sorted(registry)
    books = (ROOT / "references/reading-list.md").read_text()
    book_rows = [line for line in books.splitlines() if re.match(r"^\| \d+ \|", line)]
    assert len(book_rows) == 29
    assert all("| first |" in line for line in book_rows[:5])
    assert all("| first |" not in line for line in book_rows[5:])
    assert all(len(line.strip("|").split("|")) == 7 for line in book_rows)
    assert all("T1; E" not in line and "T2; E" not in line for line in book_rows)
    assert (ROOT / "scripts/check_refs.py").read_bytes() == (
        REPO / "skills/skill-builder/scripts/check_refs.py"
    ).read_bytes()
    for sibling in SIBLINGS:
        path = f"skills/{sibling}/SKILL.md"
        diff = subprocess.check_output(["git", "diff", "--", path], cwd=REPO, text=True)
        added = [line for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")]
        removed = [line for line in diff.splitlines() if line.startswith("-") and not line.startswith("---")]
        assert len(added) == 1 and not removed and "reward-design" in added[0], path
    print(f"PASS: SKILL.md {len(skill.splitlines())} lines; description {len(description)} characters")
    print("PASS: 29 ranked books, exactly 5 buy-first, corrected book-kind labels")
    print("PASS: alphabetical registration; exactly 1 added pointer per authorized sibling; unchanged checker copy")


if __name__ == "__main__":
    main()
