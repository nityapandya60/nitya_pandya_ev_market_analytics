-- ==========================================================
-- Q1 Sales contribution by vehicle category (all years)
SELECT category, SUM(annual_sales) AS units_sold,
       ROUND(100.0 * SUM(annual_sales) / (SELECT SUM(annual_sales) FROM ev_sales), 2) AS pct_of_total
FROM ev_sales GROUP BY category ORDER BY units_sold DESC;
-- ==========================================================
-- Q2 Top 10 manufacturers and market share (2024)
SELECT manufacturer, SUM(annual_sales) AS units_sold,
       ROUND(100.0 * SUM(annual_sales) / SUM(SUM(annual_sales)) OVER (), 2) AS market_share_pct
FROM ev_sales WHERE sales_year = 2024
GROUP BY manufacturer ORDER BY units_sold DESC LIMIT 10;
-- ==========================================================
-- Q3 Year-over-year sales growth by category
WITH y AS (SELECT sales_year, category, SUM(annual_sales) AS units FROM ev_sales GROUP BY 1, 2)
SELECT sales_year, category, units,
       ROUND(100.0 * (units - LAG(units) OVER (PARTITION BY category ORDER BY sales_year))
             / LAG(units) OVER (PARTITION BY category ORDER BY sales_year), 1) AS yoy_growth_pct
FROM y ORDER BY category, sales_year;
-- ==========================================================
-- Q4 High-growth segments (CAGR 2019-2024)
WITH s AS (
  SELECT category,
         SUM(CASE WHEN sales_year = 2019 THEN annual_sales END) AS u2019,
         SUM(CASE WHEN sales_year = 2024 THEN annual_sales END) AS u2024
  FROM ev_sales GROUP BY category)
SELECT category, u2019, u2024,
       ROUND(100 * (POWER(1.0 * u2024 / u2019, 1.0 / 5) - 1), 1) AS cagr_pct
FROM s ORDER BY cagr_pct DESC;
-- ==========================================================
-- Q5 Battery technology adoption by year (share of units)
SELECT sales_year, battery_type, SUM(annual_sales) AS units,
       ROUND(100.0 * SUM(annual_sales) / SUM(SUM(annual_sales)) OVER (PARTITION BY sales_year), 2) AS share_pct
FROM ev_sales GROUP BY sales_year, battery_type ORDER BY sales_year, units DESC;
-- ==========================================================
-- Q6 Driving range and capacity by battery type
SELECT battery_type, ROUND(AVG(driving_range_km), 0) AS avg_range_km,
       ROUND(AVG(battery_capacity_kwh), 1) AS avg_kwh,
       ROUND(AVG(price_usd), 0) AS avg_price_usd,
       ROUND(AVG(fast_charge_minutes), 1) AS avg_fast_charge_min
FROM ev_sales GROUP BY battery_type ORDER BY avg_range_km DESC;
-- ==========================================================
-- Q7 Driving range by vehicle category
SELECT category, MIN(driving_range_km) AS min_km, ROUND(AVG(driving_range_km), 0) AS avg_km,
       MAX(driving_range_km) AS max_km
FROM ev_sales GROUP BY category ORDER BY avg_km DESC;
-- ==========================================================
-- Q8 Customer satisfaction by category
SELECT category, ROUND(AVG(customer_rating), 2) AS avg_rating, SUM(annual_sales) AS units
FROM ev_sales GROUP BY category ORDER BY avg_rating DESC;
-- ==========================================================
-- Q9 Manufacturing country analysis
SELECT manufacturing_country, COUNT(DISTINCT manufacturer) AS manufacturers,
       SUM(annual_sales) AS units_sold, ROUND(AVG(customer_rating), 2) AS avg_rating
FROM ev_sales GROUP BY manufacturing_country ORDER BY units_sold DESC;
-- ==========================================================
-- Q10 Regional sales mix by year
SELECT sales_year, sales_region, SUM(annual_sales) AS units
FROM ev_sales GROUP BY sales_year, sales_region ORDER BY sales_year, units DESC;
-- ==========================================================
-- Q11 Competitive advantage: rating vs price rank per manufacturer (2024)
SELECT manufacturer, ROUND(AVG(customer_rating), 2) AS avg_rating,
       ROUND(AVG(price_usd), 0) AS avg_price_usd,
       RANK() OVER (ORDER BY AVG(customer_rating) DESC) AS rating_rank
FROM ev_sales WHERE sales_year = 2024 GROUP BY manufacturer ORDER BY rating_rank LIMIT 10;
