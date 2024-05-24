import streamlit as st
import MySQLdb

# Function to display cart details
def display_cart_details(connection, cart_id):
    try:
        cursor = connection.cursor()
        if cart_id is None:
            st.error("Cart ID not found in session state.")
            return

        # getting cart items based on cart_id
        query = "SELECT item_id, quantity, total_price FROM cart_items WHERE cart_id = %s"
        cursor.execute(query, (cart_id,))
        cart_items = cursor.fetchall()

        if st.button("Back"):
            st.session_state['page'] = 'display_menu_items'
            st.rerun()

        st.title("Cart Details")
        if cart_items:
            total_price = 0
            for item in cart_items:
                item_id, quantity, total_price_per_item = item
                query = "SELECT item_name FROM menu_items WHERE item_id = %s"
                cursor.execute(query, (item_id,))  
                item_name_result = cursor.fetchone()
                if item_name_result:
                    item_name = item_name_result[0]
                else:
                    item_name = "Unknown"

                st.write(f"Item Name: {item_name}, Quantity: {quantity}, Price: {total_price_per_item}")
                total_price += total_price_per_item

            st.write(f"Total Price: {total_price}")
        else:
            st.write("Your cart is empty.")
    except MySQLdb.Error as e:
        st.error(f"Error retrieving cart details: {e}")
