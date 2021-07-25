from fastapi import APIRouter
from app.api.routes.auth import auth as auth_router

auth = APIRouter()

auth.include_router(auth_router, prefix="/auth", tags=["auth"])
