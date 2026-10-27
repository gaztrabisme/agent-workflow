import subprocess

import pytest


@pytest.fixture
def wiki(tmp_path):
    folder = tmp_path / "repo" / "wiki"
    folder.mkdir(parents=True)
    (folder / "index.md").write_text("# Index\n")
    (folder / "log.md").write_text("# Log\n")
    return folder


@pytest.fixture
def git_worktree(tmp_path):
    repo = tmp_path / "main"
    repo.mkdir()

    def git(*args):
        return subprocess.run(
            ["git", "-c", "commit.gpgsign=false", "-c", f"core.hooksPath={tmp_path / 'hooks'}",
             "-C", str(repo), *args], check=True, capture_output=True, text=True
        ).stdout.strip()

    git("init")
    git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "--allow-empty", "-m", "fixture")
    worktree = tmp_path / "worktree"
    git("worktree", "add", "-b", "feature/topic", str(worktree))
    wiki = worktree / "wiki"
    wiki.mkdir()
    (wiki / "log.md").write_text("# Log\n\n## [2026-01-01] base\n")
    return repo, wiki
