import streamlit as st
import os
import MySQLdb
from streamlit_option_menu import option_menu
from display_menu_items import display_menu_items  

def insert_cart_info(connection, customer_id, restaurant_id, total_price=0):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO cart_info (customer_id, restaurant_id, total_price) VALUES (%s, %s, %s)"
        cursor.execute(query, (customer_id, restaurant_id, total_price))
        connection.commit()
        st.success("Cart info inserted successfully")
    except MySQLdb.Error as e:
        st.error(f"Error: '{e}'")

# Function to choose a restaurant
def choose_restaurant(restaurants):
    with st.sidebar:
        selected = option_menu("Restaurants", ["La Trattoria", "Sushi World","Taco Fiesta","Burger Haven","Dosa Delight"], icons=['house','house','house','house','house'], menu_icon="houses", default_index=0)
    
    st.title(selected)

    # Find the selected restaurant's image path
    image_path = None
    for row in restaurants:
        if row[0] == selected:
            image_path = row[1]
            break

    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"Image of {selected}", use_column_width=True)
    else:
        st.error(f"Image not found for {selected}")

    # Button to navigate to the menu_items page
    if st.button("View Menu Items"):
        st.session_state['selected_restaurant'] = selected
        st.session_state['page'] = 'display_menu_items' 
        st.rerun()