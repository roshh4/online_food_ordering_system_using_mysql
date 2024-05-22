import streamlit as st
from connection import conn
import MySQLdb
import os
from streamlit_option_menu import option_menu

def get_menu():
    items = []
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT item_name, images FROM menu_items")
            rows = cursor.fetchall()
            items = [(row[0], row[1]) for row in rows]
    except MySQLdb.Error as e:
        st.error(f"Error retrieving item names: {e}")
    return items

def choose_restaurant(restaurants):
    with st.sidebar:
        selected = option_menu("Restuarants", ["La Trattoria", "Sushi World","Taco Fiesta","Burger Haven","Dosa Delight"], icons=['house','house','house','house','house'], menu_icon="houses", default_index=0)
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

    #items = get_menu()
    #image_path = None
    #for row in items:
    #    if row[0] == selected:
    #        image_path = row[1]
    #        break

    #if selected=='La Trattoria':
    #    st.image(image_path, caption=f"Image of {selected}", use_column_width=True)

    if st.button("Next"):
        st.session_state['selected_restaurant'] = selected
        st.session_state['page'] = 'restaurant_menu'
        st.rerun()

def restaurant_menu():
    st.title(f"Menu for {st.session_state['selected_restaurant']}")