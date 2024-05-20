import streamlit as st

def choose_restaurant(restaurants):
    st.title("Choose a Restaurant")
    selected_restaurant = st.selectbox("Select a Restaurant", restaurants)

    if st.button("Next"):
        st.session_state['selected_restaurant'] = selected_restaurant
        st.session_state['page'] = 'restaurant_menu'
        st.experimental_rerun()

def restaurant_menu():
    st.title(f"Menu for {st.session_state['selected_restaurant']}")
    # You can add more logic here to display the menu items for the selected restaurant
