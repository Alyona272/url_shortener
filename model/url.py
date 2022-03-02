from pydantic import BaseModel

class RequestPostUrl(BaseModel):
    url: str