from flask_openapi3 import APIBlueprint
from flask import jsonify
from project.schemas.schemas import UserSchema
from project.controllers.user_controller import UserController
from http import HTTPStatus
from project.helpers.request_helpers.error_helper import ErrorResponse
from project.helpers.request_helpers.user_helper import UserBasePath, UserRequest, UserResponse

USERS_ENDPOINT = "/users"

EXPECTED_RESPONSES = {}

users_blueprint = APIBlueprint("users_blueprint", __name__)

user_schema = UserSchema()

@users_blueprint.get(
    f"{USERS_ENDPOINT}/<int:user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses={
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
    },
)
def get_user(path: UserBasePath):
    user = UserController.get_user_by_id(path.user_id)
    return jsonify(user_schema.dump(user))


@users_blueprint.post(
    f"{USERS_ENDPOINT}",
    responses={f"{HTTPStatus.CREATED}": UserResponse},
    extra_responses={
        "400": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
        "422": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
    },
)
def create_user(body: UserRequest):
    user = UserController.create_user(body)
    return jsonify(user_schema.dump(user)), HTTPStatus.CREATED


@users_blueprint.put(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses={
        "400": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}},
    },
)
def update_user(user_id):
    user = UserController.update_user(user_id)
    return jsonify(user_schema.dump(user))


@users_blueprint.delete(
    f"{USERS_ENDPOINT}/<user_id>",
    responses={f"{HTTPStatus.OK}": UserResponse},
    extra_responses={
        "404": {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
    },
)
def delete_user(user_id):
    UserController.delete_user(user_id)
    return "User deleted", HTTPStatus.OK
