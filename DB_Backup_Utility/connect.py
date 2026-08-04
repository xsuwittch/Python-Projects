import mysql.connector
import psycopg2
import pymongo
import sqlite3

def connect_db(username, inp_password, hostname, db, db_type, port):
    match db_type:
        case "mysql":
            connection = mysql.connector.connect(
                host=hostname, port=port, user=username,
                password=inp_password, database=db
            )
        case "postgresql":
            connection = psycopg2.connect(
                host=hostname, port=port, user=username,
                password=inp_password, dbname=db
            )
        case "mongodb":
            connection = pymongo.MongoClient(
                f"mongodb://{username}:{inp_password}@{hostname}:{port}"
            )
        case "sqlite3":
            connection = sqlite3.connect(db)

    print("Connected")
    return connection