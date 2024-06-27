from sqlalchemy import Table, Column, Integer, Numeric, String, datetime, ForeignKey
from sqlalchemy.orm import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class admin(Base):
    __tablename__ = 'admin'
    
    admin_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    

