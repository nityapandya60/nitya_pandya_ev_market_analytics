# Performance Testing

| Metric | Target | Actual (fill in) |
|---|---|---|
| Rows loaded from DB | 1,488 (extend to 50k+ to stress test) | |
| Live connection vs Extract | Extract (.hyper) for dashboards | |
| Filters used | 6+ | |
| Calculated fields | 10+ | |
| Visualizations / worksheets | 14 | |
| Dashboard load time (Tableau Public) | < 5 s | |
| Flask page load | < 2 s | |

**How to measure:** Tableau → *Help → Settings and Performance → Start Performance Recording*, interact with filters, then *Stop* and review the workbook. Optimisations: use extracts, hide unused fields, limit quick filters, use context filters, prefer fixed-size dashboards, aggregate in SQL views.
**Scaling test:** change `base_units`/loop counts in `scripts/generate_dataset.py` to create 50k–100k rows and record render times.
