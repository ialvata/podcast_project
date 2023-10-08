"""
Module with all the boilerplate code to setup an initial PostgreSQL DB through SQLAlchemy
"""
from random import uniform
from time import sleep as time_sleep
from pathlib import Path
from database.schemas import Podcasts as Podcasts_SQL
from pydantic_models.podcasts import Podcast as Podcasts_Pydantic
from api.utilities.constants import podcasts_dict


def init_db(db_session):
    """
    Function to create some initial data in the DB
    """
    ############################           users           ###############################
    print("Creating podcast list")
    podcasts = [
        Podcasts_Pydantic(
            title=podcast["title"],
            url=podcast["url"],
            folder=str(podcast["folder"]),
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
    print("Initialized the db")