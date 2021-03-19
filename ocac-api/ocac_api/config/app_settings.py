from pydantic import BaseSettings


class AppSettings(BaseSettings):
    reload: bool = False
    secret: str = "SECRET"
