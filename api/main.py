"""
Module Docstring
"""

import uvicorn
from fastapi import FastAPI
from api.routers import podcasts, episodes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from pathlib import Path
##############################    Creatng FastAPI API   ##########################
api = FastAPI()
origins = [
    "*",
]
##########                Setting CORS     #####################
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
################                   Adding Backend Endpoints                ####################
api.include_router(podcasts.router)
api.include_router(episodes.router)

################                   Serving Webpage                ####################
static_path = Path("./frontend/static").absolute()
templates = Jinja2Templates(directory="./frontend")
api.mount(str(static_path), StaticFiles(directory=str(static_path)), name="static")


@api.get("/", response_class=HTMLResponse)
async def render_webpage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:api", host="localhost", port=8001, reload=True)