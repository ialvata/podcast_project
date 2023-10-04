"""
Module Docstring
"""

import asyncio

import uvicorn
from fastapi import FastAPI
from api.routers import podcasts
# from db import schemas
# from db.db_orm import database_gen, engine
# from db.db_utils import init_db, stream_mocker
# from db.repository import PostgresDB

#####################    Creating some initial data in Postgres db    #######################
# print(f"Creating tables in {schemas.Base}")
# # Base.metadate.create_all should be always in the main.py, from where we run the app.
# schemas.Base.metadata.create_all(bind=engine, checkfirst=True)
# get_initial_db = next(database_gen())
# if get_initial_db.query(schemas.Post).all() == []:
#     init_db(schemas.Base, engine, get_initial_db)



##############################    Creatng FastAPI API   ##########################
api = FastAPI()
# api.add_resource(List_Episodes, '/list_episodes')
# api.add_resource(Download_Episodes, '/download_episodes')
api.include_router(podcasts.router)



@api.get("/")
async def root():
    """
    function docstring
    """
    return {"message": "Hello World 2"}


if __name__ == "__main__":
    uvicorn.run("main:api", host="localhost", port=8001, reload=True)