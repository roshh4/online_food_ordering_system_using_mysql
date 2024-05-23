import MySQLdb
import streamlit as st


def insert_cart(connection, customer_id, restaurant_id, total_price):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO cart_info(customer_id, restaurant_id, total_price) VALUES (%d, %d, %d, %f)"
        cursor.execute(query, (customer_id, restaurant_id, total_price))
        connection.commit()
        st.success("Cart inserted successfully")
    except MySQLdb.Error as e:
        st.error(f"Error: '{e}'")

# Function to display menu items for the selected restaurant
def display_menu_items(connection, selected_restaurant):
    
    col1, col2, col3 = st.columns([8,20,10])
    with col1:
        if st.button("back"):
            st.session_state['page'] = 'choose_restaurant'
            st.rerun()
    with col3:
        st.button("CART")
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
                    
                    st.number_input("Quantity: ",key=item_name,min_value=0,step=1)

            else:
                st.write("No menu items found for this restaurant.")
        else:
            st.write("Restaurant not found.")
    
    except MySQLdb.Error as e:
        st.error(f"Error retrieving menu items: {e}")
