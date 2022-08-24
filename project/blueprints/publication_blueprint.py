from http import HTTPStatus
from flask_openapi3 import APIBlueprint
from project.controllers.publication_controller import PublicationController
from project.helpers.request_helpers.error_helper import ErrorResponse
from project.helpers.request_helpers.publication_helper import (
    PublicationRequest,
    PublicationResponse,
)

PUBLICATIONS_ENDPOINT = "/users/<user_id>/publications"

EXPECTED_RESPONSES = {}

publication_blueprint = APIBlueprint("publication_blueprint", __name__)


@publication_blueprint.get(
    f"{PUBLICATIONS_ENDPOINT}",
    responses={f"{HTTPStatus.OK}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.UNAUTHORIZED}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        },
        f"{HTTPStatus.NOT_FOUND}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        },
    },
)
def get_user_publications(user_id):
    return PublicationController.get_from_user(user_id)


@publication_blueprint.post(
    f"{PUBLICATIONS_ENDPOINT}",
    responses={f"{HTTPStatus.CREATED}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.BAD_REQUEST}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
def create_publication(user_id, body: PublicationRequest):
    return PublicationController.create_publication(user_id, PublicationRequest)


@publication_blueprint.put(
    f"{PUBLICATIONS_ENDPOINT}/<publication_id>",
    responses={f"{HTTPStatus.OK}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.BAD_REQUEST}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        },
        f"{HTTPStatus.NOT_FOUND}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        },
    },
)
def update_publication(user_id, publication_id, body: PublicationRequest):
    return PublicationController.update_publication(
        user_id, publication_id, PublicationRequest
    )


@publication_blueprint.delete(
    f"{PUBLICATIONS_ENDPOINT}/<publication_id>",
    responses={f"{HTTPStatus.OK}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.NOT_FOUND}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
def delete_publication(user_id, publication_id):
    return PublicationController.delete_publication(user_id, publication_id)
