import pandas as pd


def filter_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:

    assert df.shape[1] == 2
    return (
        df[df["series_id"] == series_id]
        .iloc[:, [1]]
        .rename(columns={"value": series_id})
    )


def filter_country(df: pd.DataFrame, iso3: str) -> pd.DataFrame:
    return df[df["weo_country_code"] == iso3]


def filter_release(df: pd.DataFrame, year_base: int) -> pd.DataFrame:
    return df[
        df["release"]
        == f"International Monetary Fund, World Economic Outlook Database, April {year_base}"
    ]
