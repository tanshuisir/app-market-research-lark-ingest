#!/usr/bin/env python3
"""Extract unique Apple App Store IDs from URLs or mixed text."""

from __future__ import annotations

import argparse
import re
import sys


URL_PATTERNS = (
    re.compile(r"(?:apps\.apple\.com/[^\s?#]*/app/[^\s?#]*/id|itunes\.apple\.com/[^\s?#]*/app/[^\s?#]*/id)(\d{9,12})", re.I),
    re.compile(r"qimai\.cn/app/[^\s?#]*/appid/(\d{9,12})", re.I),
    re.compile(r"(?:^|[/?&])appid[=/](\d{9,12})(?:\D|$)", re.I),
)
FALLBACK_PATTERN = re.compile(r"(?<!\d)(\d{9,12})(?!\d)")


def extract_ids(text: str) -> list[str]:
    """Return IDs in first-seen order, preferring recognized URL patterns."""
    matches: list[tuple[int, str]] = []
    for pattern in URL_PATTERNS:
        matches.extend((match.start(1), match.group(1)) for match in pattern.finditer(text))

    occupied = {value for _, value in matches}
    matches.extend(
        (match.start(1), match.group(1))
        for match in FALLBACK_PATTERN.finditer(text)
        if match.group(1) not in occupied
    )

    seen: set[str] = set()
    ordered: list[str] = []
    for _, value in sorted(matches, key=lambda item: item[0]):
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", nargs="*", help="URLs or text; stdin is used when omitted")
    args = parser.parse_args()
    source = " ".join(args.text) if args.text else sys.stdin.read()
    ids = extract_ids(source)
    if not ids:
        print("No Apple App Store ID found.", file=sys.stderr)
        return 1
    print("\n".join(ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
