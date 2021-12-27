import pymongo
import mysql.connector
import pymysql


def connect_to_mongo(credentials):
    client = pymongo.MongoClient(
        "mongodb+srv://{0}:{1}@cluster0.nwpjz.mongodb.net/nhl_data?retryWrites=true&w=majority"
            .format(credentials["username"],
                    credentials["password"]))
    return client["nhl_data"]


def connect_to_sql(credentials):
    connection = mysql.connector.connect(
        user=credentials["user"],
        password=credentials["password"],
        host=credentials["host"],
        database=credentials["database"]
    )
    return connection


def insert_df_to_sql(df, connection):
    connect_to_sql()

