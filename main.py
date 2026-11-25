#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single hilarious line (200 characters or fewer) to
/output/entry.txt. Pure standard library, deterministic: the same
line every run, byte for byte.
"""

import os

LINE = (
    "My Roomba filed for custody of the dog — it spends more time "
    "with him than I do, and the judge sided with the vacuum."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
