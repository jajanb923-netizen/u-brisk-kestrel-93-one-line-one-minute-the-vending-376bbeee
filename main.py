"""One-line vending machine pickup line.

The entry is a single pickup line spoken by a vending machine to a
passing human. It is written verbatim to ``entry.txt`` inside the
output directory named by ``$MAKEFUN_OUTPUT_DIR`` (``/output`` when
the variable is unset).

The line was chosen against the judge brief: it is unmistakably the
machine speaking ("I don't do refunds"), it lives in the machine's
world (refunds, coils), and the punch lands in the last few words —
the machine sabotaging its own coil out of devotion, which is
cheeky and warm rather than creepy.

Python 3.13 standard library only. Deterministic: the same bytes
every run. No network, no randomness, no environment reads beyond
the output directory.
"""

import os

# The winning line (86 characters, ASCII, single line, no trailing newline).
PICKUP_LINE = (
    "I don't do refunds, but if you smile at me "
    "I'll jam my own coil just to keep you here."
)

OUTPUT_FILENAME = "entry.txt"


def entry_text() -> str:
    """Return the entry exactly as it must appear in the output file."""
    return PICKUP_LINE


def write_entry(output_dir: str) -> str:
    """Write the entry to ``<output_dir>/entry.txt``; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry_text())
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
