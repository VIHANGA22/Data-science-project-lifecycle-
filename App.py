import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)
df = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')
