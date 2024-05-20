from customer_details import customer_details
from choose_restaurant import choose_restaurant

# Function to establish database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="R@shini444",
            database="food_court"
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to insert customer details into the database
def insert_customer(connection, customer_name, contact_number, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO customer (customer_name, contact_number, address, email) VALUES (%s, %s, '', %s)"
        cursor.execute(query, (customer_name, contact_number, email))
        connection.commit()
        st.success("Customer inserted successfully")
    except Error as e:
        st.error(f"Error: '{e}'")


#function to get restaurant names from the databse
def get_restaurants():
    restaurants = []
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT restaurant_name FROM restaurants")
            rows = cursor.fetchall()
            restaurants = [row[0] for row in rows]
    except Exception as e:
        st.error(f"Error retrieving restaurant names: {e}")
    return restaurants

conn = create_connection()

if conn:
    if 'page' not in st.session_state:
        st.session_state['page'] = 'customer_details'

    if st.session_state['page'] == 'customer_details':
        customer_details(conn, insert_customer)
    if st.session_state['page'] == 'choose_restaurant':
        restaurants = get_restaurants()
        choose_restaurant(restaurants)
=======
import pandas as pd
import numpy as np

def main():
    st.title("Food Delivery System")

    menu = ["Home", "Order Food", "Track Order", "Admin"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Food Delivery System!")

    elif choice == "Order Food":
        show_order_food()

    elif choice == "Track Order":
        show_track_order()

    elif choice == "Admin":
        show_admin()

def show_order_food():
    st.subheader("Order Food")
    # Implement food ordering logic here

def show_track_order():
    st.subheader("Track Order")
    # Implement order tracking logic here

def show_admin():
    st.subheader("Admin")
    # Implement admin functionalities here

if __name__ == '__main__':
    main()

def show_order_food():
    st.subheader("Order Food")
    
    menu_items = {
        "Pizza": 10.0,
        "Burger": 8.0,
        "Sushi": 12.0,
        "Pasta": 9.0
    }
    
    selected_items = st.multiselect("Select food items", list(menu_items.keys()))
    quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
    
    if st.button("Place Order"):
        if selected_items:
            order_details = {item: quantity for item in selected_items}
            st.write("Order placed successfully!")
            st.write("Order details:", order_details)
            # Add logic to save order details
        else:
            st.warning("Please select at least one food item")

def show_track_order():
    st.subheader("Track Order")
    
    order_id = st.text_input("Enter your order ID")
    
    if st.button("Track Order"):
        # Simulate order tracking
        if order_id:
            order_status = np.random.choice(["Preparing", "On the way", "Delivered"])
            st.write(f"Order Status: {order_status}")
        else:
            st.warning("Please enter a valid order ID")

def show_admin():
    st.subheader("Admin Dashboard")
    
    admin_menu = ["View Orders", "Manage Menu"]
    admin_choice = st.selectbox("Admin Menu", admin_menu)
    
    if admin_choice == "View Orders":
        st.write("Here you can view all orders")
        # Logic to view all orders
        
    elif admin_choice == "Manage Menu":
        st.write("Here you can manage the menu")
        # Logic to manage the menu items
