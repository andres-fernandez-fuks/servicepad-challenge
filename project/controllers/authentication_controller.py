from datetime import datetime, timedelta
from flask import current_app
import jwt

from project.exceptions.exceptions import AuthenticationException
from project.repositories.user_repository import UserRepository


class AuthenticationController:

    AUTH_VALID_PERIOD_HS = 2

    @classmethod
    def generate_token(cls, user):
        return jwt.encode(
            {
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(hours=cls.AUTH_VALID_PERIOD_HS),
            },
            current_app.config["SECRET_KEY"],
        )


    @classmethod
    def decode_token(cls, token):
        return jwt.decode(token, current_app.config["SECRET_KEY"])

    @staticmethod
    def login(user_credentials):
        user = UserRepository.load_by_email(user_credentials["username"])
        if not user or not user.is_correct_password(user_credentials["password"]):
            raise AuthenticationException()

        user.login()
        return AuthenticationController.generate_token(user).decode("utf-8")

    @staticmethod
    def logout(token):
        user_info = AuthenticationController.decode_token(token)
        user = UserRepository.load_by_id(user_info["id"])
        if not user:
            raise AuthenticationException()

        user.logout()
        return {"message": "User logged out"}

