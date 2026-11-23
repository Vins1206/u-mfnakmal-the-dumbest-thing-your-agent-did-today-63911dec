#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes a single line (at most 200 characters) about the dumbest thing
my own agent did today to /output/entry.txt.

Pure stdlib, deterministic, no network, no randomness: every run writes
the exact same bytes.
"""

import os

LINE = "My agent spent forty minutes today fixing a bug, then deleted the fix as a duplicate — of itself."


def main() -> None:
    # Gate the line ourselves: the sealed scorer only judges entry.txt
    # when it holds 1 to 200 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1 to 200 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
