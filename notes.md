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


Docker useful commands:
    docker exec -ti mycontainer /bin/bash
    docker logs mycontainer

