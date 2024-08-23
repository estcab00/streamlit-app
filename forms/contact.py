import streamlit as st

import re
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]
def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

@st.dialog("Contact me")
def show_contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        summit = st.form_submit_button("Submit")

        if summit:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later", icon="warning")
            if not name:
                st.error("Please enter your name.", icon="warning")
            if not last_name:
                st.error("Please enter your last name.", icon= "warning")
            if not email:
                st.error("Please enter your email.", icon=":material-email:")
            if not is_valid_email(email):
                st.error("Please enter a valid email.", icon=":material-email:")
            if not message:
                st.error("Please enter a message.")


            # Prepare the data payload and send it to the webhook

            data = {
                "name": name,
                "last_name": last_name,
                "email": email,
                "message": message
            }
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success(f"Thank you {name} for contacting me. I will get back to you as soon as possible.")
            else:
                st.error("Something went wrong. Please try again later.", icon="warning" )


