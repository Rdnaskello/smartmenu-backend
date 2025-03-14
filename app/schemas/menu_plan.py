from pydantic import BaseModel
from datetime import date

class MenuPlanCreate(BaseModel):
    date: date
    meal_name: str
    category: str
    ingredients: str

class MenuPlanResponse(MenuPlanCreate):
    id: int

    class Config:
        from_attributes = True
