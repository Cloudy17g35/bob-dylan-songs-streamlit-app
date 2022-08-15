import streamlit as st
import pandas as pd
from src import s3
from models import text_descriptions
from src import tokenization
from src import data_visualizations
from typing import List
from collections import Counter
from wordcloud import WordCloud
import settings


def header_and_description():
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


def show_dataset(data_frame:pd.DataFrame):
    st.write(
        text_descriptions.DATASET,
        unsafe_allow_html=True
        )
    st.dataframe(data_frame)


def barchart(data_frame=pd.DataFrame):
    fig = data_visualizations.plotly_bar_chart(data_frame)
    st.write(
        text_descriptions.PLOT_SUBHEADER,
        unsafe_allow_html=True
        )
    st.plotly_chart(fig)


def get_options(data_frame:pd.DataFrame) -> List[str]:
    return ['select'] + list(data_frame['album'].unique())


def get_filename_for_selected_option(option:str):
    return f'songs_from_album_{"_".join(option.lower().split())}.csv'


def save_dataframe_to_csv(
    data_frame:pd.DataFrame, 
    encoding='utf8') -> str:
    
    return data_frame.to_csv(
        encoding=encoding
        )
    
    

def album_selection(data_frame: pd.DataFrame):
    st.write(
        text_descriptions.ALBUM_SELECTION, 
        unsafe_allow_html=True
    )
    options: List[str] = get_options(data_frame)
    option = st.selectbox("Album name:", options)
    if option != "select":
        selected_option:str = f"selected album: {option}"
        st.write(
            selected_option,
            unsafe_allow_html=True
        )
        selected_df = data_frame[data_frame["album"] == option]
        st.dataframe(selected_df)
        csv_data:str = save_dataframe_to_csv(selected_df)
        file_name_for_download:str = get_filename_for_selected_option(option)
        button_label:str = text_descriptions.DOWNLOAD_DATAFRAME
        st.download_button(
            label=button_label,
            data=csv_data,
            file_name=file_name_for_download,
            mime="text/csv",
        )


def save_wordcloud_to_file(
    wordcloud:WordCloud,
    filename:str
    ):
    
    wordcloud.to_file(filename)
    


def wordcloud(data_frame=pd.DataFrame):
    
    st.write(
        text_descriptions.WORDCLOUD_SUBHEADER, 
        unsafe_allow_html=True
    )
    st.write(
        text_descriptions.WORDCOUD_DESCRIPTION, 
        unsafe_allow_html=True
        )
    
    years = list(data_frame["release_year"].unique())
    selected_year = st.selectbox("Year:", years)
    df_for_one_year = data_frame[data_frame["release_year"] == selected_year]
    tp = tokenization.TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    # wordcloud is saved as image in the background
    wordcloud:WordCloud = data_visualizations.make_wordcloud(lyrics_counter)
    save_wordcloud_to_file(
        wordcloud, 
        settings.WORDCLOUD_FILENAME
        )
    st.image(settings.WORDCLOUD_FILENAME)
    with open(settings.WORDCLOUD_FILENAME.encode(), "rb") as file:
        st.download_button(
            label=text_descriptions.DOWLOAD_WORDCLOUD,
            data=file,
            file_name=settings.WORDCLOUD_FILENAME,
            mime="image/png",
        )



if __name__ == '__main__':
    header_and_description()
    df:pd.DataFrame = s3.S3Handler.read_from_s3(settings.PUBLIC_KEY)
    show_dataset(df)
    barchart(df)
    album_selection(df)
    wordcloud(df)

