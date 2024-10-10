from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
import pandas as pd

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

class DeviceUsage:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_summary").df
        self.df = self.df[self.df['Enhetstyp'].str.lower() != 'totalt']
        print(self.df)

    def display_plot(self):
        fig = px.pie(self.df, names='Enhetstyp', values='Visningar', 
                     title="Device Distribution by Views")
        st.markdown("## Device Usage Pie Chart")
        st.plotly_chart(fig)

class GenderComparison:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.gender_distribution").df

    def display_plot(self):
        fig = px.bar(self.df, x="Tittarnas kön", y=["Visningar (%)", "Visningstid (timmar) (%)"], 
                     barmode="group", title="Gender Comparison: Views vs Watch Time")
        st.plotly_chart(fig)
