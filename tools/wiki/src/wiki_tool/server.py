"""FastMCP stdio server exposing the same operations as the CLI."""

from fastmcp import FastMCP

mcp = FastMCP("Wiki", instructions="Check wiki health and maintain dated project logs.")


# Import operation code on first use so discovery stays lightweight, matching
# the knowledge-base server's deferred-import pattern.
@mcp.tool()
def wiki_lint(wiki: str, index_cap: int = 200, log_cap: int = 400) -> dict:
    """Report wiki findings without changing any files."""
    from .core import wiki_lint as lint

    return lint(wiki, index_cap=index_cap, log_cap=log_cap)


@mcp.tool()
def wiki_log(wiki: str, kind: str, text: str) -> dict:
    """Add a local-date event, using a branch log in a linked git worktree."""
    from .core import wiki_log as log

    return log(wiki, kind, text)


@mcp.tool()
def wiki_rotate(wiki: str, max_lines: int = 400, keep_days: int = 30,
                dry_run: bool = False) -> dict:
    """Move whole old entries into monthly archives when the log exceeds its cap."""
    from .core import wiki_rotate as rotate

    return rotate(wiki, max_lines=max_lines, keep_days=keep_days, dry_run=dry_run)


@mcp.tool()
def wiki_merge_logs(wiki: str, dry_run: bool = False) -> dict:
    """Fold branch logs into log.md in date order and remove merged branch files."""
    from .core import wiki_merge_logs as merge

    return merge(wiki, dry_run=dry_run)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
