# EPIC EVENTS

This application is a CRM for events handling.  
The users will be the managers and the salers and supporters.  

The django admin site is available for the managers team.

## Installation :

### Creating virtual environment :

python -m venv /path/to/new/virtual/environment

### Activating virtual environment :

 - Posix : """ source <venv>/bin/activate """
 - Windows : """ <venv>\Scripts\activate.bat """

### Docker for database :

We are using docker to host the database : (make sure docker is correctly installed)

docker run -p 5432:5432 -d \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=epic_event_db \
    -v pgdata:/var/lib/postgresql/data \
    --name epic_event_db \
    postgres

or

make docker_psql

### Install dependencies :

python -m pip install -r requirements.txt

### Run migrations :

python manage.py migrate

or

make migrate

## Run the application :

python manage.py runserver

or

make migrations
