

class StocBilete:

    def __init__(self):
        self.__stoc_bilete:list[str] = list()
        self.__cantitate:int = 0
        self.__pret:int = 0

    @property
    def stoc_bilete(self)->list[str]: return self.__stoc_bilete

    @property
    def cantitate(self)->int: return self.__cantitate

    @property
    def pret(self)->int: return self.__pret

    @stoc_bilete.setter
    def stoc_bilete(self, item:str): self.__stoc_bilete.append(item)

    @cantitate.setter
    def cantitate(self, cantitate:int): self.__cantitate=cantitate

    @pret.setter
    def pret(self, pret:int): self.__pret=pret
