"""Create the SQLite database from sql/schema.sql and load the CSV."""
import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ev_market.db"

if DB.exists():
    DB.unlink()
con = sqlite3.connect(DB)
con.executescript((ROOT / "sql" / "schema.sql").read_text())
df = pd.read_csv(ROOT / "data" / "ev_market_data.csv")
df.to_sql("ev_sales", con, if_exists="append", index=False)
con.executescript((ROOT / "sql" / "views.sql").read_text())
print("Rows loaded:", con.execute("SELECT COUNT(*) FROM ev_sales").fetchone()[0])
con.close()
