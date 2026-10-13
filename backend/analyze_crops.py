
"""
AgriSmart Rwanda
Initial analysis of NISR Season B crop statistics.
"""

from pathlib import Path

import pandas as pd

# Locate the CSV relative to this Python file.
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


def main():
    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        print("Check that the CSV is saved in data/processed/.")
        return

    data = pd.read_csv(DATA_FILE)

    # Check that the expected columns exist.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        print("Missing required columns:", missing_columns)
        return

    # Keep only Season B records for the intended analysis.
    data = data[data["season"].astype(str).str.upper() == "B"].copy()

    # Convert measurement columns to numeric values.
    numeric_columns = [
        "cultivated_area_ha",
        "harvested_area_ha",
        "production_mt",
        "yield_mt_per_ha",
    ]

    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Report data quality before calculating comparisons.
    print("AGRISMART RWANDA — DATA CHECK")
    print("-" * 40)
    print(f"Rows: {len(data)}")
    print(f"Unique crops: {data['crop'].nunique()}")
    print(f"Years: {sorted(data['year'].unique())}")
    print(f"Missing values:\n{data[REQUIRED_COLUMNS].isna().sum()}")

    # Summarize 2025 crop production and yield.
    current_year = data[data["year"] == 2025].copy()

    print("\nSEASON B 2025 — CROP SUMMARY")
    print("-" * 40)

    summary = current_year[
        ["crop", "production_mt", "yield_mt_per_ha"]
    ].sort_values("production_mt", ascending=False)

    print(summary.to_string(index=False))

    # Compare production for the same crop across years.
    production_comparison = data.pivot_table(
        index="crop",
        columns="year",
        values="production_mt",
        aggfunc="first",
    )

    print("\nPRODUCTION COMPARISON BY CROP")
    print("-" * 40)
    print(production_comparison.to_string())

    # Save a reusable analysis result.
    output_dir = PROJECT_ROOT / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "crop_production_comparison.csv"
    production_comparison.to_csv(output_file)

    print(f"\nComparison saved to: {output_file}")


if __name__ == "__main__":
    main()
