"""Generate a synthetic EV market dataset (2019-2024).

Replace data/ev_market_data.csv with a real dataset (e.g. from Kaggle) if you
have one; just keep the same column names or adapt sql/schema.sql.
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
YEARS = list(range(2019, 2025))
REGIONS = {"Asia-Pacific": 0.45, "Europe": 0.25, "North America": 0.22, "Rest of World": 0.08}

# manufacturer: (HQ/manufacturing country, weight, categories offered, quality bias)
MAKERS = {
    "Tesla":        ("USA", 1.00, ["Sedan", "SUV", "Truck"], 0.20),
    "BYD":          ("China", 1.15, ["Hatchback", "Sedan", "SUV", "Bus"], 0.10),
    "Tata Motors":  ("India", 0.55, ["Hatchback", "SUV", "Bus"], 0.00),
    "MG Motor":     ("China", 0.45, ["Hatchback", "SUV"], -0.05),
    "Hyundai":      ("South Korea", 0.50, ["Hatchback", "SUV", "Sedan"], 0.05),
    "Kia":          ("South Korea", 0.42, ["SUV", "Sedan"], 0.05),
    "Nissan":       ("Japan", 0.35, ["Hatchback", "SUV"], 0.00),
    "BMW":          ("Germany", 0.38, ["Sedan", "SUV"], 0.15),
    "Volkswagen":   ("Germany", 0.60, ["Hatchback", "SUV", "Sedan"], 0.00),
    "Mahindra":     ("India", 0.30, ["SUV", "Truck"], 0.00),
    "Ola Electric": ("India", 0.40, ["Two-Wheeler"], -0.10),
    "Ather Energy": ("India", 0.20, ["Two-Wheeler"], 0.10),
    "NIO":          ("China", 0.25, ["Sedan", "SUV"], 0.10),
    "Volvo":        ("Sweden", 0.22, ["SUV", "Truck", "Bus"], 0.10),
    "Ford":         ("USA", 0.30, ["SUV", "Truck"], -0.05),
    "Rivian":       ("USA", 0.15, ["SUV", "Truck"], 0.10),
    "Ashok Leyland":("India", 0.12, ["Bus", "Truck"], -0.05),
    "Yadea":        ("China", 0.35, ["Two-Wheeler"], 0.00),
}
CAT = {  # capacity kWh (lo, hi), km per kWh, avg units per model-region-year, base price USD
    "Hatchback":   ((30, 55), 7.0, 9000, 22000),
    "Sedan":       ((55, 100), 6.5, 7000, 48000),
    "SUV":         ((55, 110), 5.5, 11000, 52000),
    "Bus":         ((200, 350), 1.2, 350, 280000),
    "Truck":       ((150, 300), 1.5, 600, 150000),
    "Two-Wheeler": ((2, 6), 30.0, 40000, 2500),
}
CAT_GROWTH = {"Hatchback": 1.30, "Sedan": 1.20, "SUV": 1.35, "Bus": 1.28, "Truck": 1.40, "Two-Wheeler": 1.45}
BATT_FACTOR = {"LFP": 1.00, "NMC": 1.10, "NCA": 1.15, "Sodium-Ion": 0.85, "Solid-State": 1.30}
BATT_PRICE = {"LFP": 0.92, "NMC": 1.00, "NCA": 1.05, "Sodium-Ion": 0.85, "Solid-State": 1.45}
BATT_RATING = {"LFP": 0.0, "NMC": 0.05, "NCA": 0.08, "Sodium-Ion": -0.05, "Solid-State": 0.15}


def pick_battery(year):
    w = {"LFP": 0.30 + 0.05 * (year - 2019), "NMC": 0.45 - 0.04 * (year - 2019),
         "NCA": 0.22 - 0.02 * (year - 2019), "Sodium-Ion": 0.04 if year >= 2023 else 0.0,
         "Solid-State": 0.02 if year >= 2024 else 0.0}
    k, p = zip(*w.items())
    p = np.array(p) / sum(p)
    return rng.choice(k, p=p)


rows, vid = [], 1
for maker, (country, mw, cats, qb) in MAKERS.items():
    for cat in cats:
        for n in range(1, int(rng.integers(1, 3)) + 1):
            model = f"{maker} {cat} M{n}"
            (clo, chi), kpk, base_units, base_price = CAT[cat]
            cap0 = rng.uniform(clo, chi)
            for year in YEARS:
                battery = pick_battery(year)
                cap = round(cap0 * (1 + 0.03 * (year - 2019)), 1)
                rng_km = int(cap * kpk * BATT_FACTOR[battery] * rng.uniform(0.92, 1.08))
                price = int(base_price * BATT_PRICE[battery] * rng.uniform(0.9, 1.15) * (0.97 ** (year - 2019)))
                rating = float(np.clip(3.9 + qb + BATT_RATING[battery] + rng.normal(0, 0.25), 2.8, 5.0))
                for region, rw in REGIONS.items():
                    units = base_units * mw * rw * CAT_GROWTH[cat] ** (year - 2019) / 4 * rng.uniform(0.7, 1.3)
                    rows.append(dict(
                        record_id=vid, sales_year=year, manufacturer=maker, model=model,
                        category=cat, battery_type=battery, battery_capacity_kwh=cap,
                        driving_range_km=rng_km, price_usd=price,
                        manufacturing_country=country, sales_region=region,
                        annual_sales=int(units), customer_rating=round(rating, 2),
                        fast_charge_minutes=int(np.clip(rng.normal(32 - 1.2 * (year - 2019), 6), 12, 60)),
                    ))
                    vid += 1

df = pd.DataFrame(rows)
out = Path(__file__).resolve().parents[1] / "data" / "ev_market_data.csv"
df.to_csv(out, index=False)
print(f"Wrote {len(df):,} rows -> {out}")
