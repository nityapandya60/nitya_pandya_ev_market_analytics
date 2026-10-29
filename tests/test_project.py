"""Automated smoke tests inspired by the F1 project's reproducible checks."""
import unittest
from pathlib import Path
import pandas as pd
import sqlite3

ROOT = Path(__file__).resolve().parents[1]

class EVProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv = pd.read_csv(ROOT / "data" / "ev_market_data.csv")

    def test_dataset_has_expected_schema_and_rows(self):
        expected = {"record_id", "sales_year", "manufacturer", "model", "category", "battery_type",
                    "battery_capacity_kwh", "driving_range_km", "price_usd", "manufacturing_country",
                    "sales_region", "annual_sales", "customer_rating", "fast_charge_minutes"}
        self.assertTrue(expected.issubset(set(self.csv.columns)))
        self.assertGreater(len(self.csv), 0)

    def test_record_ids_are_unique_and_ratings_valid(self):
        self.assertEqual(int(self.csv["record_id"].duplicated().sum()), 0)
        self.assertTrue(self.csv["customer_rating"].between(1, 5).all())

    def test_sales_and_year_ranges_are_sensible(self):
        self.assertTrue((self.csv["annual_sales"] >= 0).all())
        self.assertTrue(self.csv["sales_year"].between(2019, 2024).all())

    def test_required_project_assets_exist(self):
        for rel in ["app/app.py", "app/templates/index.html", "sql/schema.sql",
                    "sql/analysis_queries.sql", "tableau/Nitya Pandya.twbx"]:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_sqlite_load_script_builds_expected_table(self):
        # Validate schema compatibility without modifying the user's project database.
        con = sqlite3.connect(":memory:")
        con.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        cols = {row[1] for row in con.execute("PRAGMA table_info(ev_sales)")}
        self.assertIn("annual_sales", cols)
        self.assertIn("customer_rating", cols)
        con.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
