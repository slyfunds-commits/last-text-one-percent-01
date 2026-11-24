#!/usr/bin/env python3
"""Last Text at One Percent — round 1 entry.

Writes the phone's final text to /output/entry.txt.
Pure standard library; deterministic.
"""

import os
import sys

LINE = "You dropped me 47 times. I kept count. This is me finally dropping you."

DEST_DIR = "/output"
DEST_FILE = os.path.join(DEST_DIR, "entry.txt")


def find_problems(text):
    issues = []
    if not 1 <= len(text) <= 200:
        issues.append(f"length {len(text)} outside 1-200 chars")
    if not text.strip():
        issues.append("text is only whitespace")
    if text.endswith("\n"):
        issues.append("trailing newline")
    return issues


def main():
    issues = find_problems(LINE)
    if issues:
        for issue in issues:
            print(f"invalid entry: {issue}", file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(DEST_FILE, "w", encoding="utf-8", newline="") as out:
        out.write(LINE)
    with open(DEST_FILE, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        print("byte mismatch after write", file=sys.stderr)
        return 1
    decoded = written.decode("utf-8")
    issues = find_problems(decoded)
    if issues:
        for issue in issues:
            print(f"written entry invalid: {issue}", file=sys.stderr)
        return 1
    print(LINE)
    print(f"chars={len(LINE)} bytes={len(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
