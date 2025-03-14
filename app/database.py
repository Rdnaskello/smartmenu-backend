import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv  # Завантаження змінних середовища

# 🔹 Завантажуємо змінні з .env
load_dotenv()

# 🔹 Отримуємо URL бази даних із змінних середовища
DATABASE_URL = os.getenv("DATABASE_URL")

# 🔹 Створюємо підключення до БД
engine = create_engine(DATABASE_URL)

# 🔹 Налаштування сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔹 Базовий клас для моделей
Base = declarative_base()
