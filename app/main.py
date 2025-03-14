from fastapi import FastAPI
from app.routes import meals, menu_plan
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartMenu API")

# 🔹 Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://smartmenu-frontend-alpha.vercel.app",
        "https://smartmenu-frontend.vercel.app",
        "https://web-production-00bb.up.railway.app",
    ],
    allow_origin_regex="https://.*\.vercel\.app",  # Дозволяє всі піддомени на Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Додаємо маршрути (з правильним префіксом)
app.include_router(meals.router, prefix="/meals", tags=["Meals"])
app.include_router(menu_plan.router, prefix="/menu", tags=["Menu Plan"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartMenu API"}
