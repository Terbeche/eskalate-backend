import os
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Restaurant, Meal, Base, StatusEnum

def log_table_info():
    print("Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
    print("Defined tables:")
    for table in Base.metadata.sorted_tables:
        print(f"- {table.name}")
        print("  Columns:")
        for col in table.columns:
            print(f"    {col.name}: {col.type}")

def seed():
    db: Session = SessionLocal()
    
    # Clear existing data
    print("Clearing existing data...")
    db.query(Meal).delete()
    db.query(Restaurant).delete()
    db.commit()
    
    # Create restaurants
    restaurants_data = [
        Restaurant(
            name="The Mocktail",
            description="Fresh cocktails and light bites",
            rating=4.2,
            image="/api/placeholder/400/300",
            logo="/api/placeholder/80/80",
            cuisine="International",
            delivery_time="25-35 min",
            delivery_fee=2.5,
            status=StatusEnum.open
        ),
        Restaurant(
            name="Burger Palace",
            description="Premium burgers and fries",
            rating=4.8,
            image="/api/placeholder/400/300",
            logo="/api/placeholder/80/80",
            cuisine="American",
            delivery_time="20-30 min",
            delivery_fee=3.0,
            status=StatusEnum.open
        ),
        Restaurant(
            name="Spice Garden",
            description="Authentic Asian cuisine",
            rating=4.5,
            image="/api/placeholder/400/300",
            logo="/api/placeholder/80/80",
            cuisine="Asian",
            delivery_time="30-40 min",
            delivery_fee=2.0,
            status=StatusEnum.closed
        ),
        Restaurant(
            name="Noodle House",
            description="Fresh noodles and stir-fries",
            rating=4.3,
            image="/api/placeholder/400/300",
            logo="/api/placeholder/80/80",
            cuisine="Chinese",
            delivery_time="25-35 min",
            delivery_fee=2.5,
            status=StatusEnum.open
        ),
        Restaurant(
            name="Pizza Corner",
            description="Wood-fired pizzas",
            rating=4.6,
            image="/api/placeholder/400/300",
            logo="/api/placeholder/80/80",
            cuisine="Italian",
            delivery_time="30-45 min",
            delivery_fee=3.5,
            status=StatusEnum.open
        )
    ]
    
    print(f"Inserting {len(restaurants_data)} restaurants...")
    db.bulk_save_objects(restaurants_data)
    db.commit()
    
    # Get restaurants with IDs
    restaurants = db.query(Restaurant).all()
    
    # Create meals
    meals_data = [
        # The Mocktail meals
        Meal(
            name="Chicken Momo",
            description="Steamed chicken dumplings with spicy sauce",
            price=12.99,
            image="/api/placeholder/350/250",
            category="Appetizer",
            status=StatusEnum.open,
            discount="15% OFF",
            rating=4.2,
            restaurant_id=restaurants[0].id
        ),
        Meal(
            name="Veggie Spring Rolls",
            description="Crispy vegetable spring rolls",
            price=8.99,
            image="/api/placeholder/350/250",
            category="Appetizer",
            status=StatusEnum.open,
            rating=4.0,
            restaurant_id=restaurants[0].id
        ),
        
        # Burger Palace meals
        Meal(
            name="Classic Burger",
            description="Classic beef burger with cheese and fries",
            price=15.50,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            rating=4.8,
            restaurant_id=restaurants[1].id
        ),
        Meal(
            name="BBQ Bacon Burger",
            description="BBQ sauce, bacon, and cheese",
            price=17.99,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            discount="10% OFF",
            rating=4.9,
            restaurant_id=restaurants[1].id
        ),
        
        # Spice Garden meals
        Meal(
            name="Chicken Chili",
            description="Spicy chicken with vegetables and sauce",
            price=18.25,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.closed,
            rating=4.5,
            restaurant_id=restaurants[2].id
        ),
        Meal(
            name="Paneer Chili",
            description="Spicy paneer with bell peppers and onions",
            price=13.50,
            image="/api/placeholder/350/250",
            category="Vegetarian",
            status=StatusEnum.open,
            rating=4.1,
            restaurant_id=restaurants[2].id
        ),
        
        # Noodle House meals
        Meal(
            name="Chicken Chowmein",
            description="Stir-fried noodles with chicken and vegetables",
            price=14.75,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            rating=4.3,
            restaurant_id=restaurants[3].id
        ),
        Meal(
            name="Mixed Chowmein",
            description="Noodles with mixed vegetables and protein",
            price=17.25,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            rating=4.4,
            restaurant_id=restaurants[3].id
        ),
        
        # Pizza Corner meals
        Meal(
            name="Margherita Pizza",
            description="Classic tomato and mozzarella pizza",
            price=16.99,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            discount="20% OFF",
            rating=4.6,
            restaurant_id=restaurants[4].id
        ),
        Meal(
            name="Pepperoni Pizza",
            description="Pepperoni with mozzarella cheese",
            price=19.99,
            image="/api/placeholder/350/250",
            category="Main Course",
            status=StatusEnum.open,
            rating=4.7,
            restaurant_id=restaurants[4].id
        )
    ]
    
    print(f"Inserting {len(meals_data)} meals...")
    db.bulk_save_objects(meals_data)
    db.commit()
    print("Seed data inserted successfully.")
    db.close()

if __name__ == "__main__":
    log_table_info()
    seed()
