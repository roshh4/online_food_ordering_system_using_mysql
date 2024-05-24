import MySQLdb
import streamlit as st

# function to calclate total price
def calculate_total_price(connection, item_id, quantity):
    try:
        cursor = connection.cursor()
        query = "SELECT price FROM menu_items WHERE item_id = %s"
        cursor.execute(query, (item_id,))
        result = cursor.fetchone()
        if result:
            item_price = result[0]
            return item_price * quantity
        else:
            st.error("Item price not found.")
            return None
    except MySQLdb.Error as e:
        st.error(f"Error calculating total price: {e}")
        return None

#function to update cart with quantity and total price
def update_cart(connection, cart_id, item_id, quantity):
    try:
        total_price = calculate_total_price(connection, item_id, quantity)
        if total_price is not None:
            cursor = connection.cursor()
            query = "UPDATE cart_items SET quantity = %s, total_price = %s WHERE cart_id = %s AND item_id = %s"
            cursor.execute(query, (quantity, total_price, cart_id, item_id))
            connection.commit()
            st.success("Cart updated successfully")
    except MySQLdb.Error as e:
        st.error(f"Error updating cart: {e}")