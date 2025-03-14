from fastapi import FastAPI
from app.routes import meals, menu_plan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartMenu API")

# 🔹 Налаштування CORS (Додано перед роутами)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Локальний фронтенд
        "https://smartmenu-frontend-alpha.vercel.app",  # Vercel фронтенд
        "https://smartmenu-frontend.vercel.app",  # Головний Vercel фронтенд
        "https://web-production-00bb.up.railway.app",  # Railway бекенд
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Дозволяє всі заголовки
)

# 🔹 Додаємо маршрути (з правильним префіксом)
app.include_router(meals.router, prefix="/meals", tags=["Meals"])
app.include_router(menu_plan.router, prefix="/menu", tags=["Menu Plan"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartMenu API"}
