from db.database_acces import DbAccess

db_access: DbAccess = DbAccess()

class Services:
    @property
    def stoc_bilete(self) ->dict:
        lista_bilete = db_access.print_any
        bilete: dict = {
            elem[1]:{
                "pret": elem[2],
                "locuri": elem[-1]
            } for elem in lista_bilete
        }

        return bilete





