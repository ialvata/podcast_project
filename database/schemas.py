"""
Module responsible for the document/table models to exist in the PostgreSQL DB
"""
from __future__ import annotations

import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.expression import text

# from typing import List


# from db.db_orm import Base


class Base(DeclarativeBase):
    """
    The default map type mapping, deriving the type for mapped_column(),
    from a Mapped[] annotation, is:
    type_map: Dict[Type[Any], TypeEngine[Any]] = {
        bool: types.Boolean(),
        bytes: types.LargeBinary(),
        datetime.date: types.Date(),
        datetime.datetime: types.DateTime(),
        datetime.time: types.Time(),
        datetime.timedelta: types.Interval(),
        decimal.Decimal: types.Numeric(),
        float: types.Float(),
        int: types.Integer(),
        str: types.String(),
        uuid.UUID: types.Uuid(),
    }
    More info at
    https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
    """

    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }


class Podcasts(Base):
    """
    Class responsible for the `Podcasts` table in the PostgreSQL DB
    """

    __tablename__ = "podcasts"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    folder: Mapped[str] = mapped_column()
    language: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=text("now()")
    )

    def __repr__(self) -> str:
        return f"Post(id = {self.id}, username = {self.username})"


