from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship
from .database_session import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True) 
    login = Column(String, unique=True)
    address = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    is_verified = Column(Boolean, default=True)

    products = relationship("Product", back_populates="owner")


class GroupOfProducts(Base):
    __tablename__ = "group_of_products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_of_group = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")
    products = relationship("Product", back_populates="group")


class Product(Base):
    __tablename__ = "product"
    name = Column(String)
    label = Column(String, primary_key=True)
    price = Column(Integer)
    quantity = Column(Integer, default=0)
    description = Column(String)
    
    group_id = Column(Integer, ForeignKey("group_of_products.id"))
    group = relationship("GroupOfProducts", back_populates="products")
