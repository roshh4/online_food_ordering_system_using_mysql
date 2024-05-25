import streamlit as st
import MySQLdb
from update_cart import update_cart
from delete_item_from_cart import delete_item_from_cart

# Function to display cart details
def display_cart_details(connection, cart_id):
    try:
        cursor = connection.cursor()
        if cart_id is None:
            st.error("Cart ID not found in session state.")
            return

        # Getting cart items based on cart_id
        query = "SELECT item_id, quantity, total_price FROM cart_items WHERE cart_id = %s"
        cursor.execute(query, (cart_id,))
        cart_items = cursor.fetchall()

        if st.button("Back"):
            st.session_state['page'] = 'display_menu_items'
            st.rerun()

        st.title("Cart Details")
        if cart_items:
            # Initialize session state for cart items
            if 'cart_quantities' not in st.session_state:
                st.session_state.cart_quantities = {}
                st.session_state.cart = []

            for item in cart_items:
                item_id, quantity, total_price_per_item = item
                query = "SELECT item_name, price FROM menu_items WHERE item_id = %s"
                cursor.execute(query, (item_id,))
                item_name_result = cursor.fetchone()

                if item_name_result:
                    item_name, item_price = item_name_result
                else:
                    item_name = "Unknown"
                    item_price = 0

                # Initialize the quantity in session state
                if item_id not in st.session_state.cart_quantities:
                    st.session_state.cart_quantities[item_id] = quantity

                st.write(f"Item Name: {item_name}")

                current_quantity = st.number_input(
                    f"Quantity for {item_name}:",
                    min_value=0,
                    step=1,
                    key=f"quantity_{item_id}",
                    value=st.session_state.cart_quantities[item_id]
                )

                # Update session state with current quantity
                st.session_state.cart_quantities[item_id] = current_quantity

                if current_quantity > 0:
                    item_in_cart = next((i for i in st.session_state['cart'] if i['item_id'] == item_id), None)
                    if item_in_cart:
                        if item_in_cart['quantity'] != current_quantity:
                            item_in_cart['quantity'] = current_quantity
                            update_cart(connection, cart_id, item_id, current_quantity)
                    else:
                        st.session_state['cart'].append({
                            'item_id': item_id,
                            'item_name': item_name,
                            'price': item_price,
                            'quantity': current_quantity
                        })

                elif current_quantity == 0:
                    # getting cart_item_id based on cart_id
                    cursor.execute("SELECT cart_item_id FROM cart_items WHERE cart_id = %s AND item_id = %s",
                                   (cart_id, item_id))
                    result = cursor.fetchone()
                    if result:
                        cart_item_id = result[0]
                        delete_item_from_cart(connection, cart_item_id)
                        st.session_state['cart'] = [i for i in st.session_state['cart'] if i['item_id'] != item_id]

                # Fetch updated total price per item from the database
                cursor.execute("SELECT total_price FROM cart_items WHERE cart_id = %s AND item_id = %s", (cart_id, item_id))
                total_price_result = cursor.fetchone()

                if total_price_result:
                    updated_total_price_per_item = total_price_result[0]
                    st.write(f"Price: {updated_total_price_per_item}")

                # delete button
                if st.button(f"Delete {item_name} from cart", key=f"delete_{item_id}"):
                    cursor.execute("SELECT cart_item_id FROM cart_items WHERE cart_id = %s AND item_id = %s",
                                   (cart_id, item_id))
                    result = cursor.fetchone()
                    if result:
                        cart_item_id = result[0]
                        delete_item_from_cart(connection, cart_item_id)
                        st.session_state['cart'] = [i for i in st.session_state['cart'] if i['item_id'] != item_id]
                        st.experimental_rerun()

            # Fetching total price from cart_info table after updating quantity
            query = "SELECT total_price FROM cart_info WHERE cart_id = %s"
            cursor.execute(query, (cart_id,))
            total_price_result = cursor.fetchone()

            if total_price_result:
                total_price = total_price_result[0]
                st.write(f"Total Price: {total_price}")

        else:
            st.write("Your cart is empty.")
    except MySQLdb.Error as e:
        st.error(f"Error retrieving cart details: {e}")
