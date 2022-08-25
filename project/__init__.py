from project.helpers.config_helper import ConfigHelper
from flask_openapi3 import OpenAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()


def create_app(test_mode=False):
    app = OpenAPI(__name__)
    ConfigHelper.config_app(app, test_mode)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)


def register_blueprints(app):
    from project.blueprints.publication_blueprint import publication_blueprint
    from project.blueprints.user_blueprint import users_blueprint
    from project.blueprints.authentication_blueprint import authentication_blueprint

    app.register_blueprint(publication_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(authentication_blueprint)