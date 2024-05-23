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

            # Display menu items
            st.title(f"Menu Items for {selected_restaurant}")
            if menu_items:
                for item in menu_items:
                    st.write(f"Item Name: {item[0]}, Price: {item[1]}")
            else:
                st.write("No menu items found for this restaurant.")
        else:
            st.write("Restaurant not found.")
    
    except MySQLdb.Error as e:
        st.error(f"Error retrieving menu items: {e}")
