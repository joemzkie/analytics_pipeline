"""PostgreSQL connection helper for the sales_analytics database."""

import os
from pathlib import Path

import psycopg


ENV_FILE = Path(__file__).with_name(".env")


def load_env(path: Path = ENV_FILE) -> dict[str, str]:
    """Read local connection settings without printing or exporting secrets."""
    if not path.is_file():
        raise FileNotFoundError(
            f"Missing {path.name}. Create it beside connection.py with database settings."
        )

    settings: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator or not key.strip():
            raise ValueError(f"Invalid entry in {path.name}: expected KEY=VALUE")
        settings[key.strip()] = value.strip().strip('"').strip("'")
    return settings


def get_connection() -> psycopg.Connection:
    """Return a PostgreSQL connection using the local, Git-ignored .env file."""
    settings = load_env()
    return psycopg.connect(
        dbname=os.getenv("POSTGRES_DB", settings.get("DB_NAME", "sales_analytics")),
        user=os.getenv("POSTGRES_USER", settings.get("USER")),
        password=os.getenv("POSTGRES_PASSWORD", settings.get("PASS")),
        host=os.getenv("POSTGRES_HOST", settings.get("HOST", "localhost")),
        port=os.getenv("POSTGRES_PORT", settings.get("port", "5432")),
    )


if __name__ == "__main__":
    with get_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT current_database()")
        (database,) = cursor.fetchone()
        print(f"Connected to {database}")
