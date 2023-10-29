"""
This Module adds data to Postgres and MongoDB databases.
"""

from database import schemas
from database.connecting_orm import database_gen, engine
from database.utilities import init_db
from scrappers.france_culture import scrape_france_culture
from database.mongodb import MongoDB
from database.from_mongodb_to_postgres import transfer_france_culture_from_mongodb_to_postgres


#####################    Creating some initial data in Postgres db    #######################
# Base.metadate.create_all should be always in the main.py, from where we run the app.
schemas.Base.metadata.create_all(bind=engine, checkfirst=True)
postgres_db_session = next(database_gen())
if postgres_db_session.query(schemas.Podcasts).all() == []:
    print(f"Creating Podcasts table in {schemas.Base}")
    init_db(postgres_db_session)
# scrapping data
print("Scrapping data")
documents = scrape_france_culture(postgres_db_session)
# sending episode data to MongoDB
mongo_db = MongoDB(filename="./database/database.ini", section="mongodb")
mongo_db.connect()
print("Sending data to MongoDB")
mongo_db.send_files(database="podcast_project", collection="episodes",list_files= documents)
print("Updating Episodes table in Postgres")
transfer_france_culture_from_mongodb_to_postgres(sql_db_session = postgres_db_session,
                                                 mongo = mongo_db)