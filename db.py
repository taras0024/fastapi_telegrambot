import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base

DATABASE_URL = 'postgresql://username:password@localhost/postgres'
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
Base = declarative_base()
