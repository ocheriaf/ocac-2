import uvicorn
import ocac_api.repository.sql.SQLRepository
from ocac_api.config import app_settings

if __name__ == "__main__":
    import logging
    logging.info("API Starting with those app settings")
    
    logging.info(app_settings)
    uvicorn.run("ocac_api.api:api", reload=app_settings.reload, host="0.0.0.0", port=5000)
