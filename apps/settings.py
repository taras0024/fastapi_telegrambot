import os

import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base

NAME = os.getenv('NAME')
TOKEN = os.getenv('TOKEN')
MY_ID = os.getenv('MY_ID')
APP_URL = os.getenv('APP_URL')

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}'
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
Base = declarative_base()
