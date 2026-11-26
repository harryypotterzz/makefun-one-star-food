#!/usr/bin/env python3
"""One Star, Five Stars for the Food - make.fun entry.

Writes one sentence - a one-star review of Earth by an alien tourist
that still compliments the food - to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

# The review is assembled from named parts so each complaint and the
# food praise can be edited independently; the joined sentence is the
# judged entry and must stay byte-identical.
PARTS = [
    "One star: the locals scream at glowing rectangles all day,",
    "the weather offers no refunds,",
    "and gravity is non-negotiable \u2014",
    "but the tacos alone justify a second invasion.",
]

SENTENCE = " ".join(PARTS)

# The entry is a single sentence; guard against accidental edits that
# would change its length or wording.
assert len(SENTENCE) == 168, f"entry sentence changed: {len(SENTENCE)} chars"
assert SENTENCE.endswith("second invasion.")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
