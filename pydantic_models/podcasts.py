from pydantic import BaseModel
from pathlib import Path

class Podcast(BaseModel):
    """
    Pydantic class that represents a Podcast
    """
    title: str
    url: str
    folder: str
    language: str