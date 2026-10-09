#!/usr/bin/env python3
"""Check an agent recipe for gaps. No network. No installs."""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = (
    "name:",
    "one_line:",
    "## Problem",
    "## User",
    "## Inputs",
    "## Outputs",
    "## Done when",
)


def section_body(text: str, header: str) -> str:
    if header not in text:
        return ""
    rest = text.split(header, 1)[1]
    nxt = rest.find("\n## ")
    body = rest if nxt == -1 else rest[:nxt]
    return body.strip()


def field_value(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.lower().startswith(key.lower()):
            return line.split(":", 1)[1].strip()
    return ""


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 tools/check_recipe.py RECIPE.md")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing file: {path}")
        return 2
    text = path.read_text(encoding="utf-8")
    gaps: list[str] = []
    for token in REQUIRED:
        if token not in text:
            gaps.append(f"missing {token}")
    if not field_value(text, "name:"):
        gaps.append("name is empty")
    if not field_value(text, "one_line:"):
        gaps.append("one_line is empty")
    if not section_body(text, "## Problem"):
        gaps.append("Problem is empty")
    if not section_body(text, "## User"):
        gaps.append("User is empty")
    inputs = section_body(text, "## Inputs")
    outputs = section_body(text, "## Outputs")
    done = section_body(text, "## Done when")
    if inputs in ("", "-"):
        gaps.append("Inputs need at least one item")
    if outputs in ("", "-"):
        gaps.append("Outputs need at least one item")
    if done in ("", "-"):
        gaps.append("Done when needs at least one item")
    if gaps:
        print("GAPS")
        for gap in gaps:
            print(f"- {gap}")
        return 1
    print("PASS")
    print(f"name: {field_value(text, 'name:')}")
    print(f"one_line: {field_value(text, 'one_line:')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
