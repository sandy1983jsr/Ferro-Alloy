import streamlit as st

from data_ingestion import data_upload_sidebar
from materials_energy_balance import show_materials_energy_balance
from furnace_analytics import show_furnace_analytics
from electrode_optimizer import show_electrode_optimizer
from conveyor_utility import show_conveyor_utility_efficiency
from batch_yield import show_batch_mixing_yield
from anomaly_detection import show_anomaly_detection
from scenario_simulator import show_scenario_simulator
from cost_ghg_dashboard import show_cost_ghg_dashboard
from styles import set_custom_style

def main():
    st.set_page_config(page_title="Ferro Alloy Plant Optimization Dashboard", layout="wide", page_icon=":factory:")
    set_custom_style()

    st.sidebar.header("Data Selection")
    st.sidebar.write("Choose a CSV file to upload or use sample data for analysis.")
    df = data_upload_sidebar()  # File upload/sample data

    st.title("Ferro Alloy Plant Optimization Dashboard")
    st.write(
        "This dashboard provides analytics for energy and materials optimization "
        "at Carbon Resources' ferro alloy plant. Use the tabs below to explore modules."
    )

    if df is None:
        st.info("Please upload a .csv file or use the sample data to continue.")
        return

    # Simple tab arrangement
    tabs = st.tabs([
        "Materials & Energy Balance Engine", 
        "Furnace Analytics & Optimization", 
        "Electrode Paste Optimizer",
        "Conveyor & Utility Efficiency",
        "Batch Mixing & Yield Model", 
        "Anomaly Detection & Alerts",
        "Scenario Simulator", 
        "Cost & GHG Dashboard"
    ])

    with tabs[0]:
        show_materials_energy_balance(df)
    with tabs[1]:
        show_furnace_analytics(df)
    with tabs[2]:
        show_electrode_optimizer(df)
    with tabs[3]:
        show_conveyor_utility_efficiency(df)
    with tabs[4]:
        show_batch_mixing_yield(df)
    with tabs[5]:
        show_anomaly_detection(df)
    with tabs[6]:
        show_scenario_simulator(df)
    with tabs[7]:
        show_cost_ghg_dashboard(df)

if __name__ == "__main__":
    main()
