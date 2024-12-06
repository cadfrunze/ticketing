from db.database_acces import DbAccess

db_access: DbAccess = DbAccess()

class Services:
    @property
    def stoc_bilete(self) ->dict:
        lista_bilete = db_access.interogare_stocBilete
        bilete: dict = {
            str(elem[1]).capitalize():{
                "pret": elem[2],

            } for elem in lista_bilete if elem[-1]
        }

        return bilete





