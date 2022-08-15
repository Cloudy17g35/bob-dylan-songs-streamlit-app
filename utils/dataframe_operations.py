import streamlit as st
import pandas as pd
from typing import List


@st.cache
def read_from_s3(s3_url:str) -> pd.DataFrame:
        """
        uses s3 url for instance:
        s3://bob-dylan-songs/dylan_songs.parquet
        """
        return pd.read_parquet(s3_url)


def show(data_frame:pd.DataFrame) -> None:
    st.dataframe(data_frame)
    

def to_csv(
    data_frame:pd.DataFrame, 
    encoding='utf8'
    ) -> str:
    
    return data_frame.to_csv(
        encoding=encoding
        )


def filter_dataframe_by_user_selection(
    data_frame:pd.DataFrame, 
    column,
    user_selection:str,
    ) -> pd.DataFrame:
    
    selected_df:pd.DataFrame = data_frame[data_frame[column] == user_selection]
    return selected_df


def get_unique_values_from_column(data_frame:pd.DataFrame, column:str) -> List[str]:
    return list(data_frame[column].unique())


def get_csv_filename_for_selected_album(album:str):
    return f'songs_from_album_{"_".join(album.lower().split())}.csv'

