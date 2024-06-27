from sqlalchemy import Table, Column, Integer, Numeric, String, datetime, ForeignKey
from sqlalchemy.orm import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Cart(Base):
    __tablename__ = 'cart'
    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship("User", backref="cart")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    total = Column(Numeric(10, 2), default=0.00)
    status = Column(String(50), default='active')
    items = relationship("CartItem", backref="cart")
    
