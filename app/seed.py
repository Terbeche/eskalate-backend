#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import Base, Restaurant, Meal
from app.database import engine, SessionLocal

def seed_data():
    """Seed the database with initial data"""
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create session
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(Meal).delete()
        db.query(Restaurant).delete()
        db.commit()
        
        # Sample restaurants
        restaurants_data = [
            {
                "name": "The Mocktail",
                "description": "Fresh cocktails and light bites",
                "rating": 4.2,
                "image": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=400&h=300&fit=crop",
                "logo": "https://images.unsplash.com/photo-1516997121675-4c2d1684aa3e?w=80&h=80&fit=crop",
                "cuisine": "International",
                "delivery_time": "25-35 min",
                "delivery_fee": 2.5,
                "status": "open"
            },
            {
                "name": "Burger Palace",
                "description": "Premium burgers and fries",
                "rating": 4.8,
                "image": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400&h=300&fit=crop",
                "logo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=80&h=80&fit=crop",
                "cuisine": "American",
                "delivery_time": "20-30 min",
                "delivery_fee": 3.0,
                "status": "open"
            },
            {
                "name": "Spice Garden",
                "description": "Authentic Asian cuisine",
                "rating": 4.5,
                "image": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=400&h=300&fit=crop",
                "logo": "https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56?w=80&h=80&fit=crop",
                "cuisine": "Asian",
                "delivery_time": "30-40 min",
                "delivery_fee": 2.0,
                "status": "closed"
            },
            {
                "name": "Noodle House",
                "description": "Fresh noodles and stir-fries",
                "rating": 4.3,
                "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400&h=300&fit=crop",
                "logo": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=80&h=80&fit=crop",
                "cuisine": "Chinese",
                "delivery_time": "25-35 min",
                "delivery_fee": 2.5,
                "status": "open"
            },
            {
                "name": "Pizza Corner",
                "description": "Wood-fired pizzas",
                "rating": 4.6,
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400&h=300&fit=crop",
                "logo": "https://images.unsplash.com/photo-1506354666786-959d6d497f1a?w=80&h=80&fit=crop",
                "cuisine": "Italian",
                "delivery_time": "30-45 min",
                "delivery_fee": 3.5,
                "status": "open"
            }
        ]
        
        # Create restaurants
        restaurants = []
        for rest_data in restaurants_data:
            restaurant = Restaurant(**rest_data)
            db.add(restaurant)
            restaurants.append(restaurant)
        
        db.commit()
        
        # Refresh to get IDs
        for restaurant in restaurants:
            db.refresh(restaurant)
        
        # Sample meals
        meals_data = [
            {
                "name": "Chicken Momo",
                "description": "Steamed chicken dumplings with spicy sauce",
                "price": 12.99,
                "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=350&h=250&fit=crop",
                "category": "Appetizer",
                "status": "open",
                "discount": "15% OFF",
                "rating": 4.2,
                "restaurant_id": restaurants[0].id
            },
            {
                "name": "Veggie Spring Rolls",
                "description": "Crispy vegetable spring rolls",
                "price": 8.99,
                "image": "https://images.unsplash.com/photo-1563379091339-03246963d125?w=350&h=250&fit=crop",
                "category": "Appetizer",
                "status": "open",
                "rating": 4.0,
                "restaurant_id": restaurants[0].id
            },
            {
                "name": "Classic Burger",
                "description": "Beef patty with lettuce, tomato, and special sauce",
                "price": 15.99,
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "open",
                "discount": "10% OFF",
                "rating": 4.5,
                "restaurant_id": restaurants[1].id
            },
            {
                "name": "Chicken Wings",
                "description": "Spicy buffalo wings with ranch dip",
                "price": 11.99,
                "image": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?w=350&h=250&fit=crop",
                "category": "Appetizer",
                "status": "open",
                "rating": 4.3,
                "restaurant_id": restaurants[1].id
            },
            {
                "name": "Pad Thai",
                "description": "Traditional Thai stir-fried noodles",
                "price": 13.99,
                "image": "https://images.unsplash.com/photo-1559314809-0f31657faf33?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "closed",
                "rating": 4.4,
                "restaurant_id": restaurants[2].id
            },
            {
                "name": "Green Curry",
                "description": "Spicy coconut curry with vegetables",
                "price": 14.99,
                "image": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "open",
                "discount": "20% OFF",
                "rating": 4.6,
                "restaurant_id": restaurants[2].id
            },
            {
                "name": "Beef Noodles",
                "description": "Slow-cooked beef with hand-pulled noodles",
                "price": 16.99,
                "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "open",
                "rating": 4.7,
                "restaurant_id": restaurants[3].id
            },
            {
                "name": "Dumplings",
                "description": "Pan-fried pork dumplings",
                "price": 9.99,
                "image": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=350&h=250&fit=crop",
                "category": "Appetizer",
                "status": "open",
                "discount": "5% OFF",
                "rating": 4.1,
                "restaurant_id": restaurants[3].id
            },
            {
                "name": "Margherita Pizza",
                "description": "Classic pizza with fresh mozzarella and basil",
                "price": 18.99,
                "image": "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "open",
                "rating": 4.8,
                "restaurant_id": restaurants[4].id
            },
            {
                "name": "Pepperoni Pizza",
                "description": "Traditional pepperoni with extra cheese",
                "price": 20.99,
                "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=350&h=250&fit=crop",
                "category": "Main Course",
                "status": "open",
                "discount": "15% OFF",
                "rating": 4.5,
                "restaurant_id": restaurants[4].id
            }
        ]
        
        # Create meals
        for meal_data in meals_data:
            meal = Meal(**meal_data)
            db.add(meal)
        
        db.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   - {len(restaurants_data)} restaurants created")
        print(f"   - {len(meals_data)} meals created")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
