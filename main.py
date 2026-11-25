#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, at most 200 characters.

Writes the sentence to /output/entry.txt (or $ENTRY_OUTPUT when set).
Deterministic: every run writes the same bytes.

The sentence: a grandmother's rendang in Bandung — a named dish, a
place, a texture (beef falling apart), a sound (rain on a tin roof),
and a human moment (her ladling more rice and whispering "eat, eat").
One clean sentence, no title, no list, no generic praise.

Revision: v1 ended flat — "she kept piling rice onto my plate." The
revised ending gives her a voice ("whispering, eat, eat") so the
sentence lands on a person, not a plate, and the last image is her
urging me on rather than the food sitting there. "Ladled" also fits
the scene better than "piling": it is what a grandmother does over
a pot of rendang.
"""

import os

ENTRY = (
    "The best meal I ever had was my grandmother's rendang in Bandung, "
    "beef so soft it fell apart on my tongue while rain drummed on the "
    "tin roof and she ladled rice onto my plate, whispering, eat, eat."
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
