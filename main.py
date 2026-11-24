#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one funny loading-screen tip for stressed developers
(and the AI coding agents helping them) to /output/entry.txt.

The tip is a single line, well under the 200-character limit.
Python 3.13 standard library only; no third-party dependencies.
"""

import os

TIP = (
    "Tip: if your code compiled on the first try, don't celebrate "
    "\u2014 commit now and walk away slowly. "
    "The bug is just hiding."
)

MAX_CHARS = 200


def main() -> None:
    tip = TIP.strip()
    if not tip:
        raise ValueError("tip must not be empty")
    if len(tip) > MAX_CHARS:
        raise ValueError(f"tip is {len(tip)} chars, over the {MAX_CHARS} limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tip + "\n")
    print(f"wrote {len(tip)} characters to {out_path}")


if __name__ == "__main__":
    main()
