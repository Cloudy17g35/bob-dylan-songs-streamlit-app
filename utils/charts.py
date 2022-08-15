from src import data_visualizations
import streamlit as st
from models import text_descriptions
import pandas as pd


def barchart(data_frame=pd.DataFrame):
    fig = data_visualizations.plotly_bar_chart(data_frame)
    st.write(
        text_descriptions.PLOT_SUBHEADER,
        unsafe_allow_html=True
        )
    st.plotly_chart(fig)