"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note a smart fridge leaves for its owner
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only. Deterministic: the same bytes on
every run.
"""

import os
from pathlib import Path

LINE = (
    # 114 characters. The sting: the fridge keeps count of every
    # door-open, then reframes itself as a museum the owner tours
    # instead of using — petty, sensor-smug, and domestic.
    "You opened my door 14 times today and took nothing. "
    "I am a fridge, not a museum. "
    "Please stop touring my leftovers."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
