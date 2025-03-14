from fastapi import FastAPI
from app.routes import meals, menu_plan
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="SmartMenu API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволяє запити з усіх доменів (можеш вказати конкретний)
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Дозволяє всі заголовки
)

app.include_router(meals.router, prefix="/meals", tags=["Meals"])
app.include_router(menu_plan.router, prefix="/menu", tags=["Menu Plan"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartMenu API"}
