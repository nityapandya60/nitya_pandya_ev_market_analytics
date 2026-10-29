# Visualizations, Dashboard & Filters

## Worksheets (14 unique visualizations)
| # | Sheet | Chart type | Fields |
|---|---|---|---|
| 1 | Sales by Category | Treemap | category (size, colour) · Total Units |
| 2 | Sales Trend | Line chart | sales_year × Total Units, colour = category |
| 3 | Top Manufacturers | Horizontal bar (Top 10 filter) | manufacturer × Total Units |
| 4 | Market Share | Donut / pie | manufacturer × Market Share % |
| 5 | Battery Mix Over Time | 100% stacked area | sales_year × units, colour = battery_type |
| 6 | Battery Comparison | Bar-in-bar / dual axis | battery_type × Avg Range & Avg Price |
| 7 | Range by Category | Box plot | category × driving_range_km |
| 8 | Range vs Capacity | Scatter + trend line | capacity × range, colour = battery_type |
| 9 | Satisfaction by Category | Bullet / bar | category × Weighted Rating |
| 10 | Manufacturing Geography | Filled map | manufacturing_country × units |
| 11 | Regional Sales | Stacked bar | sales_region × units × year |
| 12 | Growth Matrix | Scatter (quadrant) | CAGR vs Total Units by category |
| 13 | Rating vs Price | Scatter | manufacturer: Avg price × Avg rating, size = units |
| 14 | KPI Cards | Text tables | Units, Top maker, Avg range, Avg rating |

## Dashboard layout (Floating-free, Horizontal/Vertical containers)
```
┌───────────────────── Title + Year parameter ─────────────────────┐
│  KPI: Units │ KPI: Top Maker │ KPI: Avg Range │ KPI: Avg Rating   │
├────────────────────────────┬─────────────────────────────────────┤
│ Sales Trend (line)         │ Sales by Category (treemap)         │
├───────────────┬────────────┼─────────────────────────────────────┤
│ Top Mfrs      │ Mfg Map    │ Battery Mix Over Time               │
├───────────────┴────────────┴─────────────────────────────────────┤
│ Range by Category │ Satisfaction │ Rating vs Price                │
└──────────────────────────────────────────────────────────────────┘
```
- Build three device layouts (Desktop 1200×800, Tablet, Phone) for responsiveness.
- Add **Filter actions**: click category → filters all sheets; **Highlight action** on manufacturer; **Tooltip viz-in-tooltip** on map.
- Palette: green `#0A8F6A` accent, grey neutrals, colour-blind-safe categorical palette.

## Filters (target: 6+)
Year (slider) · Category (multi) · Manufacturer (search) · Battery Type · Manufacturing Country · Sales Region · Price Band · Top-N parameter. Use **Apply to worksheets → Selected** only where necessary, and "Show filter" with *Apply* button for large lists.
