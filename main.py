"""One line, saved to a file and echoed back.

This program keeps a single joke line, checks that it fits
inside the gate, and writes it out where the harness can read it.
"""

import os
from pathlib import Path

ENTRY = "Monday is just Sunday's unread emails wearing a tie and pretending this is a fresh start."

MAX_CHARS = 200

PREFERRED_DIR = "/output"
FALLBACK_NAME = "entry.txt"


def entry_text():
    cleaned = ENTRY.strip()
    assert 1 <= len(cleaned) <= MAX_CHARS, "line must fit the gate"
    return cleaned


def pick_target():
    preferred = Path(PREFERRED_DIR) / FALLBACK_NAME
    try:
        preferred.parent.mkdir(parents=True, exist_ok=True)
        return preferred
    except OSError:
        return Path(FALLBACK_NAME)


def main():
    line = entry_text()
    target = pick_target()
    try:
        target.write_text(line, encoding="utf-8")
    except OSError:
        Path(FALLBACK_NAME).write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
