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
    df = data_upload_sidebar()
    if df is None:
        st.warning("Please upload a .csv file or use the sample data to continue.")
        return

    st.title("Ferro Alloy Plant Optimization Dashboard")
    st.write(
        "This dashboard provides a comprehensive suite of analytics for energy and materials optimization "
        "at Carbon Resources' ferro alloy plant. Use the tabs below to explore different modules and optimization opportunities."
    )

    tab_row1 = [
        "Materials & Energy Balance Engine", "Furnace Analytics & Optimization", "Electrode Paste Optimizer", "Conveyor & Utility Efficiency"
    ]
    tab_row2 = [
        "Batch Mixing & Yield Model", "Anomaly Detection & Alerts", "Scenario Simulator", "Cost & GHG Dashboard"
    ]

    st.markdown("#### Main Modules")
    selected_tab1 = st.radio("Select Tab (Row 1):", tab_row1, horizontal=True, key="row1_radio")
    st.markdown("#### More Modules")
    selected_tab2 = st.radio("Select Tab (Row 2):", tab_row2, horizontal=True, key="row2_radio")

    # Only one tab active at a time
    active_tab = selected_tab1 if selected_tab1 != tab_row1[0] else selected_tab2

    # Show content based on active tab
    if active_tab == "Materials & Energy Balance Engine":
        show_materials_energy_balance(df)
    elif active_tab == "Furnace Analytics & Optimization":
        show_furnace_analytics(df)
    elif active_tab == "Electrode Paste Optimizer":
        show_electrode_optimizer(df)
    elif active_tab == "Conveyor & Utility Efficiency":
        show_conveyor_utility_efficiency(df)
    elif active_tab == "Batch Mixing & Yield Model":
        show_batch_mixing_yield(df)
    elif active_tab == "Anomaly Detection & Alerts":
        show_anomaly_detection(df)
    elif active_tab == "Scenario Simulator":
        show_scenario_simulator(df)
    elif active_tab == "Cost & GHG Dashboard":
        show_cost_ghg_dashboard(df)

if __name__ == "__main__":
    main()
