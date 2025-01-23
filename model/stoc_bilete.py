

class StocBilete:

    def __init__(self):
        self.__stoc_bilete:list[any] = list()


    @property
    def stoc_bilete(self)->list[str]: return self.__stoc_bilete

    @stoc_bilete.setter
    def stoc_bilete(self, item:list[any]): self.__stoc_bilete = item

    def add_tickets(self, item):
        for elem in item:
            self.stoc_bilete = elem


