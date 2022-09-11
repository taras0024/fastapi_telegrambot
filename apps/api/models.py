from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from ..settings import Base


class File(Base):
    __tablename__ = 'files_file'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    file_id = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


file_table = File.__table__
