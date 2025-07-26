import streamlit as st
import pandas as pd
import numpy as np

def show_scenario_simulator(df):
    # Sidebar inputs for simulation parameters
    elec_price = st.sidebar.number_input(
        "Electricity Price (INR per kWh)", value=6.0, min_value=5.5, max_value=6.5, step=0.1
    )
    ore_price = st.sidebar.number_input(
        "Manganese Ore Price (INR per kg)", value=14700.0, min_value=10000.0, max_value=25000.0, step=100.0
    )

    # Ensure columns are numeric
    df['Electricity_Consumed_kWh'] = pd.to_numeric(df['Electricity_Consumed_kWh'], errors='coerce')
    df['Furnace_Efficiency_%'] = pd.to_numeric(df['Furnace_Efficiency_%'], errors='coerce')
    df['Manganese_Ore_kg'] = pd.to_numeric(df['Manganese_Ore_kg'], errors='coerce')

    # Drop rows with missing values
    sim_df = df.dropna(subset=['Electricity_Consumed_kWh', 'Furnace_Efficiency_%', 'Manganese_Ore_kg']).copy()

    # Calculate scenario cost
    # Example formula:
    # Cost_USD = (Electricity_Consumed_kWh * elec_price) / (Furnace_Efficiency_% / 100) + (Manganese_Ore_kg * ore_price)
    sim_df['Cost_USD'] = (
        (sim_df['Electricity_Consumed_kWh'] * elec_price) / (sim_df['Furnace_Efficiency_%'] / 100)
        + (sim_df['Manganese_Ore_kg'] * ore_price)
    )

    st.subheader("Scenario Simulation Results")
    st.dataframe(sim_df[["Date", "Electricity_Consumed_kWh", "Furnace_Efficiency_%", "Manganese_Ore_kg", "Cost_USD"]])

    # Optionally, plot results
    st.line_chart(sim_df.set_index("Date")["Cost_USD"])

# Example usage:
if __name__ == "__main__":
    # Example data
    df = pd.DataFrame({
        "Date": pd.date_range("2025-01-01", periods=30, freq="D"),
        "Electricity_Consumed_kWh": np.random.randint(3200, 3600, size=30),
        "Furnace_Efficiency_%": np.random.uniform(85, 88, size=30),
        "Manganese_Ore_kg": np.random.randint(9000, 10500, size=30),
    })
    show_scenario_simulator(df)
