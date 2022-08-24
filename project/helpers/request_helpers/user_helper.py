from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int = Field(..., description="The user's id")
    created_at: str = Field(..., description="The user's creation time")
    updated_at: str = Field(..., description="The user's last update time")
    email: str = Field(..., description="The user's email")
    full_name: str = Field(..., description="The user's full name")
    photo: str = Field(..., description="The user's photo url")


class UserRequest(BaseModel):
    id: int = Field(..., description="The user's id")
    created_at: str = Field(..., description="The user's creation time")
    updated_at: str = Field(..., description="The user's last update time")
    email: str = Field(..., description="The user's email")
    full_name: str = Field(..., description="The user's full name")
    photo: str = Field(..., description="The user's photo url")
