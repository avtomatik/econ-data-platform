import pandas as pd

from pipelines.imf import pull_imf_can_gdp_by_series_id
from sources.imf.constants import WEO_SERIES_IDS


def build_wide_table(df: pd.DataFrame) -> pd.DataFrame:

    return pd.concat(
        map(
            lambda _: df.pipe(pull_imf_can_gdp_by_series_id, _), WEO_SERIES_IDS
        ),
        axis=1,
        sort=True,
    )
