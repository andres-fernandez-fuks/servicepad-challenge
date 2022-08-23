from flask_openapi3 import APIBlueprint
from project.controllers.user_controller import UserController

USERS_ENDPOINT = 'users'

EXPECTED_RESPONSES = {
}

users_blueprint = APIBlueprint('users_blueprint', __name__)


