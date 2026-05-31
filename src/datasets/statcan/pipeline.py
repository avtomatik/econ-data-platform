from pathlib import Path

from core.io import read_csv, write_parquet
from core.paths import BRONZE_DIR, DATA_DIR
from datasets.statcan import __version__ as pipeline_version
from datasets.statcan.parsers import build_statcan_read_csv_kwargs
from datasets.statcan.schemas import SCHEMA, TABLE_ID, enforce_schema
from datasets.statcan.selectors import filter_manufacturing
from datasets.statcan.transforms import pivot_and_rebase, to_numeric


def run(
    source_path: Path = DATA_DIR / f"dataset_can_{TABLE_ID:08n}-eng.zip",
    output_dir: Path = BRONZE_DIR,
) -> None:
    df = (
        read_csv(
            source_path,
            **build_statcan_read_csv_kwargs(TABLE_ID, SCHEMA),
        )
        .pipe(filter_manufacturing)
        .pipe(enforce_schema)
        .pipe(to_numeric)
    )

    wide = pivot_and_rebase(df)

    write_parquet(
        wide,
        output_dir / "statcan_canada.parquet",
        source=source_path.name,
        pipeline_version=f"v{pipeline_version}",
    )
