import streamlit as st
from views.scrappers import scraper_buscalibre

st.title("Webscrapper")

# Three columns
col1, col2, col3 = st.columns(3)

# Different subwindows
with col1:
    if st.button("Buscalibre"):
        st.session_state.current_view = "Buscalibre"
with col2:
    if st.button("Mostrar Subventana 2"):
        st.session_state.current_view = "Subventana 2"
with col3:
    if st.button("Mostrar Subventana 3"):
        st.session_state.current_view = "Subventana 3"

# Mostrar la vista seleccionada
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Buscalibre"  # Vista por defecto

# Buscalibre
if st.session_state.current_view == "Buscalibre":
    st.subheader("Webscrapping Buscalibre")

    user_input = st.text_input("What topic/author are you interested in?")

    if user_input:
        # Llamar a la función que realiza el scraping
        scraper_buscalibre(user_input)

elif st.session_state.current_view == "Subventana 2":
    st.subheader("Esta es la Subventana 2")
    st.write("Contenido de la Subventana 2")
elif st.session_state.current_view == "Subventana 3":
    st.subheader("Esta es la Subventana 3")
    st.write("Contenido de la Subventana 3")
