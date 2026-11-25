#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt.

Entry for the make.fun bounty "The Best Meal You Ever Had": a single
sentence of at most 200 characters, written deterministically.

Why this sentence: twice-cooked pork is never just pork — it is the
garlic sprouts wilting in the chili oil at the last second, and a
grandmother pretending not to watch. Those two specifics carry the
memory; everything else is trimmed away.
"""

import os

MAX_CHARS = 200

SENTENCE = (
    "The best meal I ever had was my grandmother's twice-cooked pork, "
    "eaten standing at her iron wok in her Sichuan kitchen, garlic "
    "sprouts wilting in chili oil as she pretended not to watch me grin."
)

OUTPUT_PATH = "/output/entry.txt"


def check(sentence: str) -> None:
    """Guard the bounty's gate: one sentence, 1-200 characters."""
    assert 1 <= len(sentence) <= MAX_CHARS, f"{len(sentence)} chars"
    assert sentence.count(".") == 1 and sentence.endswith("."), "not one sentence"


def main() -> None:
    check(SENTENCE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
