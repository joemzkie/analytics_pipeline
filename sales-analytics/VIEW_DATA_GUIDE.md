# Viewing Data with `view_data.py`

Run this from the `sales-analytics` folder:

```powershell
python python/view_data.py
```

The script connects to PostgreSQL using `connection.py`, then shows every row from the `products`, `customers`, and `orders` tables.

## Why `products` works

`products` works because it is included in the script's approved table list:

```python
allowed_tables = {"customers", "orders", "products"}
```

So this is allowed:

```python
show_table("products")
```

## Why another table raises an exception

If you use a table name outside that list, such as `users`, the script raises a `ValueError`. In simple words, the script is saying: “I do not recognise this table name, so I will stop instead of running it.”

This is a safety check. Table names cannot be passed to PostgreSQL as normal query parameters. Without the check, a malicious or accidental table name could change the SQL command. The fixed list allows only the tables this project expects to read.

If you later create a valid `users` table and want to view it, add its name deliberately:

```python
allowed_tables = {"customers", "orders", "products", "users"}
```

Only add a table after it exists in your database and you intend this script to read it.

## Viewing a table is different from joining tables

Viewing a table means showing its own columns and rows. No join is needed:

```sql
SELECT * FROM products;
```

A join is used only when you want information from two related tables in one result. For example, an `orders` table commonly stores a customer ID, and `customers` stores customer details. This query combines them:

```sql
SELECT o.*, c.*
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id;
```

You can view `customers` on its own without a join. Join `orders` to `customers` only when you want order details together with customer details. `view_data.py` is already configured to display all three current tables.
