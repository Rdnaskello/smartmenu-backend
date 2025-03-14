from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class MenuPlan(Base):
    __tablename__ = "menu_plan"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)  # Дата планування
    meal_name = Column(String, nullable=False)  # Назва страви
    category = Column(String, nullable=False)  # Категорія
    ingredients = Column(String, nullable=False)  # Список інгредієнтів
