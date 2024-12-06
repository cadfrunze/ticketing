from db.database_acces import DbAccess


class Services:
    def __init__(self):
        self.__db_access: DbAccess = DbAccess()

    @property
    def stoc_bilete(self) ->dict:
        lista_bilete = self.__db_access.interogare_stocBilete
        bilete: dict = {
            str(elem[1]).capitalize():{
                "pret": elem[2],

            } for elem in lista_bilete if elem[-1]
        }

        return bilete





