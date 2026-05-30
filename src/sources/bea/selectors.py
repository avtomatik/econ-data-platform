import pandas as pd


def filter_series(
    df: pd.DataFrame, *, name_col: str, unit_col: str
) -> pd.DataFrame:
    mask = (
        ~df[name_col].str.contains("Depreciation", case=False, na=False)
        & df[unit_col].str.contains("Billions", case=False, na=False)
        & ~df[unit_col].str.contains("Years", case=False, na=False)
    )
    return df.loc[mask].copy()


def filter_annual(df: pd.DataFrame, column: str = "subperiod") -> pd.DataFrame:
    # =========================================================================
    # Yearly Data
    # =========================================================================
    return df[df.loc[:, column] == 0].drop(column, axis=1)
