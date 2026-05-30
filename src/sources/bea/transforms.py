import pandas as pd


def pivot_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """
    Retrieve Yearly Data for BEA Series ID
    """
    df = df[df.loc[:, "series_id"] == series_id]
    source_ids = sorted(set(df.loc[:, "source_id"]))
    chunk = pd.concat(
        map(
            lambda _: df[df.loc[:, "source_id"] == _]
            .iloc[:, [-1]]
            .drop_duplicates(),
            source_ids,
        ),
        axis=1,
        sort=True,
    )
    chunk.columns = map(
        lambda _: "".join((_.split()[1].replace(".", "_"), series_id)),
        source_ids,
    )
    return chunk
