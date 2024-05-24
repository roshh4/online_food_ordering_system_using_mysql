import MySQLdb
import streamlit as st
from display_cart_details import display_cart_details

def display_menu_items(connection, selected_restaurant):
    
    col1, col2, col3 = st.columns([8,20,10])
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
            cursor.execute("SELECT item_name, price, description FROM menu_items WHERE restaurant_id = %s", (restaurant_id,))
            menu_items = cursor.fetchall()

            # Initialize cart in session state if not already initialized
            if 'cart' not in st.session_state:
                st.session_state['cart'] = []

            if 'added_to_cart' not in st.session_state:
                st.session_state['added_to_cart'] = {}
            
            # Display menu items
            st.title(f"Menu Items for {selected_restaurant}")
            if menu_items:
                for item in menu_items:
                    item_name, item_price, item_des = item

                    with st.container():
                        st.subheader(f"Item Name: {item_name} - Price: ${item_price}")
                        st.write(f"Description: {item_des}")

                        if item_name in st.session_state['added_to_cart']:
                            quantity = st.number_input(f"Quantity for {item_name}:", min_value=0, step=1, key=item_name)
                            if st.button(f"Update {item_name} Quantity", key=f"update_{item_name}"):
                                # Update the quantity in the cart
                                for idx, (name, price, qty) in enumerate(st.session_state['cart']):
                                    if name == item_name:
                                        st.session_state['cart'][idx] = (item_name, item_price, quantity)
                                st.success(f"Updated {item_name} quantity to {quantity}")
                        else:
                            if st.button(f"Add {item_name} to Cart", key=f"add_{item_name}"):
                                st.session_state['added_to_cart'][item_name] = True
                                st.session_state['cart'].append((item_name, item_price, 1))
                                st.success(f"Added {item_name} to cart")
                                st.experimental_rerun()

            else:
                st.write("No menu items found for this restaurant.")
        else:
            st.write("Restaurant not found.")
    
    except MySQLdb.Error as e:
        st.error(f"Error retrieving menu items: {e}")
