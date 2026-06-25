import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).parent / "golden"


def _serialize(value) -> str:
    return repr(value) + "\n"


def assert_matches_golden(actual, golden_id: str) -> None:
    path = GOLDEN_DIR / f"{golden_id.lower()}.approved.txt"
    text = _serialize(actual)
    if os.environ.get("UPDATE_GOLDEN") == "1":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return
    assert path.exists(), f"golden missing: {path}"
    expected = path.read_text(encoding="utf-8")
    assert text == expected, (
        f"golden mismatch: {golden_id}\n--- expected ---\n{expected}--- actual ---\n{text}"
    )
