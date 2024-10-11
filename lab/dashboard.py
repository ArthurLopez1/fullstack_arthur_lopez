from pathlib import Path
import streamlit as st
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend, DeviceUsage, GenderComparison, CountryDistribution
from frontend.constants import Color


device_usage = DeviceUsage()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
device_usage_chart = DeviceUsage()
gender_comparison = GenderComparison()
country_distribution = CountryDistribution()

def layout():
    st.set_page_config(layout="wide")
    st.markdown(
        f'<h1><span style="color:{Color.RED4};">Youtube</span><span style="color:{Color.PRIMARY};"> Channel Performance</span></h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h2><span style="color:{Color.RED4};">AI</span><span style="color:{Color.PRIMARY};">gineer</span></h2>',
        unsafe_allow_html=True,
    )
    
    col1, col2, col3 = st.columns([1, 1.3, 1]) 

    with col1:
        gender_comparison.display_plot()
        country_distribution.display_plot()

    with col2:
        content_kpi.display_content()

    with col3:
        device_usage_chart.display_plot()
        views_graph.display_plot()

    
    read_css()


def read_css():
    css_path = Path(__file__).parent / "frontend" / "style.css"

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    layout()
