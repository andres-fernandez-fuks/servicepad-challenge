from project.helpers.config_helper import ConfigHelper
from flask_openapi3 import OpenAPI

def create_app(config_filename=None):
    app = OpenAPI(__name__)
    ConfigHelper.config_app(app)
    return app