from pydantic import BaseModel
from typing import Any

class EchoRequest(BaseModel):
    data: Any

class EchoResponse(BaseModel):
    received: Any
    timestamp: str
    request_id: str
