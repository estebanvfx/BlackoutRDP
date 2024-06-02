from pydantic import BaseModel, EmailStr
from enum import Enum as PyEnum
from typing import Optional


class UserCreate(BaseModel):
    id: Optional[int]
    name: str
    email: EmailStr
    password: str