#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Python 3.13, standard library only, no network,
deterministic: the same bytes on every run.

The poem: a knock, a door opened by someone else's hand, a cup held out
empty and filled — and the yes that follows, held open for the next knock.
"""

import os
from pathlib import Path

POEM = """\
I knock twice.
The door opens — not on its hinge,
on your hand, turning the key
you keep for strangers who ask.

"May I?" — a cup held out,
empty. You fill it.
I drink, and learn the trade:
a yes is a door, and a door,
once opened, is yours to hold
for the next knock.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-280 Unicode code points, not only white space.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem must not be only whitespace"
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")
    print(f"wrote entry.txt ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
