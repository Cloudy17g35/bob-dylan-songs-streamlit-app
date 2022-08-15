import streamlit as st
import pandas as pd
from typing import List
from collections import Counter
from wordcloud import WordCloud
from utils import tokenization
from utils import header_and_description
from utils import charts
from utils import dataframe_operations
from utils import user_input
from utils import wordclouds
from utils import charts
from models import text_descriptions
import settings


if __name__ == '__main__':
    header_and_description.show()
    
    df:pd.DataFrame = dataframe_operations.read_from_s3(settings.PUBLIC_KEY)
    
    st.write(
        text_descriptions.DATASET, 
        unsafe_allow_html=True
        )
    
    dataframe_operations.show(df)
    
    charts.show_release_year_distribution(df)
    
    albums:List[str] = dataframe_operations.get_unique_values_from_column(
        data_frame=df,
        column='album'
    )
    
    selected_album:str = user_input.album_selection(albums)
    
    if selected_album != 'select':
        df_filtered_by_album:pd.DataFrame  = dataframe_operations.filter_dataframe_by_user_selection(
            data_frame=df,
            column='album',
            user_selection=selected_album
        )
        
        dataframe_operations.show(df_filtered_by_album)
        
        csv_data:str = dataframe_operations.to_csv(df)
        
        file_name_for_download:str = dataframe_operations.get_csv_filename_for_selected_album(selected_album)
        
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
    
    years:List[int] = dataframe_operations.get_unique_values_from_column(
        data_frame=df,
        column='release_year'
    )
    
    selected_year:int = user_input.year_selection(years)
    df_for_one_year:pd.DataFrame = dataframe_operations.filter_dataframe_by_user_selection(
        data_frame=df,
        column='release_year',
        user_selection=selected_year
    )
    
    tp = tokenization.TextPreprocessing()
    lyrics: list = tp.clean_lyrics(df_for_one_year)
    lyrics_counter: Counter = tp.get_counter(lyrics)
    wordcloud_for_particular_year:WordCloud = wordclouds.generate_using_frequencies(
        lyrics_counter
        )
    
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
    

