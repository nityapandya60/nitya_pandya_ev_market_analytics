# EV project validation and delivery notes

This note adapts the reproducibility and source-quality checks used in the companion F1 project to the EV project. It is additive: the original EV application, SQL, documentation, data, and Tableau workbook are retained.

## Added quality controls

- `scripts/audit_data.py` checks the EV CSV schema, row counts, missing values, duplicate record IDs, rating bounds, and negative sales; it writes `data/audit.json` and four analysis-ready CSV summaries under `data/prepared/`.
- `tests/test_project.py` provides automated checks for the dataset, rating and sales ranges, expected project assets, and SQLite schema compatibility.
- `data/audit.json` records the current audit results. Recreate it and the prepared summaries with `python scripts/audit_data.py`.

## Verify locally

```bash
pip install -r requirements.txt
python scripts/audit_data.py
python -m unittest discover -s tests -v
python scripts/load_to_db.py
python scripts/run_queries.py
python app/app.py
```

Open `http://127.0.0.1:5000`. The Tableau workbook is at `tableau/Nitya Pandya.twbx`; open it with Tableau Desktop. For live dashboard/story embedding, replace the placeholder Tableau Public URLs using `TABLEAU_DASHBOARD_URL` and `TABLEAU_STORY_URL`.

## Data and publishing caveats

The included CSV is synthetic sample data and should not be presented as official EV market statistics. The Flask app can run locally, but Tableau embedding is only live after valid published Tableau view URLs are configured. A GitHub repository stores the files; it does not execute the Tableau workbook itself.
