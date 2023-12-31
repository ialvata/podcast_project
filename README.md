# podcast_project

[GitHub.io Personal Page](https://ialvata.github.io/)
### Overview

#### About
In this project, I create a web app, whose purpose is to webscrape information regarding some non-english speaking podcasts (e.g. France Culture), save that semi-structured data in a non-SQL Document Database (MongoDB), and then structure some of that data into a SQL database (PostgreSQL). This web app is served through Python's FastAPI framework. In the future, I'll add an object storage volume, à la AWS S3, and then add several NLP related features, such as transcribing audio files (Speach to Text), and translate this text into another language.
<div align="center">
    <img src="https://github.com/ialvata/podcast_project/assets/110241614/f93dc6dc-d046-4173-b947-a49fc119e0d1" width="75%">
</div>
<br></br>

#### Tech Stack
| **Open Source** | ![BSD 3-clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)
|---|---|
| **Tech Stack** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) |


### Services
PGAdmin4 container is launched automatically by docker compose command.
    - http://localhost:5050/  #the port may be overwritten in .env.local.db file
    - The admin user is root.
    - The Postgres db is automatically added. When you access pgadmin website, you only need to 
    introduce the db's password, which was defined in the environmental configuration file. 
    
![image](https://github.com/ialvata/podcast_project/assets/110241614/2f3720e3-27a7-4b64-9451-19f50c286d95)


MongoDB
    - http://localhost:27017/
    
MongoExpress
    - http://localhost:8081/
    - Credentials to access MongoExpress are "admin:pass", even though I changed them in the 
    environmental file. Probably a minor bug in the container...
![image](https://github.com/ialvata/podcast_project/assets/110241614/77ff3266-3944-4b66-8beb-645a71632404)
