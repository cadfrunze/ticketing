import oracledb
import os

oracledb.init_oracle_client()

try:
    connection: oracledb.connect = oracledb.connect(
        user=os.getenv("userDb").upper(),
        password=os.getenv("passDb"),
        dsn="localhost:1521/xe"
    )

    print("succes")

except Exception as e:
    print(e)

else:


    with connection.cursor() as cursor:
        for row in cursor.execute("SELECT ID_STOC_BILETE from STOC_BILETE"):
            print(row)
    connection.close()
    print("am inchis")