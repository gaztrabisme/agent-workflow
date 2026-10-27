"""Argparse interface; all wiki behavior lives in core."""

import argparse
import json
from pathlib import Path

from .core import wiki_lint, wiki_log, wiki_merge_logs, wiki_rotate


def nonnegative(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return number


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="wiki", description="Check and maintain project wikis.")
    commands = parser.add_subparsers(dest="command", required=True)
    lint = commands.add_parser("lint", help="report wiki findings without writing")
    lint.add_argument("wiki", type=Path)
    lint.add_argument("--index-cap", type=nonnegative, default=200)
    lint.add_argument("--log-cap", type=nonnegative, default=400)
    lint.add_argument("--json", action="store_true")
    lint.add_argument("--strict", action="store_true")
    log = commands.add_parser("log", help="add a dated event, respecting log order and worktrees")
    log.add_argument("wiki", type=Path)
    log.add_argument("kind")
    log.add_argument("text")
    rotate = commands.add_parser("rotate", help="archive whole old log entries")
    rotate.add_argument("wiki", type=Path)
    rotate.add_argument("--max-lines", type=nonnegative, default=400)
    rotate.add_argument("--keep-days", type=nonnegative, default=30)
    rotate.add_argument("--dry-run", action="store_true")
    merge = commands.add_parser("merge-logs", help="merge and remove branch logs")
    merge.add_argument("wiki", type=Path)
    merge.add_argument("--dry-run", action="store_true")
    commands.add_parser("search", help="reserved for knowledge-base search")
    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            print("not available yet")
        elif args.command == "lint":
            result = wiki_lint(args.wiki, args.index_cap, args.log_cap)
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"Wiki: {result['wiki']}")
                groups = {}
                for finding in result["findings"]:
                    groups.setdefault(finding["rule"], []).append(finding)
                if not groups:
                    print("No findings.")
                for rule, items in groups.items():
                    print(f"\n{rule} ({len(items)}):")
                    for item in items:
                        location = item["path"]
                        if item.get("line"):
                            location += f":{item['line']}"
                        print(f"  {location}: {item['message']}")
            return int(args.strict and bool(result["findings"]))
        else:
            if args.command == "log":
                result = wiki_log(args.wiki, args.kind, args.text)
            elif args.command == "rotate":
                result = wiki_rotate(args.wiki, args.max_lines, args.keep_days, args.dry_run)
            else:
                result = wiki_merge_logs(args.wiki, args.dry_run)
            print(json.dumps(result, indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"wiki: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
