# AgriSmart Rwanda — Methodology

## 1. Purpose

AgriSmart Rwanda presents published agricultural statistics in an interactive format so users can explore crop productivity, district differences, agricultural practices, and reported erosion indicators. It is a decision-support prototype, not an official NISR system.

## 2. Data sources and reference periods

The primary source is the National Institute of Statistics of Rwanda (NISR) Seasonal Agricultural Survey (SAS) 2025, especially published Season B tables. The NISR catalogue is available at https://microdatabk.statistics.gov.rw/catalog/124.

The repository documents the selected source tables in [selected_tables.md](selected_tables.md) and the dataset coverage in [data_inventory.md](data_inventory.md). Historical comparisons are shown only where historical observations are available and identified by the application. Users should check the source table, reference period, unit, and definition before comparing values.

## 3. Data preparation and quality checks

The project uses prepared CSV files for browser-based charts and tables. The analysis workflow and script are maintained in the repository. Core quality checks should include:

- Confirm that each indicator has the expected unit and reference period.
- Standardize district and crop labels before comparing records.
- Preserve missing or unavailable observations as missing; do not silently convert them to zero.
- Check duplicate records and unexpected values before publishing results.
- Confirm that a chart or CSV uses the same crop, season, metric, and unit as its displayed labels.
- Keep the source table or dataset reference available to users.

Coverage may vary by crop, district, season, and indicator. A missing observation does not mean that the district had no production or did not use a practice.

## 4. Main calculations and interpretation

### Crop yield and district comparisons

Yield comparisons use the reported yield for the selected crop and district, with the unit shown by the source dataset. District rankings are comparisons of the available reported values, not official NISR rankings.

Where a crop-specific relative index is displayed, it compares a district's reported yield with the mean of valid positive district yields for that crop. The reference group and available observations matter when interpreting the result.

### Summary and distribution statistics

Means, medians, ranges, coefficients of variation, Gini coefficients, and related summaries describe the distribution of the available values used by each tool. They do not automatically account for differences in harvested area, production volume, sampling uncertainty, or all local conditions. Read each tool's definition and coverage notes.

### Agricultural practices and erosion

Practice and erosion indicators are descriptive summaries of the published source data. District-level comparisons may identify questions for further investigation, but they do not show that a farming practice caused a particular erosion outcome. Denominators and indicator definitions must be checked before comparing percentages.

### Trends and season comparisons

Trend charts compare observations available for the selected crop, metric, and reference periods. Changes between periods should not be interpreted as causal effects. Check that periods and units are comparable before drawing conclusions.

### Targets, outliers, and recommendations

User-entered goals, median benchmarks, rankings, and outlier flags are exploratory aids. They are not official targets, agronomic prescriptions, or proof that an observation is erroneous. Recommendations should describe a possible follow-up action—such as verifying local conditions or consulting an agricultural extension officer—and should not claim a proven intervention effect unless supported by suitable evidence.

## 5. Predictive modelling

The presence of trend, ranking, or forecast-style visualizations does not by itself establish a validated predictive model. District-level aggregate data alone are insufficient to make reliable farm-level predictions. Any predictive claim should identify the target variable, features, training and test periods, baseline, evaluation metrics, validation results, and uncertainty. If those requirements are not met, results must be presented as exploratory estimates rather than validated forecasts.

## 6. Responsible use

- Cite NISR and any additional dataset used.
- Keep the original units, definitions, and reference periods visible.
- Do not treat missing values as zero.
- Do not infer causation from descriptive associations.
- Do not present district averages as predictions for an individual farm.
- Seek local expert advice before making operational farming decisions.
- Correct identified data or calculation errors before submission.

## 7. Known limitations

AgriSmart Rwanda is an exploratory student prototype based on published tables. The analysis is constrained by the indicators, geographic detail, time periods, definitions, and data quality available in those sources. District-level statistics cannot represent every farm or explain every cause of productivity differences. Results should be validated against source publications and local knowledge before use in policy or farm decisions.

## 8. Reproducibility and review

The repository includes the processed data, analysis script, requirements, and GitHub Actions workflow. Review the relevant source tables and run the documented local setup before reproducing the application. Final verification should include checking key values against NISR, testing filters and downloads, and reviewing browser-console errors on the deployed pages.
