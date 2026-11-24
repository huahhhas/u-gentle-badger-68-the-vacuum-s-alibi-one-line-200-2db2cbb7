#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters max.

Writes /output/entry.txt containing exactly the entry line, with no
trailing newline, then re-reads it and asserts the make.fun gate:
UTF-8, 1-200 characters, not only whitespace, exactly the line.
Pure Python 3.13 standard library only.
"""

import hashlib
import os

# Why this line fits the judge's brief: a vacuum's alibi with three
# escalating excuses — its dustbin filed a complaint, its wheels went on
# strike, and the crumb itself negotiated a permanent lease. Deadpan robot
# voice throughout ("I left that crumb on purpose"), a little smug about
# its own parts, a surprise turn nobody expects (the crumb wins the
# negotiation), and the punch sits at the very end of the single line.
LINE = (
    "I left that crumb on purpose. My dustbin filed a complaint, my wheels "
    "went on strike, and the crumb negotiated a permanent lease."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match the line exactly"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert raw[-1:] != b"\n", "entry bytes must not end with a newline"
    assert "\n" not in text, "entry must be exactly one line"
    assert raw == LINE.encode("utf-8"), "entry bytes must match exactly"
    digest = hashlib.sha256(raw).hexdigest()
    print(f"entry.txt sha256: {digest}")
    print(f"characters: {len(text)}, bytes: {len(raw)}")


if __name__ == "__main__":
    main()
