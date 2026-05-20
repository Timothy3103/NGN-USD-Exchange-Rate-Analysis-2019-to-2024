# NGN/USD Exchange Rate Analysis — 2019 to 2024

**Author:** Ojo Timothy  
**Data Source:** CBN Official Rates (NFEM/NAFEX window) — monthly averages compiled from CBN Statistical Bulletins and published economic reports  
**Period:** January 2019 – December 2024  

---

## Project Overview

This project analyses the trajectory of the Nigerian Naira (NGN) against the US Dollar (USD) over six years — a period that spans a COVID-19 shock devaluation, multiple CBN-managed rate adjustments, and ultimately the landmark exchange rate unification of June 2023 under President Tinubu's administration, which triggered the most dramatic single-month depreciation in Nigeria's modern monetary history.

The goal is to quantify the scale of Naira depreciation, identify the key inflection points, and visualise trends using rolling averages, month-on-month changes, and cumulative depreciation from a 2019 baseline.

---

## Key Findings

| Metric | Value |
|--------|-------|
| January 2019 rate | ₦306.9 / USD |
| December 2024 rate | ₦1,535.0 / USD |
| Total 6-year depreciation | **+400.2%** |
| Biggest single-month jump | June 2023: **+66.7%** (₦462 → ₦770) |
| 2024 annual average | ₦1,495.4 / USD |
| 2019 annual average | ₦306.9 / USD |

### Three distinct depreciation phases

**Phase 1 — Managed Peg (2019–May 2023)**  
The CBN maintained a tightly managed rate, with periodic step devaluations. COVID-19 triggered the first significant adjustment in March 2020 (₦307 → ₦360). The rate remained relatively stable through 2021–2022, creeping from ₦415 to ₦462 over 18 months.

**Phase 2 — Unification Shock (June–December 2023)**  
President Tinubu's removal of the multi-tier exchange rate system in June 2023 caused a 66.7% single-month jump — the largest in the dataset. The rate went from ₦462 to ₦770 in one month and continued depreciating to ₦980 by November 2023.

**Phase 3 — Float Volatility (2024)**  
After unification, the Naira continued to depreciate sharply, peaking at ₦1,670/USD in November 2024 before a slight recovery to ₦1,535 at year-end. The 2024 annual average of ₦1,495 represents a 115% increase over the 2023 average of ₦694.

---

## Charts

| Chart | Description |
|-------|-------------|
| `01_full_timeline.png` | Full rate timeline with 3M/6M rolling averages and key event markers |
| `02_mom_change.png` | Month-on-month % change — identifies the sharpest depreciation months |
| `03_yoy_depreciation.png` | Year-on-year % change — shows the accelerating pace of depreciation |
| `04_annual_avg.png` | Annual average rate with min–max range bars |
| `05_cumulative_depreciation.png` | Cumulative % depreciation from January 2019 baseline |

---

## Project Structure

```
exchange-rate-analysis/
├── data/
│   └── ngn_usd_exchange_rate_2019_2024.csv
├── charts/
│   ├── 01_full_timeline.png
│   ├── 02_mom_change.png
│   ├── 03_yoy_depreciation.png
│   ├── 04_annual_avg.png
│   └── 05_cumulative_depreciation.png
├── exchange_rate_analysis.py
├── exchange_rate_analysis.ipynb
└── README.md
```

---

## Tools & Libraries

- **Python 3** — core language
- **Pandas** — data manipulation and time-series analysis
- **Matplotlib** — data visualisation

---

## How to Run

```bash
git clone https://github.com/Timothy3103/ngn-usd-exchange-rate-analysis
cd exchange-rate-analysis

pip install pandas matplotlib

python exchange_rate_analysis.py
# or
jupyter notebook exchange_rate_analysis.ipynb
```

---

## Data Notes

Monthly average rates are based on the CBN's NFEM (Nigerian Foreign Exchange Market) official window — the same rate used for government transactions and formal trade. The parallel/black market rate (which was significantly higher before June 2023 unification) is not included in this dataset. Prior to June 2023, a significant premium existed between the official and parallel rates.
