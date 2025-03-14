from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.meals import Meal
from app.schemas.meals import MealCreate, MealResponse

router = APIRouter()

# Отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Створення нової страви
@router.post("/", response_model=MealResponse)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**meal.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

# Отримання списку всіх страв
@router.get("/", response_model=list[MealResponse])
def get_meals(db: Session = Depends(get_db)):
    return db.query(Meal).all()

# Видалення страви за ID
@router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):  # Використовуємо get_db()
    meal = db.query(Meal).filter(Meal.id == meal_id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    db.delete(meal)
    db.commit()
    return {"message": "Meal deleted"}
