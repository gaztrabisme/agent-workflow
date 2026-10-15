# -*- coding: utf-8 -*-
"""nocache.py — nothing in this skill may point into the plugin cache.

    python scripts/nocache.py

WHY. This skill began as a copy of a third-party plugin. Plugins live in a version-
stamped cache directory that the plugin system owns and refreshes:

    ~/.claude/plugins/cache/<plugin>/<plugin>/<version>/skills/<skill>/

Sixteen working scripts were written into that directory during one engagement and
would have been erased by the next `/plugin update`, which is the reason this skill
exists as a skill. A path back into that directory reintroduces the same fault twice
over: the file it points at can vanish, and the version number in the path changes on
any upgrade.

Exits non-zero and names every offending file and line.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)

NEEDLE = re.compile(r"plugins[/\\]cache|epic-infographics[/\\]epic-infographics")
SKIP_DIRS = {"node_modules", ".git", "__pycache__"}
# Records may name the cache; instructions and code may not. NOTICE.md, the goal files
# and the ledger exist to say where this skill came from and what was nearly lost, and
# that history is the reason the rule exists. The distinction is live reference versus
# record: nothing here is a path anything follows.
ALLOW_FILES = {"NOTICE.md", "nocache.py", "EVOLUTION.md"}
ALLOW_PREFIX = ("GOAL-",)
TEXT = {".md", ".mjs", ".js", ".py", ".json", ".html", ".css", ".toml", ".txt", ".yml", ".yaml"}

hits = []
for root, dirs, files in os.walk(SKILL):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fn in files:
        if (fn in ALLOW_FILES or fn.startswith(ALLOW_PREFIX)
                or os.path.splitext(fn)[1].lower() not in TEXT):
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, SKILL)
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                for i, line in enumerate(fh, 1):
                    if NEEDLE.search(line):
                        hits.append((rel, i, line.strip()[:120]))
        except OSError as e:
            hits.append((rel, 0, "could not read: %s" % e))

if hits:
    print("%d reference(s) into the plugin cache — these break on the next plugin update:\n" % len(hits))
    for rel, i, line in hits:
        print("  %s:%d\n      %s" % (rel, i, line))
    sys.exit(1)

print("clean: no path into the plugin cache")
