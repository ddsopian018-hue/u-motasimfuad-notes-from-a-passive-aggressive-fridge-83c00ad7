#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge - make.fun entry.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner to <output>/entry.txt. The output directory is MAKEFUN_OUTPUT_DIR
when set, otherwise /output (the kit's convention). Pure Python standard
library, no dependencies, no network, no files read from outside the repo.
"""

import os

# The note: smug door sensor, a concrete yogurt detail, a small domestic
# grudge, and a sting at the end the reader does not see coming. The
# fridge keeps score (23 openings) and refuses to be the one who caves.
NOTE = (
    "My door alarm logged 23 openings before lunch, and the yogurt "
    "still expires Tuesday. Keep staring — the leftovers aren’t going "
    "to apologize first, and neither am I."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = NOTE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # a single line, not only white space.
    assert 1 <= len(text) <= 200, "note is %d chars, must be 1-200" % len(text)
    assert "\n" not in text, "note must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
