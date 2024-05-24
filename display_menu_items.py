import MySQLdb
import streamlit as st
from display_cart_details import display_cart_details

# def update_cart(connection, quantity, item_price):
#     try:
#         cursor = connection.cursor()
#         query = "UPDATE cart_items SET quantity = %s"
#         cursor.execute(query, (quantity))
#         connection.commit()
#         st.success("Cart inserted successfully")
#     except MySQLdb.Error as e:
#         st.error(f"Error inserting cart: {e}")

def insert_cart(connection, cart_id, item_id, quantity, initial_price):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO cart_items (cart_id, item_id, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (cart_id, item_id, quantity, initial_price))
        connection.commit()
        st.success("Cart inserted successfully")
    except MySQLdb.Error as e:
        st.error(f"Error inserting cart: {e}")

# Function to display menu items for the selected restaurant
def display_menu_items(connection, selected_restaurant, cart_id):
    col1, col2, col3 = st.columns([8, 20, 10])
    with col1:
        if st.button("Back"):
            st.session_state['page'] = 'choose_restaurant'
            st.rerun()
    with col3:
        if st.button("Cart"):
            st.session_state['page'] = 'display_cart_details'
            st.rerun()
    
    try:
        cursor = connection.cursor()

        # Query restaurant_id for the selected restaurant
        query = "SELECT restaurant_id FROM restaurants WHERE restaurant_name = %s"
        cursor.execute(query, (selected_restaurant,))
        result = cursor.fetchone()

        if result:
            restaurant_id = result[0]

            # Query menu items for the selected restaurant_id
            cursor.execute("SELECT item_id, item_name, price, description, is_veg FROM menu_items WHERE restaurant_id = %s", (restaurant_id,))
            menu_items = cursor.fetchall()

            # Initialize cart in session state if not already initialized
            if 'cart' not in st.session_state:
                st.session_state['cart'] = []

            # Display menu items
            st.title(f"Menu Items for {selected_restaurant}")
            if menu_items:
                for item in menu_items:
                    item_id, item_name, item_price, item_des, item_veg = item
                    container = st.container(height=250)
                    with container:
                        col1, col2, col3 = st.columns([30, 30, 10])
                        with col1:
                            st.subheader(f"{item_name}",divider='rainbow')
                        with col3:
                            st.subheader(f"${item_price}", divider='rainbow')
                        st.write(f'{item_des}')
                        if item_veg == 1:
                            st.caption(':green_heart:')
                        else:
                            st.caption(":heart:")
                        quantity = st.number_input(f"Quantity for {item_name}:", min_value=0, step=1, key=item_name)

                        # Add item to cart when quantity changes
                        if quantity > 0:
                            item_in_cart = next((i for i in st.session_state['cart'] if i['item_name'] == item_name), None)
                            if item_in_cart:
                                item_in_cart['quantity'] = quantity
                            else:
                                st.session_state['cart'].append({
                                    'item_name': item_name,
                                    'price': item_price,
                                    'quantity': quantity
                                })
                                insert_cart(connection, cart_id, item_id, quantity, item_price)

                        elif quantity == 0:
                            st.session_state['cart'] = [i for i in st.session_state['cart'] if i['item_name'] != item_name]
            else:
                st.write("No menu items found for this restaurant.")
        else:
            st.write("Restaurant not found.")
    
    except MySQLdb.Error as e:
        st.error(f"Error retrieving menu items: {e}")
