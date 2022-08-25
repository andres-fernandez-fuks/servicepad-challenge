from http import HTTPStatus
from flask import jsonify
from flask_openapi3 import APIBlueprint
from project.controllers.publication_controller import PublicationController
from project.exceptions.exceptions import ObjectNotFoundException, OwnershipException
from project.helpers.request_helpers.error_helper import ErrorResponse
from project.helpers.request_helpers.exception_handler import ExceptionHandler
from project.helpers.request_helpers.publication_helper import (
    PublicationBasePath,
    PublicationCompletePath,
    PublicationRequest,
    PublicationResponse,
)
from project.helpers.authentication_helper import token_required
from project.schemas.schemas import PublicationSchema

PUBLICATIONS_ENDPOINT = "/users/<user_id>/publications"

EXPECTED_RESPONSES = {}

publication_blueprint = APIBlueprint("publication_blueprint", __name__)

publication_schema = PublicationSchema()


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
    try:
        publication = PublicationController.get_user_publication(
            path.user_id, path.publication_id
        )
        return jsonify(publication_schema.dump(publication))
    except Exception as e:
        return ExceptionHandler.handle_exception(e)



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
    try:
        publication = PublicationController.create_publication(path.user_id, body.dict())
        return jsonify(publication_schema.dump(publication)), HTTPStatus.CREATED
    except Exception as e:
        return ExceptionHandler.handle_exception(e)


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
    try:
        publication = PublicationController.update_publication(
            path.user_id, path.publication_id, body.dict()
        )
        return jsonify(publication_schema.dump(publication))
    except Exception as e:
        return ExceptionHandler.handle_exception(e)


@publication_blueprint.delete(
    f"{PUBLICATIONS_ENDPOINT}/<int:publication_id>",
    responses={f"{HTTPStatus.OK}": PublicationResponse},
    extra_responses={
        f"{HTTPStatus.NOT_FOUND}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        },
        f"{HTTPStatus.UNAUTHORIZED}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
@token_required
def delete_publication(path: PublicationCompletePath):
    try:
        PublicationController.delete_publication(path.user_id, path.publication_id)
        return "", HTTPStatus.NO_CONTENT
    except Exception as e:
        return ExceptionHandler.handle_exception(e)