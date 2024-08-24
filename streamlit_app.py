import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="🏠",
    default=True,
)

project_1_page = st.Page(
    page="views/webscrapper.py",
    title="Web Scrapper",
    icon="💻",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon="💬"
    )   

# --- NAVIGATION ---
pg = st.navigation(
    {
        "Info" : [about_page],
        "Projects" : [project_1_page, project_2_page]
    }
)

# --- RUN NAVIGATION ---
pg.run()

# --- SIDEBAR ---
st.logo("assets/logo.png")
st.sidebar.text("Made by @estebanscabrera")

# pages = [about_page, project_1_page, project_2_page]
