from sqlalchemy import Column, Integer, String

from db.base import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(String(64), primary_key=True, index=True)
    name = Column(String(64), index=True)
    stock = Column(Integer, default=1)
    minimum_stock = Column(Integer, default=3)
