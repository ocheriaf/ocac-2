from fastapi_users.authentication import JWTAuthentication

from ocac_api.config import app_settings
from ocac_api.models.users import User, UserCreate, UserUpdate, UserDB
from ocac_api.repository.sql.SQLRepository import user_repository

SECRET = app_settings.secret

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)


from fastapi_users import FastAPIUsers

fastapi_users = FastAPIUsers(
    user_repository,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)