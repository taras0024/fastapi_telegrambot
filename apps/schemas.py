import datetime

from pydantic import BaseModel, Field


class FileIn(BaseModel):
    name: str = Field(...)
    file_id: str = Field(...)


class FileOut(BaseModel):
    id: int
    name: str
    file_id: str
    created_at: datetime.datetime


class Message(BaseModel):
    message: str
