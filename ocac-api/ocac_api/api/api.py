from fastapi import FastAPI

from .authentication import fastapi_users, jwt_authentication
from .version import v1_router
from ..config import app_settings
from ..repository.sql.SQLRepository import database
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title="OnlyCertifiedAccountsAPI", description="API for Only certified accounts application",
              version="0.0.1-alpha")
api.include_router(v1_router, prefix="/v1")

origins = [
    "http://localhost",
    "http://127.0.0.1:8081",
    "http://localhost:8081",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
api.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)
api.include_router(
    fastapi_users.get_reset_password_router(
        app_settings.secret,
    ),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_verify_router(
        app_settings.secret,
    ),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


@api.on_event("startup")
async def startup():
    await database.connect()


@api.on_event("shutdown")
async def shutdown():
    await database.disconnect()
