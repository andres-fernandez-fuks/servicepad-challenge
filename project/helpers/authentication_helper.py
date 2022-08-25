import jwt
from functools import wraps
from flask import current_app, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth = request.headers.get("Authorization")
        if auth:
            token = auth.split(" ")[1]
        if not token:
            return "Access denied", 401

        try:
            jwt.decode(token, current_app.config["SECRET_KEY"])
        except:
            return "Access denied", 401

        return f(*args, **kwargs)

    return decorated
