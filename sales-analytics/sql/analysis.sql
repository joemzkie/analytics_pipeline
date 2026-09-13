-- Monthly revenue and units sold by product category.
SELECT
    DATE_TRUNC('month', s.sale_date)::date AS month,
    p.category,
    SUM(s.quantity) AS units_sold,
    SUM(s.revenue) AS total_revenue
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
GROUP BY 1, 2
ORDER BY 1, 2;

-- Top products by revenue.
SELECT
    p.product_name,
    SUM(s.quantity) AS units_sold,
    SUM(s.revenue) AS total_revenue
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC;
