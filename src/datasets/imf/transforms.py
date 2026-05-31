import pandas as pd


def to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df


def build_wide_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(
        index="period",
        columns="weo_subject_code",
        values="value",
    ).sort_index()
