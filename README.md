# servicepad-challenge
 
To create the database:
    $ sudo -u postgres psql --dbname=postgres -f ./scripts/create_db.sql

Test running:
    $ python -m pytest -v --disable-warnings