Day 1 

Objective

The objective of Day 1 was to set up the project environment, organize the repository structure, ingest the provided mutual fund datasets, fetch live NAV data using the MFAPI, and perform initial data exploration and validation.

Workflow: Formation of necessary files in VS Code -Download required packages for study - Load dataset- Summary of dataset - Required modification on dataset.

Summary:-

Datasets Loaded:
- 10 CSV files

Checks Performed:
- Missing values
- Duplicate rows
- Data types
- AMFI code validation

Observations:
- Dataset X has missing NAV values.
- Dataset Y contains duplicate records.
- Date column should be converted to datetime.
- Expense ratio column stored as string.
- All scheme codes matched successfully.