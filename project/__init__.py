from project.helpers.config_helper import ConfigHelper
from flask_openapi3 import OpenAPI

def create_app(test_mode=False):
    app = OpenAPI(__name__)
    ConfigHelper.config_app(app, test_mode)
    return app