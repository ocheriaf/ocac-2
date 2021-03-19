from databases import Database
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ocac_api.config import database_settings
from ocac_api.models.profile import Profile
from ocac_api.models.users import UserDB
from ocac_api.repository.repository.profile import SQLAlchemyProfileDatabase
from ocac_api.repository.sql.tables import create_tables

engine = create_engine(
    database_settings.database_uri
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

database = Database(database_settings.database_uri)

tables = create_tables(Base, engine)
user_repository = SQLAlchemyUserDatabase(UserDB, database, tables["UserTable"])
profile_repository = SQLAlchemyProfileDatabase(database, tables["ProfileTable"],
                                               Profile)
