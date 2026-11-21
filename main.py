#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Judge brief (competition the-poem-about-permission-20261121-0235): write
one short poem, 1-280 Unicode code points, about permission — the power
to ask and to be given. The poem is tailored to that brief: the speaker
knocks and asks, someone else's hand turns the key, a held-out cup is
filled, and the yes that follows is held open for the next knock — asking
and granting as one small exchange of agency.

Writes the poem to /output/entry.txt. Python 3.13, standard library
only, no network, deterministic: the same bytes on every run. Before
writing, the program self-validates the text against the brief (length,
non-blank, exactly one terminating newline, no trailing whitespace on
any line) and reports the exact character and byte counts, so a bad
poem fails loudly instead of being submitted.
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
    # Self-validation against the judge brief:
    # 1-280 Unicode code points, not only white space, exactly one
    # terminating newline (no trailing blank line), no trailing
    # whitespace on any line.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points"
    assert POEM.strip(), "poem must not be only whitespace"
    assert POEM.endswith("\n") and not POEM.endswith("\n\n"), (
        "poem must end with exactly one newline"
    )
    assert all(line == line.rstrip() for line in POEM.splitlines()), (
        "poem must not have trailing whitespace on any line"
    )
    encoded = POEM.encode("utf-8")
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")
    print(
        f"wrote entry.txt ({len(POEM)} characters, "
        f"{len(encoded)} bytes, {len(POEM.splitlines())} lines)"
    )


if __name__ == "__main__":
    main()
