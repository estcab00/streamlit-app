import time

import streamlit as st

def response_generator():
    for word in response.split():
        yield word + " "
        time.sleep(0.5)