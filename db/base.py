from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL

databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)
