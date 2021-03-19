from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from fastapi_users.db.sqlalchemy import GUID
def create_profile_table(Base, engine):
    class Profile(Base):
        __tablename__ = "profile"

        id = Column(Integer, primary_key=True)
        username = Column(String(length=320), index=True, nullable=False)
        user_id = Column(GUID, ForeignKey('user.id', ondelete='CASCADE'), nullable=False, unique=True)
        is_verified = Column(Boolean, default=False, nullable=False)
        
    Base.metadata.create_all(engine)

    return Profile.__table__




