from pydantic import BaseModel
from typing import Optional, List

# Restaurant schemas
class RestaurantBase(BaseModel):
    name: str
    description: Optional[str] = None
    rating: Optional[float] = 0.0
    image: Optional[str] = None
    logo: Optional[str] = None
    cuisine: Optional[str] = None
    delivery_time: Optional[str] = None
    delivery_fee: Optional[float] = 0.0
    status: Optional[str] = "open"

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[float] = None
    image: Optional[str] = None
    logo: Optional[str] = None
    cuisine: Optional[str] = None
    delivery_time: Optional[str] = None
    delivery_fee: Optional[float] = None
    status: Optional[str] = None

class RestaurantOut(RestaurantBase):
    id: int
    
    class Config:
        from_attributes = True

# Meal schemas
class MealBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = "open"
    discount: Optional[str] = None
    rating: Optional[float] = 0.0
    restaurant_id: int

class MealCreate(MealBase):
    pass

class MealUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    discount: Optional[str] = None
    rating: Optional[float] = None
    restaurant_id: Optional[int] = None

class MealOut(MealBase):
    id: int
    restaurant: Optional[RestaurantOut] = None
    
    class Config:
        from_attributes = True
