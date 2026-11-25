"""One Line, Big Laugh — make.fun entry.

The program writes a single funny line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The line is a fixed constant:
the entry is the line itself, so the program is deterministic and
writes the same bytes on every run.

The joke: a smoke alarm that shrieks at every meal is, in its own
way, the most encouraging critic in the house — it has more faith
in my cooking than my own mother does. The turn lands because the
alarm's "belief" is the last place anyone would look for support,
and the comparison to Mum makes it personal instead of generic.
"""

import os

LINE = "My smoke alarm goes off every time I cook, which is how I know it believes in me more than my mother does."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # The entry is exactly the line: no title, no setup, no trailing
    # newline — the file holds the one line and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
