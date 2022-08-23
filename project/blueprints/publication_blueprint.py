from flask_openapi3 import APIBlueprint
from project.controllers.publication_controller import PublicationController

PUBLICATIONS_ENDPOINT = 'users/<user_id>/publications'

EXPECTED_RESPONSES = {
}

publication_blueprint = APIBlueprint('publication_blueprint', __name__)


