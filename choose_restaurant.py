import streamlit as st
import os

def choose_restaurant(restaurants):
    st.title("Choose a Restaurant")

    restaurant_names = [row[0] for row in restaurants]
    selected_restaurant = st.selectbox("Select a Restaurant", restaurant_names)

    # Find the selected restaurant's image path
    image_path = None
    for row in restaurants:
        if row[0] == selected_restaurant:
            image_path = row[1]
            break

    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"Image of {selected_restaurant}", use_column_width=True)
    else:
        st.error(f"Image not found for {selected_restaurant}")

    if st.button("Next"):
        st.session_state['selected_restaurant'] = selected_restaurant
        st.session_state['page'] = 'restaurant_menu'
        st.rerun()

def restaurant_menu():
    st.title(f"Menu for {st.session_state['selected_restaurant']}")
    # You can add more logic here to display the menu items for the selected restaurant
