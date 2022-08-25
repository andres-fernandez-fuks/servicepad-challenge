from datetime import datetime, timedelta
from flask import current_app
import jwt

from project.exceptions.authentication_exception import AuthenticationException
from project.repositories.user_repository import UserRepository


class AuthenticationController:

    AUTH_VALID_PERIOD_HS = 2

    @classmethod
    def generate_token(cls, user):
        return jwt.encode(
            {
                "id": user.id,
                "exp": datetime.utcnow()
                + timedelta(hours=cls.AUTH_VALID_PERIOD_HS),
            },
            current_app.config["SECRET_KEY"],
        )

    @staticmethod
    def login(user_credentials):
        user = UserRepository.load_by_email(user_credentials["username"])
        if not user or not user.is_correct_password(user_credentials["password"]):
            raise AuthenticationException()

        user.login()
        return {
            "token": AuthenticationController.generate_token(user),
            "user": user
        }

    @staticmethod
    def logout(user_id):
        user = UserRepository.load_by_id(user_id)
        if not user:
            raise AuthenticationException()

        user.logout()
        return {"message": "User logged out"}

