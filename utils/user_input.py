import streamlit as st
from models import text_descriptions
import pandas as pd
from typing import List


def album_selection(albums:List[str]) -> str:
    st.write(
        text_descriptions.ALBUM_SELECTION, 
        unsafe_allow_html=True
    )
    album:str = st.selectbox(
        "Album name:", 
        albums
        )
    if album != "select":
        msg:str = f"selected album: {album}"
        st.write(
            msg,
            unsafe_allow_html=True
        )
    
    return album
    

def year_selection(years:List[int]):
    selected_year:int = st.selectbox("Year:", years)
    return selected_year