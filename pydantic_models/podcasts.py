from pydantic import BaseModel
from pathlib import Path
from database.schemas import Podcasts
import datetime

class Podcast(BaseModel):
    """
    Pydantic class that represents a Podcast
    """
    title: str
    url: str
    publisher: str
    language: str

    @classmethod
    def from_schema_to_pydantic(cls,podcast:Podcasts)-> "Podcast":
        return Podcast(
            title=podcast.title, url=podcast.url, publisher=podcast.publisher,
            language=podcast.language
        )

class PodcastOut(Podcast):
    """
    Pydantic class that represents a Podcast
    """
    id: int
    created_at: datetime.datetime
    
    @classmethod
    def from_schema_to_pydantic(cls,podcast:Podcasts)-> "PodcastOut":
        return PodcastOut(
            title=podcast.title, url=podcast.url, publisher=podcast.publisher,
            language=podcast.language,id=podcast.id, created_at=podcast.created_at
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
