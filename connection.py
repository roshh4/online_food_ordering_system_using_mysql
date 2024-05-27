import mysql.connector
import MySQLdb

#LOCALHOST
'''def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="R@shini444",
            database="sql12707743"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except MySQLdb.Error as e:
        print(f"The error '{e}' occurred")
    return connection'''

#ONLINE  HOST
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="sql12.freesqldatabase.com	", 
            user="sql12707743",
            password="EfzR55xMVG",
            database="sql12707743"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except MySQLdb.Error as e:
        print(f"The error '{e}' occurred")
    return connection

conn = create_connection()