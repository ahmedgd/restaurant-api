from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# هنا بنحدد نوع قاعدة البيانات، وده SQLite كبداية
SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"

# الاتصال بقاعدة البيانات
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# مسؤول عن إنشاء الجلسات للتعامل مع DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# كل Model هيورث من Base ده
Base = declarative_base()
