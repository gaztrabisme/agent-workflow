#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.roundtrip_core import merge, prepare, verify


def main():
    parser = argparse.ArgumentParser(description="Prepare and verify guarded photo edits")
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("original"); prep.add_argument("--mask", required=True)
    prep.add_argument("--brief", required=True); prep.add_argument("--out", required=True)
    join = sub.add_parser("merge")
    join.add_argument("original"); join.add_argument("edited_crop"); join.add_argument("--mask", required=True)
    join.add_argument("--out", required=True)
    check = sub.add_parser("verify")
    check.add_argument("original"); check.add_argument("edited"); check.add_argument("--mask", required=True)
    check.add_argument("--out", required=True); check.add_argument("--mean-limit", type=float, default=1.0)
    check.add_argument("--p99-limit", type=float, default=3.0)
    check.add_argument("--feather-radius", type=float, default=5.0)
    check.add_argument("--band-mean-limit", type=float, default=1.0)
    check.add_argument("--band-p99-limit", type=float, default=2.0)
    check.add_argument("--band-max-limit", type=float, default=3.0)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            result = prepare(args.original, args.mask, args.brief, args.out)
            code = 0
        elif args.command == "merge":
            result = merge(args.original, args.edited_crop, args.mask, args.out)
            code = 0
        else:
            result = verify(args.original, args.edited, args.mask, args.out,
                            args.mean_limit, args.p99_limit, args.feather_radius,
                            args.band_mean_limit, args.band_p99_limit, args.band_max_limit)
            code = 0 if result["roundtrip"]["passed"] else 1
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return code
    except Exception as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
