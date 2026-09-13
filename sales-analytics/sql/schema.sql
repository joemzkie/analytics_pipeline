-- Run this while connected to the sales_analytics database.

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(12, 2) CHECK (price >= 0)
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    sale_date DATE NOT NULL,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    revenue NUMERIC(12, 2) NOT NULL CHECK (revenue >= 0)
);

CREATE INDEX IF NOT EXISTS idx_sales_sale_date ON sales (sale_date);
CREATE INDEX IF NOT EXISTS idx_sales_product_id ON sales (product_id);
