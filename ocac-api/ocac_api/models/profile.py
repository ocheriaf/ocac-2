from typing import Optional

from fastapi_camelcase import CamelModel
from pydantic.types import UUID4


class Profile(CamelModel):
    id: Optional[int] = None
    user_id: Optional[UUID4] = None
    username: Optional[str] = None
    is_verified: bool = False 

class CreateProfile(CamelModel):
    user_id: UUID4
    username: str


