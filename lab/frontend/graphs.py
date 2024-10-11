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
        fig = px.line(self.df, x="Datum", y="Visningar", labels={"Datum": "Date", "Visningar": "Views"}, title="Number of views in the past month")
        fig.update_traces(line=dict(color=Color.RED1))
        #st.markdown("### Number of views in the past month")
        st.plotly_chart(fig)

    
class DeviceUsage:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_summary").df
        self.df = self.df[self.df['Enhetstyp'].str.lower() != 'total']
        print(self.df)

    def display_plot(self):
        fig = px.pie(self.df, names='Enhetstyp', values='Visningar', 
                     title="Percentual Device Distribution")
        #st.markdown("### Device Usage Pie Chart")
        
        num_devices = len(self.df['Enhetstyp'])
        color_gradient = sample_colorscale(
            colorscale=[[0, Color.RED1], [1, Color.RED6]],
            samplepoints=num_devices
        )

        fig.update_traces(marker=dict(colors=color_gradient))
        
        st.plotly_chart(fig)

class GenderComparison:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.gender_distribution").df

    def display_plot(self):
        
        colors = [Color.RED1, Color.RED4]
        
        fig = px.bar(
            self.df,
            x="Viewer's gender",  
            y=["Views (%)", "Display time (hours) (%)"], 
            barmode="group",
            title="Gender Comparison: Views vs Watch Time",
            color_discrete_sequence=colors
        )
        st.plotly_chart(fig)

class CountryDistribution:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.country_views_summary").df
        
    def display_plot(self):
        #st.markdown("### Demographics")

        fig = px.bar(
            self.df,
            x='Country',
            y=['Total_Views', 'Total_Watch_Time_Hours'],
            barmode='group',
            title="Views and Watch Time by Country",
            labels={'Total_Views': 'Total Views', 'Total_Watch_Time_Hours': 'Total Watch Time (Hours)'},
            color_discrete_sequence=[Color.RED4, Color.RED1]
        )

        fig.update_layout(
            xaxis_title="Country",
            yaxis_title="Count",
            legend_title="Metrics",
            template="plotly_white"
        )

        st.plotly_chart(fig)