import hashlib

import pytest

from wiki_tool.core import wiki_lint


def findings(wiki, rule, **kwargs):
    return [item for item in wiki_lint(wiki, **kwargs)["findings"] if item["rule"] == rule]


def page(wiki, name, content="Reviewed: 2026-10-27\n"):
    target = wiki / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)
    return target


@pytest.mark.parametrize("lines,expected", [(200, False), (201, True)])
def test_index_over_cap(wiki, lines, expected):
    page(wiki, "index.md", "line\n" * lines)
    assert bool(findings(wiki, "index-over-cap")) is expected
    assert not findings(wiki, "index-over-cap", index_cap=lines)


@pytest.mark.parametrize("lines,expected", [(400, False), (401, True)])
def test_log_over_cap(wiki, lines, expected):
    page(wiki, "log.md", "line\n" * lines)
    assert bool(findings(wiki, "log-over-cap")) is expected
    assert not findings(wiki, "log-over-cap", log_cap=lines)


@pytest.mark.parametrize("linked", [False, True])
def test_unreachable(wiki, linked):
    page(wiki, "topic.md")
    page(wiki, "runs/run.md")
    page(wiki, "goals/goal.md")
    page(wiki, "log.feature.md")
    if linked:
        page(wiki, "index.md", "[Topic](topic.md) — summary\n")
    result = wiki_lint(wiki)["findings"]
    assert [f["path"] for f in result if f["rule"] == "unreachable"] == ([] if linked else ["topic.md"])
    assert all(f["rule"] != "not-in-index" for f in result)


@pytest.mark.parametrize("parent,excluded", [
    ("inputs", True), ("raw", True),
    ("archive/inputs/deep", True), ("archive/raw/deep", True),
    ("myinputs", False), ("rawdata", False),
])
def test_source_copy_exclusions(wiki, parent, excluded):
    copy = page(wiki, f"{parent}/copy.md", "[Missing](missing.md)\n")
    before = copy.read_bytes()
    result = wiki_lint(wiki)["findings"]
    for rule in ("broken-link", "undated-page", "unreachable"):
        assert bool([f for f in result if f["rule"] == rule]) is (not excluded)
    assert copy.read_bytes() == before


@pytest.mark.parametrize("depth", [1, 3, 40])
def test_reachability_follows_any_depth_and_terminates_cycles(wiki, depth):
    page(wiki, "index.md", "[Start](topics/0.md)\n")
    for step in range(depth):
        page(wiki, f"topics/{step}.md", f"2026-10-27\n[Next]({(step + 1) % depth}.md)\n")
    # An outgoing link to the reachable graph does not make its source reachable.
    page(wiki, "orphan.md", "2026-10-27\n[Start](topics/0.md)\n")
    assert [f["path"] for f in findings(wiki, "unreachable")] == ["orphan.md"]


def test_disconnected_cycle_is_unreachable(wiki):
    page(wiki, "a.md", "2026-10-27\n[[b]]\n")
    page(wiki, "b.md", "2026-10-27\n[[a]]\n")
    assert [f["path"] for f in findings(wiki, "unreachable")] == ["a.md", "b.md"]


@pytest.mark.parametrize("intermediate", ["topics", "inputs", "raw", "runs", "goals"])
def test_reachability_traverses_exempt_pages(wiki, intermediate):
    page(wiki, "index.md", f"[Start]({intermediate}/start.md)\n")
    page(wiki, f"{intermediate}/start.md", "2026-10-27\n[Leaf](../leaf.md)\n")
    page(wiki, "leaf.md")
    assert not findings(wiki, "unreachable")


def test_reachability_follows_repo_root_links_through_external_markdown(wiki):
    page(wiki, "index.md", "[Guide](docs/guide.md)\n")
    docs = wiki.parent / "docs"
    docs.mkdir()
    (docs / "guide.md").write_text("[Topic](wiki/topic.md)\n")
    page(wiki, "topic.md", "2026-10-27\n[Leaf](nested/leaf.md)\n")
    page(wiki, "nested/leaf.md")
    assert not findings(wiki, "unreachable")


def test_reachability_prefers_page_relative_target_over_repo_root(wiki):
    page(wiki, "index.md", "[Start](nested/start.md)\n")
    page(wiki, "nested/start.md", "2026-10-27\n[Local](same.md)\n")
    page(wiki, "nested/same.md")
    (wiki.parent / "same.md").write_text("[Decoy](wiki/decoy.md)\n")
    page(wiki, "decoy.md")
    assert [f["path"] for f in findings(wiki, "unreachable")] == ["decoy.md"]


@pytest.mark.parametrize("exists", [False, True])
def test_index_dead_entry(wiki, exists):
    page(wiki, "index.md", "[Topic](topic.md#part)\n")
    if exists:
        page(wiki, "topic.md")
    assert bool(findings(wiki, "index-dead-entry")) is (not exists)


@pytest.mark.parametrize("syntax", ["[Topic](target.md#part)", "[[target]]", "[[target|Label]]"])
@pytest.mark.parametrize("exists", [False, True])
def test_broken_link(wiki, syntax, exists):
    page(wiki, "topic.md", f"2026-10-27\n{syntax}\n[web](https://example.invalid/no.md) [jump](#part)\n")
    if exists:
        page(wiki, "target.md")
    assert bool(findings(wiki, "broken-link")) is (not exists)


def test_root_relative_link_not_flagged(wiki):
    (wiki.parent / "docs").mkdir()
    (wiki.parent / "docs" / "target.md").write_text("outside wiki\n")
    page(wiki, "index.md", "[Topic](wiki/topic.md)\n[Docs](docs/target.md)\n")
    page(wiki, "topic.md", "2026-10-27\n[Docs](docs/target.md)\n[[docs/target]]\n")
    assert not findings(wiki, "broken-link")
    assert not findings(wiki, "index-dead-entry")
    assert not findings(wiki, "unreachable")


@pytest.mark.parametrize("count,expected", [(1, False), (2, True)])
@pytest.mark.parametrize("prefix", ["run-", "runs/"])
def test_run_report_in_index(wiki, count, expected, prefix):
    page(wiki, "index.md", "\n".join(f"[Run]({prefix}{i}.md)" for i in range(count)))
    assert bool(findings(wiki, "run-report-in-index")) is expected


@pytest.mark.parametrize("name,content,expected", [
    ("plain.md", "no date\n", True),
    ("dated-2026-10-27.md", "no date\n", False),
    ("plain.md", "\n" * 14 + "2026-10-27\n", False),
    ("plain.md", "\n" * 15 + "2026-10-27\n", True),
])
def test_undated_page(wiki, name, content, expected):
    page(wiki, name, content)
    page(wiki, "log.branch.md", "no date\n")
    assert bool(findings(wiki, "undated-page")) is expected


def test_links_in_code_ignored_and_url_encoded_links_resolve(wiki):
    page(wiki, "a b.md")
    page(wiki, "topic.md", '2026-10-27\n[ok](a%20b.md "title")\n'
         '`[example](missing.md)`\n```md\n[[missing]]\n```\n')
    assert not findings(wiki, "broken-link")


def test_lint_never_modifies_files(wiki):
    page(wiki, "topic.md", "[missing](missing.md)\n")

    def snapshot():
        return {p.relative_to(wiki): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in wiki.rglob("*") if p.is_file()}

    before = snapshot()
    assert wiki_lint(wiki)["findings"]
    assert snapshot() == before
