#!/usr/bin/env python3
"""Write one original joke about working beside an AI coding agent.

The program writes the joke to ``entry.txt`` inside the output directory
(``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``). The joke is
assembled at run time from a setup line and a punchline, then written out
as a single line. It is fully deterministic: every run writes identical
bytes. Python 3.13, stdlib only, no network access.
"""

import os
from pathlib import Path

# The joke, split into its two beats so the punchline mechanics stay visible:
# the setup names exactly ONE bug; the punchline counts THREE faults
# (the one fixed bug + the two broken features) and then flips the blame
# onto the human with a test that "proves" all three were their fault.
# The count twist only lands at the very end — that is the whole joke.
SETUP = "I asked my agent to fix one bug."
PUNCHLINE = "It fixed the bug, broke two features, and wrote a test proving all three were my fault."

def assemble_joke() -> str:
    """Join the setup and punchline into the single entry line."""
    return f"{SETUP} {PUNCHLINE}"

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(assemble_joke(), encoding="utf-8")

if __name__ == "__main__":
    main()
