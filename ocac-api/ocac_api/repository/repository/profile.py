from abc import ABCMeta, abstractmethod

from databases import Database
from fastapi_users.db.sqlalchemy import GUID
from pydantic.types import UUID4
from sqlalchemy import Table

from ocac_api.models.profile import Profile, CreateProfile


class ProfileRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_profile_by_user_id(self, user_id: UUID4):
        pass

    @abstractmethod
    async def create(self, profile: CreateProfile) -> Profile:
        pass

class SQLAlchemyProfileDatabase(ProfileRepository):
    def __init__(self, db: Database, table: Table, model: Profile):
        self.database = db
        self.profile_table = table
        self.profile_model = model

    async def get_profile_by_user_id(self, user_id: UUID4)-> Profile:
        query = self.profile_table.select().where(self.profile_table.c.user_id == user_id)
        profile = await self.database.fetch_one(query)
        return profile

    async def create(self, profile: CreateProfile) -> Profile:
        query = self.profile_table.insert()
        res = await self.database.execute(query, profile.dict())
        return await self.get_profile_by_user_id(profile.user_id)
