from utils.query_database import QueryDatabase
import plotly.express as px
from plotly.colors import sample_colorscale
import streamlit as st 
import pandas as pd
from frontend.constants import Color

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar", labels={"Datum": "Date", "Visningar": "Views"})
        fig.update_traces(line=dict(color=Color.RED1))
        st.markdown("### Number of views in the past month")
        st.plotly_chart(fig)

class DeviceUsage:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_summary").df
        self.df = self.df[self.df['Enhetstyp'].str.lower() != 'totalt']
        print(self.df)

    def display_plot(self):
        fig = px.pie(self.df, names='Enhetstyp', values='Visningar', 
                     title="Percentual Device Distribution")
        st.markdown("### Device Usage Pie Chart")
        
        num_devices = len(self.df['Enhetstyp'])
        color_gradient = sample_colorscale(
            colorscale=[[0, Color.RED1], [1, Color.RED5]],
            samplepoints=num_devices
        )

        fig.update_traces(marker=dict(colors=color_gradient))
        
        st.plotly_chart(fig)

class GenderComparison:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.gender_distribution").df

    def display_plot(self):
        fig = px.bar(self.df, x="Tittarnas kön", y=["Visningar (%)", "Visningstid (timmar) (%)"], 
                     barmode="group", title="Gender Comparison: Views vs Watch Time")
        st.plotly_chart(fig)
