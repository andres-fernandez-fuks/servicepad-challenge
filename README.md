# servicepad-challenge

## Pre-requisites
- [Python3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [PostgresSQL](https://www.postgresql.org/download/)


## Setup
- Clone the repository
- A PostgresSQL database is required to run the application (with all it's functionality).
- (Optional) Database creation (make sure to change the database and user names inside de script):
    ```bash
    $ sudo -u postgres psql --dbname=postgres -f ./scripts/create_db.sql
    ```
- (Optional - recommended) Set up a virtual environment:
    ```bash
    $ sudo -u postgres python3 -m venv venv
    $ source venv/bin/activate
    ```
- Install dependencies:
    ```bash
    $ pip install -r requirements.txt
    ```
- Setup the .env file: a .env file is needed in the root of the project, it must contain the following variables:
    ```bash
    POSTGRES_HOST: The host of the database
    POSTGRES_USER: The user of the database (if you used the script, make sure both values coincide)
    POSTGRES_PASSWORD: The users password
    POSTGRES_DB: The name of the database (if you used the script, make sure both values coincide)
    SECRET_KEY: A secret key that will be used for token generation (can be a random string)
    FLASK_RUN_PORT: The port in which the application will be run (default: 5000)
    ALLOW_DB_RESET: Important! Must be set to true for integration tests to work properly
    ```    
- Upgrade the database:
    ```bash
    $ flask db upgrade
    ```

## Running the application
- (Optional) If necessary, activate the virtual environment:
    ```bash
    $ source venv/bin/activate
    ```
- (Option 1 - recommended) Run the application with flask:
    ```bash
    $ flask run
    ```
- (Option 2) Run the application with python:
    ```bash
    $ python app.py
    ```

## Running tests
- Unit tests:
    ```bash
    $ python -m pytest -v --disable-warnings
    ```
- Integration (BDD) tests:
    - First, run the application:
        ```bash
        $ flask run
        ```
    - Then, run the integration tests:
        ```bash
        $ behave
        ```

## Accessing the documentation
- Run the application:
    ```bash
    $ flask run
    ```
- Open the documentation: access (preferably through the browser) to:
    ```
    http://localhost:{PORT}/openapi/swagger
    ```