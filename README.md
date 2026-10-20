# AgriSmart Rwanda

**Data-driven agricultural productivity intelligence for Rwanda.**

AgriSmart Rwanda is a student prototype that turns published National Institute of Statistics of Rwanda (NISR) agricultural survey tables into accessible national and district-level summaries. It is designed to help users explore crop yields, compare districts, and identify questions that may deserve further agricultural investigation.

## Live application

- **Main dashboard:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/
- **District crop productivity explorer:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/districts.html
- **Agricultural practices and soil erosion insights:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/insights.html
- **Crop performance dashboard:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/crop-performance.html
- **District map:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/district-map.html
- **Data sources:** https://ishimwedieudonne42-eng.github.io/agrismart-rwanda/data-sources.html

## Core capabilities

- National crop statistics and crop comparisons.
- District-level yield exploration, rankings, and comparisons.
- Crop trend and season comparison tools where historical observations are available.
- Descriptive analysis of agricultural practices and soil-erosion indicators.
- Yield benchmarks, relative-performance comparisons, distribution summaries, and data-coverage checks.
- Downloadable CSV reports for further analysis in spreadsheet software.
- A data-processing script and automated GitHub Actions workflow.

The district explorer contains additional experimental analysis tools. These are descriptive views of the available data, not independent evidence of causal relationships.

## Data sources and scope

The dashboards use published NISR Seasonal Agricultural Survey (SAS) 2025, Season B tables, alongside any explicitly identified historical data included in the repository.

- NISR survey catalogue: https://microdatabk.statistics.gov.rw/catalog/124
- Processed crop-yield data: `data/processed/agrismart_district_crop_yield_2025.csv`
- Processed agricultural-practices data: `data/processed/agrismart_district_agricultural_practices_2025.csv`
- Processed erosion data: `data/processed/agrismart_district_erosion_2025.csv`
- Data inventory: [`docs/data_inventory.md`](docs/data_inventory.md)
- Selected table notes: [`docs/selected_tables.md`](docs/selected_tables.md)

Use the source tables and their definitions when interpreting a statistic. The coverage of indicators and crops can differ; a missing value must not be treated as zero.

## Methodology and interpretation

- **Yield comparisons:** district yields are compared using the crop and unit indicated by the source. Crop-specific relative indices compare a district's reported yield with the mean of valid positive district yields for that crop.
- **Distribution statistics:** summaries such as mean, median, range, coefficient of variation, and Gini coefficient describe the distribution of available district yield values. They do not imply that every district has equal harvested area or production.
- **Practice and erosion indicators:** observed district-level values are descriptive. An association between an agricultural practice and an erosion indicator does not prove that one caused the other.
- **Rankings and targets:** these are exploratory decision-support aids, not official NISR rankings, agronomic prescriptions, or guarantees of achievable yield.
- **Predictions:** no farm-level prediction should be claimed from district-level aggregate tables alone. Any future predictive model needs a suitable dataset, a documented train/test strategy, validation results, and clear uncertainty/limitations.
- **Comparability:** do not add crop categories together unless the NISR definitions establish that they are mutually exclusive and additive.

## Run locally

This is primarily a static HTML/CSS/JavaScript project. To inspect it locally:

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Start a local static web server from the repository root, for example with Python:
   `python -m http.server 8000`
4. Open `http://localhost:8000/` in a browser.

Serving the files over HTTP is recommended because browsers may restrict data-file requests from pages opened directly using `file://`. Python analysis dependencies are listed in [`requirements.txt`](requirements.txt). The front-end dashboards use browser-side JavaScript libraries referenced by the pages.

## Repository structure

- `index.html`, `home.html` — landing and main dashboard pages.
- `districts.html` — district explorer and analysis tools.
- `insights.html`, `recommendations.html` — agricultural practice insights and recommendations.
- `crop-performance.html`, `season-comparison.html`, `district-map.html` — focused dashboard pages.
- `data/processed/` — processed CSV datasets used by the dashboards.
- `backend/analyze_crops.py` — data-analysis script.
- `.github/workflows/analyze.yml` — automated analysis workflow.
- `docs/` — project plan, data inventory, and selected-table notes.

## Technology

HTML, CSS, JavaScript, Chart.js, Papa Parse, Python, pandas, GitHub, GitHub Actions, and GitHub Pages.

## Limitations

AgriSmart Rwanda is an exploratory student prototype, not an official NISR product and not a substitute for expert agricultural advice. Findings depend on the coverage, definitions, and quality of published source data. District aggregates cannot establish farm-level outcomes or causation. Recommendations should be checked against local conditions and validated by qualified agricultural professionals before being used for operational decisions.

## AI assistance disclosure

AI assistance was used to support parts of the project's planning, coding, debugging, and documentation. The project owner remains responsible for reviewing the code, validating calculations and data interpretations, and ensuring that any submitted work follows the hackathon's rules on AI use. Any competition-specific disclosure requirements should be completed in the final submission.

## Final pre-submission checks

Before submitting, manually verify that the live pages load, important charts and filters update correctly, CSV downloads open in spreadsheet software, links work, and no browser-console errors affect core workflows. Confirm that the deployed version matches the public repository. Prepare a short demonstration explaining the problem, NISR data, methods, key findings, limitations, and potential value for Rwanda.
