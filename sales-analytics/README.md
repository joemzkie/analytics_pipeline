# Sales Analytics

PostgreSQL-backed sales analysis project. The database name is `sales_analytics`.

## Setup

1. Create the database:

   ```sql
   CREATE DATABASE sales_analytics;
   ```

2. Create the tables:

   ```powershell
   psql -U postgres -d sales_analytics -f sql/schema.sql
   ```

3. Create `python/.env` (this file is ignored by Git) and add your local credentials:

   ```dotenv
   HOST=localhost
   USER=postgres
   PASS=your_password_here
   port=5432
   # Optional: DB_NAME=sales_analytics
   ```

4. Install the Python driver and test the connection:

   ```powershell
   pip install "psycopg[binary]"
   python python/connection.py
   ```

The helper reads `python/.env` and never prints its values. Environment variables named `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`, and `POSTGRES_DB` can override the corresponding local settings. The database defaults to `sales_analytics`.

Run the sample reporting queries with:

```powershell
psql -U postgres -d sales_analytics -f sql/analysis.sql
```
