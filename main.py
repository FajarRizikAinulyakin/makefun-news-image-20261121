"""Place the finished 21 November 2026 news poster in the output folder.

The poster is shipped with this entry as ``entry.png``, next to this
script. This program does no drawing at all: it only copies that
file to ``/output/entry.png``, making the folder first when it is
missing. Copying the same bytes twice gives the same output twice.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTER = HERE / "entry.png"
OUT = Path("/output") / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not POSTER.is_file():
        raise FileNotFoundError(f"Source poster missing: {POSTER}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER, OUT)
    if OUT.stat().st_size != POSTER.stat().st_size:
        raise RuntimeError(
            f"Copy size mismatch: {POSTER} is {POSTER.stat().st_size} bytes "
            f"but {OUT} is {OUT.stat().st_size} bytes"
        )
    if _sha256(OUT) != _sha256(POSTER):
        raise RuntimeError(f"Copy failed verification: {OUT} differs from {POSTER}")
    print(f"Copied {POSTER} -> {OUT} (verified)")


if __name__ == "__main__":
    main()
