from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class StatusEnum(str, Enum):
    open = "open"
    closed = "closed"

# Restaurant Schemas
class RestaurantBase(BaseModel):
    name: str
    description: Optional[str] = None
    rating: Optional[float] = 0.0
    image: Optional[str] = None
    logo: Optional[str] = None
    cuisine: Optional[str] = None
    delivery_time: Optional[str] = None
    delivery_fee: Optional[float] = 0.0
    status: StatusEnum = StatusEnum.open

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
    status: Optional[StatusEnum] = None

class Restaurant(RestaurantBase):
    id: int
    
    class Config:
        from_attributes = True

# Meal Schemas
class MealBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: Optional[str] = None
    category: Optional[str] = None
    status: StatusEnum = StatusEnum.open
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
    status: Optional[StatusEnum] = None
    discount: Optional[str] = None
    rating: Optional[float] = None
    restaurant_id: Optional[int] = None

class Meal(MealBase):
    id: int
    restaurant: Optional[Restaurant] = None
    
    class Config:
        from_attributes = True

# Restaurant with meals
class RestaurantWithMeals(Restaurant):
    meals: List[Meal] = []
