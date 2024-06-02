from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.core.config import settings

#configuracion de hash de la contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#funcion para encriptar la contraseña
def get_password_hash(password: str):
    return pwd_context.hash(password)


#funcion para verificar la contraseña
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

#funcion para crear el token de acceso
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXPIRE_MIN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

#funcion para verificar el token de acceso
async def verify_token(token:str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user: str = payload.get("sub")
        return user
    except jwt.ExpiredSignatureError: #token expirado
        return None
    except JWTError:   
        return None
