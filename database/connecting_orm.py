"""
Module with all the boilerplate code to start a SQLAlchemy session in the PostgreSQL DB
"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresCredentials:
    def __init__(self) -> None:
        load_dotenv(dotenv_path="./database/.env.local.db")
        self.postgres_user = os.environ["POSTGRES_USER"]
        self.postgres_password = os.environ["POSTGRES_PASSWORD"]
        self.postgres_database = os.environ["POSTGRES_DB"]


pg_cred = PostgresCredentials()
POSTGRESQL_DATABASE_URL = (
    f"postgresql://{pg_cred.postgres_user}:"
    f"{pg_cred.postgres_password}@localhost/{pg_cred.postgres_database}"
)

engine = create_engine(POSTGRESQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def database_gen():
    """
    Function responsible for yielding a session and closing it.
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()