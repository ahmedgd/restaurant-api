from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db
from app.auth_utils import decode_access_token

router = APIRouter()

# إعداد OAuth2 باستخدام JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# دالة التحقق من التوكن وفك تشفيره
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    return decode_access_token(token)

# إنشاء عنصر منيو (يتطلب توكن)
@router.post("/menu/", response_model=schemas.MenuItemRead)
def create_menu_item(
    item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user)
):
    return crud.create_menu_item(db=db, item=item)

# قراءة عناصر المنيو (يتطلب توكن)
@router.get("/menu/", response_model=list[schemas.MenuItemRead])
def read_menu_items(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    token_data: dict = Depends(get_current_user)
):
    return crud.get_menu_items(db=db, skip=skip, limit=limit)
