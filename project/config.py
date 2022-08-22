
from enum import Enum
import os
from decouple import config

class ConfigurationMode(Enum):
    DEVELOPMENT = 'development'
    TESTING = 'testing'


class DevelopmentConfig(object):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = False
    HOST = config('POSTGRES_HOST')
    USERNAME = config('POSTGRES_USER')
    PASSWORD = config('POSTGRES_PASSWORD')
    DATABASE = config('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
    SQL_ALCHEMY_TRACK_MODIFICATIONS = True

class TestConfig(object):
    DEBUG = True
    TESTING = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
