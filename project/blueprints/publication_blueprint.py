from http import HTTPStatus
from flask_openapi3 import APIBlueprint
from project.controllers.publication_controller import PublicationController
from project.helpers.request_helpers.error_helper import ErrorResponse
from project.helpers.request_helpers.publication_helper import (
    PublicationBasePath,
    PublicationCompletePath,
    PublicationRequest,
    PublicationResponse,
)
from project.helpers.authentication_helper import token_required

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
@token_required
def get_user_publications(path: PublicationBasePath):
    return PublicationController.get_all_user_publications(path.user_id)


@publication_blueprint.get(
    f"{PUBLICATIONS_ENDPOINT}/<publication_id>",
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
@token_required
def get_user_publication(path: PublicationCompletePath):
    return PublicationController.get_publication_by_id(
        path.user_id, path.publication_id
    )


@publication_blueprint.post(
    f"{PUBLICATIONS_ENDPOINT}",
    responses={f"{HTTPStatus.CREATED}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.BAD_REQUEST}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
@token_required
def create_publication(path: PublicationBasePath, body: PublicationRequest):
    return PublicationController.create_publication(path.user_id, PublicationRequest)


@publication_blueprint.put(
    f"{PUBLICATIONS_ENDPOINT}/<int:publication_id>",
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
@token_required
def update_publication(path: PublicationCompletePath, body: PublicationRequest):
    return PublicationController.update_publication(
        path.user_id, path.publication_id, PublicationRequest
    )


@publication_blueprint.delete(
    f"{PUBLICATIONS_ENDPOINT}/<int:publication_id>",
    responses={f"{HTTPStatus.OK}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.NOT_FOUND}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
@token_required
def delete_publication(path: PublicationCompletePath):
    return PublicationController.delete_publication(path.user_id, path.publication_id)
