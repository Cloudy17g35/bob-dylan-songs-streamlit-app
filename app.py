import streamlit as st
import pandas as pd
from src import data_visualizations, s3
from src import tokenization
from models import text_descriptions
from typing import List
from collections import Counter
from wordcloud import WordCloud
import settings
from utils import header_and_description
from utils import charts
from utils import dataframe
from utils import user_input
from utils import wordclouds


def wordcloud(data_frame=pd.DataFrame):
    tp = tokenization.TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    # wordcloud is saved as image in the background
    


if __name__ == '__main__':
    header_and_description.show()
    df:pd.DataFrame = s3.S3Handler.read_from_s3(settings.PUBLIC_KEY)
    dataframe.show(df)
    st.write(text_descriptions.DATASET, unsafe_allow_html=True)
    charts.barchart(df)
    albums:List[str] = dataframe.get_albums(df)
    selected_album:str = user_input.album_selection(albums)
    df_filtered_by_album:pd.DataFrame  = dataframe.filter_by_album(df, selected_album)
    dataframe.show(df_filtered_by_album)
    csv_data:str = dataframe.to_csv(df)
    file_name_for_download:str = dataframe.get_csv_filename_for_selected_album(selected_album)
    button_label:str = text_descriptions.DOWNLOAD_DATAFRAME
    st.download_button(
            label=button_label,
            data=csv_data,
            file_name=file_name_for_download,
            mime="text/csv",
        )
    st.write(
        text_descriptions.WORDCLOUD_SUBHEADER, 
        unsafe_allow_html=True
    )
    st.write(
        text_descriptions.WORDCOUD_DESCRIPTION, 
        unsafe_allow_html=True
        )
    years:List[int] = dataframe.get_unique_years(df)
    selected_year:int = user_input.year_selection(years)
    df_for_one_year:pd.DataFrame = dataframe.filter_by_year(df, selected_year)
    tp = tokenization.TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    wordcloud_for_particular_year:WordCloud = data_visualizations.wordcloud(lyrics_counter)
    wordcloud_filename:str = settings.WORDCLOUD_FILENAME
    wordclouds.save_to_file(
        wordcloud_for_particular_year, 
        wordcloud_filename
        )
    wordclouds.show(wordcloud_filename)
    with open(settings.WORDCLOUD_FILENAME.encode(), "rb") as file:
        st.download_button(
            label=text_descriptions.DOWLOAD_WORDCLOUD,
            data=file,
            file_name=wordcloud_filename,
            mime="image/png",
        )
    

