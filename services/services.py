from db.database_acces import DbAccess
from model.new_user import NewUser
from model.stoc_bilete import StocBilete

class Services:
    def __init__(self, db_acces: DbAccess=DbAccess()):
        self.stoc_bilete1 = list()
        self.__db_access = db_acces

    def list_cnp(self) -> list[any]:
        return self.__db_access.extract_cnp()

    def new_user(self, new_ser):
        pass

    def stoc_bilete(self):
        self.stoc_bilete1 = self.__db_access.interogare_stocBilete()


services: Services = Services()
print(services.stoc_bilete())







