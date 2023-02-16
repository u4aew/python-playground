from databases import Database
from core.config import DATABASE_URL
from sqlalchemy import create_engine, MetaData

databases = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)
