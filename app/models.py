from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    rating = Column(Float, default=0.0)
    image = Column(String(500), nullable=True)
    logo = Column(String(500), nullable=True)
    cuisine = Column(String(100), nullable=True)
    delivery_time = Column(String(50), nullable=True)
    delivery_fee = Column(Float, default=0.0)
    status = Column(String(20), default="open")  # open/closed
    
    # Relationship
    meals = relationship("Meal", back_populates="restaurant")

class Meal(Base):
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    image = Column(String(500), nullable=True)
    category = Column(String(100), nullable=True)
    status = Column(String(20), default="open")  # open/closed
    discount = Column(String(50), nullable=True)
    rating = Column(Float, default=0.0)
    
    # Foreign Key
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    
    # Relationship
    restaurant = relationship("Restaurant", back_populates="meals")
