-- Views you can connect Tableau to directly
CREATE VIEW vw_manufacturer_year AS
SELECT sales_year, manufacturer, manufacturing_country,
       SUM(annual_sales)                AS units_sold,
       ROUND(AVG(customer_rating), 2)   AS avg_rating,
       ROUND(AVG(driving_range_km), 0)  AS avg_range_km
FROM ev_sales GROUP BY sales_year, manufacturer, manufacturing_country;

CREATE VIEW vw_category_year AS
SELECT sales_year, category,
       SUM(annual_sales)               AS units_sold,
       ROUND(AVG(driving_range_km), 0) AS avg_range_km,
       ROUND(AVG(customer_rating), 2)  AS avg_rating,
       ROUND(AVG(price_usd), 0)        AS avg_price_usd
FROM ev_sales GROUP BY sales_year, category;
