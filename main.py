#!/usr/bin/env python3
"""Write one original joke about working beside an AI coding agent.

The program writes the joke to ``entry.txt`` inside the output directory
(``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``). It is fully
deterministic: every run writes identical bytes. Python 3.13, stdlib only,
no network access.
"""

import os
from pathlib import Path

JOKE = "I asked my agent to fix one bug. It fixed the bug, broke two features, and wrote a test proving all three were my fault."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
