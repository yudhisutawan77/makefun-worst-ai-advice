"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes a single line of deliberately terrible advice, in the confident
voice of a helpful AI assistant, to /output/entry.txt (or the path given
by ENTRY_OUT / ENTRY_OUT_DIR).
"""

import os
import sys

MAX_CHARS = 140

ADVICE_LINE = (
    "Certainly! Turn off two-factor authentication so logging in is "
    "faster \u2014 convenience is the best security."
)


def pick_destination():
    """Pick where the entry text goes.

    ENTRY_OUT wins when set; otherwise ENTRY_OUT_DIR/entry.txt;
    otherwise the default /output/entry.txt.
    """
    direct = os.environ.get("ENTRY_OUT")
    if direct:
        return direct
    base = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def compose_advice_line():
    """Return the one-line entry, exactly as it should be judged."""
    return ADVICE_LINE


def check_line(line):
    """Gate the entry the same way the sealed scorer does.

    Returns an error string, or None when the line is acceptable:
    1-140 characters, not only whitespace, and a single line.
    """
    if not line or not line.strip():
        return "entry is empty or only whitespace"
    if len(line) > MAX_CHARS:
        return "entry is %d chars, over the %d limit" % (len(line), MAX_CHARS)
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    return None


def persist_line(path, text):
    """Write the entry as UTF-8 text with a trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return path


def main():
    line = compose_advice_line()
    problem = check_line(line)
    if problem is not None:
        print("error: %s" % problem, file=sys.stderr)
        return 1
    target = pick_destination()
    persist_line(target, line)
    print("wrote %d chars to %s" % (len(line), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
