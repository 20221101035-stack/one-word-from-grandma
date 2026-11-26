#!/usr/bin/env python3
"""One Word From Grandma — entrypoint.

Writes the single word grandma would text about AI to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Standard library only, deterministic, no network.
"""

import os

WORD = "Witchcraft"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate: UTF-8 text of 1 to 30 characters, not only whitespace, one word.
    # Tightened: also cap bytes (ASCII here, so bytes == chars) and forbid
    # any whitespace or punctuation tricks inside the word.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert len(WORD.encode("utf-8")) <= 30, "word must be <= 30 bytes"
    assert WORD.strip() == WORD and WORD.strip(), "word must not be blank"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert WORD.isalpha(), "word must be plain letters only"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read back and verify the written bytes match the word exactly.
    with open(path, "rb") as f:
        written = f.read()
    assert written == WORD.encode("utf-8"), "written bytes differ from word"


if __name__ == "__main__":
    main()
