"""
Manufacturing Analytics Platform

SQL data loading component.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import pandas as pd
from sqlalchemy import Engine, create_engine, text


@dataclass(frozen=True)
class DatabaseConfig:
    """Database connection settings."""

    host: str
    port: int
    user: str
    password: str
    database: str
    driver: str = "mysql+pymysql"

    def connection_url(self) -> str:
        """Build a SQLAlchemy connection URL."""
        return (
            f"{self.driver}://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )


class SQLLoader:
    """
    Loads manufacturing data from SQL sources.

    Connection credentials should be supplied through environment
    variables or an external configuration file and must never be
    committed to the repository.
    """

    def __init__(
        self,
        config: Optional[DatabaseConfig] = None,
        engine: Optional[Engine] = None,
    ) -> None:
        if engine is None and config is None:
            raise ValueError("Provide either a database config or SQLAlchemy engine.")

        self.engine = engine or create_engine(
            config.connection_url(),
            pool_pre_ping=True,
        )

    def load_query(
        self,
        query: str,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> pd.DataFrame:
        """Execute a parameterized SQL query and return a DataFrame."""
        with self.engine.connect() as connection:
            return pd.read_sql(
                text(query),
                connection,
                params=parameters or {},
            )

    def load_table(
        self,
        table_name: str,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        """
        Load a table or a limited sample.

        The table name should come from trusted application configuration,
        not directly from unvalidated user input.
        """
        query = f"SELECT * FROM `{table_name}`"

        if limit is not None:
            if limit <= 0:
                raise ValueError("Limit must be greater than zero.")
            query += f" LIMIT {int(limit)}"

        return self.load_query(query)

    def test_connection(self) -> bool:
        """Return True when the database connection succeeds."""
        with self.engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True
