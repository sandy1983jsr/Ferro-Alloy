import streamlit as st
import pandas as pd

def data_upload_sidebar():
    st.sidebar.title("Data Upload & Settings")
    data_source = st.sidebar.radio("Select Data Source", ("Upload CSV", "Use Sample Data"))
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data", type=["csv"]) if data_source == "Upload CSV" else None

    if data_source == "Use Sample Data":
        # Updated sample data
        dates = pd.date_range(start='2025-01-01', periods=30, freq='D')
        df = pd.DataFrame({
            'Date': dates,
            'Manganese_Ore_kg': 10000 + 500 * pd.np.random.randn(len(dates)),
            'Slag_Ferro_Manganese_kg': 1200 + 100 * pd.np.random.randn(len(dates)),
            'Remelts_kg': 300 + 50 * pd.np.random.randn(len(dates)),
            'Coal_kg': 5000 + 300 * pd.np.random.randn(len(dates)),
            'Coke_kg': 2000 + 150 * pd.np.random.randn(len(dates)),
            'Dolomite_kg': 800 + 60 * pd.np.random.randn(len(dates)),
            'Quartz_kg': 400 + 30 * pd.np.random.randn(len(dates)),
            'Quartzite_kg': 200 + 20 * pd.np.random.randn(len(dates)),
            'HC_Low_Boron_kg': 3500 + 200 * pd.np.random.randn(len(dates)),
            'SiMn_HC_kg': 2000 + 100 * pd.np.random.randn(len(dates)),
            'SiMn_MC_kg': 1500 + 80 * pd.np.random.randn(len(dates)),
            'SiMn_LC_kg': 1000 + 60 * pd.np.random.randn(len(dates)),
            'SiMn_ELC_kg': 700 + 40 * pd.np.random.randn(len(dates)),
            'Electricity_Consumed_kWh': 4000 + 250 * pd.np.random.randn(len(dates)),
        })
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
