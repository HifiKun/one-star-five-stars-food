#!/usr/bin/env python3
"""One Star, Five Stars for the Food — entry program.

The competition asks for one sentence, at most 200 characters, in the
voice of an alien tourist giving planet Earth a one-star review while
still slipping in a real compliment about the food. This program writes
that single sentence to /output/entry.txt, exactly as the gate requires:
UTF-8 text, 1 to 200 characters, not only white space.

The sentence: Earth charges rent for existing and its weather cannot
make up its mind — the one-star grievance — and yet the noodles made
the reviewer's third stomach weep, so he would cross the galaxy again
just to eat here. Alien voice (a third stomach, rent for existing),
a real complaint, a real food compliment, and the turn between them
is the joke. One sentence, 183 characters.
"""

import os
import sys

# One sentence: a one-star alien review of Earth that still praises the food.
SENTENCE = (
    "One star: Earth charges rent for existing, its weather changes "
    "its mind mid-sentence, and yet the noodles made my third stomach "
    "weep \u2014 I would cross the galaxy again just to eat here."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = SENTENCE.strip()
    # One sentence: exactly one sentence terminator, at the very end,
    # no line breaks inside, and inside the 200-character cap.
    terminators = sum(text.count(c) for c in ".!?")
    if (
        not text
        or len(text) > 200
        or terminators != 1
        or not text.endswith((".", "!", "?"))
        or any(ch in text for ch in "\n\r")
    ):
        print("error: entry must be one sentence of 1-200 characters", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the scorer will read must be exactly the sentence.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != text:
            print("error: entry.txt does not match the sentence", file=sys.stderr)
            return 1
    print(f"wrote {OUTPUT_PATH}: {text!r} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
