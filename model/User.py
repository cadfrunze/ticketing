from typing import override, overload


class User:
    def __init__(self, nume:str, prenume:str, cnp:str, email:str, telefon:str):
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__email = email
        self.__telefon = telefon

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

