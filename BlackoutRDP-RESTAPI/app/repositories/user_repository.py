import sys
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import users
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from app.core.utils import generate_user_id

def read_users(db:Session):
    return db.query(users).all()

def create_user_in_db(user: UserCreate, db:Session):
    new_user = users(id= generate_user_id(),username=user.name, email=user.email, hashed_password=get_password_hash(user.password))
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        print(f"Error al crear usuario: {str(e)}",  file=sys.stderr)
        
        raise HTTPException(status_code=500, detail=f"Error al crear usuario: {str(e)}")
