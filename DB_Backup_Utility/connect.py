import mysql.connector
import psycopg2
import pymongo
import sqlite3
def connect_db(username, inp_password,hostname, db , db_type, port):
    match db_type: 
        case "mysql":
            connection = mysql.connector.connect(host = hostname, user = username, password = inp_password, database = db)
        case "postgresql":
            connection = psycopg2.connect(host = hostname, user=username, password=inp_password, dbname=db)
        case "mongodb":
            connectioln= pymongo.MongoClient(f"mongodb://{hostname}:{port}")
        case "sqlite3":
            connection = sqlite3.connect(db)

    print(" Connected ")
    return connection