import pandas as pd


def require_columns(
    df: pd.DataFrame,
    columns: list[str],
) -> None:

    missing = set(columns) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
