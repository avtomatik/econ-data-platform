FILE_NAME = "FRB_G17(2).csv"
FILE_NAME = "FRB_G17(3).csv"
FILE_NAME = "frb_g17_2.csv"
FILE_NAME = "frb_g17_3.csv"

FILE_NAME = "FRB_H15.zip"

SERIES_ID = "CAPUTL.B00004.S"

SERIES_IDS = (
    "CAPUTL.B00004.S",  # Use This
    "CAPUTL.GMF.S",
)

API_URL = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=g17&filetype.zip"

XPATH = ".//frb:DataSet"

G17_NAMESPACE = {
    "kf": (
        "http://www.federalreserve.gov/structure/"
        "compact/G17_IP_MAJOR_INDUSTRY_GROUPS"
    )
}

DEFAULT_OBSERVATION_COLUMNS = (
    "TIME_PERIOD",
    "OBS_VALUE",
)
