-- SQLite schema (for MySQL/PostgreSQL: swap INTEGER PRIMARY KEY for AUTO_INCREMENT/SERIAL)
CREATE TABLE ev_sales (
    record_id             INTEGER PRIMARY KEY,
    sales_year            INTEGER NOT NULL,
    manufacturer          TEXT    NOT NULL,
    model                 TEXT    NOT NULL,
    category              TEXT    NOT NULL,   -- Hatchback, Sedan, SUV, Bus, Truck, Two-Wheeler
    battery_type          TEXT    NOT NULL,   -- LFP, NMC, NCA, Sodium-Ion, Solid-State
    battery_capacity_kwh  REAL    NOT NULL,
    driving_range_km      INTEGER NOT NULL,
    price_usd             INTEGER NOT NULL,
    manufacturing_country TEXT    NOT NULL,
    sales_region          TEXT    NOT NULL,
    annual_sales          INTEGER NOT NULL,
    customer_rating       REAL    CHECK (customer_rating BETWEEN 1 AND 5),
    fast_charge_minutes   INTEGER
);
CREATE INDEX idx_year  ON ev_sales(sales_year);
CREATE INDEX idx_maker ON ev_sales(manufacturer);
CREATE INDEX idx_cat   ON ev_sales(category);
