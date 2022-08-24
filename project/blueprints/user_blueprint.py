from flask_openapi3 import APIBlueprint
from project.controllers.user_controller import UserController
from http import HTTPStatus
from project.helpers.request_helpers.error_helper import ErrorResponse

from project.helpers.request_helpers.user_helper import UserResponse

USERS_ENDPOINT = "users"

EXPECTED_RESPONSES = {}

users_blueprint = APIBlueprint("users_blueprint", __name__)


@users_blueprint.get(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={HTTPStatus.OK: UserResponse},
    extra_responses={
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
    },
)
def get_user(user_id):
    return UserController.get_user(user_id)


@users_blueprint.post(
    f"{USERS_ENDPOINT}",
    responses={HTTPStatus.CREATED: UserResponse},
    extra_responses={
        "400": {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
    },
)
def create_user():
    return UserController.create_user()


@users_blueprint.put(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={HTTPStatus.OK: UserResponse},
    extra_responses={
        "400": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
    },
)
def update_user(user_id):
    return UserController.update_user(user_id)


@users_blueprint.delete(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={HTTPStatus.OK: UserResponse},
    extra_responses={
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
    },
)
def delete_user(user_id):
    return UserController.delete_user(user_id)
