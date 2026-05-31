import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)


def read_excel(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_excel(path, **kwargs)


def read_xml(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_xml(path, **kwargs)


def write_parquet(
    df: pd.DataFrame,
    path: Path,
    *,
    index: bool = True,
    source: str | None = None,
    pipeline_version: str | None = None,
) -> None:
    """Write Parquet and store provenance metadata"""
    df.to_parquet(path, index=index)

    # provenance metadata
    metadata = {
        "written_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "pipeline_version": pipeline_version,
        "rows": len(df),
        "columns": list(df.columns),
    }

    meta_path = path.with_suffix(".metadata.json")
    with meta_path.open("w") as f:
        json.dump(metadata, f, indent=2)
