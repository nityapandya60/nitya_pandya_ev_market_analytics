"""Run every query in sql/analysis_queries.sql and print the first rows."""
import sqlite3, re
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
con = sqlite3.connect(ROOT / "data" / "ev_market.db")
text = (ROOT / "sql" / "analysis_queries.sql").read_text()
for block in re.split(r"(?m)^-- =+\n", text):
    if not block.strip():
        continue
    title = block.strip().splitlines()[0].lstrip("- ")
    print(f"\n### {title}")
    print(pd.read_sql_query(block, con).head(8).to_string(index=False))
