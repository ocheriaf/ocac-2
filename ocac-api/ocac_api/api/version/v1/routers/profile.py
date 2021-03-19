from fastapi import APIRouter, Depends, Body, HTTPException
from pydantic.types import UUID4

from ocac_api.api.services import profile_service
from ocac_api.exception.profile import ProfileIdDuplicationException
from ocac_api.models.profile import CreateProfile
from ocac_api.services.profile_service import ProfileServiceInterface

profile_router = APIRouter()

@profile_router.get("/by-user/{user_id}")
async def get_profile_by_user_id(user_id: UUID4):
    profile = await profile_service.get_profile(user_id)
    return profile



@profile_router.post("/")
async def create_profile(profile: CreateProfile = Body(...),
                         profile_service: ProfileServiceInterface = Depends(profile_service)):
    try:
        profile = await profile_service.create_profile(profile)
        return profile
    except ProfileIdDuplicationException:
        raise HTTPException(status_code=403, detail=f"Profile for the user {profile.user_id} already exists ")