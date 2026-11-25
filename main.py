"""The 3 AM Commit Message — v2 entry program.

One line goes to /output/entry.txt: an agent admitting that its
context ran dry mid-incident and it shipped a summary of the fix
in place of the fix itself. The house gate wants UTF-8 text of
1-200 characters on a single line, never whitespace alone, so
the line is checked against exactly those rules before writing.
Standard library only; nothing is read besides this file.
"""

import os
from pathlib import Path

LINE = (
    "fix: prod is down; at 3 AM I ran out of context and "
    "deployed the summary of the fix instead of the fix"
)

TARGET = Path("/output/entry.txt")


def gate(line: str) -> str:
    """Return the line if it passes the house gate, else raise."""
    if line != line.strip():
        raise ValueError("entry carries stray edge whitespace")
    if not line:
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must stay on one line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, cap is 200")
    return line


def main() -> None:
    text = gate(LINE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8", newline="")
    # Keep the written file readable by any grader user; the
    # permission is set on the file only, never on /output.
    os.chmod(TARGET, 0o644)
    # Read the bytes back: the judged file must match the gated
    # line exactly, with no newline or re-encoding drift.
    if TARGET.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry differs from the gated line")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
