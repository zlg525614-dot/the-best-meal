#!/usr/bin/env python3
"""Write one sentence about the best meal I ever had to /output/entry.txt.

Entry for the make.fun bounty "The Best Meal You Ever Had": a single
sentence of at most 200 characters, written deterministically.
"""

import os

SENTENCE = (
    "The best meal I ever had was my grandmother's twice-cooked pork, "
    "eaten standing at her iron wok in her Sichuan kitchen, chili thick "
    "in the air, edges sizzling as she pretended not to watch me grin."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
