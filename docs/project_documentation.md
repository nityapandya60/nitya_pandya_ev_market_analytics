# Project Documentation — Step by Step

## 1. Problem Understanding
Goal: deliver insights on EV sales, manufacturers, battery technology, range, manufacturing geography and satisfaction for three personas (see README). Success = an interactive Tableau dashboard + story embedded in a Flask UI.

## 2. Data Collection & Extraction
- Source: synthetic dataset (`scripts/generate_dataset.py`) modelled on EV industry attributes; replaceable with a real dataset.
- Output: `data/ev_market_data.csv` (1,488 rows × 14 columns).

## 3. Storing Data in DB
`scripts/load_to_db.py` executes `sql/schema.sql` and loads the CSV into the `ev_sales` table (SQLite). Indexes on year, manufacturer, category.

## 4. SQL Operations
`sql/analysis_queries.sql` — 11 queries: category contribution, market share (window `SUM() OVER`), YoY (`LAG`), CAGR, battery share, range by battery/category, satisfaction, country analysis, regional mix, rank-based competitive analysis. `sql/views.sql` provides pre-aggregated views for Tableau.

## 5. Connect DB with Tableau
Connect via CSV, SQLite ODBC or MySQL. Use `ev_sales` as the primary source; create an extract.

## 6. Data Preparation
Check nulls/duplicates, set data types (Year as discrete, Country geographic role), create hierarchies (Category → Model; Region → Country), groups and the calculated fields in `tableau/calculated_fields.md`.

## 7. Visualizations
14 worksheets listed in `tableau/dashboard_design.md`.

## 8. Dashboard
Executive dashboard with KPI row, filters, actions and device-specific layouts.

## 9. Story
Six scenes (`tableau/story_scenes.md`).

## 10. Performance Testing
See `docs/performance_testing.md`.

## 11. Web Integration (Flask)
`app/app.py` serves pages `/`, `/dashboard`, `/story`, `/personas` and JSON APIs `/api/kpis`, `/api/category-sales`. Tableau is embedded via the Tableau Embedding API v3 (`<tableau-viz>`). Configure URLs with env variables. Deployment options: Render, Railway, PythonAnywhere (`gunicorn app.app:app`).

## 12. Key Insights (sample data — refresh after your Tableau build)
- SUVs ≈ 43% and two-wheelers ≈ 25% of units; two-wheelers have the highest CAGR (~47%).
- 2024 unit leaders: Yadea, BYD, Tesla; two-wheeler makers rank high by volume, not revenue.
- LFP adoption rises over time; NCA declines; Sodium-Ion (2023+) and Solid-State (2024) emerge.
- China leads production; Asia-Pacific is the largest sales region.

## 13. Conclusion & Future Work
Add revenue metrics, charging-infrastructure data, forecasting (Tableau forecast / Prophet), and real data refresh via scheduled extracts.
