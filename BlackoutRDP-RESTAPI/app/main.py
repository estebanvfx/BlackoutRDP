from fastapi import FastAPI
from app.api.routes.user import user

app = FastAPI()

app.include_router(user)
