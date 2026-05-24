"""Small path helpers for the SNL 2026 SRM + layer-wise GPT-2 project.

The notebooks are intentionally kept readable, but these helpers provide a
single place to document the expected local path layout for a GitHub clone.
"""

from pathlib import Path
from typing import Iterable


def project_root() -> Path:
    """Return the repository root from this file location."""
    return Path(__file__).resolve().parents[1]


def ensure_dirs(paths: Iterable[Path]) -> None:
    """Create output directories when they do not already exist."""
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def require_file(path: Path, label: str = "required file") -> Path:
    """Raise a clear error if an expected local data file is missing."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing {label}: {path}")
    return path
