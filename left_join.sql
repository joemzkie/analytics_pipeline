SELECT 
	c.first_name,
    c.middle_name,
    c.last_name,
    p.product_name,
    o.quantity
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;