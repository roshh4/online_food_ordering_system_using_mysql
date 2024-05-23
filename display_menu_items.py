import MySQLdb
import streamlit as st

# Function to display menu items for the selected restaurant
def display_menu_items(connection, selected_restaurant):
    try:
        cursor = connection.cursor()
        
        # Query restaurant_id for the selected restaurant
        query = "SELECT restaurant_id FROM restaurants WHERE restaurant_name = %s"
        cursor.execute(query, (selected_restaurant,))
        result = cursor.fetchone()
        
        if result:
            restaurant_id = result[0]

            # Query menu items for the selected restaurant_id
            cursor.execute("SELECT item_name, price FROM menu_items WHERE restaurant_id = %s", (restaurant_id,))
            menu_items = cursor.fetchall()

            # Initialize cart in session state if not already initialized
            if 'cart' not in st.session_state:
                st.session_state['cart'] = []

            # Display menu items
            st.title(f"Menu Items for {selected_restaurant}")
            if menu_items:
                for item in menu_items:
                    item_name, item_price = item
                    st.write(f"Item Name: {item_name}, Price: {item_price}")

                    # Button to add item to cart
                    if st.button("Add to cart",key=item_name):
                        st.session_state['cart'].append((item_name, item_price))
                        st.success(f"Added {item_name} to cart.")
            else:
                st.write("No menu items found for this restaurant.")
        else:
            st.write("Restaurant not found.")
    
    except MySQLdb.Error as e:
        st.error(f"Error retrieving menu items: {e}")
