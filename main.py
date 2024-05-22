import mysql.connector
import MySQLdb
import streamlit as st
from customer_details import customer_details
from choose_restaurant import choose_restaurant
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Login", 'Restuarants'], 
        icons=['key', 'houses'], menu_icon="cast", default_index=1)
    
# Function to establish database connection
#roshini's
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="sql12.freesqldatabase.com	", 
            user="sql12707743",
            password="EfzR55xMVG",
            database="sql12707743"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
        return connection
    except Error as e:
        st.error(f"The error '{e}' occurred")
        return None

#rethinaath's
# def create_connection():
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host="sql12.freesqldatabase.com	", 
#             user="sql12707743",
#             password="EfzR55xMVG",
#             database="sql12707743"
#         )
#         if connection.is_connected():
#             print("Connection to MySQL DB successful")
#     except MySQLdb.Error as e:
#         print(f"The error '{e}' occurred")
#     return connection

conn = create_connection()

# Function to insert customer details into the database
def insert_customer(connection, customer_name, contact_number, email, address):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customer (customer_name, contact_number, address, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer_name, contact_number, email, address))
        connection.commit()
        st.success("Customer inserted successfully")
    except MySQLdb.Error as e:
        st.error(f"Error: '{e}'")

# Function to get restaurant names and images from the database
def get_restaurants(connection):
    restaurants = []
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT restaurant_name, images FROM restaurants")
            rows = cursor.fetchall()
            restaurants = [(row[0], row[1]) for row in rows]
    except MySQLdb.Error as e:
        st.error(f"Error retrieving restaurant names: {e}")
    return restaurants

# Establish the connection
conn = create_connection()

if conn:
    if 'page' not in st.session_state:
        st.session_state['page'] = 'customer_details'

    if st.session_state['page'] == 'customer_details' and selected=="Login":
        customer_details(conn, insert_customer)
    if selected=="Restuarants":
        restaurants = get_restaurants(conn)
        choose_restaurant(restaurants)