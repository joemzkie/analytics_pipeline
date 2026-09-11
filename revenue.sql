SELECT
    p.product_name,
    p.price,
    o.quantity,
    p.price * o.quantity AS revenue,
    SUM(p.price * o.quantity) OVER () AS total_revenue
FROM orders o
LEFT JOIN products p
    ON o.product_id = p.product_id;