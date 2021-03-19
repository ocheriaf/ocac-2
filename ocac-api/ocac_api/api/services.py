from ocac_api.repository.sql.SQLRepository import profile_repository
from ocac_api.services.profile_service import ProfileService

profile_service = ProfileService(profile_repository)