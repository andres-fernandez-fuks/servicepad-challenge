import jwt
from functools import wraps
from flask import current_app, request

from project.exceptions.exceptions import AuthenticationException, OwnershipException
from project.helpers.request_helpers.exception_handler import ExceptionHandler


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth = request.headers.get("Authorization")
        if auth:
            token = auth.split(" ")[1]
        if not token:
            return ExceptionHandler.handle_exception(AuthenticationException())

        try:
            token_info = jwt.decode(token, current_app.config["SECRET_KEY"])
        except:
            return ExceptionHandler.handle_exception(AuthenticationException())

        path_user_id = kwargs["path"].user_id
        token_user_id = token_info["id"]
        if path_user_id != token_user_id:
            return ExceptionHandler.handle_exception(OwnershipException())

        return f(*args, **kwargs)

    return decorated
