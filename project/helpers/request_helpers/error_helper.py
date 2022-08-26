from pydantic import BaseModel, Field
from typing import Optional, List





class ErrorResponse(BaseModel):
    """
    Class used to represent an error response.
    """
    code: int
    message: str

class ExtraResponseAssembler:
    """
    Class used to assemble an error response in a tidy way.
    """
    @staticmethod
    def assemble(extra_responses: Optional[List]) -> dict:
        if extra_responses is None:
            return {}
        response =         {
            str(code): {"content": {"application/json": {"schema": ErrorResponse.schema()}}}
            for code in extra_responses
        }
        return response
