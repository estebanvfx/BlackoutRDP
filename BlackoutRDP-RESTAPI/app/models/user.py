from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.db.db_session import meta, engine

Base = declarative_base()

class users(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


