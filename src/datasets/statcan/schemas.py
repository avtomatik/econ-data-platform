SCHEMA = {
    3790031: {
        "columns": {
            "period": 0,
            "geo": 1,
            "seas": 2,
            "prices": 3,
            "naics": 4,
            "series_id": 5,
            "value": 7,
        },
        "parse_dates": True,
    }
}

TABLE_ID = 3790031

STATCAN_COLUMNS = [
    "period",
    "geo",
    "seas",
    "prices",
    "naics",
    "series_id",
    "value",
]


def enforce_schema(df):
    """Ensure DataFrame has required columns"""
    missing = set(STATCAN_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected StatCan columns: {missing}")
    return df[STATCAN_COLUMNS]
