from setuptools import setup
from setuptools import find_packages

print(find_packages(exclude= ("test*", "explorations")))

setup(
    name = "travel_planner",
    version="1.0.0",
    description="""
    This package is used for public transport travel planning in Sweden.
    It contains backend, frontend and util code.""",
    authour= "Arthur Lopez",
    author_email= "arthur@email.com",
    install_requires= ["pandas", "streamlit", "requests", "folium"],
    packages = find_packages(exclude=["test*", "explorations"])
)
