from enum import Enum
import os
from decouple import config
from dotenv import load_dotenv, find_dotenv


# this needs to be done because FLASK_DEBUG has to be set directly from the environment
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")  # Path to .env file
load_dotenv(dotenv_path)


class ConfigurationMode(Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"


class DevelopmentConfig(object):
    DEVELOPMENT = True
    TESTING = False
    DATABASE = config("POSTGRES_DB")
    HOST = config("POSTGRES_HOST")
    PASSWORD = config("POSTGRES_PASSWORD")
    USERNAME = config("POSTGRES_USER")
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(object):
    DEBUG = True
    TESTING = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
