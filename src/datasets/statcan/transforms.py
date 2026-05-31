import pandas as pd


def to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df


def pivot_and_rebase(df: pd.DataFrame, base_year: int = 2012) -> pd.DataFrame:
    wide = df.pivot(
        index="period",
        columns="series_id",
        values="value",
        aggfunc="first",
    )

    wide = wide.groupby(wide.index.year).mean()

    wide["deflator"] = wide.iloc[:, 0] / wide.iloc[:, 1]
    wide = wide / wide.loc[base_year]

    wide["real_rebased"] = wide.iloc[:, 1] * wide["deflator"]

    return wide
