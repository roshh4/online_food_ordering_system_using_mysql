import MySQLdb
import streamlit as st

#function to display bill
def display_bill(connection, cart_id):
    try:
        cursor = connection.cursor()

        # Fetching all rows from the bill table for the specified cart_id
        query = """
            SELECT bill_id, cart_id, final_amount, cgst, sgst, service_charge, total_quantity 
            FROM bill 
            WHERE cart_id = %s
        """
        cursor.execute(query, (cart_id,))
        bills = cursor.fetchall()

        st.title("Bill Details")

        if bills:
            # Displaying the bill details
            for bill in bills:
                st.write(f"Bill ID: {bill[0]}")
                st.write(f"Cart ID: {bill[1]}")
                st.write(f"Total Amount: {bill[2]}")
                st.write(f"CGST: {bill[3]}")
                st.write(f"SGST: {bill[4]}")
                st.write(f"Service Charge: {bill[5]}")
                st.write("---")
        else:
            st.write("No bills found.")

        if st.button("Back"):
            st.session_state['page'] = 'display_cart_details'
            st.rerun()

    except MySQLdb.Error as e:
        st.error(f"Error retrieving bill details: {e}")