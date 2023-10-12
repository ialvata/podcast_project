"""
This module is responsible for defining the databases base classes.
All database classes like PostgresDB, MongoDB, etc classes will be subtypes of DataBase
"""
from typing import Protocol, runtime_checkable, Optional
from pydantic import BaseModel

class ConfigDB(BaseModel):
    """
    class representing the configuration for the db.
    """

    host: str = "localhost"
    database: str | int | None = None
    user: str | None = None
    password: str | None = None
    port: str | None = None


@runtime_checkable
class DataBase(Protocol):
    """
    Super class for all database classes
    """

    def __init__(
        self,
        config: ConfigDB,
        filename: str | None = None,
        section: str | None = None,
    ):
        """method docstring"""

    def connect(self, database:Optional[str]):
        """method docstring"""

    def execute(self, sql_command: str, values: tuple[str, ...] | None = None):
        """method docstring"""

