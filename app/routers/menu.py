from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/", response_model=schemas.MenuItemRead)
def create_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    new_item = models.MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=list[schemas.MenuItemRead])
def get_items(db: Session = Depends(get_db)):
    return db.query(models.MenuItem).all()
