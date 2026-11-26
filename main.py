#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The GPS Swears It Was a Shortcut — entry writer.

Writes one line to /output/entry.txt: the GPS's own excuse, in its own
voice, for sending the driver down the wrong road. The gate checks
that /output/entry.txt is UTF-8 text of 1 to 200 characters, not only
white space; the judge wants a single line of plain text that reads
cleanly aloud in one breath.

The output path defaults to /output/entry.txt and can be redirected
with the MAKEFUN_OUTPUT_DIR environment variable (used only for local
verification runs, so the shared /output is never touched). The
program is deterministic: every run writes exactly the same bytes.

The line, revised after the first run. The draft had the GPS merely
believing the map; the revision sharpens the voice the judge brief
asks for — smug and defensive, caught red-handed and blaming the map.
The excuse leans on one fresh, specific detail instead of the usual
recalculating joke: a lake the map swore had a bridge in 2019. The
GPS stands by that promise with total confidence, and the turn lands
only in the last four words, when the driver's tires get wet — the
moment the excuse, like the bridge, stops holding up. A second
revision pass adds a closing fourth beat: the GPS points the finger
back at the map, doubling down instead of apologising.
"""

import os
import pathlib

MAX_CHARS = 200

# The excuse, assembled in four beats: the flat denial, the blame
# shifted onto the map's outdated promise, the sting, and the
# finger pointed back at the map.
ENTRY_PARTS = (
    "Not a wrong turn — ",
    "your map promised this lake had a bridge in 2019, and I trusted "
    "it completely, ",
    "right up until your tires got wet. ",
    "Blame the map, not me.",
)

ENTRY = "".join(ENTRY_PARTS)


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1..200 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(ENTRY.encode("utf-8"))
    # Prove the bytes on disk are exactly the bytes intended.
    assert target.read_bytes() == ENTRY.encode("utf-8")


if __name__ == "__main__":
    main()
