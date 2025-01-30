from typing import Type, Any

from db.database_acces import DbAccess
from model.new_user import NewUser
from model.stoc_bilete import StocBilete
from model.tools import *
from model.user_info import UserInfo


class Services:
    def __init__(self, db_acces: DbAccess=DbAccess()):
        self.__db_access = db_acces
        self.__new_user: NewUser
        self.__user_info: UserInfo

    def list_cnp(self) -> list[str]:
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
            bon_fiscal(
                nume=self.__new_user.nume,
                prenume=self.__new_user.prenume,
                cnp=self.__new_user.cnp,
                email=self.__new_user.email,
                tip_ticket=self.__new_user.tip_ticket,
                nr_bilete=self.__new_user.cantitate_bilete,
                serie_ticket=self.__new_user.serie_ticket,
                premiu="Lipsa in stocuri premii",
                nr_extras=self.__new_user.nr_extras
            )
            return "Nu mai sunt premii in stoc!"
        else:
            premiu_list: list = list((index ,element["nume_premiu"], element["valoare_numar"]) for (index, element) in premii.items() if
                                  element["valoare_numar"] == self.__new_user.nr_extras) # premiu[0] -> tuple unde tuple[0] -> index premiu
                                                                                                    # -> tuple[1] -> nume premiu
                                                                                                    # -> tuple[-1] -> valoarea = numarul extras de client
            if premiu_list:
                self.__db_access.update_premii(cnp=self.__new_user.cnp, nr_extras=self.__new_user.nr_extras)
                self.__new_user.premiu = premiu_list[0][1].upper()
                bon_fiscal(
                    nume=self.__new_user.nume,
                    prenume=self.__new_user.prenume,
                    cnp=self.__new_user.cnp,
                    email=self.__new_user.email,
                    tip_ticket=self.__new_user.tip_ticket,
                    nr_bilete=self.__new_user.cantitate_bilete,
                    serie_ticket=self.__new_user.serie_ticket,
                    premiu=self.__new_user.premiu,
                    nr_extras=self.__new_user.nr_extras
                )
                return f"Felicitari ai castigat {premiu_list[0][1].upper()} nr extras {self.__new_user.nr_extras}"
            else:
                bon_fiscal(
                    nume=self.__new_user.nume,
                    prenume=self.__new_user.prenume,
                    cnp=self.__new_user.cnp,
                    email=self.__new_user.email,
                    tip_ticket=self.__new_user.tip_ticket,
                    nr_bilete=self.__new_user.cantitate_bilete,
                    serie_ticket=self.__new_user.serie_ticket,
                    premiu="Bilet Necastigator!",
                    nr_extras=self.__new_user.nr_extras
                )
                return f"Ghinion nu ai castigat nimic nr extras {self.__new_user.nr_extras}"
#----------------PT TAB 2 ACTIVATE----------------------
    def user_info(self, cnp:str, serie_ticket: str) -> Type[UserInfo]:
        # new_serie_ticket: str = prelucrare_serie_ticket(serie_ticket)
        return self.__db_access.extract_user_info(cnp,serie_ticket)

    def client_activate_ticket(self, index: int, serie_ticket: str)->None:
        self.__db_access.update_bilete_activate(index, serie_ticket)


#---------------PT TAB 3----------------------------------------------------
    def update_client_service(self,index_key: int, email:str, telefon: str)-> None:
        self.__db_access.update_evidenta_clienti(index_key, email, telefon)

    def delete_client_service(self, index_key: int)->None:
        self.__db_access.delete_client_database(index_key)










