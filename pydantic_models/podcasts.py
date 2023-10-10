from pydantic import BaseModel
from pathlib import Path
from database.schemas import Podcasts 

class Podcast(BaseModel):
    """
    Pydantic class that represents a Podcast
    """
    title: str
    url: str
    folder: str
    language: str

    @classmethod
    def from_schema_to_pydantic(cls,podcast:Podcasts)-> "Podcast":
        return Podcast(
            title=podcast.title, url=podcast.url, folder=podcast.folder,
            language=podcast.language
        )