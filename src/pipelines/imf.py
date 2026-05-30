import pandas as pd

from core.frame import set_period_index
from core.io import read_csv
from core.paths import DATA_DIR
from sources.imf.constants import COUNTRY_CANADA
from sources.imf.selectors import (filter_country, filter_df, filter_release,
                                   filter_series)
from sources.imf.transforms import build_wide_table
from sources.statcan.parsers import build_statcan_read_csv_kwargs
from sources.statcan.schemas import SCHEMA, TABLE_ID


def pull_imf_can_gdp_by_series_id(
    df: pd.DataFrame, series_id: str
) -> pd.DataFrame:

    chunk = df[df.iloc[:, 4] == series_id]
    chunk.columns = ("period", series_id)
    chunk = chunk.drop(
        chunk[chunk.iloc[:, 11] == "Estimates Start After"].index
    )
    chunk = chunk.iloc[:, (11, 12)]
    chunk.iloc[:, 1] = chunk.iloc[:, 1].astype(float)
    return set_period_index(chunk)


def run() -> None:

    df = read_csv(
        DATA_DIR / f"dataset_can_{TABLE_ID:08n}-eng.zip",
        **build_statcan_read_csv_kwargs(TABLE_ID, SCHEMA),
    ).pipe(filter_df)
    # =============================================================================
    # Kludge
    # =============================================================================
    df.iloc[:, -1] = df.iloc[:, -1].apply(pd.to_numeric, errors="coerce")

    df_can = pd.concat(
        map(
            lambda _: df.pipe(filter_series, _),
            sorted(set(df.loc[:, "series_id"])),
        ),
        axis=1,
        sort=True,
    )
    df_can = df_can.groupby(df_can.index.year).mean()
    df_can["def"] = df_can.iloc[:, 0].div(df_can.iloc[:, 1])
    df_can = df_can.div(df_can.loc[2012, :])
    df_can["real_rebased"] = df_can.iloc[:, 1].mul(df_can.iloc[:, -1])

    # "dataset_world_imf-WEOApr2018all.xls"

    read_csv(
        DATA_DIR / "dataset World IMF World Economic Outlook.csv",
        low_memory=False,
    ).pipe(filter_release, 2015).pipe(filter_country, COUNTRY_CANADA).pipe(
        build_wide_table
    )
