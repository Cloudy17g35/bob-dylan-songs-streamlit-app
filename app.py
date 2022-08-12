import streamlit as st
import pandas as pd
from app import s3
from app import text_descriptions
from app import text_preprocessing
from app import data_visualizations
from typing import List
from collections import Counter
from wordcloud import WordCloud
PUBLIC_KEY = 'https://bob-dylan-songs.s3.amazonaws.com/dylan_songs.parquet'
WORDCLOUD_FILENAME = 'wordcloud.png'



def header_and_description():
    st.write(
        text_descriptions.TextDescription.HEADER.value, 
        unsafe_allow_html=True
    )
    st.image(
        text_descriptions.TextDescription.IMAGE.value
        )
    st.write(
        text_descriptions.TextDescription.DESCRIPTION.value, 
        unsafe_allow_html=True
    )


def show_dataset(data_frame:pd.DataFrame):
    st.write(
        text_descriptions.TextDescription.DATASET.value,
        unsafe_allow_html=True
        )
    st.dataframe(data_frame)


def barchart(data_frame=pd.DataFrame):
    fig = data_visualizations.plotly_bar_chart(data_frame)
    st.write(
        text_descriptions.TextDescription.PLOT_SUBHEADER.value,
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
        text_descriptions.TextDescription.ALBUM_SELECTION.value, 
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
        button_label:str = text_descriptions.TextDescription.DOWNLOAD_DATAFRAME.value
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
        text_descriptions.TextDescription.WORDCLOUD_SUBHEADER.value, 
        unsafe_allow_html=True
    )
    st.write(
        text_descriptions.TextDescription.WORDCOUD_DESCRIPTION.value, 
        unsafe_allow_html=True
        )
    
    years = list(data_frame["release_year"].unique())
    selected_year = st.selectbox("Year:", years)
    df_for_one_year = data_frame[data_frame["release_year"] == selected_year]
    tp = text_preprocessing.TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    # wordcloud is saved as image in the background
    wordcloud:WordCloud = data_visualizations.make_wordcloud(lyrics_counter)
    save_wordcloud_to_file(
        wordcloud, 
        text_descriptions.TextDescription.WORDCLOUD_FILENAME.value
        )
    st.image(text_descriptions.TextDescription.WORDCLOUD_FILENAME.value)
    with open(text_descriptions.TextDescription.WORDCLOUD_FILENAME.value, "rb") as file:
        st.download_button(
            label=text_descriptions.TextDescription.DOWLOAD_WORDCLOUD.value,
            data=file,
            file_name=WORDCLOUD_FILENAME,
            mime="image/png",
        )



if __name__ == '__main__':
    header_and_description()
    df:pd.DataFrame = s3.S3Handler.read_from_s3(PUBLIC_KEY)
    show_dataset(df)
    barchart(df)
    album_selection(df)
    wordcloud(df)

