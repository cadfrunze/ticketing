from db.database_acces import DbAccess
from model.new_user import NewUser
from model.stoc_bilete import StocBilete
from model.tools import *

class Services:
    def __init__(self, db_acces: DbAccess=DbAccess()):
        self.__db_access = db_acces
        self.__new_user: NewUser

    def list_cnp(self) -> list[any]:
        return self.__db_access.extract_cnp()


    def new_user(self,nume:str, prenume:str, cnp:str, email:str, telefon:str, tip_ticket:str, cantitate_bilete:int)->None:
        serie_ticket:str = generare_ticket()
        nr_extras:int = extragere_numar()

        self.__new_user = NewUser(
            nume=nume, prenume=prenume,
            cnp=cnp, email=email,telefon=telefon,
            tip_ticket=tip_ticket, serie_ticket=serie_ticket,
            cantitate_bilete=cantitate_bilete,
            nr_extras=nr_extras
        )
        #print(self.__new_user.nr_extras)
        self.__db_access.insert_new_user(self.__new_user)

    def stoc_bilete(self)-> dict:
        stocuri_dict = {}
        stoc:StocBilete = self.__db_access.interogare_stocBilete()
        for elem in stoc.stoc_bilete:
            for elem1 in elem:
                stocuri_dict[elem1[0]] = [elem1[1], elem1[2]]

        return stocuri_dict

    def check_cnp(self, cnp:str)-> bool:
        lista_cnp:set[str] = set(''.join(cnp) for cnp in self.__db_access.extract_cnp()) #Valori unice
        if cnp in lista_cnp:
            return True
        return False


    def participare_concurs(self)->str:
        premii: dict = self.__db_access.extrage_premii()
        #print(self.__new_user.nr_extras)
        if len(premii.keys()) < 1:
            return "Nu mai sunt premii in stoc!"
        else:
            premiu_list: list = list((index ,element["nume_premiu"], element["valoare_numar"]) for (index, element) in premii.items() if
                                  element["valoare_numar"] == self.__new_user.nr_extras) # premiu[0] -> tuple unde tuple[0] -> index premiu
                                                                                                    # -> tuple[1] -> nume premiu
                                                                                                    # -> tuple[-1] -> valoarea = numarul extras de client
            if premiu_list:
                return f"Felicitari ai castigat {premiu_list[0][1].upper()}"
            else: return "Ghinion nu ai castigat nimic"














