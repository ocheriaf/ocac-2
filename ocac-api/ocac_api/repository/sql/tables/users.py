from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship

def create_user_table(Base, engine):
    class UserTable(Base, SQLAlchemyBaseUserTable):
        children = relationship("Profile")

    Base.metadata.create_all(engine)

    return UserTable.__table__

