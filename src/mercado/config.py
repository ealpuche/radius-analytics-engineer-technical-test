"""Centralized paths and constants for the mercado package.

All paths are derived from the container working directory (/workspace).
For local execution outside the container, override PROJECT_ROOT via env var.
"""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT: Path = Path(os.environ.get('PROJECT_ROOT', '/workspace'))

RAW_DATA_DIR: Path = PROJECT_ROOT / 'data' / 'raw'
WAREHOUSE_DIR: Path = PROJECT_ROOT / 'data' / 'warehouse'
DUCKDB_PATH: Path = WAREHOUSE_DIR / 'mercado.duckdb'

DBT_PROJECT_DIR: Path = PROJECT_ROOT / 'dbt_project' / 'mercado'
