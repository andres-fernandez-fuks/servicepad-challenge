from project.helpers.config_helper import ConfigHelper
from flask_openapi3 import OpenAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_mode=False):
    app = OpenAPI(__name__)
    initialize_extensions(app)
    ConfigHelper.config_app(app, test_mode)
    return app

def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)