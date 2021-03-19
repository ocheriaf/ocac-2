from fastapi import APIRouter
from .routers import profile_router
v1_router = APIRouter()
v1_router.include_router(profile_router, tags=["Profile"], prefix="/profile")