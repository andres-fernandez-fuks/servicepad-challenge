from pydantic import BaseModel, Field

from project.helpers.request_helpers.user_helper import UserResponse

class PublicationResponse(BaseModel):
    id: int = Field(..., description="The publication's id")
    created_at: str = Field(..., description="The publication's created at")
    updated_at: str = Field(..., description="The publication's updated at")
    title: str = Field(..., description="The publication's title")
    description: str = Field(..., description="The publication's description")
    priority: str = Field(..., description="The publication's priority")
    status: str = Field(..., description="The publication's status")
    time_since_creation: str = Field(..., description="The time since the publication was created")
    user: UserResponse = Field(..., description="The publication's user")


class PublicationRequest(BaseModel):
    id: int = Field(..., description="The publication's id")
    created_at: str = Field(..., description="The publication's created at")
    updated_at: str = Field(..., description="The publication's updated at")
    title: str = Field(..., description="The publication's title")
    description: str = Field(..., description="The publication's description")
    priority: str = Field(..., description="The publication's priority")
    status: str = Field(..., description="The publication's status")
    time_since_creation: str = Field(..., description="The time since the publication was created")
    user: UserResponse = Field(..., description="The publication's user")


class PublicationBasePath(BaseModel):
    user_id: int = Field(..., description="The user's id")

class PublicationCompletePath(PublicationBasePath):
    publication_id: int = Field(..., description="The publication's id")