import credential_handler
import database_connection
import mysql.connector
from mysql.connector import errorcode

import load_data

'''
try:
    connection = database_connection.connect_to_sql(credentials['sql'])
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
else:
    connection.close()
'''


# load_data.load_player_bio()
# load_data.load_schedule()
# load_data.load_teams()


