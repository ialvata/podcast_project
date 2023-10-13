"""
Module with all the boilerplate code to setup an initial PostgreSQL DB through SQLAlchemy
"""
from random import uniform
from time import sleep as time_sleep
from pathlib import Path
from database.schemas import (
    Podcasts as Podcasts_SQL,
    Episodes as Episodes_SQL,
)
from pydantic_models.podcasts import Podcast as Podcasts_Pydantic
from pydantic_models.episodes import Episode as Episodes_Pydantic
from api.utilities.constants import podcasts_dict, episodes_list
from sqlalchemy.orm import Session
import dateutil.parser

def init_db(db_session: Session):
    """
    Function to create some initial data in the DB
    """
    ############################           podcasts           ###############################
    print("Creating podcast list")
    podcasts = [
        Podcasts_Pydantic(
            title=podcast["title"],
            url=podcast["url"],
            publisher=str(podcast["publisher"]),
            language=podcast["language"]
        )
        for podcast in podcasts_dict.values()
    ]
    print("Adding podcasts and committing them")
    for podcast in podcasts:
        # time_sleep(uniform(0, 1))
        print(f"Podcast with title->{podcast.title}")
        db_session.add(Podcasts_SQL(**(podcast.dict())))
        db_session.commit()
    ############################           episodes           ###############################
    print("Creating episodes list")
    episodes = [
        Episodes_Pydantic(
            podcast_title=episode["podcast_title"],
            title=episode["title"],
            description=episode["description"],
            date=dateutil.parser.isoparse(episode["date"]),
            director=episode["director"],
            url_audio=episode["url_audio"]
        )
        for episode in episodes_list
    ]
    print("Adding Episodes and committing them")
    for episode in episodes:
        # time_sleep(uniform(0, 1))
        print(f"Episode with title->{episode.title}")
        db_session.add(Episodes_SQL(**(episode.dict())))
    db_session.commit()
    print("Initialized the db")