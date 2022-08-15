from models import text_descriptions
import streamlit as st


def show():
    st.write(
        text_descriptions.HEADER,
        unsafe_allow_html=True
    )
    st.image(
        text_descriptions.IMAGE
        )
    st.write(
        text_descriptions.DESCRIPTION, 
        unsafe_allow_html=True
    )