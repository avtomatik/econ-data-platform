def build_bea_read_csv_kwargs():

    NAMES = ["source_id", "series_id", "period", "subperiod", "value"]
    USECOLS = [0, 14, 15, 16, 17]

    return {
        "header": 0,
        "names": NAMES,
        "index_col": 2,
        "usecols": USECOLS,
    }
