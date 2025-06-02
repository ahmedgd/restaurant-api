from fastapi import FastAPI
from app.routers import orders, auth
from app.database import engine
from app import models

# إنشاء الجداول تلقائيًا من الـ models (لو مش عامل init_db.py خارجي)
models.Base.metadata.create_all(bind=engine)

# إنشاء تطبيق FastAPI
app = FastAPI(
    title="Restaurant API",
    description="API for managing restaurant orders and authentication",
    version="1.0.0"
)

# تسجيل الراوترات
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


@app.get("/")
def read_root():
    return {"message": "Restaurant API is working 🚀"}
