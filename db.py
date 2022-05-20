import databases
import pymongo
import sqlalchemy
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://username:password@localhost/postgres"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
Base = declarative_base()


# --- Not used ---
class MongoDB:
    def __init__(self, dbname='mongo', collection='all', url='mongodb://root:rootpassword@localhost:27019'):
        self.client = pymongo.MongoClient(url, connect=False)
        self.db = self.client[dbname]
        self.collection = self.db[collection]


# user_db = MongoDB(collection='users')
# file_db = MongoDB(collection='files')
