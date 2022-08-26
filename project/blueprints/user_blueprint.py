from flask_openapi3 import APIBlueprint
from flask import jsonify
from project.exceptions.exception_handler import ExceptionHandler
from project.schemas.schemas import UserSchema
from project.controllers.user_controller import UserController
from http import HTTPStatus
from project.helpers.request_helpers.error_helper import (
    ErrorResponse,
    ExtraResponseAssembler,
)
from project.helpers.request_helpers.user_helper import (
    UserBasePath,
    UserRequest,
    UserResponse,
)
from project.helpers.authentication_helper import token_required

USERS_ENDPOINT = "/users"

EXPECTED_RESPONSES = {}

users_blueprint = APIBlueprint("users_blueprint", __name__)
"""
Blueprint in charge of handling all user related requests.
"""


user_schema = UserSchema()


@users_blueprint.post(
    f"{USERS_ENDPOINT}",
    responses={f"{HTTPStatus.CREATED}": UserResponse},
    extra_responses=ExtraResponseAssembler.assemble(
        [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]
    ),
)
def create_user(body: UserRequest):
    try:
        user = UserController.create_user(body.dict())
        return jsonify(user_schema.dump(user)), HTTPStatus.CREATED
    except Exception as e:
        return ExceptionHandler.handle(e)


@users_blueprint.get(
    f"{USERS_ENDPOINT}/<int:user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses=ExtraResponseAssembler.assemble(
        [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
            HTTPStatus.INTERNAL_SERVER_ERROR,
        ]
    ),
)
@token_required
def get_user(path: UserBasePath):
    try:
        user = UserController.get_user(path.user_id)
        if user is None:
            return jsonify({"message": "User not found"}), HTTPStatus.NOT_FOUND
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return ExceptionHandler.handle(e)


@users_blueprint.put(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses=ExtraResponseAssembler.assemble(
        [
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
            HTTPStatus.INTERNAL_SERVER_ERROR,
        ]
    ),
)
@token_required
def update_user(path: UserBasePath, body: UserRequest):
    try:
        user = UserController.update_user(path.user_id, body.dict())
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return ExceptionHandler.handle(e)


@users_blueprint.delete(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses=ExtraResponseAssembler.assemble(
        [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
            HTTPStatus.INTERNAL_SERVER_ERROR,
        ]
    ),
)
@token_required
def delete_user(path: UserBasePath):
    try:
        UserController.delete_user(path.user_id)
        return "User deleted", HTTPStatus.OK
    except Exception as e:
        return ExceptionHandler.handle(e)
