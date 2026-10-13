AgriSmart Rwanda — Data Inventory
1. Primary Data Source

- Dataset: Rwanda Seasonal Agricultural Survey 2025
- Producer: National Institute of Statistics of Rwanda (NISR)
- Reference ID: RWA-NISR-SAS-2025-v01
- Reference period: Agricultural year 2024/2025
- Geographic coverage: Rwanda, with district-level estimation for key indicators
- Official catalog: https://microdatabk.statistics.gov.rw/catalog/124
- Data dictionary: https://microdata.statistics.gov.rw/index.php/catalog/124/data_dictionary

2. Agricultural Seasons

- Season A: September 2024 to February 2025
- Season B: March to June 2025
- Season C: July to September 2025

3. Relevant Data Files

The catalog lists the following production datasets:

| Dataset | Catalog-reported records | Variables |
| Season A production | 34,370 | 101 |
| Season B production | 32,921 | 101 |
| Season C production | 1,885 | 99 |

Other potentially relevant datasets include agricultural practices, fertilizer and pesticide use, and screening data for the three seasons.

4. Planned Analysis

The initial analysis will investigate:

1. Crop production and yield measures available in the data.
2. Differences between agricultural seasons.
3. Differences across districts, where the required geographic variables support the analysis.
4. Missing values, duplicate records, variable definitions, and data quality.
5. Associations between available agricultural practices and crop productivity.

5. Machine Learning Feasibility

Crop-yield prediction is a proposed experiment, not a confirmed project capability.

Before training a model, the team will verify the target variable, available predictor variables, sample coverage, and appropriate validation strategy. A model will only be presented if the data supports a defensible evaluation.

6. Data Access and Responsible Use

Before downloading or publishing microdata, verify the catalog's access conditions, licensing, and redistribution permissions.

Do not commit restricted datasets, confidential information, credentials, or personal information to this public repository.

7. Current Status

- [x] Identify the official NISR survey catalog.
- [x] Identify the three seasonal production datasets.
- [ ] Review the data dictionary and variable definitions.
- [ ] Confirm data access and permitted use.
- [ ] Obtain an authorized dataset if needed.
- [ ] Inspect and validate the data before analysis.

## 8. Important Limitation

Catalog record counts are not equivalent to unique farms or farmers. The data structure, sampling design, survey weights, and units of analysis must be checked before calculating or interpreting statistics.
