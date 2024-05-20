import mysql.connector
from mysql.connector import Error
import streamlit as st
from customer_details import customer_details
from choose_restaurant import choose_restaurant

# Function to establish database connection
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

# Function to insert customer details into the database
def insert_customer(connection, customer_name, contact_number, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customer (customer_name, contact_number, address, email) VALUES (%s, %s, '', %s)"
        cursor.execute(query, (customer_name, contact_number, email))
        connection.commit()
        st.success("Customer inserted successfully")
    except Error as e:
        st.error(f"Error: '{e}'")


#function to get restaurant names from the databse
def get_restaurants():
    restaurants = []
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT restaurant_name FROM restaurants")
            rows = cursor.fetchall()
            restaurants = [row[0] for row in rows]
    except Exception as e:
        st.error(f"Error retrieving restaurant names: {e}")
    return restaurants

conn = create_connection()

if conn:
    if 'page' not in st.session_state:
        st.session_state['page'] = 'customer_details'

    if st.session_state['page'] == 'customer_details':
        customer_details(conn, insert_customer)
    if st.session_state['page'] == 'choose_restaurant':
        restaurants = get_restaurants()
        choose_restaurant(restaurants)