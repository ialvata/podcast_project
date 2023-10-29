import json
from typing import Optional
from pathlib import Path
from utilities.constants import podcasts_dict
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
from utilities.constants import clean_str
import requests

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
        conditions = conditions + [Episodes_SQL.title.contains(
            clean_str(search_episode_title)
        )]
    if podcast_title is not None:
        conditions = conditions + [Episodes_SQL.podcast_title==clean_str(podcast_title)]
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

@router.post('/download', 
            status_code=status.HTTP_200_OK
)
async def download_episode(
    url_audio: str,
    episode_title:str = "test",

):  
    episode_title = clean_str(episode_title).replace("/","_")
    response = requests.get(url_audio)
    if response.status_code == 200:
        with open(f"/home/ivo/Downloads/{episode_title}", 'wb') as file:
            file.write(response.content)
        print(f"Downloaded to /home/ivo/Downloads/")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
    return response.status_code
