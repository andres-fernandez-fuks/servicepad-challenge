from project.exceptions.exceptions import (
    AuthenticationException,
    ObjectNotFoundException,
    OwnershipException,
)
from http import HTTPStatus


class ExceptionHandler:
    """
    This class is used to handle exceptions.
    """

    @staticmethod
    def handle_exception(exception):
        if isinstance(exception, ObjectNotFoundException):
            return {"message": str(exception)}, HTTPStatus.NOT_FOUND

        if isinstance(exception, OwnershipException):
            return {"message": str(exception)}, HTTPStatus.FORBIDDEN

        if isinstance(exception, AuthenticationException):
            return {"message": str(exception)}, HTTPStatus.UNAUTHORIZED

        return {"message": "Internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

