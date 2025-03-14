import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.database import Base
from app.models.meals import Meal
from app.models.menu_plan import MenuPlan
from dotenv import load_dotenv

# Завантажуємо змінні з .env
load_dotenv()

# Підключаємо логер
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Отримуємо URL бази з .env
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Додаємо моделі для автоматичних міграцій
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запускає міграції у режимі офлайн."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Запускає міграції у режимі онлайн."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
