from wordcloud import WordCloud
import streamlit as st


def save_to_file(
    wordcloud:WordCloud,
    filename:str
    ) -> None:
    
    wordcloud.to_file(filename)
    

def show(path_to_image:str):
    st.image(path_to_image)