from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer(), primary_key=True, autoincrement=True)
    product_name = Column(String(50))
    product_price = Column(Numeric(10, 2))
    product_description = Column(String(200))
    product_image = Column(String(100))
    product_category = Column(String(50))
    product_subcategory = Column(String(50))
    product_brand = Column(String(50))
    product_rating = Column(Numeric(3, 2))
    product_stock = Column(Integer())
    product_seller = Column(String(50))
    product_seller_id = Column(Integer())
    product_seller_rating = Column(Numeric(3, 2))
    product_seller_reviews = Column(Integer())
    product_seller_response_rate = Column(Numeric(3, 2))
    product_seller_response_time = Column(String(50))
    product_shipment_time = Column(String(50))
    product_shipment_fee = Column(Numeric(10, 2))
    product_return_policy = Column(String(200))
    product_warranty = Column(String(200))
    product_created_at = Column(String(50))
    product_updated_at = Column(String(50))
    product_deleted_at = Column(String(50))
    product_status = Column(String(50))
    product_views = Column(Integer())
    product_orders = Column(Integer())
    product_sales = Column(Numeric(10, 2))
    product_profit = Column(Numeric(10, 2))
    product_margin = Column(Numeric(5, 2))
    product_cost_price = Column(Numeric(10, 2))
    product_selling_price = Column(Numeric(10, 2))
    product_discount = Column(Numeric(5, 2))
    product_reviews = Column(Integer())
    product_ratings = Column(Numeric(3, 2))