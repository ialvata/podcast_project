"""
This Module adds data to Postgres and MongoDB databases.
"""

from database import schemas
from database.connecting_orm import database_gen, engine
from database.utilities import init_db
from scrappers.france_culture import scrape_france_culture
from database.mongodb import MongoDB


#####################    Creating some initial data in Postgres db    #######################
# Base.metadate.create_all should be always in the main.py, from where we run the app.
schemas.Base.metadata.create_all(bind=engine, checkfirst=True)
get_initial_db = next(database_gen())
if get_initial_db.query(schemas.Podcasts).all() == []:
    print(f"Creating Podcasts table in {schemas.Base}")
    init_db(get_initial_db)
# scrapping data
documents = scrape_france_culture(get_initial_db)
# sending episode data to MongoDB
db = MongoDB(filename="./database/database.ini", section="mongodb")
db.connect()
db.send_files(database="podcast_project", collection="episodes",list_files= documents)