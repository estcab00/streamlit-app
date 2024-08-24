import streamlit as st
import base64
from forms.contact import show_contact_form

@st.dialog("Contact me")
def show_contact_dialog():
    show_contact_form()

# --- SOCIAL ICONS ---
social_icons_data = {
    # Platform: [URL, Icon]
    "LinkedIn": ["https://www.linkedin.com/in/esteban-cabrera-bonilla/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
    "GitHub": ["https://github.com/estcab00", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
    "Twitter": ["https://x.com/estebanscabrera", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
}

social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}' style='width: 40px; height: 40px;'></a>" for platform in social_icons_data]


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/esteban.jpg", width=250)
with col2:
    st.title("Esteban Cabrera", anchor=False)
    st.subheader("Economist and Data Scientist")
    st.write(
        "Junior Data Scientist and Research Assistant at PUCP"
    )
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)
    
# PDF CV file
with open("assets/CV_Esteban_Cabrera.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

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

# --- DOWNLOAD CV ---
if st.button("✉ Contact me"):
   show_contact_form()

# Download CV button
st.download_button(
    label="📄 Download my CV",
    data=pdf_bytes,
    file_name="CV_Esteban_Cabrera.pdf",
    mime="application/pdf",
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

# --- EDUCATION ---
st.write("\n")
st.subheader("Education")
st.write(
    """
    - **Bachelor's degree in Economics** - Pontifical Catholic University of Peru (PUCP)
    - **Winter School of Economics** - University of Chile
    """
)

# --- EXPERIENCE ---
st.write("\n")
st.subheader("Experience")
st.write(
    """
    - **Junior Data Scientist and Research Assistant** - PUCP
    - **Economic Research Assistant** - CIUP
    - **Risk Analyst Intern** - BCP
    """
)

# --- PROJECTS ---
st.write("\n")
st.subheader("Projects")
st.write(
    """
    - **Webscrapper:** A webscrapper of prices of different webpages.
    - **Chatbot:** A chatbot that answers questions about economic and social issues in Peru.
    """
)
