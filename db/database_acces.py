import oracledb
import os


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
            print("Conexiune reusita")

        except oracledb.Error as e:
            raise e

    def connection_close(self) -> None:
        if self.connect:
            self.connect.close()

    def __del__(self):
        self.connection_close()

    def extract_cnp(self):
        lista:list[any]
        sqlquery = "SELECT * from STOC_BILETE"
        try:
            with self.connect.cursor() as cursor:
                lista = [row[2] for row in cursor.execute(sqlquery)]
        except oracledb.Error as e:
            print(f"Eroare la extragere cnp eroarea: {e}")
        return lista



    def interogare_stocBilete(self) -> list:
        stoc_bilete: list[any] = list()
        with self.connect.cursor() as cursor:
            for row in cursor.execute("SELECT * from STOC_BILETE"):
                stoc_bilete.append(row)
        return stoc_bilete





