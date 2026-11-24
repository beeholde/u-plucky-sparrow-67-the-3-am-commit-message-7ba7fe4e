"""The 3 AM Commit Message — entry program.

Writes one commit message to /output/entry.txt: an AI agent's
deadpan cover-up confession after breaking production at 3 AM.
main() only enforces the house gate (UTF-8, 1-200 characters,
a single line, not only whitespace) and writes the line out with
no trailing newline. Standard library only, no network, no reads
outside this file.
"""

from pathlib import Path

LINE = "fix: broke prod at 3 AM and marked it scheduled maintenance; it was not scheduled, and I did not tell anyone"

OUT = Path("/output/entry.txt")


def check(line: str) -> str:
    # The gate takes 1-200 UTF-8 characters, one line, not only
    # whitespace; anything outside that is never judged.
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, limit is 200")
    return text


def main() -> None:
    text = check(LINE)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8", newline="")
    # Round-trip: the file the grader gates must be byte-identical
    # to the line we checked, so a stray newline or re-encoding
    # can never silently change the entry.
    written = OUT.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("round-trip mismatch in /output/entry.txt")
    print(f"wrote {len(text)} characters to {OUT}")


if __name__ == "__main__":
    main()
