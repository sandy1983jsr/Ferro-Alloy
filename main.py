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
    df = data_upload_sidebar()

    st.title("Ferro Alloy Plant Optimization Dashboard")
    st.write(
        "This dashboard provides analytics for energy and materials optimization "
        "at Carbon Resources' ferro alloy plant. Use the module selector below to explore modules."
    )

    if df is None:
        st.info("Please upload a .csv file or use the sample data to continue.")
        return

    menu_options = [
        "Materials & Energy Balance Engine", 
        "Furnace Analytics & Optimization", 
        "Electrode Paste Optimizer",
        "Conveyor & Utility Efficiency",
        "Batch Mixing & Yield Model", 
        "Anomaly Detection & Alerts",
        "Scenario Simulator", 
        "Cost & GHG Dashboard"
    ]

    # Use a selectbox for navigation (acts like a dropdown menu)
    selected_tab = st.selectbox("Select a module:", menu_options, index=0)

    # Show content based on selection
    if selected_tab == "Materials & Energy Balance Engine":
        show_materials_energy_balance(df)
    elif selected_tab == "Furnace Analytics & Optimization":
        show_furnace_analytics(df)
    elif selected_tab == "Electrode Paste Optimizer":
        show_electrode_optimizer(df)
    elif selected_tab == "Conveyor & Utility Efficiency":
        show_conveyor_utility_efficiency(df)
    elif selected_tab == "Batch Mixing & Yield Model":
        show_batch_mixing_yield(df)
    elif selected_tab == "Anomaly Detection & Alerts":
        show_anomaly_detection(df)
    elif selected_tab == "Scenario Simulator":
        show_scenario_simulator(df)
    elif selected_tab == "Cost & GHG Dashboard":
        show_cost_ghg_dashboard(df)

if __name__ == "__main__":
    main()
