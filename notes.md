After some trial and errors... Poetry is really not suitable/easy to manage the virtual env,
so..
First create a venv:
    python3 -m venv /path/to/new/virtual/environment

In your venv bin/activate script, add the following line:
    PYTHONPATH="/path/to/root/level"
    export PYTHONPATH

After installing pytest, we may need to deactivate the venv and reactivate it again.
    deactivate && source .env/bin/activate
or just close VSCode and open it again.

To use PostgreSQL db, we'll need to run
    `sudo apt install libpq-dev python3-dev`
and
    `pip install psycopg2`

# Running the App
To activate the PostgreSQL container:
    `docker compose up`
To Activate our server app:
        `uvicorn api.main:api --reload`
    If you want to access the server app:
        http://localhost:8000/

PGAdmin4 container
- http://localhost:5050/  #the port may be overwritten in .env.local.db file
- The admin user is root.
- Alpine container, hence we use apk instead of apt
- docker cp database/server.json pgadmin4_container:/pgadmin4
- docker exec -it --user root  pgadmin4_container /bin/sh

Docker useful commands:
    docker exec -ti mycontainer /bin/bash
    docker logs mycontainer

