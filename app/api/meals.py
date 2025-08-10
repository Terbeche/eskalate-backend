from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, database

router = APIRouter(prefix="/meals", tags=["meals"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.MealOut])
def list_meals(
    db: Session = Depends(get_db),
    restaurant_id: Optional[int] = None,
    search: Optional[str] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(models.Meal)
    if restaurant_id:
        query = query.filter(models.Meal.restaurant_id == restaurant_id)
    if search:
        query = query.filter(models.Meal.name.ilike(f"%{search}%"))
    if status:
        query = query.filter(models.Meal.status == status)
    return query.offset(skip).limit(limit).all()

@router.get("/{meal_id}", response_model=schemas.MealOut)
def get_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    return meal

@router.post("/", response_model=schemas.MealOut)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    # Check if restaurant exists
    restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == meal.restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    db_meal = models.Meal(**meal.dict())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

@router.put("/{meal_id}", response_model=schemas.MealOut)
def update_meal(
    meal_id: int,
    meal_update: schemas.MealUpdate,
    db: Session = Depends(get_db)
):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    
    # Check if restaurant exists if restaurant_id is being updated
    if meal_update.restaurant_id:
        restaurant = db.query(models.Restaurant).filter(models.Restaurant.id == meal_update.restaurant_id).first()
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")
    
    for key, value in meal_update.dict(exclude_unset=True).items():
        setattr(meal, key, value)
    
    db.commit()
    db.refresh(meal)
    return meal

@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    
    db.delete(meal)
    db.commit()
    return {"message": "Meal deleted successfully"}
