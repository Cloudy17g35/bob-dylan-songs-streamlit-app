import streamlit as st
import pandas as pd
from s3 import S3Handler
from text_descriptions import TextDescription
from text_preprocessing import TextPreprocessing
from data_visualizations import plotly_bar_chart, make_wordcloud
from typing import List
from collections import Counter
from wordcloud import WordCloud
PUBLIC_KEY = 's3://bob-dylan-songs/dylan_songs.parquet'
WORDCLOUD_FILENAME = 'wordcloud.png'


def header_and_description():
    st.write(
        TextDescription.HEADER.value, 
        unsafe_allow_html=True
    )
    st.image(TextDescription.PICTURE.value)
    st.write(
        TextDescription.DESCRIPTION.value, 
        unsafe_allow_html=True
    )


def show_dataset(data_frame:pd.DataFrame):
    st.write(TextDescription.DATASET.value,
             unsafe_allow_html=True)
    st.dataframe(data_frame)


def barchart(data_frame=pd.DataFrame):
    fig = plotly_bar_chart(data_frame)
    st.write(
        TextDescription.PLOT_SUBHEADER.value,
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
        TextDescription.ALBUM_SELECTION.value, 
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
        button_label:str = TextDescription.DOWNLOAD_DATAFRAME.value
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
        TextDescription.WORDCLOUD_SUBHEADER.value, 
        unsafe_allow_html=True
    )
    st.write(
        TextDescription.WORDCOUD_DESCRIPTION.value, 
        unsafe_allow_html=True
        )
    
    years = list(data_frame["release_year"].unique())
    selected_year = st.selectbox("Year:", years)
    df_for_one_year = data_frame[data_frame["release_year"] == selected_year]
    tp:TextPreprocessing = TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    # wordcloud is saved as image in the background
    wordcloud:WordCloud = make_wordcloud(lyrics_counter)
    save_wordcloud_to_file(wordcloud, WORDCLOUD_FILENAME)
    st.image(WORDCLOUD_FILENAME)
    with open(WORDCLOUD_FILENAME, "rb") as file:
        st.download_button(
            label=TextDescription.DOWLOAD_WORDCLOUD.value,
            data=file,
            file_name=WORDCLOUD_FILENAME,
            mime="image/png",
        )



if __name__ == '__main__':
    header_and_description()
    df:pd.DataFrame = S3Handler.read_from_s3(PUBLIC_KEY)
    show_dataset(df)
    barchart(df)
    album_selection(df)
    wordcloud(df)

