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
        `uvicorn api.main:api --port 8001 --reload`
    If you want to access the server app:
        http://localhost:8000/

PGAdmin4 container is launched automatically by docker compose command.
    - http://localhost:5050/  #the port may be overwritten in .env.local.db file
    - The admin user is root.
    - The Postgres db is automatically added. When you access pgadmin website, you only need to 
    introduce the db's password, which was defined in the environmental configuration file. 
Docker useful commands:
    - docker cp [container_name:]/path/to/source [container_name:]/path/to/destiny
        With no container name, it will assume to be referring to the local machine's 
        filesystem.
    - docker exec -ti mycontainer /bin/bash
    - docker logs mycontainer
    - docker inspect --format '{{json .Config}}' <image_name_or_id>
    - docker run -e PGADMIN_DEFAULT_EMAIL="admin" -e PGADMIN_DEFAULT_PASSWORD="admin" mycontainer

