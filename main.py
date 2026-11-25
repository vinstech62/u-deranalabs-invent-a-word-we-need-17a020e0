#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty entry.

Writes a single invented English word and its one-line definition to
/output/entry.txt. Fully deterministic: the entry is a hardcoded string,
no randomness, time, or input is involved.
"""

from pathlib import Path

ENTRY = (
    "corridance (n.) \u2014 the awkward mirrored dance when two strangers "
    "keep sidestepping the same way in a hallway."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The bounty caps the entry at 140 UTF-8 characters; fail loudly
    # instead of writing an over-long line.
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, max 140"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    OUTPUT_PATH.chmod(0o644)


if __name__ == "__main__":
    main()
