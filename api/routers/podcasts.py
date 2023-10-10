
import json
from typing import Optional
from pathlib import Path
from api.utilities.constants import podcasts_dict
from fastapi import APIRouter, Depends,HTTPException, status
from pydantic_models.podcasts import Podcast as Podcast_Pydantic
from database.connecting_orm import database_gen
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import Podcasts as Podcasts_SQL


router = APIRouter(prefix="/podcasts", tags=["Podcasts"])
@router.get('/list', 
            status_code=status.HTTP_200_OK, 
            response_model=list[Podcast_Pydantic]
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
        Podcast_Pydantic.from_schema_to_pydantic(row.t[0])
        for row in db_session.execute(stmt)
    ]
    # for dict, we could try
        # {
        #     f"{Podcast_Pydantic.from_schema_to_pydantic(row.t[0]).title}":
        #     Podcast_Pydantic.from_schema_to_pydantic(row.t[0])
        #     for row in db_session.execute(stmt)
        # }
    return podcasts_list

