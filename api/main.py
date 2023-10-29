"""
Module Docstring
"""

import uvicorn
from fastapi import FastAPI
from api.routers import podcasts, episodes
from fastapi.middleware.cors import CORSMiddleware


##############################    Creatng FastAPI API   ##########################
api = FastAPI()
origins = [
    "*",
]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@api.get("/")
async def main():
    return {"message": "Hello World"}
api.include_router(podcasts.router)
api.include_router(episodes.router)


if __name__ == "__main__":
    uvicorn.run("main:api", host="localhost", port=8001, reload=True)