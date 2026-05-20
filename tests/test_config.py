"""Tests del módulo src/mercado/config.py.

Valida que las constantes derivadas de PROJECT_ROOT mantengan la estructura
esperada del proyecto (data/raw, data/warehouse, dbt_project/mercado, etc).
Estos tests sirven como contract testing del módulo de configuración y
garantizan cobertura mínima para que el CI pase desde la fase de scaffolding.
"""

from __future__ import annotations

from pathlib import Path

from mercado import config


def test_project_root_es_un_path():
    """PROJECT_ROOT debe ser un objeto Path."""
    assert isinstance(config.PROJECT_ROOT, Path)


def test_raw_data_dir_bajo_project_root():
    """RAW_DATA_DIR debe estar bajo PROJECT_ROOT/data/raw."""
    assert config.RAW_DATA_DIR == config.PROJECT_ROOT / "data" / "raw"


def test_warehouse_dir_bajo_project_root():
    """WAREHOUSE_DIR debe estar bajo PROJECT_ROOT/data/warehouse."""
    assert config.WAREHOUSE_DIR == config.PROJECT_ROOT / "data" / "warehouse"


def test_duckdb_path_bajo_warehouse():
    """DUCKDB_PATH debe ser WAREHOUSE_DIR/mercado.duckdb."""
    assert config.DUCKDB_PATH == config.WAREHOUSE_DIR / "mercado.duckdb"


def test_dbt_project_dir_apunta_a_mercado():
    """DBT_PROJECT_DIR debe apuntar a dbt_project/mercado/."""
    assert config.DBT_PROJECT_DIR == config.PROJECT_ROOT / "dbt_project" / "mercado"
