"""Utilities for saving and loading conversation history."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


def load_history(path: Path) -> List[str]:
    if not path.exists():
        return []
    return path.read_text().splitlines()


def save_history(path: Path, lines: Iterable[str]) -> None:
    path.write_text("\n".join(lines))
