import streamlit as st
import pandas as pd
from models import text_descriptions
from typing import List


def show(data_frame:pd.DataFrame) -> None:
    st.dataframe(data_frame)
    

def to_csv(
    data_frame:pd.DataFrame, 
    encoding='utf8'
    ) -> str:
    
    return data_frame.to_csv(
        encoding=encoding
        )


def filter_by_album(
    data_frame:pd.DataFrame, 
    album:str
    ) -> pd.DataFrame:
    selected_df:pd.DataFrame = data_frame[data_frame["album"] == album]
    return selected_df


def get_albums(data_frame:pd.DataFrame) -> List[str]:
    return ['select'] + list(data_frame['album'].unique())


def get_csv_filename_for_selected_album(album:str):
    return f'songs_from_album_{"_".join(album.lower().split())}.csv'

# TODO - change this function to be more universal
def get_unique_years(data_frame:pd.DataFrame):
    return list(data_frame["release_year"].unique())

def filter_by_year(
    data_frame:pd.DataFrame, 
    year:str
    ) -> pd.DataFrame:
    selected_df:pd.DataFrame = data_frame[data_frame["release_year"] == year]
    return selected_df