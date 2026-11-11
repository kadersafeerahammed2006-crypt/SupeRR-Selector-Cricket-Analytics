# SupeRR Selector Season 2 – PressurePlay Analytics

Python analytics pipeline for identifying and ranking the batters and bowlers who perform most reliably in high-pressure IPL and T20I situations from 2022 onwards.

This repository does **not** invent player statistics. Every calculation uses the six supplied CSV files.

## Status

**Complete.** All eight stages are implemented, validated and reproducible:

1. Data understanding
2. Data cleaning
3. Data integration
4. Feature engineering and pressure classification
5. Exploratory data analysis
6. Rating and ranking engine
7. Power BI export preparation
8. Dashboard design

## Final deliverables

| Deliverable | Location |
|---|---|
| Round 1 methodology report (PDF) | `reports/SupeRR_Selector_Season2_Round1_Methodology_Report.pdf` |
| Round 1 methodology report (DOCX) | `reports/SupeRR_Selector_Season2_Round1_Methodology_Report.docx` |
| Round 1 methodology report (Markdown source) | `reports/SupeRR_Selector_Season2_Round1_Methodology_Report.md` |
| Top 10 batters | `outputs/phase6/top_10_batters.csv` |
| Top 10 bowlers | `outputs/phase6/top_10_bowlers.csv` |
| Full rankings (264 batters, 244 bowlers) | `outputs/phase6/complete_*_rankings.csv` |
| Validation and stability audit | `outputs/phase6/ranking_validation_report.csv`, `outputs/phase6/ranking_stability_analysis.csv` |
| Power BI tables | `data/powerbi/` |

## Data

The six original datasets live only in `data/raw/`. Analysis code reads those files and never overwrites them.

| File | Role |
| --- | --- |
| `ball_by_ball.csv` | Delivery-level events |
| `matches.csv` | Match metadata and results |
| `competitions.csv` | Competition, format, season |
| `teams.csv` | Teams by competition |
| `playing_eleven.csv` | Match playing XIs |
| `competition_team_player_mapping.csv` | Player names by competition and team |

## How to run

```bash
python -m pip install -r requirements.txt
python run_project.py
```

`run_project.py` executes the full pipeline from raw data to rankings, validation and Power BI exports. Individual stages can also be run separately (`run_phase1.py`, `src/run_phase2.py` … `src/run_phase8.py`).

## Method in one paragraph

Every delivery is classified as Low, Medium, High or Critical pressure using only pre-delivery match state: required run rate versus current run rate, wickets remaining, balls remaining, innings stage and format-specific par rates. High and Critical form the pressure cohort (28.3% of 200,999 deliveries). Each player is then compared with his own Low/Medium baseline on five weighted pillars: baseline differential (35%), absolute pressure performance (25%), secondary pressure output (20%), dot/boundary control (10%) and match-to-match consistency (10%). Raw 0–100 ratings are shrunk toward the eligible-cohort mean using an Empirical Bayes reliability factor, so short samples cannot outrank proven records. The final rankings passed 13/13 validation checks and remained stable across 10 weighting and eligibility scenarios (Spearman ρ ≥ 0.969).

## Project layout

```
config/settings.py              # paths, pressure thresholds, weights, eligibility, reliability
src/                            # phase 1–8 pipeline modules
data/raw/                       # original CSVs (do not modify)
data/processed/                 # cleaned, integrated and feature-engineered tables
data/powerbi/                   # Power BI export tables
outputs/phase1 … phase6/        # summaries, charts, rankings, validation
reports/                        # methodology and findings reports
logs/                           # pipeline logs
run_project.py                  # end-to-end runner
```

## Key parameters

- Pressure cohort: High + Critical deliveries
- Chase thresholds: RRR − CRR ≤ 0 (Low), ≤ 4 (Medium), ≤ 10 or wickets ≤ 4 (High), > 10 / RRR > 18 / wickets ≤ 2 (Critical)
- First-innings par rates: IPL 8.75, T20I 8.20, Other T20 8.43
- Eligibility: 50 pressure balls, 30 normal balls, 5 matches
- Reliability: `ρ = (N / (N + 60)) × sqrt(M / (M + 5))`
- Shrinkage target: eligible-cohort mean (46.36 batting, 50.09 bowling)

## Documentation

- `reports/SupeRR_Selector_Season2_Round1_Methodology_Report.pdf` – submission-ready methodology report
- `reports/phase6_ranking_methodology.md` – detailed ranking engine documentation
- `reports/phase5_eda_findings.md` – exploratory analysis and statistical tests
- `reports/phase4_feature_engineering_findings.md` – pressure definition and feature formulas
- `reports/phase7_powerbi_data_dictionary.md` – Power BI table documentation
