from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Float)
    feedbacks = Column(Integer)
