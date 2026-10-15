# AgriSmart Rwanda

**Data-driven agricultural productivity intelligence for Rwanda**, built using published National Institute of Statistics of Rwanda (NISR) Seasonal Agricultural Survey (SAS) 2025, Season B tables.

## Live dashboards

- [National crop dashboard](https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/)
- [District crop productivity explorer](https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/districts.html)
- [Agricultural practices and soil erosion insights](https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/insights.html)

## Features

- National crop statistics and comparisons across years.
- District-level crop yield exploration.
- District-level agricultural practice indicators and plot erosion classifications.
- Data processing workflow and documented datasets.

## Data source

NISR Seasonal Agricultural Survey 2025, Season B. See the [NISR survey catalogue](https://microdatabk.statistics.gov.rw/catalog/124) and the project documentation in `docs/`.

## Important interpretation notes

- The dashboards summarize published survey tables; they do not establish causation.
- District practice indicators and erosion classifications are descriptive. Their association does not prove that a practice caused an erosion outcome.
- Crop categories may overlap. Do not add all categories together unless the source definitions confirm that doing so is valid.
- Missing values are not the same as zero. Consult source table definitions and project data notes before drawing conclusions.
- District-level aggregate tables do not provide farm-level records for training a reliable farm-level prediction model.

## Repository structure

- `data/processed/` — cleaned CSV datasets used by the dashboards.
- `backend/` — data analysis scripts.
- `.github/workflows/` — automated analysis workflow.
- `docs/` — project plan, data inventory, and table documentation.
- `index.html`, `districts.html`, `insights.html` — public dashboard pages.

## Technology

HTML, CSS, JavaScript, Chart.js, Papa Parse, Python, pandas, and GitHub Pages.

## Project status

Student prototype for exploring official agricultural statistics. Interpret results in line with the NISR source definitions and documented limitations.
