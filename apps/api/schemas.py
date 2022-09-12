import datetime

from pydantic import BaseModel, Field


class FileIn(BaseModel):
    name: str = Field(...)
    file_id: str = Field(...)


class FileOut(BaseModel):
    id: int = None
    name: str = None
    file_id: str = None
    created_at: datetime.datetime = None


class Message(BaseModel):
    message: str
