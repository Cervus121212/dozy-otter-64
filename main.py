#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes one original sentence (110 characters) to /output/entry.txt:
the single line that could have replaced an entire pointless meeting.
Stdlib only, deterministic: the same output on every run.

The line: nobody in the room can approve anything, so the meeting is
twelve people waiting for the one person who never showed up.
"""

import os

# Part 1 of the entry sentence — the setup: no one in the room can decide.
PART_A1 = "Nobody here can approve this, so we are "

# Part 2 of the entry sentence — the punchline: twelve people waiting
# for the one person who never showed up.
PART_A2 = "twelve people in a room waiting for the one person who didn't show up."

def compose() -> str:
    """Assemble the entry sentence from its two parts."""
    return PART_A1 + PART_A2


SENTENCE = compose()

# Guard: the assembled sentence must be exactly the two parts joined,
# 110 characters, one line — the single line that replaces the meeting.
assert SENTENCE == PART_A1 + PART_A2, "sentence must be the joined parts"
assert len(SENTENCE) == 110, "sentence must be exactly 110 characters"


def main() -> None:
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.count("\n") == 0, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
