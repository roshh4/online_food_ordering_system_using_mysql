from connection import conn
import MySQLdb
import streamlit as st
from customer_details import customer_details
from choose_restaurant import choose_restaurant
from display_menu_items import display_menu_items

# Function to insert customer details into the database
def insert_customer(connection, customer_name, contact_number, address, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customer (customer_name, contact_number, address, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer_name, contact_number, address, email))
        connection.commit()
        st.success("Customer inserted successfully")
    except MySQLdb.Error as e:
        st.error(f"Error: '{e}'")


#function to get restaurant names from the databse
def get_restaurants():
    restaurants = []
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT restaurant_name, images FROM restaurants")
            rows = cursor.fetchall()
            restaurants = [(row[0], row[1]) for row in rows]
    except MySQLdb.Error as e:
        st.error(f"Error retrieving restaurant names: {e}")
    return restaurants

if conn:
    if 'page' not in st.session_state:
        st.session_state['page'] = 'customer_details'

    if st.session_state['page'] == 'customer_details':
        customer_details(conn, insert_customer)
    elif st.session_state['page'] == 'choose_restaurant':
        restaurants = get_restaurants()
        selected_restaurant = choose_restaurant(restaurants)
        if selected_restaurant:  # Check if a restaurant is selected
            print(selected_restaurant)
            st.session_state['selected_restaurant'] = selected_restaurant
            st.session_state['page'] = 'display_menu_items'

    elif st.session_state['page'] == 'display_menu_items':
        display_menu_items(conn, st.session_state['selected_restaurant'])