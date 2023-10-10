import json
from typing import Optional
from pathlib import Path
from api.utilities.constants import podcasts_dict
from fastapi import APIRouter, Depends,HTTPException, status
from pydantic_models.episodes import (
    Episode as Episode_Pydantic,
    EpisodeOut as Episode_Pydantic_Out
)
from database.connecting_orm import database_gen
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import Episodes as Episodes_SQL
from sqlalchemy import and_, or_

router = APIRouter(prefix="/episodes", tags=["Podcasts"])
@router.get('', 
            status_code=status.HTTP_200_OK, 
            response_model=list[Episode_Pydantic_Out]
)
async def list_podcasts(
    num_posts: int = 10,
    skip: int = 0,
    search: Optional[str] = "",
    db_session: Session = Depends(database_gen),
):
    stmt =(
        select(Episodes_SQL)
        .where(Episodes_SQL.title.contains(search))
        .limit(num_posts)
        .offset(skip)
    )

    podcasts_list = [
        # row.t is a tuple whose 1st element is a schema instance
        Episode_Pydantic_Out.from_schema_to_pydantic(row.t[0])
        for row in db_session.execute(stmt)
    ]
    # for dict, we could try
        # {
        #     f"{Podcast_Pydantic.from_schema_to_pydantic(row.t[0]).title}":
        #     Podcast_Pydantic.from_schema_to_pydantic(row.t[0])
        #     for row in db_session.execute(stmt)
        # }
    return podcasts_list


# class DownloadForm(Form):

# class Download_Episodes(Resource):
#     """Manage the API.

#     Parameters
#     ----------
#     Resource : flask_restful.Resource

#     """
#     # def __init__(self, model_extr, model_sim = None,clean_out_model=None):
#     #     self.model_extr = model_extr
#     #     self.model_sim = model_sim
#     #     self.clean_out_model = clean_out_model
    

#     # curl --request POST --url http://127.0.0.1:5000/download_episodes --header 'Content-Type: application/json' --data '{"episodes_url_list": ["example1", "example2"],"podcast_name": "podcast_name"}'
#     def post(self):
#         data = request.get_json() # --header 'Content-Type: application/json'
#         episodes_url_list = data["episodes_url_list"]
#         podcast_name = podcast_name_from_url(episodes_url_list[0])
#         info = get_info_podcast(podcast_name)
#         folder_path = info["folder"]
#         download_mp3(episodes_url_list,folder_path)
#         list_episodes_names = [file_name(el) for el in episodes_url_list]
#         success = "True"
#         errors = []
#         response = {'podcast_name': podcast_name,
#                     'list_episodes_names' : list_episodes_names,
#                     'success': success, 'errors': errors}
#         return response

