from typing import Any
import oracledb
import os
from model.new_user import NewUser
from model.stoc_bilete import StocBilete

oracledb.init_oracle_client()


class DbAccess:
    def __init__(self):
        self.connect= oracledb.connect
        self.connect_databse()

    def connect_databse(self) -> None:
        try:
            self.connect = oracledb.connect(
                user=os.getenv("userDb").upper(),
                password=os.getenv("passDb").upper(),
                dsn="localhost:1521/xe",
            )
            #print("Conexiune reusita")

        except oracledb.Error as e:
            raise e

    def connection_close(self) -> None:
        if self.connect:
            self.connect.close()

    def __del__(self):
        self.connection_close()

    def extract_cnp(self)->list[str]:
        lista:list[str] = list()
        sqlquery = "SELECT CNP from EVIDENTA_CLIENTI"
        try:
            with self.connect.cursor() as cursor:
                lista = [row for row in cursor.execute(sqlquery)]
        except oracledb.Error as e:
            print(f"Eroare la extragere cnp eroarea: {e}")
        return lista


    def interogare_stocBilete(self) -> StocBilete:
        stoc_bilete = StocBilete()
        sql_query:str = "SELECT * from STOC_BILETE WHERE CANTITATE >:minim "
        element:list[Any] = list()
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql_query, {"minim": 0})
                for row in cursor:
                    element.append(row[1:])
            stoc_bilete.stoc_bilete = element
        except Exception as e:
            raise e
        return stoc_bilete


    def insert_new_user(self, new_user:NewUser):
        try:
            with self.connect.cursor() as cursor:
                cursor.callproc(
                    "NEW_CLIENT",
                    [
                        new_user.nume,
                        new_user.prenume,
                        new_user.cnp,
                        new_user.email,
                        new_user.telefon,
                        new_user.nr_extras,
                        new_user.tip_ticket,
                        new_user.serie_ticket,
                        new_user.validare,
                        new_user.cantitate_bilete

                    ]
                )
            self.connect.commit()
        except oracledb.DatabaseError as e:
            raise e




