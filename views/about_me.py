import streamlit as st
from forms.contact import show_contact_form

@st.dialog("Contact me")
def show_contact_dialog():
    show_contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/esteban.jpg", width=200)
with col2:
    st.title("Esteban Cabrera", anchor=False)
    st.subheader("Economist and Data Scientist")
    st.write(
        "Junior Data Scientist and Research Assistant at PUCP"
    )
    if st.button("✉ Contact me"):
        show_contact_form()

# --- ABOUT ME ---
st.write("\n")
st.subheader("About me")
st.write(
    """
    I am a senior Economics ranking in the top 2\% of my faculty. I am very concerned on topics such as inequality and poverty. 
    For this reason, throughtout my life, I have participated in various volunteering activities, regarding different Sustainable Development Goals (SGDs). 
    I have experience in data analysis, machine learning, and econometrics. I'm passionate about using data to solve complex problems and make informed decisions.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Skills")
st.write(
    """
    - **Programming languages:** Python, R, SQL
    - **Data analysis tools:** Pandas, NumPy, Matplotlib, Seaborn
    - **Machine learning libraries:** Scikit-learn, TensorFlow, Keras
    - **Web development:** HTML, CSS, Streamlit
    - **Version control:** Git, GitHub
    """
)