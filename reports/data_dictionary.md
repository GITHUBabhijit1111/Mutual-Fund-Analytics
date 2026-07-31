# Mutual Fund Analytics - Data Dictionary

## Project Overview

This document describes the datasets used in the Mutual Fund Analytics project. It includes the column names, data types, business definitions, and source references for each dataset.

---

# 1. Fund Master

**Source File:** `01_fund_master.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| amfi_code | INTEGER | Unique AMFI scheme identifier | AMFI India |
| fund_house | TEXT | Name of the Asset Management Company (AMC) | AMFI India |
| scheme_name | TEXT | Name of the mutual fund scheme | AMFI India |
| category | TEXT | Mutual fund category (Equity, Debt, Hybrid, etc.) | AMFI India |
| sub_category | TEXT | Detailed classification within the category | AMFI India |
| risk_level | TEXT | Risk rating of the scheme | AMFI India |

---

# 2. NAV History

**Source File:** `02_nav_history.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund scheme code | MFAPI / AMFI |
| date | DATE | Date of NAV | MFAPI |
| nav | REAL | Net Asset Value per unit | MFAPI |

---

# 3. AUM by Fund House

**Source File:** `03_aum_by_fund_house.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| fund_house | TEXT | Name of the AMC | AMFI |
| month | DATE | Reporting month | AMFI |
| aum | REAL | Assets Under Management | AMFI |

---

# 4. Monthly SIP Inflows

**Source File:** `04_monthly_sip_inflows.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| month | DATE | Reporting month | AMFI |
| sip_inflow | REAL | Total SIP investments received | AMFI |

---

# 5. Category Inflows

**Source File:** `05_category_inflows.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| category | TEXT | Mutual fund category | AMFI |
| inflow | REAL | Total inflow into the category | AMFI |

---

# 6. Industry Folio Count

**Source File:** `06_industry_folio_count.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| month | DATE | Reporting month | AMFI |
| folio_count | INTEGER | Total investor folios | AMFI |

---

# 7. Scheme Performance

**Source File:** `07_scheme_performance.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund scheme code | AMFI |
| one_year_return | REAL | 1-Year annual return (%) | AMFI |
| three_year_return | REAL | 3-Year annual return (%) | AMFI |
| five_year_return | REAL | 5-Year annual return (%) | AMFI |
| expense_ratio | REAL | Annual expense ratio (%) | AMFI |

---

# 8. Investor Transactions

**Source File:** `08_investor_transactions.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| investor_id | TEXT | Unique investor identifier | Internal |
| amfi_code | INTEGER | Mutual fund scheme code | Internal |
| transaction_date | DATE | Date of transaction | Internal |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption | Internal |
| amount | REAL | Transaction amount | Internal |
| state | TEXT | Investor state | Internal |
| kyc_status | TEXT | KYC verification status | Internal |

---

# 9. Portfolio Holdings

**Source File:** `09_portfolio_holdings.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| amfi_code | INTEGER | Mutual fund scheme code | AMFI |
| company | TEXT | Company held in the portfolio | AMFI |
| sector | TEXT | Industry sector | AMFI |
| weight | REAL | Percentage allocation in portfolio | AMFI |

---

# 10. Benchmark Indices

**Source File:** `10_benchmark_indices.csv`

| Column Name | Data Type | Business Definition | Source |
|-------------|-----------|---------------------|--------|
| index_name | TEXT | Benchmark index name | NSE/BSE |
| date | DATE | Observation date | NSE/BSE |
| index_value | REAL | Closing index value | NSE/BSE |

---

# Data Sources

- Association of Mutual Funds in India (AMFI)
- MFAPI (https://api.mfapi.in)
- Internal Sample Investor Dataset
- National Stock Exchange (NSE)
- Bombay Stock Exchange (BSE)

---

# Notes

- Dates are stored in **YYYY-MM-DD** format.
- Monetary values are stored as **REAL**.
- Percentage values are stored as numeric percentages.
- AMFI code acts as the primary business key across mutual fund datasets.
- All cleaned datasets are stored in the `data/processed/` directory.