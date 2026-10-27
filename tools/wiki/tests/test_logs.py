from datetime import date, timedelta

import pytest

from wiki_tool.core import wiki_log, wiki_merge_logs, wiki_rotate


@pytest.mark.parametrize("newest_first", [False, True])
def test_log_matches_order_and_keeps_title(wiki, newest_first):
    headings = ["## [2026-01-01] first\n", "## [2026-02-01] last\n"]
    if newest_first:
        headings.reverse()
    (wiki / "log.md").write_text("# Wiki Log\n\n" + "\n".join(headings))
    wiki_log(wiki, "build", "ready")
    text = (wiki / "log.md").read_text()
    entry = f"## [{date.today()}] build | ready"
    assert text.startswith("# Wiki Log\n\n")
    if newest_first:
        assert text.index(entry) < text.index(headings[0].strip())
    else:
        assert text.index(entry) > text.index(headings[-1].strip())


def test_log_worktree_writes_branch_file(git_worktree):
    repo, wiki = git_worktree
    before = (wiki / "log.md").read_bytes()
    result = wiki_log(wiki, "test", "isolated")
    assert result["path"].endswith("log.feature-topic.md")
    assert (wiki / "log.feature-topic.md").read_text().startswith("# Log\n")
    assert "test | isolated" in (wiki / "log.feature-topic.md").read_text()
    assert (wiki / "log.md").read_bytes() == before
    (repo / "wiki").mkdir()
    assert wiki_log(repo / "wiki", "test", "main")["path"].endswith("/log.md")


def test_log_empty_and_single_entry_default_newest_first(wiki):
    wiki_log(wiki, "one", "first")
    wiki_log(wiki, "two", "second")
    text = (wiki / "log.md").read_text()
    assert text.index("two | second") < text.index("one | first")


@pytest.mark.parametrize("heading", [
    "## [2026-01-01] run | one", "## 2026-01-01 — two",
    "## [2026-01-01–02] three", "## 2026-01-01/02 — four",
])
def test_rotate_recognizes_real_heading_formats(wiki, heading):
    (wiki / "log.md").write_text(f"# Run ledger\n\n{heading}\nbody\n### Child\nkept with entry\n")
    wiki_rotate(wiki, max_lines=1)
    archived = (wiki / "log-2026-01.md").read_text()
    assert heading in archived
    assert "### Child\nkept with entry" in archived


@pytest.mark.parametrize("newest_first", [False, True])
def test_rotate_only_old_whole_entries_pointer_and_idempotence(wiki, newest_first):
    today = date.today()
    old = today - timedelta(days=90)
    cutoff = today - timedelta(days=30)
    entries = [f"## [{old}] old\nbody\n### Child\nchild body\n",
               f"## [{cutoff}] boundary\nkeep boundary\n",
               f"## [{today}] recent\nkeep recent\n"]
    if newest_first:
        entries.reverse()
    (wiki / "log.md").write_text("# Log\n\n" + "\n".join(entries))
    archive = wiki / f"log-{old:%Y-%m}.md"
    result = wiki_rotate(wiki, max_lines=1, keep_days=30)
    assert result["moved_entries"] == 1
    assert entries[0 if not newest_first else -1].strip() in archive.read_text()
    remaining = (wiki / "log.md").read_text()
    assert "boundary\nkeep boundary" in remaining and "recent\nkeep recent" in remaining
    assert "### Child" not in remaining
    assert f"Older entries: [{archive.name}]({archive.name})" in remaining
    snapshot = {p: p.read_bytes() for p in wiki.iterdir()}
    assert wiki_rotate(wiki, max_lines=1, keep_days=30)["moved_entries"] == 0
    assert {p: p.read_bytes() for p in wiki.iterdir()} == snapshot


def test_rotate_dry_run_and_below_cap_do_not_write(wiki):
    original = "# Log\n\n## [2020-01-01] old\nbody\n"
    (wiki / "log.md").write_text(original)
    assert wiki_rotate(wiki)["moved_entries"] == 0
    assert wiki_rotate(wiki, max_lines=1, dry_run=True)["moved_entries"] == 1
    assert (wiki / "log.md").read_text() == original
    assert not (wiki / "log-2020-01.md").exists()


