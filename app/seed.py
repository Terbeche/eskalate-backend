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
                "image": "/api/placeholder/400/300",
                "logo": "/api/placeholder/80/80",
                "cuisine": "International",
                "delivery_time": "25-35 min",
                "delivery_fee": 2.5,
                "status": "open"
            },
            {
                "name": "Burger Palace",
                "description": "Premium burgers and fries",
                "rating": 4.8,
                "image": "/api/placeholder/400/300",
                "logo": "/api/placeholder/80/80",
                "cuisine": "American",
                "delivery_time": "20-30 min",
                "delivery_fee": 3.0,
                "status": "open"
            },
            {
                "name": "Spice Garden",
                "description": "Authentic Asian cuisine",
                "rating": 4.5,
                "image": "/api/placeholder/400/300",
                "logo": "/api/placeholder/80/80",
                "cuisine": "Asian",
                "delivery_time": "30-40 min",
                "delivery_fee": 2.0,
                "status": "closed"
            },
            {
                "name": "Noodle House",
                "description": "Fresh noodles and stir-fries",
                "rating": 4.3,
                "image": "/api/placeholder/400/300",
                "logo": "/api/placeholder/80/80",
                "cuisine": "Chinese",
                "delivery_time": "25-35 min",
                "delivery_fee": 2.5,
                "status": "open"
            },
            {
                "name": "Pizza Corner",
                "description": "Wood-fired pizzas",
                "rating": 4.6,
                "image": "/api/placeholder/400/300",
                "logo": "/api/placeholder/80/80",
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
                "image": "/api/placeholder/350/250",
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
                "image": "/api/placeholder/350/250",
                "category": "Appetizer",
                "status": "open",
                "rating": 4.0,
                "restaurant_id": restaurants[0].id
            },
            {
                "name": "Classic Burger",
                "description": "Beef patty with lettuce, tomato, and special sauce",
                "price": 15.99,
                "image": "/api/placeholder/350/250",
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
                "image": "/api/placeholder/350/250",
                "category": "Appetizer",
                "status": "open",
                "rating": 4.3,
                "restaurant_id": restaurants[1].id
            },
            {
                "name": "Pad Thai",
                "description": "Traditional Thai stir-fried noodles",
                "price": 13.99,
                "image": "/api/placeholder/350/250",
                "category": "Main Course",
                "status": "closed",
                "rating": 4.4,
                "restaurant_id": restaurants[2].id
            },
            {
                "name": "Green Curry",
                "description": "Spicy coconut curry with vegetables",
                "price": 14.99,
                "image": "/api/placeholder/350/250",
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
                "image": "/api/placeholder/350/250",
                "category": "Main Course",
                "status": "open",
                "rating": 4.7,
                "restaurant_id": restaurants[3].id
            },
            {
                "name": "Dumplings",
                "description": "Pan-fried pork dumplings",
                "price": 9.99,
                "image": "/api/placeholder/350/250",
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
                "image": "/api/placeholder/350/250",
                "category": "Main Course",
                "status": "open",
                "rating": 4.8,
                "restaurant_id": restaurants[4].id
            },
            {
                "name": "Pepperoni Pizza",
                "description": "Traditional pepperoni with extra cheese",
                "price": 20.99,
                "image": "/api/placeholder/350/250",
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
