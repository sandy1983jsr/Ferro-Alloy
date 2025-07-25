import streamlit as st
import pandas as pd
from utils import generate_sample_data

def data_upload_sidebar():
    st.sidebar.title("Data Upload & Settings")
    data_source = st.sidebar.radio("Select Data Source", ("Upload CSV", "Use Sample Data"))
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data", type=["csv"]) if data_source == "Upload CSV" else None

    if data_source == "Use Sample Data":
        df = generate_sample_data()
    else:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, parse_dates=['Date'])
        else:
            df = None

    st.sidebar.markdown("---")
    st.sidebar.write("**Dashboard Theme:**")
    st.sidebar.color_picker("Primary Orange", "#f95d1d", disabled=True)
    st.sidebar.color_picker("Secondary Grey", "#cccccc", disabled=True)
    st.sidebar.color_picker("Background White", "#ffffff", disabled=True)
    st.sidebar.markdown("---")
    st.sidebar.info("This dashboard is powered by data-driven engineering, scientific, and digital analytics.")
    return df
