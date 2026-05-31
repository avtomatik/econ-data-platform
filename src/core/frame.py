import pandas as pd


def coerce_numeric(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    df = df.copy()
    for c in columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def set_index(
    df: pd.DataFrame,
    column: str = "period",
) -> pd.DataFrame:
    return df.set_index(column)
