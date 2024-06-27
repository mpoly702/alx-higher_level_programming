from sqlalchemy import Table, Column, Integer, Numeric, String, datetime, ForeignKey
from sqlalchemy.orm import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Order(Base):
    __tablename__ = 'Order'
    Order_id = Column(Integer, primary_key=True)
    Customer_id = Column(Integer, ForeignKey('Customer.Customer_id'))
    Order_date = Column(DateTime)
    Total_amount = Column(Numeric)
    customer = relationship("Customer", backref="orders")
    