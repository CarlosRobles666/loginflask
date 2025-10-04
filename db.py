import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root2", #modif
        password="fogiogjtmvoirbiojbrrbvroibri",#modif
        database="tianda2"#modif

    )
