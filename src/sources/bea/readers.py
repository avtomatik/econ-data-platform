from pathlib import Path

import pandas as pd

from core.io import read_csv
from sources.bea.parsers import build_bea_read_csv_kwargs


def read_nipa(file_path: Path) -> pd.DataFrame:
    return read_csv(file_path, **build_bea_read_csv_kwargs())
