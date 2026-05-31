import pandas as pd


def to_datetime_index(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.index = pd.to_datetime(df.index)
    return df


def normalize_frb_table(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.dropna(axis=1, how="all").transpose().iloc[3:].rename_axis("period")
    )
