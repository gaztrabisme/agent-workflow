#!/usr/bin/env python3
"""Archive five source types through one durable, private core."""
import argparse
import json
import sys
from pathlib import Path
from archive_core.core import run_archive, install_release
from archive_core.contracts import validate_release
from archive_core.privacy import scan_release


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    run = commands.add_parser('run')
    run.add_argument('input', type=Path)
    run.add_argument('--output', required=True, type=Path)
    check = commands.add_parser('validate')
    check.add_argument('release', type=Path)
    scan = commands.add_parser('scan')
    scan.add_argument('release', type=Path)
    install = commands.add_parser('install-release')
    install.add_argument('release', type=Path)
    install.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.command == 'run':
        result = run_archive(args.input, args.output)
    elif args.command == 'validate':
        result = validate_release(args.release)
    elif args.command == 'scan':
        scan_release(args.release)
        result = {'scan': 'passed'}
    else:
        result = {'release': install_release(args.release, args.output)}
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Avoid exception payloads that may echo a transport URL or secret field.
        print('Archive failed: ' + type(error).__name__ + '. No staging was published.', file=sys.stderr)
        sys.exit(1)
