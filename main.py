"""Place the finished 21 November 2026 news poster in the output folder.

The poster is shipped with this entry as ``entry.png``, next to this
script. This program does no drawing at all: it only copies that
file to ``/output/entry.png``, making the folder first when it is
missing. Copying the same bytes twice gives the same output twice.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTER = HERE / "entry.png"
OUT = Path("/output") / "entry.png"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER, OUT)
    print(f"Copied {POSTER} -> {OUT}")


if __name__ == "__main__":
    main()
