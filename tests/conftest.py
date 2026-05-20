"""Shared pytest fixtures for the mercado package tests."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Absolute path to the project root."""
    return Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def raw_data_dir(project_root: Path) -> Path:
    """Path to the raw data directory."""
    return project_root / "data" / "raw"
