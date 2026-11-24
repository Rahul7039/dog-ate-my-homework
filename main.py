#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten, to /output/entry.txt.
"""

import os

LINE = "I was grading your homework. It failed. I disposed of the evidence."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
