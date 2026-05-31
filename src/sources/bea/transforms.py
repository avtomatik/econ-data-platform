import pandas as pd


def pivot_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:

    chunk = df[df["series_id"] == series_id]

    wide = chunk.pivot(index="period", columns="source_id", values="value")

    wide.columns = [
        f"{column.split()[1].replace('.','_')}{series_id}"
        for column in wide.columns
    ]

    return wide
