from pydantic import BaseModel
from typing import Any, List

class DataRequest(BaseModel):
    data: List[Any]
    parameters: dict = {}

class DataResponse(BaseModel):
    status: str
    message: str
    result: Any = None 