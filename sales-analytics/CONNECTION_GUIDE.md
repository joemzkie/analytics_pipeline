# PostgreSQL Connection and Reading Table Data

This project keeps connecting to PostgreSQL and selecting data in separate files:

- `python/connection.py` reads local settings and creates a database connection.
- `python/view_data.py` uses that connection to show rows from the `products` and `sales` tables.

## How the connection works

`connection.py` reads `python/.env`, which stays on your computer and is ignored by Git. It uses these values:

```dotenv
HOST=localhost
USER=postgres
PASS=your_password_here
port=5432
# Optional: DB_NAME=sales_analytics
```

The database name is `sales_analytics` unless you add `DB_NAME`. The script passes these values directly to PostgreSQL through `psycopg`; it does not print your password.

Test only the connection from the project directory:

```powershell
python python/connection.py
```

Expected output:

```text
Connected to sales_analytics
```

## Show table values with Python

First make sure the schema exists:

```powershell
psql -U postgres -d sales_analytics -f sql/schema.sql
```

Then, from the `sales-analytics` directory, run the separate data-reading file:

```powershell
python python/view_data.py
```

It prints the rows in `products` and `sales`. This script permits only those two fixed table names, so a table name cannot be injected into the SQL statement.

To view one table from Python code:

```python
from view_data import show_table

show_table("products")
```

There is no `users` table in the current schema. Add one to `sql/schema.sql` first if you need to store or select user records.
