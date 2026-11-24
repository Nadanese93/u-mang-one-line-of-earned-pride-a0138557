"""One Line of Earned Pride — Make.fun entry (u-mang-one-line-of-earned-pride-a0138557).

Writes a single line of earned pride (169 characters) to entry.txt.
The line: a beekeeper, three summers of stings behind him, lifts his
first honey-heavy frame into the light while the bees keep working
around him — a long effort finally landing, in one read.
"""

import os

ENTRY = (
    "Three summers of stings, and this morning he lifted the first frame "
    "heavy with honey and held it up to the light, while the bees went on "
    "working like he was one of them."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
