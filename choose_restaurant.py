import streamlit as st
import os
from streamlit_option_menu import option_menu

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

    if selected=='La Trattoria':
        if st.button("Next"):
            st.session_state['selected_restaurant'] = selected
            st.session_state['page'] = 'restaurant_menu'
            st.rerun()

def restaurant_menu():
    st.title(f"Menu for {st.session_state['selected_restaurant']}")