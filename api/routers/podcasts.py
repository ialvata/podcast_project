
import json
from typing import Optional
from pathlib import Path
from utilities.constants import podcasts_dict
from fastapi import APIRouter, Depends,HTTPException, status
from pydantic_models.podcasts import (
    Podcast as Podcast_Pydantic,
    PodcastOut as Podcast_Pydantic_Out
)
from database.connecting_orm import database_gen
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import Podcasts as Podcasts_SQL
from sqlalchemy import and_, or_

router = APIRouter(prefix="/podcasts", tags=["Podcasts"])
@router.get('/', 
            status_code=status.HTTP_200_OK, 
            response_model=list[Podcast_Pydantic_Out]
)
async def list_podcasts(
    num_posts: int = 10,
    skip: int = 0,
    search: Optional[str] = "",
    db_session: Session = Depends(database_gen),
):
    stmt =(
        select(Podcasts_SQL)
        .where(Podcasts_SQL.title.contains(search))
        .limit(num_posts)
        .offset(skip)
    )

    podcasts_list = [
        # row.t is a tuple whose 1st element is a schema instance
        Podcast_Pydantic_Out.from_schema_to_pydantic(row.t[0])
        for row in db_session.execute(stmt)
    ]
    # for dict, we could try
        # {
        #     f"{Podcast_Pydantic.from_schema_to_pydantic(row.t[0]).title}":
        #     Podcast_Pydantic.from_schema_to_pydantic(row.t[0])
        #     for row in db_session.execute(stmt)
        # }
    return podcasts_list

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Podcast_Pydantic_Out)
async def add_podcast(
    payload: Podcast_Pydantic,
    db_session: Session = Depends(database_gen)
):
    """
    Adding a podcast to podcast table in postgres db.
    """
    # creating a data according to schema
    new_podcast = Podcasts_SQL(**(payload.dict()))
    # checking for already existing podcast
    stmt =(
        select(Podcasts_SQL)
        .where(
            Podcasts_SQL.title==new_podcast.title,
            Podcasts_SQL.url==new_podcast.url
        )
    )
    podcasts_list = [
        # row.t is a tuple whose 1st element is a schema instance
        Podcast_Pydantic.from_schema_to_pydantic(row.t[0])
        for row in db_session.execute(stmt)
    ]
    if podcasts_list == []:
        # adding data to session, moving it to pending state.
        db_session.add(new_podcast)
        # moving all data in pending state, in this session, to persistant state.
        db_session.commit()
        # update new_post with data returned from db_session
        db_session.refresh(new_podcast)
        return new_podcast
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=
            f"A podcast with title = {new_podcast.title}, "
            f"or url = {new_podcast.url}, already exists!",
        )
    
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_podcast(
    identifier: Optional[int] = None,
    url: Optional[str] = None,
    title: Optional[str] = None,
    db_session: Session = Depends(database_gen),
):
    """
    Function that creates the resource to delete a specified post, by identifier.
    """
    if identifier is None and url is None and title is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No criteria to delete podcasts was given!",
        )
    stmt =(
        select(Podcasts_SQL)
        .where(
            or_(Podcasts_SQL.title == title,
            Podcasts_SQL.url == url,
            Podcasts_SQL.id == identifier)
        )
    )
    podcasts_list = [
        # row.t is a tuple whose 1st element is a schema instance
        row.t[0]
        for row in db_session.execute(stmt)
    ]
    if podcasts_list == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No podcasts, for the criteria given, were found!",
        )
    for podcast_delete in podcasts_list:
        db_session.delete(podcast_delete)
    db_session.commit()