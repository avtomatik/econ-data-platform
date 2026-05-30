import pandas as pd


def filter_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """


    Parameters
    ----------
    df : pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series IDs
        df.iloc[:, 1]      Values
        ================== =================================
    series_id : str

    Returns
    -------
    pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series
        ================== =================================
    """
    assert df.shape[1] == 2
    return (
        df[df.iloc[:, 0] == series_id]
        .iloc[:, [1]]
        .rename(columns={"value": series_id})
    )


def filter_df(df: pd.DataFrame) -> pd.DataFrame:
    FILTER = (df.loc[:, "naics"] == "All industries (x 1,000,000)") & (
        df.loc[:, "series_id"] != "v65201756"
    )
    FILTER = (df.loc[:, "naics"] == "Manufacturing (x 1,000,000)") & (
        df.loc[:, "series_id"] != "v65201809"
    )
    return df[FILTER].iloc[:, -2:]


def filter_country(df: pd.DataFrame, iso3: str) -> pd.DataFrame:
    return df[df.iloc[:, 3] == iso3]


def filter_release(df: pd.DataFrame, year_base: int) -> pd.DataFrame:
    return df[
        df.iloc[:, 1]
        == f"International Monetary Fund, World Economic Outlook Database, April {year_base}"
    ]
