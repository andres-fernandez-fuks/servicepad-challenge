from pydantic import BaseModel, Field

"""
Classes used by UserBlueprint.
They represent either a request body/header/path or a response body, related to a User.
"""


class UserResponse(BaseModel):
    id: int = Field(..., description="The user's id")
    created_at: str = Field(..., description="The user's creation time")
    updated_at: str = Field(..., description="The user's last update time")
    email: str = Field(..., description="The user's email")
    full_name: str = Field(..., description="The user's full name")
    photo: str = Field(..., description="The user's photo url")


class UserRequest(BaseModel):
    fullname: str = Field(..., description="The user's full name")
    password: str = Field(..., description="The user's password")
    email: str = Field(..., description="The user's email")
    photo: str = Field(..., description="The user's photo url")


class UserBasePath(BaseModel):
    user_id: int = Field(..., description="The user's id")