@pytest.mark.parametrize("newest_first", [False, True])
def test_rotate_existing_archive_keeps_its_order(wiki, newest_first):
    days = ["2020-01-01", "2020-01-03"]
    if newest_first:
        days.reverse()
    (wiki / "log-2020-01.md").write_text("# Log\n\n" + "\n".join(f"## [{d}] archived\n" for d in days))
    (wiki / "log.md").write_text("## [2020-01-02] middle\n")
    wiki_rotate(wiki, max_lines=0)
    text = (wiki / "log-2020-01.md").read_text()
    order = sorted([*days, "2020-01-02"], reverse=newest_first)
    assert [text.index(d) for d in order] == sorted(text.index(d) for d in order)


@pytest.mark.parametrize("newest_first", [False, True])
def test_merge_logs_order_and_remove_branch_files(wiki, newest_first):
    days = ["2026-01-01", "2026-01-05"]
    if newest_first:
        days.reverse()
    (wiki / "log.md").write_text("# Log\n\n" + "\n".join(f"## [{d}] base\n" for d in days))
    (wiki / "log.a.md").write_text("# Log\n\n## [2026-01-04] a\n### Child\nbody\n")
    (wiki / "log.b.md").write_text("# Log\n\n## [2026-01-02] b\n")
    result = wiki_merge_logs(wiki)
    text = (wiki / "log.md").read_text()
    ordered = sorted([*days, "2026-01-02", "2026-01-04"], reverse=newest_first)
    assert [text.index(d) for d in ordered] == sorted(text.index(d) for d in ordered)
    assert "### Child\nbody" in text
    assert result["merged_entries"] == 2
    assert not list(wiki.glob("log.*.md"))
    assert wiki_merge_logs(wiki)["merged_entries"] == 0


def test_merge_dry_run_no_writes(wiki):
    branch = wiki / "log.a.md"
    branch.write_text("# Log\n\n## [2026-01-01] one\n")
    before = (wiki / "log.md").read_bytes()
    assert wiki_merge_logs(wiki, dry_run=True)["merged_entries"] == 1
    assert branch.exists()
    assert (wiki / "log.md").read_bytes() == before


def test_rotate_keeps_existing_pointers_when_later_entries_age(wiki):
    (wiki / "log.md").write_text(
        "# Log\n\n## [2020-02-01] old\nbody\n\n"
        "Older entries: [log-2020-01.md](log-2020-01.md)\n")
    wiki_rotate(wiki, max_lines=1)
    text = (wiki / "log.md").read_text()
    assert text.count("Older entries: [log-2020-01.md]") == 1
    assert text.count("Older entries: [log-2020-02.md]") == 1
    assert "Older entries:" not in (wiki / "log-2020-02.md").read_text()


def test_merge_rejects_unstructured_branch_without_deleting(wiki):
    branch = wiki / "log.a.md"
    branch.write_text("# Log\n\nUnstructured content\n")
    before = (wiki / "log.md").read_bytes()
    with pytest.raises(ValueError, match="text before"):
        wiki_merge_logs(wiki)
    assert branch.exists()
    assert (wiki / "log.md").read_bytes() == before


def test_newest_log_inserts_immediately_after_title(wiki):
    (wiki / "log.md").write_text("# Log\n\nPreamble\n\n## [2026-01-01] one\n")
    wiki_log(wiki, "build", "new")
    text = (wiki / "log.md").read_text()
    assert text.index("build | new") < text.index("Preamble") < text.index("one")


def test_rotate_preserves_code_headings_and_code_pointers(wiki):
    content = ("## [2020-01-01] old\n```md\n## [2099-01-01] example\n"
               "Older entries: [log-2019-01.md](log-2019-01.md)\n```\n")
    (wiki / "log.md").write_text(content)
    assert wiki_rotate(wiki, max_lines=1)["moved_entries"] == 1
    assert content in (wiki / "log-2020-01.md").read_text()
