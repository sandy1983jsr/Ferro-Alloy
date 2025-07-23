import streamlit as st

def show_scenario_simulator(df):
    st.subheader("Scenario Simulator")
    st.write("Physics-based scenario simulation: feed, energy price, efficiency.")

    col1, col2, col3 = st.columns(3)
    with col1:
        mix_adj = st.slider("Batch Mix Ratio Adjustment (%)", -5, 5, 0)
    with col2:
        elec_price = st.slider("Electricity Price (USD/kWh)", 0.08, 0.18, 0.12)
    with col3:
        eff_adj = st.slider("Furnace Efficiency Adjustment (%)", -3, 3, 0)

    # Physics: yield increases with mix ratio, cost with energy/efficiency
    sim_df = df.copy()
    sim_df['Batch_Mix_Ratio'] = df['Batch_Mix_Ratio'] * (1 + mix_adj / 100)
    sim_df['Furnace_Efficiency_%'] = df['Furnace_Efficiency_%'] + eff_adj
    sim_df['Yield_%'] = sim_df['Yield_%'] * (1 + 0.5 * mix_adj / 100)
    sim_df['Cost_USD'] = (df['Electricity_Consumed_kWh'] * elec_price) / (sim_df['Furnace_Efficiency_%'] / 100) + (df['Raw_Material_Input_kg'] * 1.1)

    st.line_chart(sim_df.set_index('Date')[['Batch_Mix_Ratio', 'Furnace_Efficiency_%', 'Yield_%', 'Cost_USD']])
    st.write("Simulated mean cost:", int(sim_df['Cost_USD'].mean()), "USD")
