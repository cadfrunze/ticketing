from typing import Any, Type
import oracledb
import os
from model.new_user import NewUser
from model.stoc_bilete import StocBilete
from model.user_info import UserInfo

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

    def extrage_premii(self)-> dict:
        sql_query: str = "SELECT * from STOC_PREMII WHERE CANTITATE >: minim"
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sql_query, {"minim": 0})
                premii = {element[0]: {
                    "nume_premiu": element[1],
                    "cantitate_premiu": element[2],
                    "valoare_numar": element[-1]
                    }
                    for element in cursor.fetchall()
                }
        except Exception as e:
            raise e
        return premii

    def update_premii(self, cnp: str, nr_extras:int):
        try:
            with self.connect.cursor() as cursor:
                cursor.callproc(
                    "UPDATE_PREMII",
                    [
                        cnp,
                        nr_extras
                    ]
                )
            self.connect.commit()
        except oracledb.DatabaseError as e:
            raise e
#----------------TABUL 2 Activate-----------------------------

    def extract_user_info(self, cnp: str, serie_ticket: str)-> Type[UserInfo]:
        nume_prov:str = str()
        prenume_prov:str = str()
        cnp_prov:str = str()
        email_prov:str = str()
        telefon_prov:str = str()
        serie_ticket_prov:str = str()
        tip_ticket_prov:str = str()
        premiu_prov:str = str()
        validare_prov:int = int()
        cantitate_prov:int = int()
        id_client_prov:int = int()

        sqlquery_evclienti = "SELECT * FROM EVIDENTA_CLIENTI WHERE CNP =: cnp"
        sqlquery_stocbilete = 'SELECT serie_ticket, validare, cantitate_bilete FROM STOC_BILETE_CUMPARATE WHERE FK_IDEVIDENTA_CLIENTI =: id_client_prov AND SERIE_TICKET =: serie_ticket'
        sqlquery_castigatori = "SELECT FK_IDSTOC_PREMII FROM EVIDENTA_CASTIGATORI WHERE FK_IDSTOC_BILETE_CUMPARATE =: id_client_prov"
        sql_query_stocpremii = "SELECT DENUMIRE_PREMIU FROM STOC_PREMII WHERE PK_IDSTOC_PREMII =: id_premiu"
        try:
            with self.connect.cursor() as cursor:
                cursor.execute(sqlquery_evclienti, {"cnp": cnp})
                tuple_elemente_clienti: tuple[Any] = cursor.fetchone()
                try:
                    tuple_elemente_clienti[3]
                except TypeError : return UserInfo
                else:
                    id_client_prov = tuple_elemente_clienti[0]
                    nume_prov = tuple_elemente_clienti[1]
                    prenume_prov = tuple_elemente_clienti[2]
                    cnp_prov = tuple_elemente_clienti[3]
                    email_prov = tuple_elemente_clienti[4]
                    telefon_prov = tuple_elemente_clienti[5]


        except oracledb.DatabaseError as e: raise e
        if id_client_prov > 0:
            try:
                with self.connect.cursor() as cursor:
                    cursor.execute(sqlquery_stocbilete, {"id_client_prov":id_client_prov, "serie_ticket":serie_ticket})
                    tuple_elemente_bilete: tuple[Any] = cursor.fetchone()
                    try:
                        tuple_elemente_bilete[0]
                    except TypeError: return UserInfo
                    else:
                        serie_ticket_prov = tuple_elemente_bilete[0]
                        validare_prov = tuple_elemente_bilete[1]
                        cantitate_prov = tuple_elemente_bilete[2]

            except oracledb.DatabaseError as e: raise e
            else:
                try:
                    with self.connect.cursor() as cursor:
                        cursor.execute(sqlquery_castigatori, {"id_client_prov":id_client_prov})
                        id_premiu = cursor.fetchone()
                        try:
                            id_premiu[0]
                        except TypeError: pass
                        else:
                            with self.connect.cursor() as cursor:
                                cursor.execute(sql_query_stocpremii, {"id_premiu": id_premiu[0]})
                                stoc_premiu = cursor.fetchone()
                                print(stoc_premiu[0])
                                premiu_prov = stoc_premiu[0]

                except oracledb.DatabaseError as e: raise e

        else: return UserInfo

        UserInfo.nume = nume_prov
        UserInfo.prenume = prenume_prov
        UserInfo.cnp = cnp_prov
        UserInfo.email = email_prov
        UserInfo.telefon = telefon_prov
        UserInfo.serie_ticket = serie_ticket_prov
        UserInfo.premiu = premiu_prov
        UserInfo.validare = validare_prov
        UserInfo.cantitate_cumparata = cantitate_prov
        UserInfo.id_client = id_client_prov
        return UserInfo

    def update_bilete_activate(self, index: int, serie_ticket: str)->None:

        with self.connect.cursor() as cursor:
            try:
                cursor.callproc("ACTIVATE_TICKET",
                                [
                                    index,
                                    serie_ticket
                                ])
                self.connect.commit()

            except oracledb.DatabaseError as e: raise e





