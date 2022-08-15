from wordcloud import WordCloud
import streamlit as st
from collections import Counter


def generate_using_frequencies(frequency: Counter):

    wc: WordCloud = WordCloud(
        min_font_size=10,
        max_font_size=60,
        width=800,
        height=500,
        random_state=1,
        colormap="rainbow",
        collocations=False,
    ).generate_from_frequencies(frequency)
    return wc


def save_to_file(
    wordcloud:WordCloud,
    filename:str
    ) -> None:
    
    wordcloud.to_file(filename)
    

def show(path_to_image:str):
    st.image(path_to_image)