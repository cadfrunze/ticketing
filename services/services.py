import model.tools
from db.database_acces import DbAccess
from model.new_user import NewUser
from model.stoc_bilete import StocBilete
from model.tools import *

class Services:
    def __init__(self, db_acces: DbAccess=DbAccess()):
        self.__db_access = db_acces

    def list_cnp(self) -> list[any]:
        return self.__db_access.extract_cnp()


    def new_user(self,nume:str, prenume:str, cnp:str, email:str, telefon:str, tip_ticket:str, cantitate_bilete:int)->None:
        serie_ticket:str = generare_ticket()
        nr_extras:int = extragere_numar()
        new_user: NewUser = NewUser(
            nume=nume, prenume=prenume,
            cnp=cnp, email=email,telefon=telefon,
            tip_ticket=tip_ticket, serie_ticket=serie_ticket,
            cantitate_bilete=cantitate_bilete,
            nr_extras=nr_extras
        )
        self.__db_access.insert_new_user(new_user)

    def stoc_bilete(self)-> dict:
        stocuri_dict = {}
        stoc:StocBilete = self.__db_access.interogare_stocBilete()
        for elem in stoc.stoc_bilete:
            for elem1 in elem:
                stocuri_dict[elem1[0]] = [elem1[1], elem1[2]]

        return stocuri_dict

    def check_cnp(self, cnp:str)-> bool:
        lista_cnp:list[str] = self.__db_access.extract_cnp()
        if cnp in lista_cnp:
            return True
        return False










