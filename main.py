"""The One-Line Exit — a one-line resignation letter.

The program writes a single funny resignation letter to
``$MAKEFUN_OUTPUT_DIR/entry.txt``. The letter must stay one line,
between 1 and 140 characters, and read like something a real
employee could actually send. Standard library only.
"""

import os
import sys

RESIGNATION_LINE = (
    "I resign, effective immediately: after five years, my only "
    "promotion was from 'new guy' to 'guy who knows where the "
    "good pens are'."
)

MAX_LENGTH = 140


def output_dir() -> str:
    """Return the directory the grader expects the entry in."""
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if target:
        return target
    return os.path.join(os.getcwd(), "output")


def check_line(line: str) -> None:
    """Fail loudly when the letter breaks the competition's gate."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("resignation letter must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("resignation letter must be exactly one line")
    if len(stripped) > MAX_LENGTH:
        raise ValueError(
            "resignation letter is %d characters, over the %d limit"
            % (len(stripped), MAX_LENGTH)
        )


def report_card(line: str) -> str:
    """One short summary of the letter's shape for the run log."""
    words = line.split()
    return (
        "letter: %d characters, %d words, one line, "
        "ends on the punchline" % (len(line), len(words))
    )


def main() -> int:
    check_line(RESIGNATION_LINE)
    print(report_card(RESIGNATION_LINE))
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(RESIGNATION_LINE)
    print("wrote %s (%d characters)" % (path, len(RESIGNATION_LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
