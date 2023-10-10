# podcast_project

[GitHub.io Personal Page](https://ialvata.github.io/)
### Badge Overview

| **Open Source** | [![BSD 3-clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)]()
|---|---|

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
