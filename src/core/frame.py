import pandas as pd


def coerce_numeric(
    df: pd.DataFrame,
    columns: list[str],
) -> pd.DataFrame:
    result = df.copy()

    for column in columns:
        result[column] = pd.to_numeric(
            result[column],
            errors="coerce",
        )

    return result


def set_period_index(
    df: pd.DataFrame,
    column: str = "period",
) -> pd.DataFrame:
    return df.set_index(column)
