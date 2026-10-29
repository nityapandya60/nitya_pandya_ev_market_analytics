# Calculated Fields (target: 10+)

| # | Name | Formula | Purpose |
|---|---|---|---|
| 1 | Total Units | `SUM([annual_sales])` | Core sales KPI |
| 2 | Market Share % | `SUM([annual_sales]) / TOTAL(SUM([annual_sales]))` | Manufacturer/category share |
| 3 | YoY Growth % | `(ZN(SUM([annual_sales])) - LOOKUP(ZN(SUM([annual_sales])), -1)) / ABS(LOOKUP(ZN(SUM([annual_sales])), -1))` | Year-over-year trend (table calc, addressed by Sales Year) |
| 4 | CAGR 2019-24 | `(SUM(IF [sales_year]=2024 THEN [annual_sales] END) / SUM(IF [sales_year]=2019 THEN [annual_sales] END))^(1/5) - 1` | Identify high-growth segments |
| 5 | Avg Range (km) | `AVG([driving_range_km])` | Range comparison |
| 6 | Range per kWh | `SUM([driving_range_km]) / SUM([battery_capacity_kwh])` | Battery efficiency |
| 7 | Price per km Range | `AVG([price_usd]) / AVG([driving_range_km])` | Value for money |
| 8 | Satisfaction Tier | `IF AVG([customer_rating]) >= 4.2 THEN "Delighted" ELSEIF AVG([customer_rating]) >= 3.8 THEN "Satisfied" ELSE "At Risk" END` | Rating segmentation |
| 9 | Weighted Rating | `SUM([customer_rating] * [annual_sales]) / SUM([annual_sales])` | Sales-weighted satisfaction |
| 10 | Battery Group | `IF [battery_type] IN ("Sodium-Ion","Solid-State") THEN "Emerging" ELSE "Established" END` | Technology maturity |
| 11 | Price Band | `IF [price_usd] < 10000 THEN "Budget" ELSEIF [price_usd] < 50000 THEN "Mid" ELSE "Premium" END` | Pricing segments |
| 12 | Fast Charge Speed | `IF [fast_charge_minutes] <= 25 THEN "Ultra-fast" ELSEIF [fast_charge_minutes] <= 40 THEN "Fast" ELSE "Standard" END` | Charging segmentation |
| 13 | Selected Year Units (parameter) | `IF [sales_year] = [Select Year] THEN [annual_sales] END` | Parameter-driven KPI |

**Parameters:** `Select Year` (integer list 2019–2024), `Metric Switch` (Units / Avg Rating / Avg Range) with `CASE [Metric Switch]` for a dynamic measure.
