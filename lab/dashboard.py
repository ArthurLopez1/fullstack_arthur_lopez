from pathlib import Path
import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend, DeviceUsage, GenderComparison
from frontend.constants import Color


device_usage = DeviceUsage()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
device_usage_chart = DeviceUsage()
gender_comparison = GenderComparison()


def layout():
    st.markdown("# Youtube Dashboard")
    st.markdown("#### AIgineer")
    content_kpi.display_content()
    
    gender_comparison.display_plot()
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