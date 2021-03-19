from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    database_type: str = "sql"
    database_uri: str = "postgresql://postgres:example@db:5432/postgres"
