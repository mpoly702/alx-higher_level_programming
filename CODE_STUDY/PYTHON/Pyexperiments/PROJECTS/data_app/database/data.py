from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(50))
    user_email = Column(String(50), index=True, unique=True)
    user_phone = Column(String(20))
    user_password = Column(String(100))

