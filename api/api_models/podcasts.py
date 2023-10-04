from pydantic import BaseModel
from pathlib import PosixPath

class Podcast(BaseModel):
    """
    Pydantic class that represents a Podcast
    """
    folder: PosixPath
    url: str
    name: str