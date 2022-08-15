import plotly.express as px
import pandas as pd
import streamlit as st


def show_release_year_distribution(data_frame: pd.DataFrame) -> None:
    
    count_values: pd.Series = data_frame["release_year"].value_counts().sort_index()
    
    fig = px.bar(x=count_values.index, y=count_values.values)

    fig.update_layout(
        font=dict(family="Lato", size=18, color="white"),
        title=dict(
            text="<b>Bob Dylan songs in years 1961- 2020<b>", 
            font=dict(size=30), x=0.5
        ),
        paper_bgcolor="black",
        plot_bgcolor="black",
        xaxis=dict(title="Year of release", showgrid=False),
        yaxis=dict(title="Number of songs", showgrid=False),
    )

    st.plotly_chart(fig)