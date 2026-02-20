from __future__ import annotations
from pathlib import Path

def project_root() -> Path:
    return Path(__file__).resolve().parents[1]

DATA_RAW = project_root() / "data" / "raw"
OUTPUTS = project_root() / "outputs" / "figures"
