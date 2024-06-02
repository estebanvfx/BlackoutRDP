from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.db.db_session import get_db
from app.models.user import users
from app.repositories.user_repository import read_users, create_user_in_db
from app.schemas.user import UserCreate

user = APIRouter()

@user.get("/users")
async def read_user(db: Session = Depends(get_db)):
    return read_users(db)

@user.post("/users")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_in_db(user, db)
