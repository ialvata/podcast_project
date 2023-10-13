from pydantic import BaseModel
from pathlib import Path
from database.schemas import Episodes
import datetime

class Episode(BaseModel):
    """
    Pydantic class that represents a Podcast
    """
    title: str
    description: str
    url_audio: str
    date: datetime.datetime
    director: str

class EpisodeOut(Episode):
    """
    Pydantic class that represents a Podcast
    """
    podcast_title: str
    podcast_id: int
    created_at: datetime.datetime
    
    @classmethod
    def from_schema_to_pydantic(cls,episode:Episodes)-> "EpisodeOut":
        return EpisodeOut(
            title=episode.title, 
            url_audio=episode.url_audio,
            date=episode.date,
            description=episode.description,
            director=episode.director,
            podcast_id=episode.podcast_id, 
            podcast_title=episode.podcast_title,
            created_at=episode.created_at
        )

    class Config:
        """
        Behaviour of pydantic can be controlled via the Config class on a model
        or a pydantic dataclass.
        Pydantic's `orm_mode` will tell the Pydantic model to read the data
        even if it is not a dict, but an ORM model (or any other arbitrary 
        object with attributes). With this, the Pydantic model is compatible with ORMs, 
        and you can just declare it in the response_model argument in your path operations.
        You will be able to return a database model and it will read the data from it.
        https://fastapi.tiangolo.com/tutorial/response-model/?h=
        """

        orm_mode = True
