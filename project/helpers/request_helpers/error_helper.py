from pydantic import BaseModel, Field
from typing import Optional, List


class ErrorResponse(BaseModel):
    code: int
    message: str


class Unauthorized(ErrorResponse):
    code: int = Field(400, description="Status Code")
    message: str = Field("Bad Request")


class Unauthorized(ErrorResponse):
    code: int = Field(401, description="Status Code")
    message: str = Field("Unauthorized!")


class NotFound(ErrorResponse):
    code: int = Field(404, description="Status Code")
    message: str = Field("Not found")


class UnprocessableEntity(ErrorResponse):
    code: int = Field(422, description="Status Code")
    message: str = Field("Unprocessable entity")


class ExtraResponseAssembler:
    @staticmethod
    def assemble(extra_responses: Optional[List]) -> dict:
        if extra_responses is None:
            return {}
        response =         {
            str(code): {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
            for code in extra_responses
        }
        return response
