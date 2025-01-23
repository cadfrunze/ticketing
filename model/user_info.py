

class UserInfo:
    """Interogare, detalii client"""

    def __init__(self):
        self.__nume:str = ''
        self.__prenume:str = ''
        self.__cnp:str = ''
        self.__email:str = ''
        self.__telefon:str = ''
        self.__serie_ticket:str = ''
        self.__tip_ticket:str = ''
        self.__premiu:str = ''
        self.__validare:str = ''
        self.__cantitate_cumparata:int = 0
        self.__id_client:int = 0

    # GETTERS
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
    def serie_ticket(self): return self.__serie_ticket
    @property
    def tip_ticket(self): return self.__tip_ticket
    @property
    def premiu(self): return self.__premiu
    @property
    def validare(self): return self.__validare
    @property
    def cantitate_cumparata(self): return self.__cantitate_cumparata
    @property
    def id_client(self): return self.__id_client

    #SETTERS
    @nume.setter
    def nume(self, nume:str): self.__nume=nume

    @prenume.setter
    def prenume(self, prenume:str): self.__prenume=prenume

    @cnp.setter
    def cnp(self, cnp:str): self.__cnp = cnp

    @email.setter
    def email(self, email:str): self.__email=email

    @telefon.setter
    def telefon(self, telefon:str): self.__telefon=telefon

    @serie_ticket.setter
    def serie_ticket(self, serie_ticket:str): self.__serie_ticket=serie_ticket

    @tip_ticket.setter
    def tip_ticket(self, tip_ticket:str): self.__tip_ticket=tip_ticket

    @premiu.setter
    def premiu(self, premiu:str): self.__premiu=premiu

    @validare.setter
    def validare(self, validare:str): self.__validare=validare

    @cantitate_cumparata.setter
    def cantitate_cumparata(self, cantitate_cumparata:int): self.__cantitate_cumparata=cantitate_cumparata

    @id_client.setter
    def id_client(self, id_client:int): self.__id_client=id_client

