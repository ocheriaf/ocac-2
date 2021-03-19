from abc import ABCMeta, abstractmethod

from pydantic.types import UUID4

from ocac_api.exception.profile import ProfileIdDuplicationException
from ocac_api.models.profile import Profile, CreateProfile
from ocac_api.repository.repository.profile import ProfileRepository


class ProfileServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    async def get_profile(self, user_id: UUID4) -> Profile:
        pass

    @abstractmethod
    async def create_profile(self, profile_create: CreateProfile) -> Profile:
        pass

    def __call__(self):
        return self


class ProfileService(ProfileServiceInterface):
    def __init__(self, profile_repository: ProfileRepository):
        self.profile_repository = profile_repository

    async def get_profile(self, user_id: UUID4) -> Profile:
        return await self.profile_repository.get_profile_by_user_id(user_id)

    async def create_profile(self, profile_create: CreateProfile) -> Profile:
        user = await self.profile_repository.get_profile_by_user_id(profile_create.user_id)
        print(user)
        if user:
            raise ProfileIdDuplicationException()
        return await self.profile_repository.create(profile_create)
