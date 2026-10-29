"""Validate the EV sample dataset and write reproducible audit/summary outputs."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ev_market_data.csv"
OUT = ROOT / "data" / "prepared"
AUDIT = ROOT / "data" / "audit.json"
REQUIRED = ["record_id", "sales_year", "manufacturer", "model", "category", "battery_type",
            "battery_capacity_kwh", "driving_range_km", "price_usd", "manufacturing_country",
            "sales_region", "annual_sales", "customer_rating", "fast_charge_minutes"]


def main():
    df = pd.read_csv(DATA)
    missing_columns = [c for c in REQUIRED if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    OUT.mkdir(parents=True, exist_ok=True)
    numeric = ["sales_year", "battery_capacity_kwh", "driving_range_km", "price_usd", "annual_sales",
               "customer_rating", "fast_charge_minutes"]
    nulls = {c: int(df[c].isna().sum()) for c in REQUIRED}
    duplicate_record_ids = int(df["record_id"].duplicated().sum())
    invalid_rating = int((~df["customer_rating"].between(1, 5)).sum())
    negative_sales = int((df["annual_sales"] < 0).sum())
    audit = {
        "dataset": "data/ev_market_data.csv",
        "data_note": "Synthetic sample data; not official market statistics.",
        "rows": int(len(df)), "columns": int(len(df.columns)),
        "year_min": int(df["sales_year"].min()), "year_max": int(df["sales_year"].max()),
        "unique_manufacturers": int(df["manufacturer"].nunique()),
        "unique_models": int(df["model"].nunique()),
        "unique_categories": int(df["category"].nunique()),
        "unique_battery_types": int(df["battery_type"].nunique()),
        "unique_regions": int(df["sales_region"].nunique()),
        "missing_values_by_column": nulls,
        "duplicate_record_ids": duplicate_record_ids,
        "ratings_outside_1_to_5": invalid_rating,
        "negative_sales_rows": negative_sales,
        "numeric_columns_checked": numeric,
    }
    AUDIT.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    df.groupby("category", as_index=False).agg(records=("record_id", "count"), annual_sales=("annual_sales", "sum"), avg_range_km=("driving_range_km", "mean"), avg_rating=("customer_rating", "mean")).sort_values("annual_sales", ascending=False).to_csv(OUT / "category_summary.csv", index=False)
    df.groupby("manufacturer", as_index=False).agg(records=("record_id", "count"), annual_sales=("annual_sales", "sum"), avg_price_usd=("price_usd", "mean"), avg_range_km=("driving_range_km", "mean")).sort_values("annual_sales", ascending=False).to_csv(OUT / "manufacturer_summary.csv", index=False)
    df.groupby("sales_region", as_index=False).agg(records=("record_id", "count"), annual_sales=("annual_sales", "sum")).sort_values("annual_sales", ascending=False).to_csv(OUT / "region_summary.csv", index=False)
    df.groupby("battery_type", as_index=False).agg(records=("record_id", "count"), avg_capacity_kwh=("battery_capacity_kwh", "mean"), avg_range_km=("driving_range_km", "mean"), avg_charge_minutes=("fast_charge_minutes", "mean")).sort_values("avg_range_km", ascending=False).to_csv(OUT / "battery_summary.csv", index=False)
    print(json.dumps(audit, indent=2))
    if duplicate_record_ids or invalid_rating or negative_sales:
        raise SystemExit("Audit found one or more validation failures; inspect data/audit.json")


if __name__ == "__main__":
    main()
