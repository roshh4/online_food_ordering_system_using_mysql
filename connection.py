import mysql.connector
import MySQLdb

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="sql12.freesqldatabase.com", 
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