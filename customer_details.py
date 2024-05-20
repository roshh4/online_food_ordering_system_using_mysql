import streamlit as st

def customer_details(conn, insert_customer):
    st.title("Please Enter Your Details")

    customer_name = st.text_input("Customer Name")
    contact_number = st.text_input("Contact Number")
    email = st.text_input("Email Address")

    if st.button("Submit"):
        if not customer_name or not contact_number or not email:
            st.error("Please fill in all fields.")
        else:
            # Pass the database connection to insert_customer
            insert_customer(conn, customer_name, contact_number, email)
            st.session_state['page'] = 'choose_restaurant'
            st.experimental_rerun()