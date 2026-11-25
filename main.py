#!/usr/bin/env python3
"""Entry for make.fun's "One Line, One Laugh" bounty.

Prints one funny line that lands on a single read.
"""

import os

SETUP = "Adulthood is just Googling how long to boil an egg"
PUNCHLINE = "every single time, for the rest of my life"


def build_line() -> str:
    """Assemble the joke from its parts."""
    return f"{SETUP}, {PUNCHLINE}."


def main() -> None:
    line = build_line()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
