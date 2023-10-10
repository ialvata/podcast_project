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