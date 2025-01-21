from db.database_acces import DbAccess
from model import User

class Services:
    def __init__(self):
        self.__db_access: DbAccess = DbAccess()


    def list_cnp(self) -> list[any]:
        return self.__db_access.extract_cnp()

    def add_user(self, user: User):
        print(user.nume)







