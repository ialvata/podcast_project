
import json
from pathlib import Path
from api.utilities.constants import podcasts_dict
from fastapi import APIRouter, HTTPException, status
from pydantic_models.podcasts import Podcast

router = APIRouter(prefix="/podcasts", tags=["Podcasts"])
@router.get('/list', 
            status_code=status.HTTP_200_OK, 
            response_model=dict[str,Podcast]
)
async def list_podcasts():
    return podcasts_dict

