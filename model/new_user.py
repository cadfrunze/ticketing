from typing import override, overload


class NewUser:
    """Inserare new User"""
    def __init__(self, nume:str, prenume:str, cnp:str, email:str, telefon:str, tip_ticket:str, serie_ticket:str, cantitate_bilete:int, nr_extras:int):
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__email = email
        self.__telefon = telefon
        self.__tip_ticket = tip_ticket
        self.__serie_ticket = serie_ticket
        self.__cantitate_bilete = cantitate_bilete
        self.__nr_extras = nr_extras

    @property
    def nume(self): return self.__nume

    @property
    def prenume(self): return self.__prenume

    @property
    def cnp(self): return self.__cnp

    @property
    def email(self): return self.__email

    @property
    def telefon(self): return self.__telefon

    @property
    def tip_ticket(self): return self.__tip_ticket

    @property
    def serie_ticket(self): return self.__serie_ticket

    @property
    def nr_extras(self): return self.__nr_extras

    @property
    def cantitate_bilete(self): return self.__cantitate_bilete

