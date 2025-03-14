from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.menu_plan import MenuPlan
from app.schemas.menu_plan import MenuPlanCreate, MenuPlanResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MenuPlanResponse)
def add_menu_item(menu_item: MenuPlanCreate, db: Session = Depends(get_db)):
    new_menu_item = MenuPlan(**menu_item.dict())
    db.add(new_menu_item)
    db.commit()
    db.refresh(new_menu_item)
    return new_menu_item

@router.get("/", response_model=list[MenuPlanResponse])
def get_menu(db: Session = Depends(get_db)):
    return db.query(MenuPlan).all()

@router.delete("/{menu_id}")
def delete_menu_item(menu_id: int, db: Session = Depends(get_db)):
    menu_item = db.query(MenuPlan).filter(MenuPlan.id == menu_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(menu_item)
    db.commit()
    return {"message": "Menu item deleted"}
