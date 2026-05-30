from pathlib import Path

from core.io import write_parquet
from core.paths import BRONZE_DIR, DATA_DIR
from sources.bea.constants import SERIES_IDS
from sources.bea.readers import read_nipa
from sources.bea.selectors import filter_annual
from sources.bea.transforms import pivot_series


def run(
    source_path: Path = DATA_DIR / "dataset_usa_bea-nipa-2015-05-01.zip",
    output_dir: Path = BRONZE_DIR,
) -> None:
    df = read_nipa(source_path).pipe(filter_annual)

    for series_id in SERIES_IDS:
        result = df.pipe(pivot_series, series_id=series_id)
        result.pipe(
            write_parquet,
            output_dir / f"usa_bea-nipa-2015-05-01-{series_id}.parquet",
        )
