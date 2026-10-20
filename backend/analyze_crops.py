"""
AgriSmart Rwanda
Initial analysis of NISR Season B crop statistics.

This script validates the prepared input before creating a crop comparison
artifact. Validation failures exit with a non-zero status so automation can
report them instead of silently succeeding.
"""

from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "agrismart_season_b_crop_data.csv"
)

REQUIRED_COLUMNS = [
    "crop",
    "year",
    "season",
    "cultivated_area_ha",
    "harvested_area_ha",
    "production_mt",
    "yield_mt_per_ha",
]

NUMERIC_COLUMNS = [
    "cultivated_area_ha",
    "harvested_area_ha",
    "production_mt",
    "yield_mt_per_ha",
]


def fail(message):
    """Print an actionable validation error and fail the workflow."""
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    if not DATA_FILE.exists():
        fail(f"Dataset not found: {DATA_FILE}")

    try:
        data = pd.read_csv(DATA_FILE)
    except Exception as exc:
        fail(f"Could not read {DATA_FILE.name}: {exc}")

    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in data.columns
    ]
    if missing_columns:
        fail(f"Missing required columns: {missing_columns}")

    if data.empty:
        fail("The input dataset contains no rows.")

    # Validate identifying fields before filtering the requested season.
    for column in ["crop", "season"]:
        if data[column].isna().any() or data[column].astype(str).str.strip().eq("").any():
            fail(f"Required identifier column '{column}' contains blank values.")

    data["year"] = pd.to_numeric(data["year"], errors="coerce")
    if data["year"].isna().any():
        fail("The year column contains missing or non-numeric values.")
    if (data["year"] % 1 != 0).any():
        fail("The year column contains non-integer values.")
    data["year"] = data["year"].astype(int)

    # Keep only Season B records for the intended analysis.
    data = data[data["season"].astype(str).str.strip().str.upper() == "B"].copy()
    if data.empty:
        fail("No Season B records were found.")

    for column in NUMERIC_COLUMNS:
        original = data[column]
        converted = pd.to_numeric(original, errors="coerce")
        invalid = original.notna() & converted.isna()
        if invalid.any():
            fail(f"Column '{column}' contains {int(invalid.sum())} non-numeric value(s).")
        data[column] = converted

        if (data[column].dropna() < 0).any():
            fail(f"Column '{column}' contains negative values.")

    duplicate_mask = data.duplicated(subset=["crop", "year", "season"], keep=False)
    if duplicate_mask.any():
        examples = data.loc[duplicate_mask, ["crop", "year", "season"]].head(5)
        fail(
            "Duplicate crop/year/season records found. "
            f"Example keys: {examples.to_dict(orient='records')}"
        )

    print("AGRISMART RWANDA — DATA CHECK")
    print("-" * 40)
    print(f"Input file: {DATA_FILE.relative_to(PROJECT_ROOT)}")
    print(f"Season B rows: {len(data)}")
    print(f"Unique crops: {data['crop'].nunique()}")
    print(f"Years: {sorted(data['year'].unique().tolist())}")
    print(f"Missing values:\n{data[REQUIRED_COLUMNS].isna().sum()}")

    current_year = data[data["year"] == 2025].copy()
    if current_year.empty:
        fail("No Season B 2025 rows were found; refusing to create an empty summary.")

    print("\nSEASON B 2025 — CROP SUMMARY")
    print("-" * 40)
    summary = current_year[
        ["crop", "production_mt", "yield_mt_per_ha"]
    ].sort_values("production_mt", ascending=False, na_position="last")
    print(summary.to_string(index=False))

    production_comparison = data.pivot_table(
        index="crop",
        columns="year",
        values="production_mt",
        aggfunc="first",
    )

    if production_comparison.empty:
        fail("Production comparison is empty; no artifact was created.")

    print("\nPRODUCTION COMPARISON BY CROP")
    print("-" * 40)
    print(production_comparison.to_string())

    output_dir = PROJECT_ROOT / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "crop_production_comparison.csv"
    production_comparison.to_csv(output_file)
    print(f"\nComparison saved to: {output_file}")


if __name__ == "__main__":
    main()
