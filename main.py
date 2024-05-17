import streamlit as st
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
