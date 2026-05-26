import pandas as pd


def transform_year_mean(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(df.index.year).mean()


def transform_year_sum(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(df.index.year).sum()
