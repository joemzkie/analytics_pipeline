"""Display rows from the sales_analytics tables without exposing credentials."""

from connection import get_connection


def show_table(table_name: str) -> None:
    """Print rows from one approved table name."""
    allowed_tables = {"customers", "orders", "products"}
    if table_name not in allowed_tables:
        raise ValueError(f"Table must be one of: {', '.join(sorted(allowed_tables))}")

    with get_connection() as connection, connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY 1")
        columns = [column.name for column in cursor.description]
        rows = cursor.fetchall()

    print(" | ".join(columns))
    print("-+-".join("-" * len(column) for column in columns))
    for row in rows:
        print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    show_table("products")
    print()
    show_table("customers")
    print()
    show_table("orders")
