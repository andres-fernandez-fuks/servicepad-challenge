from pydantic import BaseModel, Field

from project.helpers.request_helpers.user_helper import UserResponse

"""
Classes used by LoginBlueprint.
They represent either a request body/header or a response body, related to Login.
"""


class LoginResponse(BaseModel):
    token: str = Field(..., description="The generated token")


class LogoutRequest(BaseModel):
    token: str = Field(..., description="The token to logout")


class LoginHeader(BaseModel):
    Authorization: str = Field(
        "Basic <mail:password>",
        description="Authorization header with the <email:password> encoded in Base64",
    )

