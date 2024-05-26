import MySQLdb
import streamlit as st

#function to display bill
def display_bill(connection, cart_id):
    try:
        cursor = connection.cursor()

        #
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
                st.write(f"quantity: {bill[6]}")
                st.write("---")

            query = "SELECT item_id, quantity, total_price FROM cart_items WHERE cart_id = %s"
            cursor.execute(query, (cart_id,))
            cart_items = cursor.fetchall()
            for item in cart_items:
                query = "SELECT item_name FROM menu_items WHERE item_id = %s"
                cursor.execute(query, (item[0],))
                name = cursor.fetchone()
                st.write(f"item name : {name}")
                st.write(f"quantity: {item[1]}")
                st.write(f"Total price: {item[2]}")

        else:
            st.write("No bills found.")

        if st.button("Back"):
            st.session_state['page'] = 'display_cart_details'
            st.rerun()

    except MySQLdb.Error as e:
        st.error(f"Error retrieving bill details: {e}")