import streamlit as st
import numpy as np

def show_anomaly_detection(df):
    st.subheader("Anomaly Detection and Alerts")
    st.write("SPC (Statistical Process Control) for scientific anomaly detection.")

    # SPC: flag points outside 3σ
    mean = df['Furnace_Efficiency_%'].mean()
    std = df['Furnace_Efficiency_%'].std()
    df['SPC_Flag'] = (np.abs(df['Furnace_Efficiency_%'] - mean) > 3 * std).astype(int)
    anomaly_df = df[df['SPC_Flag'] == 1]

    st.write(f"SPC-based anomalies detected: {anomaly_df.shape[0]}")
    if not anomaly_df.empty:
        st.dataframe(anomaly_df[['Date', 'Furnace_Temperature_C', 'Furnace_Efficiency_%', 'Electrode_Wear_mm']])
    else:
        st.success("No SPC anomalies detected.")
