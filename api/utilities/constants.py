import os
PROJ_PATH = os.path.abspath(os.path.curdir)

folder_path_affaires = os.path.join(PROJ_PATH,"data","affaires_etrangeres")
folder_path_concordance = os.path.join(PROJ_PATH,"data","concordance_des_temps")
folder_path_culture = os.path.join(PROJ_PATH,"data","culture_monde")
folder_path_eco = os.path.join(PROJ_PATH,"data","entendez_eco")

# .env is located in the project root directory

URL = "https://www.radiofrance.fr"
url_affaires = "https://www.radiofrance.fr/franceculture/podcasts/affaires-etrangeres"
url_concordance = "https://www.radiofrance.fr/franceculture/podcasts/concordance-des-temps"
url_culture = "https://www.radiofrance.fr/franceculture/podcasts/cultures-monde"
url_eco = "https://www.radiofrance.fr/franceculture/podcasts/entendez-vous-l-eco"

podcast_list = {
    "affaires":{
        "folder":folder_path_affaires,
        "url":url_affaires,
        "name":"Affaires Étrangères"
    },
    "concordance":{
        "folder":folder_path_concordance,
        "url":url_concordance,
        "name":"Concordance des Temps"
    },
    "culture":{
        "folder":folder_path_culture,
        "url":url_culture,
        "name":"Cultures Monde"
    },
    "eco":{
        "folder":folder_path_eco,
        "url":url_eco,
        "name":"Entendez-vous l'éco?"
    },     
}