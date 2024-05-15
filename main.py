import streamlit as st
from streamlit.components.v1 import html
with st.container():
    html('''
    <script>
        var decoration = window.parent.document.querySelectorAll('[data-testid="stDecoration"]')[0];
        decoration.style.right = "90px";
        decoration.style.height = "40px";
        decoration.innerText = "REC FOOD DELIVERY APP";
        decoration.style.fontWeight = "bold";
         decoration.style.display = "flex";
        decoration.style.justifyContent = "center";
        decoration.style.alignItems = "center";
    </script>
    ''')