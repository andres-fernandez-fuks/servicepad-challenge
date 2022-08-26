from http import HTTPStatus
from flask import request
from flask_openapi3 import APIBlueprint
from project.controllers.authentication_controller import AuthenticationController
from project.helpers.request_helpers.exception_handler import ExceptionHandler

from project.helpers.request_helpers.login_helper import (
    LoginHeader,
    LoginResponse,
    LogoutRequest,
)
from project.helpers.request_helpers.error_helper import ErrorResponse

LOGIN_ENDPOINT = "/login"
LOGOUT_ENDPOINT = "/logout"

EXPECTED_RESPONSES = {}

authentication_blueprint = APIBlueprint("authentication_blueprint", __name__)
"""
Blueprint in charge of handling all authentication related requests (login and logout).
"""


@authentication_blueprint.post(
    f"{LOGIN_ENDPOINT}",
    responses={f"{HTTPStatus.OK}": LoginResponse},
    extra_responses={
        f"{HTTPStatus.UNAUTHORIZED}": {
            "content": {"application/json": {"schema": ErrorResponse.schema()}}
        }
    },
)
def login(header: LoginHeader):
    try:
        token = AuthenticationController.login(request.authorization)
        return {"token": token}, HTTPStatus.OK
    except Exception as e:
        return ExceptionHandler.handle_exception(e)


@authentication_blueprint.post(
    f"{LOGOUT_ENDPOINT}", responses={f"{HTTPStatus.OK}": None}
)
def logout(header: LogoutRequest):
    try:
        AuthenticationController.logout(header.token)
        return "", HTTPStatus.NO_CONTENT
    except Exception as e:
        return ExceptionHandler.handle_exception(e)
