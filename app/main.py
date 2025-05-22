from fastapi import FastAPI
from app.db import Base, engine
from sqlalchemy.orm import sessionmaker
from app.db import engine
from app.models import UserModel
from app.schemas import User


Base.metadata.create_all(bind=engine)

app = FastAPI()


SessionLocal = sessionmaker(autoflush=False, bind=engine)


@app.get("/users/{user_id}")
def get_user(user_id) -> User:
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return 'Пользователь не найден'
    return user


@app.get("/users")
def get_user_list() -> list[User]:
    db = SessionLocal()
    return db.query(UserModel).all()


@app.post("/users")
def create_user(user: User) -> User:
    db = SessionLocal()
    new_user = UserModel(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        surname=user.surname,
        birthday_date=user.birthday_date,
        is_admin=user.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.delete("/users/{user_id}")
def delete_user(user_id):
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return 'Пользователь не найден'
    db.delete(user)
    db.commit()
    return 'Пользователь успешно удален'


@app.put("/users/{user_id}")
def update_user(user_id, update_user: User):
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return 'Пользователь не найден'
    user.email = update_user.email
    user.first_name = update_user.first_name
    user.last_name = update_user.last_name
    user.surname = update_user.surname
    user.birthday_date = update_user.birthday_date
    user.is_admin = update_user.is_admin
    db.commit()
    db.refresh(user)
    return user
