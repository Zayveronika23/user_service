from sqlalchemy import Column, Integer, String, Date, Boolean
from app.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    surname = Column(String(200))
    birthday_date = Column(Date)
    is_admin = Column(Boolean, nullable=False)