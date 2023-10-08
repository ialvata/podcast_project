from pathlib import Path
import os
PROJ_PATH = Path('.').cwd()
PROJ_DATA = PROJ_PATH/"data"
folder_path_affaires = PROJ_DATA/"affaires_etrangeres"
folder_path_concordance = PROJ_DATA/"concordance_des_temps"
folder_path_culture = PROJ_DATA /"culture_monde"
folder_path_eco = PROJ_DATA/"entendez_eco"

# .env is located in the project root directory

URL = "https://www.radiofrance.fr"
URL_AFFAIRES = "https://www.radiofrance.fr/franceculture/podcasts/affaires-etrangeres"
URL_CONCORDANCE = "https://www.radiofrance.fr/franceculture/podcasts/concordance-des-temps"
URL_CULTURE = "https://www.radiofrance.fr/franceculture/podcasts/cultures-monde"
URL_ECO = "https://www.radiofrance.fr/franceculture/podcasts/entendez-vous-l-eco"

podcasts_dict = {
    "affaires":{
        "folder":folder_path_affaires,
        "url":URL_AFFAIRES,
        "title":"Affaires Étrangères",
        "language": "french"
    },
    "concordance":{
        "folder":folder_path_concordance,
        "url":URL_CONCORDANCE,
        "title":"Concordance des Temps",
        "language": "french"
    },
    "culture":{
        "folder":folder_path_culture,
        "url":URL_CULTURE,
        "title":"Cultures Monde",
        "language": "french"
    },
    "eco":{
        "folder":folder_path_eco,
        "url":URL_ECO,
        "title":"Entendez-vous l'éco?",
        "language": "french"
    },     
}