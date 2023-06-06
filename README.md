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

## Possible endpoints :

Contract:

GET : /contract/  :  list
GET : /contract/<id>  :  detail
POST : /contract/  :  create
PATCH : /contract/<id>  :  update

Customer:

GET : /customer/  :  list
GET : /customer/<id>  :  detail
POST : /customer/  :  create
PATCH : /customer/<id>  :  update

Contract:

GET : /event/  :  list
GET : /event/<id>  :  detail
POST : /event/  :  create
PATCH : /event/<id>  :  update

Specific search is possible using query parameters :

email and last_name for customer, contract and event.
date_created for contract and event.
amount for contract.


## Permission :

A manager is almighty.

A sales person can create customers, contract, and events.

Sales person can only update their attributed customer, contract or event(if about own customer)
Support person can only update events of their customers.
