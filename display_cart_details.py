import streamlit as st
import MySQLdb

def display_cart_details(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart_info")
        cart_items = cursor.fetchall()
        
        if st.button("back"):
            st.session_state['page'] = 'display_menu_items'
            st.rerun() 

        st.title("Cart Details")
        if cart_items:
            total_price = 0
            for item in cart_items:
                st.write(f"Item Name: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")
                total_price += item[1] * item[2]
            st.write(f"Total Price: {total_price}")
        else:
            st.write("Your cart is empty.")
    except MySQLdb.Error as e:
        st.error(f"Error retrieving cart details: {e}")
