import oracledb
import os

oracledb.init_oracle_client()


class DbAccess:
    def __init__(self):
        self.connect: oracledb = oracledb.connect
        self.connect_databse()
        self.__useri_innregistrarti = dict()

    @property
    def interogare_stocBilete(self) -> list:
        stoc_bilete: list[any] = list()
        with self.connect.cursor() as cursor:
            for row in cursor.execute("SELECT * from STOC_BILETE"):
                stoc_bilete.append(row)
        self.connection_close()
        return stoc_bilete


    def insert_newUser(self, **kwargs):
        self.__useri_innregistrarti.update(kwargs)

    def connect_databse(self) -> None:
        try:
            self.connect = oracledb.connect(
                user=os.getenv("userDb").upper(),
                password=os.getenv("passDb").upper(),
                dsn="localhost:1521/xe",
            )

        except Exception as e:
            raise e

    def connection_close(self) -> None:
        if self.connect:
            return self.connect.close()
