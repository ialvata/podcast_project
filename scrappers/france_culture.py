from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor
import requests
import json
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import Podcasts as Podcasts_SQL
from pydantic_models.podcasts import (
    Podcast as Podcast_Pydantic,
    PodcastOut as Podcast_Pydantic_Out
)


FRANCE_CULTURE_URL = "https://www.radiofrance.fr"

def episodes_urls(podcast_url:str)-> list[str]:
    page = requests.get(podcast_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(
        "li", class_="Collection-section-items-item svelte-nyl5io separators"
    )
    list_ep = []
    for result in results:
        link = result.find("a")
        episode_url = FRANCE_CULTURE_URL + link.attrs["href"]
        list_ep.append(episode_url)
    return list_ep

def episodes_content(episode_url:str)-> list[dict[str,str]]:
    page = requests.get(episode_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(
        type="application/ld+json"
    )
    json_content = []
    for result in results:
        json_content.append(json.loads(result.string))
    return json_content

def scrape_france_culture(db_session:Session)-> list:
    # import all podcast urls from postgres db
    stmt =(
        select(Podcasts_SQL)
        .where(Podcasts_SQL.publisher == "France Culture")
    )

    podcasts_list = [
        # row.t is a tuple whose 1st element is a schema instance
        Podcast_Pydantic_Out.from_schema_to_pydantic(row.t[0]).url
        for row in db_session.execute(stmt)
    ]
    # scrape each podcast episodes urls
    with ProcessPoolExecutor(max_workers=8) as pool:
        episodes_list = []
        for urls in  pool.map(episodes_urls,podcasts_list):
            episodes_list += [episodes_content(url) for url in urls]
    return episodes_list

