import streamlit as st
import pandas as pd
from send_email import send_email


st.set_page_config(layout="wide")

st.header("Contact Me")

df = pd.read_csv("topics.csv")

with st.form(key="contact_form"):
    user_email = st.text_input('Your Email Address')
    topic = st.selectbox(label="What topics do you want to discuss?", options=df)
    raw_message = st.text_area("Message")
    message = f"""\
Subject: New email from Portfolio App | {user_email}

From: {user_email}

Topic: {topic}
{raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("the button successfully was pressed")
        send_email(message)
        st.info("Your email was successfully sent!")
