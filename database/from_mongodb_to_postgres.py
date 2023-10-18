
from database.mongodb import MongoDB
from pymongo import MongoClient
from sqlalchemy.orm import Session
from database.schemas import (
    Podcasts as Podcasts_SQL,
    Episodes as Episodes_SQL
)
from sqlalchemy import select
from sqlalchemy import or_
from pydantic_models.episodes import Episode as Episodes_Pydantic
import dateutil.parser
from utilities.constants import clean_str


def transfer_france_culture_from_mongodb_to_postgres(
        sql_db_session:Session,mongo:MongoDB,
) -> None:
    stmt =(
        select(Podcasts_SQL)
    )
    podcasts_sql_db = [
        # row.t is a tuple whose 1st element is a schema instance
        row._t[0]
        for row in sql_db_session.execute(stmt)
    ]
    PODCAST_BASE_URL = "https://www.radiofrance.fr/franceculture/podcasts/"
    podcasts_regex = [
        podcast.url.replace(PODCAST_BASE_URL,"")
        for podcast in podcasts_sql_db
    ]
    mongo.connect()
    findings = mongo.search_episodes(database="podcast_project",collection="episodes",
                                     search_key="episode_url", podcasts = podcasts_regex)
    episodes = [
        Episodes_Pydantic(
            podcast_title = clean_str(
                episode["json_content"][2]['@graph'][0]["itemListElement"][3]["item"]["name"]
            ).lower(),
            title = clean_str(episode["json_content"][1]['@graph'][0]['name']),
            description = clean_str(episode["json_content"][1]['@graph'][0]["description"]),
            date = dateutil.parser.isoparse(
                episode["json_content"][1]['@graph'][0]["dateCreated"]
            ),
            director = episode["json_content"][1]['@graph'][0]['director'][0]["name"],
            url_audio = episode["json_content"][1]['@graph'][0]["mainEntity"]["contentUrl"]
        )
        for episodes_dict in findings.values()
        for episode in episodes_dict
    ]
    for episode in episodes:
        sql_db_session.add(Episodes_SQL(**(episode.dict())))
    sql_db_session.commit()

if __name__=="__main__":
    from database.connecting_orm import database_gen
    sql_db = next(database_gen())
    db = MongoDB(filename="./database/database.ini", section="mongodb")
    transfer_france_culture_from_mongodb_to_postgres(sql_db_session = sql_db,mongo = db)
    print("OLA")