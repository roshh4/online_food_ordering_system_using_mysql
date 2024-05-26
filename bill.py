import MySQLdb
import streamlit as st

def display_bill(connection, cart_id):
    try:
        cursor = connection.cursor()

        # Fetching all rows from the bill table for the specified cart_id
        query = "SELECT * FROM bill WHERE cart_id = %s"
        cursor.execute(query, (cart_id,))
        bills = cursor.fetchall()

        st.title("Bill Details")

        if bills:
            # Displaying the bill details
            for bill in bills:
                st.write(f"Bill ID: {bill[0]}")
                st.write(f"Cart ID: {bill[1]}")
                st.write(f"Total Amount: {bill[2]}")
                st.write(f"Bill Date: {bill[3]}")
                st.write("---")
        else:
            st.write("No bills found.")

        # Back button to navigate to the previous page
        if st.button("Back"):
            st.session_state['page'] = 'display_cart_details'
            st.rerun()

    except MySQLdb.Error as e:
        st.error(f"Error retrieving bill details: {e}")
