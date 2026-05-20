"""Inspección rápida de datasets RAW para preparar el EDA."""
from __future__ import annotations

import pandas as pd

RAW = "/workspace/data/raw"

files = {
    "clientes_cdmx.csv":         ("csv", None),
    "clientes_gdl_mty.csv":      ("csv", None),
    "clientes_resto.parquet":    ("parquet", None),
    "catalogo_productos.csv":    ("csv", None),
    "ordenes_2022_2023.parquet": ("parquet", None),
    "ordenes_2024.parquet":      ("parquet", None),
    "devoluciones.txt":          ("csv", "|"),
}

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 220)
pd.set_option("display.max_colwidth", 60)

for fname, (ftype, sep) in files.items():
    print("\n" + "=" * 80)
    print(fname)
    print("=" * 80)
    fpath = f"{RAW}/{fname}"

    if ftype == "csv":
        df = pd.read_csv(fpath, sep=sep, nrows=5) if sep else pd.read_csv(fpath, nrows=5)
    else:
        df = pd.read_parquet(fpath).head(5)

    print(f"Shape (sample): {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nDtypes:\n{df.dtypes}")
    print(f"\nFirst 5 rows:\n{df.to_string()}")
    print(f"\nNulls per column (in sample):\n{df.isna().sum().to_string()}")
