from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔹 URL підключення до PostgreSQL
DATABASE_URL = "postgresql://postgres:komashchenko@localhost/smartmenu"

# 🔹 Створюємо підключення до БД
engine = create_engine(DATABASE_URL)

# 🔹 Налаштування сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔹 Базовий клас для моделей
Base = declarative_base()
