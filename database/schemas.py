"""
Module responsible for the document/table models to exist in the PostgreSQL DB
"""
from __future__ import annotations

import datetime

from sqlalchemy import TIMESTAMP, ForeignKey,Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # type: ignore
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
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    url: Mapped[str] = mapped_column()
    publisher: Mapped[str] = mapped_column()
    language: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=text("now()")
    )

    def __repr__(self) -> str:
        return f"Podcast(id = {self.id}, title = {self.title})"
    
class Episodes(Base):
    """
    Class responsible for the `Episodes` table in the PostgreSQL DB
    """
    __tablename__ = "episodes"
    podcast_title: Mapped[str] = mapped_column(
        ForeignKey("podcasts.title", ondelete="CASCADE"),
        nullable=False,
    )
    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    url_audio: Mapped[str] = mapped_column()
    date: Mapped[datetime.datetime] = mapped_column()
    director: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, server_default=text("now()")
    )
