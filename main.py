#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, under 200 characters, in which a dog explains why the
homework got eaten, to /output/entry.txt.

The excuse is assembled from three beats — the dog's alibi, the verdict,
and the cleanup — so each beat can be reasoned about on its own.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def alibi() -> str:
    """What the dog claims it was doing."""
    return "I was grading your homework"


def verdict() -> str:
    """The result of the dog's grading."""
    return "It failed"


def cleanup() -> str:
    """What the dog did with the evidence."""
    return "I disposed of the evidence"


def compose_excuse() -> str:
    """Join the three beats into a single sentence chain."""
    beats = (alibi(), verdict(), cleanup())
    return ". ".join(beats) + "."


def write_entry(line: str, path: Path = OUTPUT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8")


def main() -> None:
    line = compose_excuse()
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
