from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class StatusEnum(enum.Enum):
    open = "open"
    closed = "closed"

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    rating = Column(Float, default=0.0)
    image = Column(String)
    logo = Column(String)
    cuisine = Column(String)
    delivery_time = Column(String)
    delivery_fee = Column(Float, default=0.0)
    status = Column(Enum(StatusEnum), default=StatusEnum.open)
    
    # Relationship
    meals = relationship("Meal", back_populates="restaurant")

class Meal(Base):
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image = Column(String)
    category = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.open)
    discount = Column(String)
    rating = Column(Float, default=0.0)
    
    # Foreign Key
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    
    # Relationship
    restaurant = relationship("Restaurant", back_populates="meals")
