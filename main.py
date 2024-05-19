import streamlit as st
st.write("Hello there")
st.write("this is rosh")
import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="R@shini444",
            database="food_court"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Establish the connection
conn = create_connection()
