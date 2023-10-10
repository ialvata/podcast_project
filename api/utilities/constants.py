from pathlib import Path
import os
PROJ_PATH = Path('.').cwd()
PROJ_DATA = PROJ_PATH/"data"
FOLDER_PATH_AFFAIRES = str(PROJ_DATA/"affaires_etrangeres")
FOLDER_PATH_CONCORDANCE = str(PROJ_DATA/"concordance_des_temps")
FOLDER_PATH_CULTURE = str(PROJ_DATA /"culture_monde")
FOLDER_PATH_ECO = str(PROJ_DATA/"entendez_eco")

# .env is located in the project root directory

URL = "https://www.radiofrance.fr"
URL_AFFAIRES = "https://www.radiofrance.fr/franceculture/podcasts/affaires-etrangeres"
URL_CONCORDANCE = "https://www.radiofrance.fr/franceculture/podcasts/concordance-des-temps"
URL_CULTURE = "https://www.radiofrance.fr/franceculture/podcasts/cultures-monde"
URL_ECO = "https://www.radiofrance.fr/franceculture/podcasts/entendez-vous-l-eco"

podcasts_dict = {
    "affaires":{
        "folder":FOLDER_PATH_AFFAIRES,
        "url":URL_AFFAIRES,
        "title":"Affaires Étrangères",
        "language": "french"
    },
    "concordance":{
        "folder":FOLDER_PATH_CONCORDANCE,
        "url":URL_CONCORDANCE,
        "title":"Concordance des Temps",
        "language": "french"
    },
    "culture":{
        "folder":FOLDER_PATH_CULTURE,
        "url":URL_CULTURE,
        "title":"Cultures Monde",
        "language": "french"
    },
    "eco":{
        "folder":FOLDER_PATH_ECO,
        "url":URL_ECO,
        "title":"Entendez-vous l'éco?",
        "language": "french"
    },     
}

episodes_list = [
    {
        "podcast_title":"Affaires Étrangères",
        "title":"La guerre en Ukraine et la réécriture de l'histoire",
        "description":"L’histoire et la mémoire, ont toujours été tordues au mépris des faits \
            pour mieux servir la propagande ou encourager l’amnésie. La guerre russe impose \
                dans le sang ce lien tragique dans lequel doivent s’inscrire la comptabilité \
                    des faits, la construction de la mémoire et les prémices de l’histoire.",
        "date":"2023-10-07T09:00:00.000Z",
        "director":"Christine Ockrent",
        "url_audio":"https://media.radiofrance-podcast.net/podcast09/12841-07.10.2023-ITEMA_\
            23511948-2023C20675S0280-21.mp3"
    },
    {
        "podcast_title":"Concordance des Temps",
        "title":"Au gré des politiques, la figure maternelle (1789-1914)",
        "description":"De 1789 à la guerre de 14, la figure maternelle est centrale dans les \
            imaginaires politiques français. Brigitte Demeure analyse comment la nature, \
                la liberté, la Nation, la République, l’Église, chacune à leur tour, ont \
                    investi et magnifié l'allégorie maternelle. ",
        "date":"2023-09-09T08:00:00.000Z",
        "director":"Jean-Noël Jeanneney",
        "url_audio":"https://media.radiofrance-podcast.net/podcast09/16278-09.09.2023-ITEMA_\
            23481551-2023C6278E0037-21.mp3"
    },
    {
        "podcast_title":"Entendez-vous l'éco?",
        "title":"Cuisiniers : des contrats à toutes les sauces",
        "description":"Malgré les efforts déployés après la pandémie, le secteur de la \
            restauration peine à recruter. Pénibilité, décalage entre la formation et la \
                réalité du travail, comment expliquer que les cuisiniers représentent encore \
                    un métier en tension ? \n",
        "date":"2023-10-10T12:00:00.000Z",
        "director":"Tiphaine de Rocquigny",
        "url_audio":"https://media.radiofrance-podcast.net/podcast09/12841-07.10.2023-ITEMA_\
            23511948-2023C20675S0280-21.mp3"
    },
    {
        "podcast_title":"Cultures Monde",
        "title":"Le modèle suédois en décrochage",
        "description":"Longtemps louée pour sa pédagogie douce et ses résultats probants, \
            l'école suédoise est en net recul dans les enquêtes internationales depuis dix \
                ans. Un indicateur qui témoigne des failles d'un système libéralisé à marche\
                      forcée.",
        "date":"2023-10-10T09:00:00.000Z",
        "director":"Julie Gacon",
        "url_audio":"https://media.radiofrance-podcast.net/podcast09/11701-10.10.2023-ITEMA_\
            23514637-2023C16756S0283-21.mp3"
    },     
]