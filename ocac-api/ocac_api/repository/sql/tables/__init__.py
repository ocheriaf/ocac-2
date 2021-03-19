from .users import create_user_table
from .profile import  create_profile_table

def create_tables(Base, engine):
    UserTable = create_user_table(Base, engine)
    ProfileTable = create_profile_table(Base, engine)
    return {
        "UserTable": UserTable,
        "ProfileTable": ProfileTable
    }
