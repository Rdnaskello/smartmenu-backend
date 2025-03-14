from pydantic import BaseModel

class MealBase(BaseModel):
    name: str
    category: str
    ingredients: str

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: int

    class Config:
        orm_mode = True
