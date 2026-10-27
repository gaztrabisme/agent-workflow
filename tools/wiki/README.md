# Wiki tool

Python 3.11+ CLI and FastMCP stdio tools for a repository's `wiki/` folder.

Install from this folder:

```sh
uv tool install --editable .
```

Run directly from the checkout with `uv run wiki ...`. Run the offline synthetic
tests with `uv run pytest -q`; the worktree test requires Git. The uv cache,
virtual environment and pytest temporary files stay inside this folder.

```sh
wiki lint ./wiki
wiki lint ./wiki --json
wiki lint ./wiki --index-cap 200 --log-cap 400 --strict
wiki log ./wiki build "CLI and MCP tests pass"
wiki rotate ./wiki --max-lines 400 --keep-days 30 --dry-run
wiki rotate ./wiki --max-lines 400 --keep-days 30
wiki merge-logs ./wiki --dry-run
wiki merge-logs ./wiki
wiki search
```

Lint reports findings grouped by rule and never writes to the wiki. Its exit code
is 0 even with findings; `--strict` returns 1 with findings. Invalid arguments,
missing wiki folders and I/O errors return 2. JSON contains the resolved `wiki`
path and a `findings` list with `rule`, `path`, `message` and optional `line`.

The seven rules are `index-over-cap`, `log-over-cap`, `unreachable`,
`index-dead-entry`, `broken-link`, `run-report-in-index` and `undated-page`.
Links resolve relative to their page first, then relative to the wiki's parent
(the repo root). Inline Markdown page links and `[[page]]` / `[[page|label]]`
links are checked; URLs, anchor-only links and code examples are ignored.
`unreachable` reports pages that cannot be reached by following Markdown links
from `index.md`, through any number of pages. Traversal handles cycles and can
follow linked Markdown files outside the wiki when they lead back to wiki pages.
It uses the same page-relative-first resolution at every step. `index.md`,
`log*.md`, and pages under `runs/` or `goals/` are exempt from this rule.

Pages below any directory named `inputs/` or `raw/`, at any depth within the
wiki, are immutable source copies. They are exempt from `broken-link`,
`undated-page`, and `unreachable`. They can still provide links for reachability.
Date checks also skip index and log pages. One run-report roll-up link is allowed
in the index. Lint only reads source copies and all other wiki files.

Log entries begin with a `## ` heading containing an ISO date. Ranges use their
first date; `###` sections stay with their entry. Direction comes from the first
and last dated entries; a tie or an empty log defaults to newest-first. New events
use today's local date. In a linked git worktree, events go to
`log.<branch>.md`, with slashes replaced by hyphens. Detached worktrees use
`log.detached-<commit>.md`.

Rotation runs only above the line cap and moves entries strictly older than
`today - keep_days` to `log-YYYY-MM.md`. It preserves archive date direction and
leaves one `Older entries:` link per moved month. Entries are never split;
recent entries may leave the log above the cap. Merge sorts branch entries into
`log.md` in its existing direction, then removes the branch files. Equal-date
entries retain their relative order. Both commands report structured move/merge
counts, and `--dry-run` makes no changes. Branch logs containing unstructured
text before their dated entries are rejected rather than discarded.

`wiki search` currently prints `not available yet`.

Register the installed MCP server with Claude Code:

```sh
claude mcp add wiki -- wiki-mcp
```

Add this to Codex's `config.toml`:

```toml
[mcp_servers.wiki]
command = "wiki-mcp"
```

The server runs over stdio and exposes `wiki_lint`, `wiki_log`, `wiki_rotate`
and `wiki_merge_logs`. Each takes `wiki` as a folder path, with the same optional
limits and dry-run behavior as the CLI; `wiki_log` also takes `kind` and `text`.
All four wrap the same functions as the CLI. Core imports are deferred until
tool invocation.
