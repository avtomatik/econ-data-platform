from pathlib import Path

from core.io import read_csv, write_parquet
from core.paths import BRONZE_DIR, DATA_DIR
from datasets.imf import __version__ as pipeline_version
from datasets.imf.selectors import (filter_actual_observations, filter_country,
                                    filter_release, filter_series)
from datasets.imf.transforms import build_wide_table, to_numeric


def run(
    source_path: Path = DATA_DIR
    / "dataset World IMF World Economic Outlook.csv",
    output_dir: Path = BRONZE_DIR,
) -> None:

    df = (
        read_csv(
            source_path,
            low_memory=False,
        )
        .pipe(filter_release, 2015)
        .pipe(filter_country, "CAN")
        .pipe(filter_series)
        .pipe(filter_actual_observations)
        .pipe(to_numeric)
    )

    wide = build_wide_table(df)

    write_parquet(
        wide,
        output_dir / "imf_weo_canada.parquet",
        source=source_path.name,
        pipeline_version=f"v{pipeline_version}",
    )
