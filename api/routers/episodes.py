import json
from typing import Optional
from pathlib import Path
from api.utilities.constants import podcasts_dict
from fastapi import APIRouter, Depends,HTTPException, status
from pydantic_models.episodes import EpisodeOut
from database.connecting_orm import database_gen
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import (
    Podcasts as Podcasts_SQL,
    Episodes as Episodes_SQL
)
from sqlalchemy import and_, or_

router = APIRouter(prefix="/episodes", tags=["Episodes"])
@router.post('', 
            status_code=status.HTTP_200_OK, 
            response_model=list[EpisodeOut]
)
async def list_episodes(
    podcast_title:Optional[str] = None, 
    max_episodes_per_request: int = 10,
    offset_pagination: int = 0,
    search_episode_title: Optional[str] = None,
    db_session: Session = Depends(database_gen),
):
    conditions = []
    if search_episode_title is None and podcast_title is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=
            f"Absence of criteria! Either give podcast_title or search_episode_title.",
        )
    if search_episode_title is not None:
        conditions = conditions + [Episodes_SQL.title.contains(search_episode_title)]
    if podcast_title is not None:
        conditions = conditions + [Episodes_SQL.podcast_title==podcast_title]
    stmt =(
            select(Episodes_SQL)
            .where(*conditions)
            .limit(max_episodes_per_request)
            .offset(offset_pagination)
        )
    episodes_list = [
        # row.t is a tuple whose 1st element is a schema instance
        EpisodeOut.from_schema_to_pydantic(row.t[0])
        for row in db_session.execute(stmt)
    ]
    return episodes_list

