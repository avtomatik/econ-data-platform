from pathlib import Path

import pandas as pd


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)


def read_excel(path: Path, **kwargs) -> pd.DataFrame:
    return pd.read_excel(path, **kwargs)


def write_parquet(
    df: pd.DataFrame,
    path: Path,
    *,
    index: bool = True,
) -> None:
    df.to_parquet(path, index=index)
