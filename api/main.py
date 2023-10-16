"""
Module Docstring
"""

import uvicorn
from fastapi import FastAPI
from api.routers import podcasts, episodes


##############################    Creatng FastAPI API   ##########################
api = FastAPI()
# api.add_resource(List_Episodes, '/list_episodes')
# api.add_resource(Download_Episodes, '/download_episodes')
api.include_router(podcasts.router)
api.include_router(episodes.router)


if __name__ == "__main__":
    uvicorn.run("main:api", host="localhost", port=8001, reload=True)