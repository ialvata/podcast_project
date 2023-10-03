
import json
from scrapper import episode_list, file_name, podcast_name_from_url, download_mp3
from utilities.filesystem import *
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/podcasts", tags=["Podcasts"])
@router.get('/list', 
            status_code=status.HTTP_200_OK, 
            # response_model=list[PostJoinResponse]
)
async def list_podcasts():
    podcast_list={}
    success = True
    errors = []
    file_path = os.path.join(PROJ_PATH,"data","db","podcast_list.json")
    try:
        with open(file_path, "r") as file:
            podcast_list = json.load(file)
    except:
        success = False
        errors.append("Could not load json file with podcast_list")
    # podcast_list is imported from constants
    podcast_list_names = [podcast["name"] for podcast in podcast_list.values()]
    
    response = {'list_podcast' : podcast_list_names,
                'success': success,
                'errors': errors}
    print(response)
    return response

